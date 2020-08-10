from django.contrib.auth.models import UserManager as UManager

class UserManager(UManager):
    def _create_user(self, national_id, password, **extra_fields):
        if not national_id:
            raise ValueError('The given national_id must be set')
        user = self.model(national_id=national_id,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, national_id,password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user( national_id=national_id, password=password, **extra_fields)

    def create_superuser(self, national_id, password,  **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user( national_id=national_id, password=password, **extra_fields)
