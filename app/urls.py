from django.urls import path
from app import views
urlpatterns = [
    path('',views.home,name='home'),
    path('pixel',views.pixel,name='register'),
    path('wtb',views.wtb,name='whatthebuzz'),
    path('success',views.sucess,name='success'),
    # path('movie',views.mn,name='movie'),
    # path('speaker',views.speaker,name='speaker'),
    path('code',views.code,name='codeoclock'),
    path('clowncanard',views.cc,name='theclowncanard'),
]
