from django.core.management.base import BaseCommand
from Task1.models import User, Student

class Command(BaseCommand):
    help = 'Creates student profiles for users with Student role that don\'t have one'

    def handle(self, *args, **kwargs):
        users = User.objects.filter(role='Student')
        created_count = 0
        
        for user in users:
            try:
                # Check if student profile exists
                student = user.student_profile
                self.stdout.write(f'Student profile already exists for {user.username}')
            except Student.DoesNotExist:
                # Create student profile if it doesn't exist
                Student.objects.create(user=user)
                created_count += 1
                self.stdout.write(f'Created student profile for {user.username}')
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created {created_count} student profiles')) 