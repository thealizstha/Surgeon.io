from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
     return render(request,'index.html')
     
def about(request):
     return HttpResponse("This is about section")

def report(request):
     return HttpResponse("This is report section")

def login(request):
     return render(request,'login.html')

