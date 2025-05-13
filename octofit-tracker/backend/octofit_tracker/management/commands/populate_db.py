from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create test users
        user1 = User.objects.create(username='john_doe', email='john@example.com', password='password123')
        user2 = User.objects.create(username='jane_doe', email='jane@example.com', password='password123')

        # Additional test users
        user3 = User.objects.create(username='alice_smith', email='alice@example.com', password='password123')
        user4 = User.objects.create(username='bob_jones', email='bob@example.com', password='password123')

        # Create test teams
        team1 = Team.objects.create(name='Team Alpha')

        # Additional test teams
        team2 = Team.objects.create(name='Team Beta')
        team3 = Team.objects.create(name='Team Gamma')

        # Create test activities
        Activity.objects.create(_id=ObjectId(), user=user1, activity_type='Running', duration=timedelta(seconds=3600))  # Duration in seconds
        Activity.objects.create(_id=ObjectId(), user=user2, activity_type='Cycling', duration=timedelta(seconds=7200))

        # Additional test activities
        Activity.objects.create(_id=ObjectId(), user=user3, activity_type='Swimming', duration=timedelta(seconds=1800))
        Activity.objects.create(_id=ObjectId(), user=user4, activity_type='Hiking', duration=timedelta(seconds=5400))

        # Create test leaderboard entries
        Leaderboard.objects.create(user=user1, score=150)
        Leaderboard.objects.create(user=user2, score=200)

        # Additional test leaderboard entries
        Leaderboard.objects.create(user=user3, score=120)
        Leaderboard.objects.create(user=user4, score=180)

        # Create test workouts
        Workout.objects.create(name='Morning Yoga', description='A relaxing morning yoga session.')
        Workout.objects.create(name='HIIT', description='High-intensity interval training.')

        # Additional test workouts
        Workout.objects.create(name='Evening Pilates', description='A calming pilates session to end the day.')
        Workout.objects.create(name='Strength Training', description='A workout focused on building muscle strength.')

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
