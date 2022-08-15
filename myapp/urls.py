from django.urls import path
from .import views

urlpatterns=[
    path('product',views.productfn,name='product'),
     path('billing',views.billingfn,name='billing'),

]