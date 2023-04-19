
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("sell/",views.sell_toy,name="sell"),
    path('ad_detail/<int:ad_id>/', views.ad_detail, name='ad_detail'),
    path('user_ads/',views.user_ads,name="user_ads"),
]