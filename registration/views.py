from django.shortcuts import render
from django.http import HttpResponse
from registration.models import Course, Batch, Student
# Create your views here.
def index(request):
    return HttpResponse("<center><h1>Welcome to Prime Intuit Registration page</h1>")
def Home(request):
    batch_list = Batch.objects.order_by('batch_ID')
    data_dict = {'access_record':batch_list, 'insert_me':'I am a text from registration/Views.py'}
 #   return HttpResponse("<center><h1>Welcome to Prime Intuit home page</h1>")
   # my_dict = {'Insert_Me': "I am a text from registration/Views.py"}

    return render(request,'registration/index.html',context= data_dict)