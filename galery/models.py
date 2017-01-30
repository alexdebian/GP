from django.db import models
from django.contrib.auth.models import AbstractUser
from gpproject import settings


class Users(AbstractUser):
    class Meta:
        db_table = 'users'

    # birthday = models.DateField(blank=False)
    # gender = models.CharField(max_length=5, choices=GENDERS.items(), help_text='Выберите пол')
    phone_number = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=50, blank=True)
    index = models.IntegerField(default=0, blank=True)
    city = models.CharField(max_length=50, blank=True)
    street = models.CharField(max_length=100, blank=True)
    house = models.CharField(max_length=6, blank=True)
    apartment = models.CharField(max_length=6, blank=True)


class Images(models.Model):

    imagefile = models.FileField(upload_to='images')
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL)

    def get_my_files(self, current_user):
        return self.objects.filter(uploaded_by=current_user)
