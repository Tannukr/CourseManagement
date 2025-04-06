from rest_framework import serializers
from .models import User,Course,Student


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class StudentInfoSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = Student
        fields = ['id', 'username', 'email']


class CourseSerializer(serializers.ModelSerializer):
    instructor_name = serializers.ReadOnlyField(source='instructor.username')
    enrolled_students = StudentInfoSerializer(source='students', many=True, read_only=True)
    
    class Meta:
        model = Course
        fields = ['id', 'course_name', 'course_code', 'credits', 'description', 
                  'instructor', 'instructor_name', 'enrolled_students']
        read_only_fields = ['instructor']

    def validate_course_code(self, value):
        # Skip validation if value is None (happens on partial updates)
        if value is None:
            return value
            
        # Print debugging info
        instance_id = getattr(self.instance, 'id', None)
        print(f"Validating course_code: {value}, instance_id: {instance_id}")
        
        # Skip validation if we're updating and using the same code
        if self.instance and self.instance.course_code and self.instance.course_code.lower() == value.lower():
            print(f"Same course code used in update: {value}")
            return value
        
        # Check if another course already has this code
        existing_courses = Course.objects.filter(course_code__iexact=value)
        
        # For update operations, exclude the current instance from the uniqueness check
        if self.instance:
            existing_courses = existing_courses.exclude(id=self.instance.id)
            
        if existing_courses.exists():
            print(f"Validation error: Course code {value} already exists")
            raise serializers.ValidationError("A course with this code already exists.")
            
        return value
        
    def update(self, instance, validated_data):
        print(f"Updating instance: {instance.id} with data: {validated_data}")
        updated_instance = super().update(instance, validated_data)
        print(f"After update: {updated_instance.course_name}, {updated_instance.course_code}")
        return updated_instance


class StudentSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(many=True, queryset=Course.objects.all())

    class Meta:
        model = Student
        fields = '__all__'