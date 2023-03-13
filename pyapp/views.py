from django.shortcuts import render,redirect
from pyapp.models import studentdb,catdb,productdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def indexpage(request):
    return render(request,'index.html')
def student(request):
    return render(request,'addstudent.html')
def display(request):
    data=studentdb.objects.all()
    return render(request,'displaydata.html',{'data':data})
def imagesave(request):
    if request.method=="POST":
        na = request.POST.get('name')
        ag = request.POST.get('age')
        ph= request.POST.get('phone')
        img = request.FILES['image']
        obj = studentdb(name=na,age=ag,phone=ph,image=img)
        obj.save()
        return redirect(student)
def editpage(request ,dataid):
    data=studentdb.objects.get(id=dataid)
    print(data)
    return render(request,'editdata.html',{'data':data})
def update(request, dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        ag = request.POST.get('age')
        ph= request.POST.get('phone')
        try:
             img = request.FILES['image']
             fs=FileSystemStorage()
             file=fs.save(img.name,img)
        except MultiValueDictKeyError:
             file= studentdb.objects.get(id=dataid).image
    studentdb.objects.filter(id=dataid).update(name=na,age=ag,phone=ph,image=file)
    return redirect(display)
def deletedata(request,dataid):
    data=studentdb.objects.filter(id=dataid)
    data.delete()
    return redirect(display)
def addcategorypage(request):
    return render(request,'addcat.html')
def displaycategory(request):
     data = catdb.objects.all()
     return render(request, "displaycat.html", {'data': data})
def addcategory(request):
    if request.method=="POST":
        cna = request.POST.get('catname')
        cdis = request.POST.get('catdis')
        cimg = request.FILES['catimg']
        obj = catdb(catname=cna,catdis=cdis,catimg=cimg)
        obj.save()
        return redirect(addcategorypage)
def editcat(request ,dataid):
    data=catdb.objects.get(id=dataid)
    print(data)
    return render(request, 'editcat.html', {'data': data})
def updatecat(request, dataid):
    if request.method=="POST":
        cna = request.POST.get('catname')
        cdis = request.POST.get('catdis')
        try:
             cimg = request.FILES['catimg']
             fs=FileSystemStorage()
             file=fs.save(cimg.name,cimg)
        except MultiValueDictKeyError:
             file= catdb.objects.get(id=dataid).catimg
    catdb.objects.filter(id=dataid).update(catname=cna,catdis=cdis,catimg=file)
    return redirect(displaycategory)

def deletecategory(request,dataid):
    data=catdb.objects.get(id=dataid)
    data.delete()
    return redirect(displaycategory)
def addproduct(request):
    data=catdb.objects.all()
    return render(request,'addproduct.html',{'data':data})
def displayproduct(request):
    data = productdb.objects.all()

    return render(request, "displayproduct.html", {'data': data})
def saveproduct(request):
    if request.method=="POST":
        na = request.POST.get('name')
        pr = request.POST.get('price')
        qty= request.POST.get('quantity')
        img = request.FILES['image']
        cat=request.POST.get('category')
        obj = productdb(name=na,price=pr,quantity=qty,image=img,category=cat)
        obj.save()
        return redirect(addproduct)
def editpro(request ,dataid):
    data=productdb.objects.get(id=dataid)
    da=catdb.objects.all()
    print(data)
    return render(request,'editproduct.html',{'data':data,'da':da})
def updatepro(request, dataid):
    if request.method=="POST":
        cna = request.POST.get('name')
        pr = request.POST.get('price')
        qty= request.POST.get('quantity')
        cat= request.POST.get('category')
        try:
             img = request.FILES['image']
             fs=FileSystemStorage()
             file=fs.save(img.name,img)
        except MultiValueDictKeyError:
             file= productdb.objects.get(id=dataid).image
    productdb.objects.filter(id=dataid).update(name=cna,price=pr,quantity=qty,image=file,category=cat)
    return redirect(displayproduct)
def deleteproduct(request,dataid):
    data=productdb.objects.get(id=dataid)
    data.delete()
    return redirect(displayproduct)
