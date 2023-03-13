from django.shortcuts import render
from pyapp.models import catdb,productdb
# Create your views here.
def home(request):
    data=catdb.objects.all()
    return render(request,'indexpage.html',{'data':data})
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')