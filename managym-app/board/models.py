from hashlib import md5

from django.db import models
from django.contrib.auth.models import User
from dj.choices import Choices, Choice
from django.db.models import Func

class Round2(Func):
  function = 'ROUND'
  arity = 2



class TargetResult(models.Model):
    """Model representing the target/results for an athlete on an event on an apparatus."""

    athlete = models.ForeignKey('Athlete', on_delete=models.DO_NOTHING)
    apparatus = models.ForeignKey('Apparatus', on_delete=models.DO_NOTHING)
    event = models.ForeignKey('Event', on_delete=models.DO_NOTHING)
    target_sv = models.FloatField(null=True, blank=True)
    target_ex = models.FloatField(null=True, blank=True)
    result_sv = models.FloatField(null=True, blank=True)
    result_ex = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = "TargetResult"
        verbose_name_plural = "TargetsResults"
        unique_together = [['athlete', 'apparatus', 'event']]

    def __str__(self):
        return f'{self.athlete} - {self.event} - {self.apparatus}'
    

class Gender(Choices):
    male = Choice("male").extra(label="Male")
    female = Choice("female").extra(label="Female")
    not_specified = Choice("not specified").extra(label="Not specified")


class Athlete(models.Model):
    """Model representing an athlete."""

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    gender = models.IntegerField(choices=Gender(),
                                 default=Gender.not_specified.id)
    birth_date = models.DateField()
    email = models.EmailField(max_length=100)
    email_2 = models.EmailField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    phone_number_2 = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=64, null=True, blank=True)
    city = models.CharField(max_length=64, null=True, blank=True)
    province = models.CharField(max_length=2, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Athlete"
        verbose_name_plural = "Athletes"

    def __str__(self):
        """String for representing the Athlete object."""
        return f'{self.first_name} {self.last_name}'

    def picture(self, size=192):
        email = self.email or 'email@test.com'
        digest = md5(email.lower().encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}'

    def gend(self):
        gender = Gender.from_id(self.gender)
        if gender == Gender.male:
            return 'male'
        elif gender == Gender.female:
            return 'female'
        else:
            return 'not specified'

class Group(models.Model):
    """Model representing a group of athletes."""

    name = models.CharField(max_length=120, default="New group")
    users = models.ManyToManyField(User, related_name='groups_of_athletes', blank=True)

    class Meta:
        verbose_name = "Group of athletes"
        verbose_name_plural = "Groups of athletes"

    def __str__(self):
        return self.name
    
    
class Apparatus(models.Model):
    """Model representing an apparatus."""

    short_name = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name = "Apparatus"
        verbose_name_plural = "Apparatus"

    def __str__(self):
        return self.name

class Event(models.Model):
    """Model representing an event."""

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=140, null=True, blank=True)
    date = models.DateField()
    place= models.CharField(max_length=120, null=True)
    type = models.ForeignKey('TypeEvent', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.name

class TypeEvent(models.Model):
    """Model representing the type of an event."""

    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = "TypeEvent"
        verbose_name_plural = "TypesEvent"

    def __str__(self):
        return self.name

class Information(models.Model):
    """Model representing an information."""

    body = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    type = models.ForeignKey('TypeInformation', on_delete=models.DO_NOTHING)
    athlete = models.ForeignKey('Athlete', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Information"
        verbose_name_plural = "Information"

    def __str__(self):
        return self.body
    
class TypeInformation(models.Model):
    """Model representing a type on information."""

    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = "TypeInformation"
        verbose_name_plural = "TypesInformation"

    def __str__(self):
        return self.name
    
    
    
    