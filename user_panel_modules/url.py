from django.urls import path
from . import views

urlpatterns= [
    path('',views.UserPanelDashboardPage.as_view(),name='dashboard'),
    path('edit-profile', views.EditUserProfilePage.as_view(), name='edit_pofile_page'),
    path('change-pass', views.ChangePassword.as_view(), name='change_password_page'),
    path('address-page', views.AddressEditPage.as_view(), name='edit_address_page'),
    path('user-basket', views.user_basket, name='user-basket'),
    path('remove-order-detail', views.remove_order_detail, name='remove-order-detail'),
    path('change-order-detail', views.change_order_details_count, name='change_order_details_count'),

]