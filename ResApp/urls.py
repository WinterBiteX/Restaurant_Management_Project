from django.urls import path
from ResApp import views

urlpatterns = [
    path("index/",views.index_page,name = "index"),
    path("add_foodstyle/",views.add_foodstyle,name = "add_foodstyle"),
    path("save_foodstyle/",views.save_foodstyle,name = "save_foodstyle"),
    path("display_foodstyle/",views.display_foodstyle,name = "display_foodstyle"),
    path("edit_foodstyle/<int:fs_id>/",views.edit_foodstyle,name = "edit_foodstyle"),
    path("update_foodstyle/<int:fs_id>/",views.update_foodstyle,name = "update_foodstyle"),
    path("delete_foodstyle/<int:fs_id>/",views.delete_foodstyle,name = "delete_foodstyle"),
    path("add_food/",views.add_food,name = "add_food"),
    path("save_food/",views.save_food,name = "save_food"),
    path("display_food/",views.display_food,name = "display_food"),
    path("edit_food/<int:fo_id>/",views.edit_food,name = "edit_food"),
    path("update_food/<int:fo_id>/",views.update_food,name = "update_food"),
    path("delete_food/<int:fo_id>/",views.delete_food,name = "delete_food"),
    path("login_page/",views.login_page,name = "login_page"),
    path("admin_login/",views.admin_login,name="admin_login"),
    path("admin_logout/",views.admin_logout,name="admin_logout"),
    path("profile/",views.profile,name="profile"),
    path("display_contact/",views.display_contact,name="display_contact"),
    path("delete_contact/<int:con_id>/",views.delete_contact,name="delete_contact")
]
