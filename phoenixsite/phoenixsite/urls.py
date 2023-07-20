"""
URL configuration for phoenixsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from productManagement import views as pv
from useraccount import views as v
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include("main.urls")),
    path('home/', include("main.urls")),
    path('aboutus/', include("main.urls")),
    path('contactus/', include("main.urls")),
    path('products/', pv.products, name = 'products'),
    path('store/',pv.store, name = 'store'),
    path('cart/', pv.cart, name = 'cart'),
    path('checkout/', pv.checkout, name = 'checkout'),
    
    path('register/', v.register, name ='register'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),                                           
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html',
        html_email_template_name='registration/password_reset_email.html'
    ), name='password-reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),
]
    #path('logout/', LogoutView.as_view(next_page='login'),name='logout'),




