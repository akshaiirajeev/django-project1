from django.db import models
from django.contrib.auth.models import User


class companydetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username
    # def __str__(self):
    #     return self.user.email


class postjob(models.Model):
    catchoice = [
        ('Hybrid', 'Hybrid'),
        ('Remote', 'Remote')
    ]

    jobtype = [
        ('Part Time', 'Part Time'),
        ('Full Time', 'Full Time'),
    ]

    exp = [
        ('0-1', '0-1'),
        ('1-2', '1-2'),
        ('2-3', '2-3'),
        ('3-4', '3-4'),
        ('4-5', '4-5'),

    ]

    Jobtitle = models.CharField(max_length=30)
    companyname = models.CharField(max_length=30)
    jobdescription = models.CharField(max_length=255)
    Experience = models.CharField(max_length=30, choices=exp)
    workplace = models.CharField(max_length=30, choices=catchoice)
    Employmenttype =models.CharField(max_length=30, choices=jobtype)



class employeemodel(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.EmailField()
    userpassword=models.CharField(max_length=50)



class apply_job(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    resume=models.FileField( upload_to='wehireapp/static')
    current_position=models.CharField(max_length=100,default="")
    current_company=models.CharField(max_length=100,default="")
    date=models.DateField(auto_now_add=True)
    job_title=models.CharField(max_length=50,default="")
    company_name=models.CharField(max_length=100,default="")

    def _str_(self):
        return self.email


