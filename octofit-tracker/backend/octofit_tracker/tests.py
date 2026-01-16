from django.test import TestCase
from rest_framework.test import APIClient
from .models import User, Team, Activity, Workout, Leaderboard

class OctofitTrackerTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name="Test Team")
        self.user = User.objects.create(name="Test User", email="test@example.com", team=self.team)
        self.workout = Workout.objects.create(name="Pushups", description="Do 20 pushups")
        self.activity = Activity.objects.create(user=self.user, type="run", duration=30, date="2024-01-01")
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100)

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.user.team.name, "Test Team")

    def test_team_creation(self):
        self.assertEqual(Team.objects.count(), 1)

    def test_activity_creation(self):
        self.assertEqual(Activity.objects.count(), 1)
        self.assertEqual(self.activity.user, self.user)

    def test_workout_creation(self):
        self.assertEqual(Workout.objects.count(), 1)

    def test_leaderboard_creation(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
        self.assertEqual(self.leaderboard.score, 100)

    def test_api_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("users", response.data)

    def test_user_api(self):
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, 200)

    def test_team_api(self):
        response = self.client.get("/teams/")
        self.assertEqual(response.status_code, 200)

    def test_activity_api(self):
        response = self.client.get("/activities/")
        self.assertEqual(response.status_code, 200)

    def test_workout_api(self):
        response = self.client.get("/workouts/")
        self.assertEqual(response.status_code, 200)

    def test_leaderboard_api(self):
        response = self.client.get("/leaderboard/")
        self.assertEqual(response.status_code, 200)
