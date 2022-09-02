from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.index,name="index"),
    path('succeed/',views.succeed),
    path('show_all/',views.show_all),
    path('generateInvoice/<int:id>',views.generate),
]