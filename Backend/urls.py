from django.urls import path
from Backend import views

urlpatterns = [
    path('indexpage/', views.indexpage, name="indexpage"),

    path('addcategorypage/', views.addcategorypage, name="addcategorypage"),
    path('displaycategorypage/', views.displaycategorypage, name="displaycategorypage"),
    path('savecategorydata/', views.savecategorydata, name="savecategorydata"),
    path('editcategorypage/<int:cat_id>/', views.editcategorypage, name="editcategorypage"),
    path('updatecategorydeatils/<int:ctgry_id>/', views.updatecategorydeatils, name="updatecategorydeatils"),
    path('deletecategorydata/<int:ctgry_id>/', views.deletecategorydata, name="deletecategorydata"),

    path('additemspage/', views.additemspage, name="additemspage"),
    path('saveitemdata/', views.saveitemdata, name="saveitemdata"),
    path('displayitemspage/', views.displayitemspage, name="displayitemspage"),
    path('edititemspage/<int:item_id>/', views.edititemspage, name="edititemspage"),
    path('updateitemsdata/<int:item_id>/', views.updateitemsdata, name="updateitemsdata"),
    path('deleteitemsdata/<int:item_id>/', views.deleteitemsdata, name="deleteitemsdata"),

    path('contactdata/', views.contactdata, name="contactdata"),
    path('deletecontactdata/<int:msg_id>/', views.deletecontactdata, name="deletecontactdata"),
    path('registeredusers/', views.registeredusers, name="registeredusers"),
    path('deleteregisteredusers/<int:user_id>/', views.deleteregisteredusers, name="deleteregisteredusers"),

    path('adminloginpage/', views.adminloginpage, name="adminloginpage"),
    path('adminloginvalidate/', views.adminloginvalidate, name="adminloginvalidate"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),

]