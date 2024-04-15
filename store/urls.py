from store.views.login import logout
from django.urls import path
from .views import Login, Home, Signup,logout,Cart,Checkout,Order_View

urlpatterns = [
    path('', Home.as_view(),name="home"),
    path('signup/', Signup.as_view(),name="signup"),
    path('login/', Login.as_view() ,name="login"),
    path('logout/',logout,name='logout'),
    path('cart/',Cart.as_view(),name='cart'),
    path('check-out',Checkout.as_view(),name='check-out'),
    path('orders',Order_View.as_view(),name='orders'),
]
