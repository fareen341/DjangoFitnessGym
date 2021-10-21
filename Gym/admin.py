from django.contrib import admin
from Gym.models import  Feedback_User, Contact, Equipment, Trainers, Customer_Database


# Register your models here.
@admin.register(Feedback_User)
# Register your models here.

class Feedback_User(admin.ModelAdmin):
    list_display=['Customer_Name','Feedback','Customer_Satisfaction',"Date"]



@admin.register(Contact)
# Register your models here.

class Contact(admin.ModelAdmin):
    list_display=['Full_Name_C','Email','Contact_Info','Subject','Query',"Date"]


@admin.register(Customer_Database)
# Register your models here.

class Customer_Database(admin.ModelAdmin):
    list_display=['Full_Name','Date_of_joining','Age','Contact','Email','Branch','Jan_Fees','Feb','March','April','May','June','July','August',
        'Sep','Oct','Nov','Dec']


@admin.register(Trainers)
# Register your models here.

class Trainers(admin.ModelAdmin):
    list_display=['Full_Name','Contact','Email','Age','Branch','Date_of_joining','Total_Annual_Salary','Jan_Salary','Feb','March','April','May','June','July','August',
        'Sep','Oct','Nov','Dec']


@admin.register(Equipment)
# Register your models here.

class Equipment(admin.ModelAdmin):
    list_display=['Name','Model_Name','Information','Price','Date_of_Purchase','Branch']
