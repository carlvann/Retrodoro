from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_page, name="logout"),
    path("register/", views.registration_page, name="register"),
    path("retrodoro/", views.retrodoro, name="retrodoro"),

]
