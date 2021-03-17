from django.urls import path, include
from . import views

urlpatterns = [
    
    
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('store/',views.store,name='store'),
    path('cart/',views.cart,name='cart'),
]