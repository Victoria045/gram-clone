from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

class TestProfile(TestCase):
  def setUp(self):
      self.user = User(username='Chris')
      self.user.save()

      self.test_profile = Profile(id=1, name='image', profile_picture="test.jpg", bio="Chris' test bio",
                                user=self.user)
  def test_instance(self):
      self.assertTrue(isinstance(self.test_profile, Profile))
  
  def test_save_profile(self):
      self.test_profile.save_profile()
      after = Profile.objects.all()
      self.assertTrue(len(after) > 0)
