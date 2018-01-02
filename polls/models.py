import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    sex = models.CharField(max_length=7, choices=sex, blank=False)
    age = (
        ('18-24', '18-24'),
        ('25-34', '25-34'),
        ('35-44', '35-44'),
        ('45-54', '45-54'),
        ('55-64', '55-64'),
        ('65+', '65+'),
    )

    age = models.CharField(max_length=10, choices=age, blank=False)
    ethnicity = (
        ('Hausa/Fulani', 'Hausa/Fulani'),
        ('Igbo', 'Igbo'),
        ('Yoruba', 'Yoruba'),
        ('Minority-South South', 'Minority-South South'),
        ('Minority-North Central', 'Minority-North Central'),
        ('Minority-North East', 'Minority-North East'),
    )

    ethnicity = models.CharField(max_length=30, choices=ethnicity, blank=False)
    residence = (
        ('North West', 'North West'),
        ('North East', 'North East'),
        ('North Central', 'North Central'),
        ('South West', 'South West'),
        ('South East', 'South East'),
        ('South South', 'South South'),
        ('Diaspora', 'Diaspora'),
    )

    residence = models.CharField(max_length=20, choices=residence, blank=False)
    education = (
        ('Less than secondary school', 'Less than secondary school'),
        ('Secondary school', 'Secondary school'),
        ('Graduate', 'Graduate'),
        ('Post graduate', 'Post graduate'),
    )

    education = models.CharField(max_length=50, choices=education, blank=False)
    employment = (
        ('Currently unemployed', 'Currently unemployed'),
        ('Employed full time', 'Employed full time'),
        ('Employed part time', 'Employed part time'),
        ('Self employed', 'Self employed'),
        ('Student', 'Student'),
        ('Retired', 'Retired'),
    )

    employment = models.CharField(max_length=30, choices=employment, blank=False)
    income = (
        ('Less than 18,000', 'Less than 18,000'),
        ('18,000 - 50,000', '18,000 - 50,000'),
        ('51,000 - 100,000', '51,000 - 100,000'),
        ('101,000 - 200,000', '101,000 - 200,000'),
        ('201,000 - 500,000', '201,000 - 500,000'),
        ('500,000+', '500,000+'),
    )

    income = models.CharField(max_length=30, choices=income, blank=False)
    marital_status = (
        ('Single-never married', 'Single-never married'),
        ('Divorced or Separated', 'Divorced or Separated'),
        ('Married', 'Married'),
        ('Widowed', 'Widowed'),
    )

    marital_status = models.CharField(max_length=30, choices=marital_status, blank=False)
    religion = (
        ('Christianity', 'Christianity'),
        ('Islam', 'Islam'),
        ('Other', 'Other'),
    )

    religion = models.CharField(max_length=20, choices=religion, blank=False)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    

    @receiver(post_save, sender=user)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=user)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Poll(models.Model):
    question = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    user = models.ManyToManyField(User)
    profile = models.ManyToManyField(Profile)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.question



class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    profile = models.ManyToManyField(Profile)

    def __str__(self):
        return self.choice_text

