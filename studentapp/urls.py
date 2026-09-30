from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_page,name='login'),
    path("form/",views.form_page,name="form"),
]
