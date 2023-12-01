<<<<<<< HEAD
from django.contrib.auth.models import User


class User(User):
=======
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
>>>>>>> new-branch
    def __str__(self):
        return self.get_full_name()
