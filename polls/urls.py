from django.urls import path

from static import views

urlpatterns = [

    path('forget_pwd/', views.forget_pwd),
]
