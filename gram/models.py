from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# from PIL import Image
import cloudinary
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = CloudinaryField('image')
    # profile_picture = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    # def save(self):
    #     super().save()

    #     img = Image.open(self.profile_picture.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.profile_picture.path)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()