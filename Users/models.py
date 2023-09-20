from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Add custom user fields as needed (e.g., profile picture, contact info)
    pass
