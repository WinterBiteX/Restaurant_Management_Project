from django.shortcuts import render,redirect
from ResApp.models import Style_Db,Food_Db
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from WebApp.models import Contact_Db
from django.contrib import messages



def index_page(req):
    return render(req,"index.html")
def add_foodstyle(req):
    return render(req,"Add_FoodStyle.html")
def save_foodstyle(request):
    if request.method == "POST":
        a = request.POST.get("foodstyle")
        b = request.POST.get("description")
        c = request.FILES['fs_img']

        obj = Style_Db(Food_Style = a,Description = b,Style_Image = c)
        obj.save()
        messages.success(request,"Food Style added..!")
        return redirect(add_foodstyle)
def display_foodstyle(request):
    data = Style_Db.objects.all()
    return render(request,"Display_FoodStyle.html",{"data":data})
def edit_foodstyle(request,fs_id):
    data = Style_Db.objects.get(id = fs_id)
    return render(request,"Edit_FoodStyle.html",{"data":data})
def update_foodstyle(request,fs_id):
    if request.method == "POST":
        a = request.POST.get("foodstyle")
        b = request.POST.get("description")

        try:
            img = request.FILES['fs_img']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = Style_Db.objects.get(id = fs_id).Style_Image
        Style_Db.objects.filter(id = fs_id).update(Food_Style = a,Description = b,Style_Image = file)
        messages.success(request,"Food Style Updated..!")
        return redirect(display_foodstyle)
def delete_foodstyle(req,fs_id):
    data = Style_Db.objects.filter(id = fs_id)
    data.delete()
    messages.warning(req,"Food Style removed..!")
    return redirect(display_foodstyle)

def add_food(req):
    data = Style_Db.objects.all()
    return render(req,"Add_Food.html",{"data":data})
def save_food(request):
    if request.method == 'POST':
        a = request.POST.get("style")
        b = request.POST.get("fname")
        c = request.POST.get("description")
        d = request.POST.get("quantity")
        e = request.POST.get("mrp")
        f = request.FILES['img1']
        g = request.FILES['img2']

        obj = Food_Db(Style = a,Food_Name = b,Food_Description = c,Quantity = d,MRP = e,Image1 = f,Image2 = g)
        obj.save()
        messages.success(request,"Food added..!")
        return redirect(add_food)
def display_food(req):
    data = Food_Db.objects.all()
    return render(req,"Display_Food.html",{"data":data})
def edit_food(req,fo_id):
    fo = Style_Db.objects.all()
    data = Food_Db.objects.get(id = fo_id)
    return render(req,"Edit_Food.html",{"data":data,"fo":fo})
def update_food(request,fo_id):
    if request.method == 'POST':
        a = request.POST.get("style")
        b = request.POST.get("fname")
        c = request.POST.get("description")
        d = request.POST.get("quantity")
        e = request.POST.get("mrp")

        try:
            f = request.FILES['img1']
            fs = FileSystemStorage()
            file1 = fs.save(f.name,f)
        except MultiValueDictKeyError:
            file1 = Food_Db.objects.get(id=fo_id).Image1

        try:
            g = request.FILES['img2']
            fs = FileSystemStorage()
            file2 = fs.save(g.name,g)
        except MultiValueDictKeyError:
            file2 = Food_Db.objects.get(id=fo_id).Image2

    Food_Db.objects.filter(id=fo_id).update(Style = a,Food_Name = b,Food_Description = c,Quantity = d,
                                            MRP = e,Image1 = file1,Image2 = file2)
    messages.success(request,"Food Updated..!")
    return redirect(display_food)
def delete_food(req,fo_id):
    data = Food_Db.objects.filter(id=fo_id)
    data.delete()
    messages.warning(req,"Food removed..!")
    return redirect(display_food)
def login_page(req):
    return render(req,"Login_Page.html")
def admin_login(request):
    if request.method == 'POST':
        un = request.POST.get("username")
        ps = request.POST.get("password")

        if User.objects.filter(username__contains = un).exists():
            user = authenticate(username=un,password=ps)
            if user is not None:
                login(request,user)
                request.session['username'] = un
                request.session['password'] = ps
                messages.success(request,"Welcome...!")
                return redirect(index_page)
            else:
                messages.error(request,"Incorrect password!")
                return redirect(login_page)
        else:
            messages.success(request,"Username does not exists!")
            return redirect(login_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request,"You are logged out!")
    return redirect(login_page)

def profile(req):
    return render(req,"Profile.html")
def display_contact(req):
    data = Contact_Db.objects.all()
    return render(req,"Display_Contact.html",{"data":data})
def delete_contact(req,con_id):
    data = Contact_Db.objects.filter(id = con_id)
    data.delete()
    return redirect(display_contact)









# Create your views here.
