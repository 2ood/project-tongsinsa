from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.utils import timezone

import uuid

class CustomUser(AbstractUser):
    """
	#   password  
    #   username
    """
    user_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student_number = models.IntegerField(editable=False)
    department = models.CharField(max_length=100)
    is_delete = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)
    email = models.EmailField()
    user_image = models.URLField(default="default_user_image.png")
    is_staff = None
    is_active = None
    is_superuser = None
    last_login = None
    first_name = None
    last_name = None

class Event(models.Model):
    event_generated = models.DateTimeField(default=timezone.now, editable=False)
    writer= models.CharField(max_length=150)
    title = models.CharField(max_length=255)
    text = models.TextField()
    info = models.JSONField()
    info_image = models.URLField(default="default_info_image.png")
    thumbnail = models.URLField(default="default_thumbnail_image.png")
    is_delete = models.BooleanField(default=False)

class list(models.Model):
    user = models.ForeignKey('CustomUser',on_delete=models.CASCADE)
    event = models.ForeignKey('Event',on_delete=models.CASCADE)
    others = models.JSONField()
    is_delete = models.BooleanField(default=False)
    