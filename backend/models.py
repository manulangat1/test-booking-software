from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    tel_no = models.CharField(max_length=18,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    def __str__(self):
        return self.username
class Disease(models.Model):
    MALARIA = 'MALARIA'
    BLOOD_GLUCOSE_CBC = 'BLOOD_GLUCOSE_CBC'
    IN_PROGRESS = 'IN_PROGRESS'
    COMPLETED = 'COMPLETED'
    STATUSES = (
        (MALARIA, MALARIA),
        (BLOOD_GLUCOSE_CBC, BLOOD_GLUCOSE_CBC),
        (IN_PROGRESS, IN_PROGRESS),
        (COMPLETED, COMPLETED),
    )
    name = models.CharField(max_length=50)
    test_for = models.CharField(choices=STATUSES,default="MALARIA",max_length=200)
    costs = models.BigIntegerField()

    def __str__(self):
        return self.name
class Test(models.Model):
    patient = models.ForeignKey(User,on_delete=models.CASCADE)
    request_at = models.DateTimeField(auto_now_add=True)
    disease = models.ManyToManyField(Disease)
    def __str__(self):
        return self.patient.username
    def total(self):
        total = 0
        for di in self.disease.all():
            total +=  di.costs
        return total


