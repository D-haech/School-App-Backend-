from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.


class CustomUser(AbstractUser):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
        ROLE_CHOICES = (
            ("school_admin", "School Admin"),
            ("teacher", "teacher"),
            ("student", "student"),
        )
        role = models.CharField(max_length=50, choices=ROLE_CHOICES, blank=False)
        school = models.ForeignKey(
            "School", on_delete=models.CASCADE, blank=False, null=False
        )

class School(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
        name= models.CharField(max_length= 150, blank=False )
        address = models.TextField(blank=False)
        created_on = models.DateTimeField(auto_now_add=True, blank=False)
    