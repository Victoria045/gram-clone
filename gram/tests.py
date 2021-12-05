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

class TestPost(TestCase):
    def setUp(self):
        self.profile_test = Profile(name='Chris', user=User(username='Chris'))
        self.profile_test.save()

        self.image_test = Post(image='default.png', name='test', caption='default test', user=self.profile_test)

    def test_insatance(self):
        self.assertTrue(isinstance(self.image_test, Post))

    def test_save_image(self):
        self.image_test.save_image()
        images = Post.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        after = Profile.objects.all()
        self.assertTrue(len(after) < 1)
