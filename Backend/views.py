from django.shortcuts import render, redirect

from Backend.models import categorydb, itemsdb
from Frontend.models import contactUsdb, userdb

from django.core.files.storage.filesystem import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.contrib import messages

# Create your views here.
def addcategorypage(req):
    return render(req, "category.html")


def indexpage(req):
    return render(req, "index.html")


def displaycategorypage(req):
    cat_data = categorydb.objects.all()
    return render(req, "displaycategory.html", {'data': cat_data})


def savecategorydata(req):
    if req.method=="POST":
        c_name = req.POST.get('category_name')
        c_desc = req.POST.get('category_desc')
        c_img = req.FILES['category_image']

        category_OBJ = categorydb(CategoryName=c_name, CategoryDescription=c_desc, CategoryImage=c_img)
        category_OBJ.save()
        messages.success(req, "Category added")
        return redirect(addcategorypage)

def editcategorypage(req, cat_id):
    cat_data = categorydb.objects.get(id=cat_id)
    return render(req, "EditCategory.html", {'data': cat_data})


def updatecategorydeatils(req, ctgry_id):
    if req.method == "POST":
        c_name = req.POST.get('category_name')
        c_desc = req.POST.get('category_desc')
        try:
            c_img = req.FILES['category_image']
            fs = FileSystemStorage()
            New_img = fs.save(c_img.name, c_img)
        except MultiValueDictKeyError:
            New_img = categorydb.objects.get(id=ctgry_id).CategoryImage

        categorydb.objects.filter(id=ctgry_id).update(CategoryName=c_name, CategoryDescription=c_desc, CategoryImage=New_img)
        messages.success(req, "Category Upated")

        return redirect(displaycategorypage)


def deletecategorydata(req, ctgry_id):
    ctgry_data = categorydb.objects.filter(id=ctgry_id)
    ctgry_data.delete()
    messages.warning(req, "Category removed")

    return redirect(displaycategorypage)

def additemspage(req):
    category_data = categorydb.objects.all()
    return render(req, "additems.html", {'data': category_data})

def saveitemdata(req):
    if req.method == "POST":
        ica = req.POST.get('item_category')
        ina = req.POST.get('item_name')
        ipr = req.POST.get('item_price')
        img1 = req.FILES['image_1']
        img2 = req.FILES['image_2']
        idesc = req.POST.get('item_desc')

        item_OBJ = itemsdb(ItemCategory=ica, ItemName=ina, ItemPrice=ipr, Image1=img1, Image2=img2, ItemDescription=idesc)

        item_OBJ.save()
        messages.success(req, "product added")

        return redirect(additemspage)


def displayitemspage(req):
    items_data = itemsdb.objects.all()
    return render(req, "displayitems.html", {'data': items_data})

def edititemspage(req, item_id):
    items_data_all = itemsdb.objects.all()
    item_data = itemsdb.objects.get(id=item_id)
    return render(req, "edititems.html", {'data': item_data, 'all_data': items_data_all})


def updateitemsdata(req, item_id):
    if req.method == "POST":
        ica = req.POST.get('item_category')
        ina = req.POST.get('item_name')
        ipr = req.POST.get('item_price')
        idesc = req.POST.get('item_desc')
        try:
            img1 = req.FILES['image_1']
            fs = FileSystemStorage()
            new_img1 = fs.save(img1.name, img1)
        except MultiValueDictKeyError:
            new_img1 = itemsdb.objects.get(id=item_id).Image1

        try:
            img2 = req.FILES['image_2']
            fs = FileSystemStorage()
            new_img2 = fs.save(img2.name, img2)
        except MultiValueDictKeyError:
            new_img2 = itemsdb.objects.get(id=item_id).Image2

        itemsdb.objects.filter(id=item_id).update(ItemCategory=ica, ItemName=ina, ItemPrice=ipr, Image1=new_img1, Image2=new_img2, ItemDescription=idesc)
        messages.success(req, "product updated")

        return redirect(displayitemspage)


def deleteitemsdata(req, item_id):
    item_data = itemsdb.objects.filter(id=item_id)
    item_data.delete()
    messages.warning(req, "product romoved")

    return redirect(displayitemspage)

def contactdata(req):
    message_data = contactUsdb.objects.all()
    return render(req, "Contactinfo.html", {'data': message_data})


def deletecontactdata(req, msg_id):
    data = contactUsdb.objects.filter(id=msg_id)
    data.delete()
    messages.warning(req, "Message Deleted")
    return redirect(contactdata)

def registeredusers(req):
    reg_data = userdb.objects.all()
    return render(req, "registeredusers.html", {'data': reg_data})

def deleteregisteredusers(req, user_id):
    data = userdb.objects.filter(id=user_id)
    data.delete()
    messages.warning(req, "User Removed")
    return redirect(registeredusers)


def adminloginpage(req):
    return render(req, "adminlogin.html")


def adminloginvalidate(req):
    if req.method == "POST":
        un = req.POST.get('uname')
        pswd = req.POST.get('password')

        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un, password=pswd)

            if x is not None:
                login(req, x)
                user_id = req.user.id
                user_email = User.objects.get(id=user_id).email
                req.session['username'] = un
                req.session['password'] = pswd
                req.session['email'] = user_email
                messages.success(req, "Welcome ")
                return redirect(indexpage)
            else:
                messages.error(req, "Invalid Credentials")
                return redirect(adminloginpage)
        else:
            messages.warning(req, "check your username and password")
            return redirect(adminloginpage)


def adminlogout(req):
    del req.session['username']
    del req.session['password']
    del req.session['email']
    messages.success(req, "Logged out")
    return redirect(adminloginpage)




