from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu", views.our_menu, name="our_menu"),
    path("mycart", views.cart, name="mycart"),
    path("add2chart", views.add2chart, name="add2chart"),
    path("calc_total", views.calc_total, name="calc_total"),
    path("changePrice", views.changePrice, name="changePrice"),
    path("checkout", views.checkout, name="checkout"),

    path("login", views.login_page, name="login"),
    path("register", views.register_page, name="register"),
    path("logout", views.logout_page, name="logout"),
]
