from tkinter.font import names

from django.urls import path
from . import views

urlpatterns =[
    # path('product_list',views.product_list,name='product_list'),
    # path('<slug:slug>',views.product_details,name='product_detail'),
    path('product_list/', views.productListView.as_view(), name='product_list'),

    path('<str:slug>', views.productDetailView.as_view(), name='product_detail'),

]