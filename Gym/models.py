from django.db import models
from django.db.models.fields import EmailField
  
class Contact(models.Model):
    Full_Name_C=models.CharField(max_length=122)
    Email=models.EmailField(max_length = 254)
    Contact_Info=models.IntegerField(null=True,blank=True)
    Subject=models.CharField(max_length=122)
    Query=models.TextField()
    Date=models.DateField()

class Feedback_User(models.Model):
    Customer_Name=models.CharField(max_length=122)
    Feedback=models.TextField()
    fdb= [
        ('yes', 'YES'),
        ('no', 'NO'),
        ]
    Customer_Satisfaction=models.CharField(max_length=100, choices=fdb)
    Date=models.DateField()

class Customer_Database(models.Model):
    Full_Name=models.CharField(max_length=122)
    Date_of_joining=models.DateField()                      
    Age=models.IntegerField()
    Contact=models.IntegerField()
    Email=models.EmailField(max_length = 254)
    option= [
        ('malad (e)', 'Malad (E)'),
        ('malad (w)', 'Malad (W)'),
        ('goregoan', 'Goregoan'),
        ('andheri (e)', 'Abdheri (E)'),
        ('andheri (w)', 'Abdheri (W)'),
        ]
    Branch=models.CharField(max_length=100, choices=option)
    fee= [
        ('paid', 'PAID'),
        ('pending', 'PENDING'),
        ]
    Jan_Fees=models.CharField(max_length=100, choices=fee,blank=True,null=True)
    Feb=models.CharField(max_length=100, choices=fee,blank=True,null=True)
    March=models.CharField(max_length=100, choices=fee,blank=True,null=True)
    April=models.CharField(max_length=100, choices=fee,blank=True,null=True)
    May=models.CharField(max_length=100, choices=fee,blank=True,null=True)
    June=models.CharField(max_length=100, choices=fee,blank=True,null=True)
    July=models.CharField(max_length=100, choices=fee,blank=True,null=True)
    August=models.CharField(max_length=100, choices=fee,blank=True,null=True)
    Sep=models.CharField(max_length=100, choices=fee,blank=True,null=True)
    Oct=models.CharField(max_length=100, choices=fee,blank=True,null=True)
    Nov=models.CharField(max_length=100, choices=fee,blank=True,null=True)
    Dec=models.CharField(max_length=100, choices=fee,blank=True,null=True)

class Trainers(models.Model):
    Full_Name=models.CharField(max_length=122)
    Email=models.EmailField(max_length = 254)
    Contact=models.IntegerField()
    option= [
        ('malad (e)', 'Malad (E)'),
        ('malad (w)', 'Malad (W)'),
        ('goregoan', 'Goregoan'),
        ('andheri (e)', 'Abdheri (E)'),
        ('andheri (w)', 'Abdheri (W)'),
        ]
    Branch=models.CharField(max_length=100, choices=option)
    Age=models.IntegerField()
    Date_of_joining=models.DateField()   
    Total_Annual_Salary= models.IntegerField()
    sal= [
        ('done', 'DONE'),
        ('pending', 'PENDING'),
        ]
    Jan_Salary=models.CharField(max_length=100, choices=sal,blank=True,null=True)
    Feb=models.CharField(max_length=100, choices=sal,blank=True,null=True)
    March=models.CharField(max_length=100, choices=sal,blank=True,null=True)
    April=models.CharField(max_length=100, choices=sal,blank=True,null=True)
    May=models.CharField(max_length=100, choices=sal,blank=True,null=True)
    June=models.CharField(max_length=100, choices=sal,blank=True,null=True)
    July=models.CharField(max_length=100, choices=sal,blank=True,null=True)
    August=models.CharField(max_length=100, choices=sal,blank=True,null=True)
    Sep=models.CharField(max_length=100, choices=sal,blank=True,null=True)
    Oct=models.CharField(max_length=100, choices=sal,blank=True,null=True)
    Nov=models.CharField(max_length=100, choices=sal,blank=True,null=True)
    Dec=models.CharField(max_length=100, choices=sal,blank=True,null=True)

class Equipment(models.Model):
    Name=models.CharField(max_length=122)
    Model_Name=models.CharField(max_length=122)
    Information=models.CharField(max_length=122)
    Price=models.IntegerField()
    Date_of_Purchase=models.DateField()
    option= [
        ('malad (e)', 'Malad (E)'),
        ('malad (w)', 'Malad (W)'),
        ('goregoan', 'Goregoan'),
        ('andheri (e)', 'Abdheri (E)'),
        ('andheri (w)', 'Abdheri (W)'),
        ]
    Branch=models.CharField(max_length=100, choices=option)