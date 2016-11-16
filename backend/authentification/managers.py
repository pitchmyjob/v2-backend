from django.contrib.auth.models import UserManager as UserManager_
from django.utils import timezone


class UserManager(UserManager_):

    def create_user(self, username, email=None, password=None, first_name=None, last_name=None):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = UserManager.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=False, is_active=True, is_superuser=False,
                          last_login=now, date_joined=now, first_name=first_name, last_name=last_name)

        user.set_password(password)
        user.save(using=self._db)
        return user
