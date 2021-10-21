from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from Gym.models import Contact, Feedback_User, Customer_Database
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method=="POST":
        Full_Name=request.POST.get('Full_Name')
        Age=request.POST.get('Age')
        Email=request.POST.get('Email')
        Contact=request.POST.get('Contact')
        Branch=request.POST.get('Branch')
        regi=Customer_Database(Full_Name=Full_Name,Age=Age,Email=Email,Contact=Contact,Branch=Branch,Date_of_joining=datetime.today())
        regi.save()
        messages.success(request, 'Registration Completed Successfully.')
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=="POST":
        Full_Name_C=request.POST.get('Full_Name_C')
        Email=request.POST.get('Email')
        Contact_Info=request.POST.get('Contact')
        Subject=request.POST.get('Subject')
        Query=request.POST.get('Query')
        contact=Contact(Full_Name_C=Full_Name_C,Email=Email,Contact_Info=Contact_Info,Subject=Subject,Query=Query,Date=datetime.today())
        contact.save()
        messages.success(request, 'Thank you for contacting us!, We have received your enquiry and will respond to you within 24 hours. For urgent enquiries please contact us on our given number.')
    return render(request,'contact.html')


def branches(request):
    return render(request,'branches.html')

def gallery(request):
    return render(request,'gallery.html')

def pricing(request):
    return render(request,'pricing.html')

def feedback(request):
    if request.method=="POST":
        Customer_Name=request.POST.get('Customer_Name')
        Customer_Satisfaction=request.POST.get('Customer_Satisfaction')
        Feedback=request.POST.get('Feedback')
        fb=Feedback_User(Customer_Name=Customer_Name,Customer_Satisfaction=Customer_Satisfaction, Feedback=Feedback, Date=datetime.today())
        fb.save()
        messages.success(request, 'Thank you! We appreciate that you have taken the time to write us.')
    return render(request,'feedback.html')

def services(request):
    return render(request,'services.html')


