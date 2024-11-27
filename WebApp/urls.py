from django.urls import path
from WebApp import views


urlpatterns = [
    path("home_page/",views.home_page,name = "home_page"),
    path("food_list/",views.food_list,name = "food_list"),
    path("food_filter/<sty_name>/",views.food_filter,name = "food_filter"),
    path("single_food/<int:fo_id>/",views.single_food,name = "single_food"),
    path("contact/",views.contact,name = "contact"),
    path("save_contact/",views.save_contact,name = "save_contact"),
    path("sign_page/",views.sign_page,name = "sign_page"),
    path("",views.sign_in,name = "sign_in"),
    path("save_login/",views.save_user,name="save_login"),
    path("user_login/",views.user_login,name="user_login"),
    path("delete_login/",views.delete_login,name="delete_login"),
    path("cart/",views.cart,name="cart"),
    path("save_cart/",views.save_cart,name="save_cart"),
    path("delete_cart/<int:car_id>/",views.delete_cart,name="delete_cart"),
    path("checkout/",views.checkout,name="checkout"),
    path("save_order/",views.save_order,name="save_order"),
    path("payment/",views.payment,name="payment"),

]
