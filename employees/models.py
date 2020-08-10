import datetime

from django.db import models
import  uuid

class Position(models.Model):
    title = models.CharField(max_length=200, blank=False, editable=True)
    registered_time = models.DateTimeField(auto_now_add=True, editable=False)
    def __str__(self):
        return  self.registered_time


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=200, editable=True, blank=False, null=False)
    national_id = models.CharField(max_length=16, unique=True)  # national id should be unique
    phone_number = models.CharField(max_length=15, unique=True)  # phone number should be unique
    email = models.EmailField(max_length=200, unique=True, null=False, blank=False)  # email should be unique
    date_of_birth = models.DateField()
    statues = {
        ('ACTIVE', 'ACTIVE'),
        ('INACTIVE', 'INACTIVE'),
    }

    status = models.CharField(max_length=50, choices=statues, default='ACTIVE')
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    registered_time = models.DateTimeField(auto_now_add=True, editable=False)

    def save(self, *args, **kwargs):

        # Not allowing the registration of an employee who is below 18 years of age.
        if self.date_of_birth:
            birthday = self.date_of_birth.year
            this_year = datetime.datetime.today().year

            if not this_year > birthday:
                raise Exception("Enter a valid date of birth")

            elif this_year - birthday < 18:
                raise Exception("Hmm! You are too young! you are not allowed!")

        # to check if phone number is Rwandan number
        if self.phone_number:
            if not str(self.phone_number).startswith('+250'):
                raise Exception("Phone number must be rwandan! hint: start with '+250'")

        super(Employee, self).save(*args, **kwargs)

    def __str__(self):
        return self.name