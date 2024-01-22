from django.urls import path
from Frontend import views

urlpatterns = [
    path('HomePage/', views.HomePage, name="HomePage"),
    path('AllProductsPage/', views.AllProductsPage, name="AllProductsPage"),
    path('ProductCategorySortedPage/<cat_name>/', views.ProductCategorySortedPage, name="ProductCategorySortedPage"),
    path('ContactUsPage/', views.ContactUsPage, name="ContactUsPage"),
    path('SaveContactusData/', views.SaveContactusData, name="SaveContactusData"),
    path('AboutPage/', views.AboutPage, name="AboutPage"),
    path('ServicesPage/', views.ServicesPage, name="ServicesPage"),
    path('ProductDetailsPage/<int:p_id>/', views.ProductDetailsPage, name="ProductDetailsPage"),

    path('UserRegisterLoginPage/', views.UserRegisterLoginPage, name="UserRegisterLoginPage"),
    path('SaveUserData/', views.SaveUserData, name="SaveUserData"),
    path('UserLogin/', views.UserLogin, name="UserLogin"),
    path('UserLogout/', views.UserLogout, name="UserLogout"),
    path('UserProfilePage/<username>/', views.UserProfilePage, name="UserProfilePage"),
    path('EditUserData/<int:user_id>/', views.EditUserData, name="EditUserData"),

    path('SaveCartData/', views.SaveCartData, name="SaveCartData"),
    path('CartPage/', views.CartPage, name="CartPage"),
    path('DeleteCartItems/<int:c_id>/', views.DeleteCartItems, name="DeleteCartItems"),

    path('CheckoutPage/', views.CheckoutPage, name="CheckoutPage"),
    path('SaveCheckoutData/', views.SaveCheckoutData, name="SaveCheckoutData"),
]