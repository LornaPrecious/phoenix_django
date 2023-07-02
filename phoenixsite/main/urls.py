from django.urls import path
from . import views 

urlpatterns = [
    path("", views.home, name = "home"),
    path("home/", views.home, name = "home"),
    path("aboutus/", views.aboutus, name = "aboutus"),
    path("contactus/", views.contactus, name = "contactus"),
    path("products/", views.products, name = "products"),
    path("store/", views.store, name = "store")
    #path("<int:id>", views.productsid, name = "productsid") #dynamic pages in terms of linking
]