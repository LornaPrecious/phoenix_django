from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name = "index"),
    path("aboutus/", views.aboutus, name = "aboutus"),
    path("contactus/", views.contactus, name = "contactus"),
    path("products/", views.products, name = "products"),
    path("<int:id>", views.productsid, name = "productsid") #dynamic pages in terms of linking
]