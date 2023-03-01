from django.urls import path
from app import views
urlpatterns = [
    path('register',views.register,name='register'),
    path('success',views.sucess,name='success'),
    path('movie&speaker',views.mss,name='success'),
    path('code',views.code,name='codeoclock'),
    path('clowncanard',views.cc,name='theclowncanard'),
]
