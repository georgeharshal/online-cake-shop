from django.shortcuts import render, redirect
from Backend.models import categorydb, itemsdb
from Frontend.models import contactUsdb, userdb, cartdb, checkoutdb
from django.core.files.storage.filesystem import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages

# Create your views here.
def HomePage(req):
    cat_data = categorydb.objects.all()
    if 'Name' in req.session:
        quantity = 0
        data = cartdb.objects.filter(Username=req.session['Name'])
        for i in data:
            quantity += i.Quantity
        return render(req, "Home.html", {'data': cat_data, 'quantity': quantity})
    else:
        return render(req, "Home.html", {'data': cat_data})
def AllProductsPage(req):
    prod_data = itemsdb.objects.all()
    if 'Name' in req.session:
        quantity = 0
        data = cartdb.objects.filter(Username=req.session['Name'])
        for i in data:
            quantity += i.Quantity
        return render(req, "AllProducts.html", {'data': prod_data, 'quantity': quantity})
    else:
        return render(req, "AllProducts.html", {'data': prod_data})


def ProductCategorySortedPage(req, cat_name):
    prod_data = itemsdb.objects.filter(ItemCategory=cat_name)
    if 'Name' in req.session:
        quantity = 0
        data = cartdb.objects.filter(Username=req.session['Name'])
        for i in data:
            quantity += i.Quantity
        return render(req, "ProductCategorySorted.html", {'data': prod_data, 'quantity': quantity})
    else:
        return render(req, "ProductCategorySorted.html", {'data': prod_data})


def ContactUsPage(req):
    if 'Name' in req.session:
        quantity = 0
        data = cartdb.objects.filter(Username=req.session['Name'])
        for i in data:
            quantity += i.Quantity
        return render(req, "Contact.html", {'quantity': quantity})
    else:
        return render(req, "Contact.html")


def SaveContactusData(req):
    if req.method=="POST":
        na = req.POST.get('c_name')
        em = req.POST.get('c_email')
        sub = req.POST.get('c_subject')
        msg = req.POST.get('c_message')

        contact_OBJ = contactUsdb(Name=na, Email_Id=em, Subject=sub, Message=msg)

        contact_OBJ.save()
        messages.success(req, "Message sent")
        return redirect(ContactUsPage)


def AboutPage(req):
    if 'Name' in req.session:
        quantity = 0
        data = cartdb.objects.filter(Username=req.session['Name'])
        for i in data:
            quantity += i.Quantity
        return render(req, "About.html", {'quantity': quantity})
    else:
        return render(req, "About.html")


def ServicesPage(req):
    if 'Name' in req.session:
        quantity = 0
        data = cartdb.objects.filter(Username=req.session['Name'])
        for i in data:
            quantity += i.Quantity
        return render(req, "Services.html", {'quantity': quantity})
    else:
        return render(req, "Services.html")


def ProductDetailsPage(req, p_id):
    prod_data = itemsdb.objects.get(id=p_id)
    if 'Name' in req.session:
        quantity = 0
        data = cartdb.objects.filter(Username=req.session['Name'])
        for i in data:
            quantity += i.Quantity
        return render(req, "ProductDetails.html", {'data': prod_data, 'quantity': quantity})
    else:
        return render(req, "ProductDetails.html", {'data': prod_data})


def UserRegisterLoginPage(req):
    return render(req, "RegistrationLogin.html")


def SaveUserData(req):
    if req.method == "POST":
        un = req.POST.get('u_name')
        em = req.POST.get('email')
        ps = req.POST.get('pass1')
        img = req.FILES['u_img']

        user_OBJ = userdb(Username=un, EmailID=em, Password=ps, ProfileImage=img)
        user_OBJ.save()
        messages.success(req, "User Registered")
        return redirect(UserRegisterLoginPage)


def UserLogin(req):
    if req.method == "POST":
        un = req.POST.get('user_name')
        ps = req.POST.get('u_pass')

        if userdb.objects.filter(Username=un, Password=ps).exists():
            req.session['Name']=un
            req.session['Password']=ps
            messages.success(req, "Welcome")
            return redirect(HomePage)
        else:
            messages.error(req, "Invalid Username or Password")
            return redirect(UserRegisterLoginPage)
    else:
        messages.warning(req, "Please check your username")
        return redirect(UserRegisterLoginPage)



def UserLogout(req):
    del req.session['Name']
    del req.session['Password']
    messages.warning(req, "Logged out")
    return redirect(UserRegisterLoginPage)


def UserProfilePage(req, username):
    user_data = userdb.objects.get(Username=username)
    if 'Name' in req.session:
        quantity = 0
        data = cartdb.objects.filter(Username=req.session['Name'])
        for i in data:
            quantity += i.Quantity
        return render(req, "UserProfile.html", {'data': user_data, 'quantity': quantity})
    else:
        return render(req, "UserProfile.html", {'data': user_data})


def EditUserData(req, user_id):
    if req.method == "POST":
        un = req.POST.get('u_name')
        em = req.POST.get('u_email')
        ps = req.POST.get('u_pass')
        try:
            img = req.FILES['u_img']
            fs = FileSystemStorage()
            new_img = fs.save(img.name, img)
        except MultiValueDictKeyError:
            new_img = userdb.objects.get(id=user_id).ProfileImage

        userdb.objects.filter(id=user_id).update(Username=un, EmailID=em, Password=ps, ProfileImage=new_img)
        messages.success(req, "Profile updated")
        return redirect(UserProfilePage, username=un)



def SaveCartData(req):

    if req.method == "POST":
        un = req.POST.get('u_name')
        pn = req.POST.get('p_name')
        pr = req.POST.get('p_price')
        qn = req.POST.get('qnty')
        tp = req.POST.get('t_price')

        cart_OBJ = cartdb(Username=un, ProductName=pn, Quantity=qn, Price=pr, TotalPrice=tp)

        cart_OBJ.save()
        messages.success(req, "Added to cart")
        return redirect(HomePage)


def CartPage(req):
    cart_data = cartdb.objects.filter(Username=req.session['Name'])
    total = 0
    quantity = 0
    for i in cart_data:
        total += i.TotalPrice
        quantity += i.Quantity
    return render(req, "Cart.html", {'data': cart_data, 'total': total, 'quantity': quantity})

def DeleteCartItems(req, c_id):
    cart_data = cartdb.objects.filter(id=c_id)
    cart_data.delete()
    messages.warning(req, "Product removed")
    return redirect(CartPage)



def CheckoutPage(req):
    checkout_data = cartdb.objects.filter(Username=req.session['Name'])
    useremailid = userdb.objects.get(Username=req.session['Name']).EmailID
    total = 0
    quantity = 0
    for i in checkout_data:
        total += i.TotalPrice
        quantity += i.Quantity
    return render(req, "Checkout.html", {'data': checkout_data, 'total': total, 'quantity': quantity, 'useremailid': useremailid})


def SaveCheckoutData(req):
    if req.method == "POST":
        un = req.POST.get('name')
        em = req.POST.get('email')
        ad = req.POST.get('address')
        cty = req.POST.get('city')
        cnt = req.POST.get('country')
        zc = req.POST.get('zipcode')
        mob = req.POST.get('tel')
        on = req.POST.get('notes')

        checkout_OBJ = checkoutdb(Name=un, Email=em, Address=ad, City=cty, Country=cnt, ZipCode=zc, MobileNo=mob, OrderNotes=on)
        checkout_OBJ.save()
        messages.success(req, "Order Placed")
        return redirect(HomePage)

