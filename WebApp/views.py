from django.shortcuts import render,redirect
from ResApp.models import Food_Db,Style_Db
from WebApp.models import Contact_Db,Login_Db,Cart_Db,Order_Db
import razorpay
from django.contrib import messages


def home_page(request):
    name = request.session.get("Name")
    count = Cart_Db.objects.filter(Holder = name).count()
    style = Style_Db.objects.all()
    food = Food_Db.objects.all()
    return render(request,"Home1.html",{"style":style,"food":food,"count":count})
def food_list(request):
    style = Style_Db.objects.all()
    food = Food_Db.objects.all()
    name = request.session["Name"]
    count = Cart_Db.objects.filter(Holder = name).count()
    return render(request,"Food_List.html",{"style":style,"food":food,"count":count})
def food_filter(request,sty_name):
    data = Food_Db.objects.filter(Style = sty_name)
    name = request.session["Name"]
    count = Cart_Db.objects.filter(Holder = name).count()
    return render(request,"Food_Filter.html",{"data":data,"count":count})
def single_food(request,fo_id):
    name = request.session["Name"]
    count = Cart_Db.objects.filter(Holder = name).count()
    data = Food_Db.objects.get(id = fo_id)
    return render(request,"Single_Food.html",{"data":data,"count":count})
def contact(request):
    name = request.session["Name"]
    count = Cart_Db.objects.filter(Holder = name).count()
    return render(request,"Contact.html",{"count":count})
def save_contact(request):
    if request.method == 'POST':
        a = request.POST.get("name")
        b = request.POST.get("email")
        c = request.POST.get("mobile")
        d = request.POST.get("message")

        obj = Contact_Db(Name = a,Email = b,Mobile = c,Message = d)
        obj.save()
        return redirect(contact)
def sign_page(request):
    return render(request,"Sign_Page.html")
def sign_in(request):
    return render(request,"Sign_In.html")
def save_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        password1 = request.POST.get("pass")
        re_password = request.POST.get("re_pass")

        obj = Login_Db(Name = name,Email = email,Mobile = mobile,
                       Password = password1,Re_Password = re_password)
        if Login_Db.objects.filter(Name = name).exists():
            messages.warning(request,"Username already exists..!")
            return redirect(sign_page)
        elif Login_Db.objects.filter(Email = email).exists():
            messages.warning(request,"Email Address already exists..!")
            return redirect(sign_page)
        elif Login_Db.objects.filter(Mobile = mobile).exists():
            messages.warning(request,"Mobile Number already in use...!")
            return redirect(sign_page)
        obj.save()
        return redirect(sign_in)
def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get("username")
        user_password = request.POST.get("password")
        if Login_Db.objects.filter(Name = user_name,Password = user_password).exists():
            request.session["Name"] = user_name
            request.session["Password"] = user_password
            messages.success(request,"Welcome.....")
            return redirect(home_page)
        else:
            messages.error(request,"Incorrect Password!")
            return redirect(sign_in)

    else:
        messages.success(request,"Username does not exists!")
        return redirect(sign_in)

def delete_login(request):
    del request.session["Name"]
    del request.session["Password"]
    messages.warning(request,"You are logged out...!")
    return redirect(sign_in)
def cart(request):
    name = request.session["Name"]
    count = Cart_Db.objects.filter(Holder = name).count()
    filter = Cart_Db.objects.filter(Holder = name)
    sum=0
    for i in filter:
        sum = sum + i.Total_Price
    print(sum)
    if sum > 1000:
        shipping = 50
    else:
        shipping = 100
    total = shipping+sum
    return render(request,"cart.html",{"filter":filter,"sum":sum,"shipping":shipping,"total":total,"count":count})
def save_cart(request):
    if request.method == "POST":
        price = request.POST.get("price")
        total = request.POST.get("total")
        name = request.POST.get("name")
        f_name = request.POST.get("f_name")
        f_img = request.POST.get("img")
        qty = request.POST.get("qty")

        obj = Cart_Db(Quantity = qty,Price = price,Total_Price = total,Holder = name,Name_Food = f_name,Image_Food = f_img)
        obj.save()
        return redirect(home_page)
def delete_cart(request,car_id):
    data = Cart_Db.objects.filter(id = car_id)
    data.delete()
    return redirect(cart)
def checkout(request):
    name = request.session["Name"]
    count = Cart_Db.objects.filter(Holder = name).count()
    filter = Cart_Db.objects.filter(Holder = name)
    sum=0
    for i in filter:
        sum = sum + i.Total_Price
    print(sum)
    if sum > 1000:
        shipping = 50
    else:
        shipping = 100
    total = shipping+sum
    return render(request,"checkout.html",{"filter":filter,"sum":sum,"shipping":shipping,"total":total,"name":name,"count":count})
def save_order(request):
    if request.method == "POST":
        name = request.POST.get("name")
        place = request.POST.get("place")
        address = request.POST.get("address")
        state = request.POST.get("state")
        order = request.POST.get("order")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        country = request.POST.get("country")
        code = request.POST.get("code")
        total = request.POST.get("total")

        obj = Order_Db(Name = name,Place = place,Address = address,State = state,Order = order,
                       Email = email,Mobile = mobile,Country = country,Code = code,Total = total)
        obj.save()
        return redirect(payment)
def payment(request):
    customer = Order_Db.objects.order_by("-id").first()

    payy = customer.Total

    amount = int(payy*100)

    pay_str = str(amount)
    for i in pay_str:
        print(i)
    if request.method == "POST":
        currency = "INR"
        client = razorpay.Client(auth=('rzp_test_C7ztg4x7jmjoLs','z7WOqqTsGgHiRHYE1NSptK3m'))
        payment = client.order.create({"amount":amount,"currency":currency})
    return render(request,"Payment.html",{"customer":customer,"pay_str":pay_str})







# Create your views here.
