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
    is_staff = None
    is_active = None
    is_superuser = None
    last_login = None
    first_name = None
    last_name = None