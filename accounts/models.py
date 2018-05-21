from django.contrib.auth.models import User
from django.db import models

from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, null=True, default='')
    city = models.CharField(max_length=100, null=False, default='')
    website = models.URLField(null=True, default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='accounts_img', blank=True)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return str(self.user)

    # def create_profile(self, sender, **kwargs):
    #     if kwargs['created']:
    #         user_profile = UserProfile.objects.create(user=kwargs['instance'])
    #
    # post_save.connect(create_profile, sender=User)




















