from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_login, name="customer_login"),
    path('register/', views.customer_register, name="customer_register"),
    path('logout/', views.customer_logout, name="customer_logout"),
    path('order_history/', views.orderHistory, name="order_history"),
    path('portal/', views.client_portal, name='portal'),
    path('portal1/', views.portal_admin, name='admin-portal'),
    path('add-products/', views.add_product, name="add-products"),
    path('product-list/', views.products, name="product-list"),
    path('docs/', views.docs, name="docs"),
    path('portal_login/', views.client_login, name='client_login'),
    path('portal_register/', views.client_register, name="client_register")

]