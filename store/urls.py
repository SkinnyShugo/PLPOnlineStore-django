from django.urls import path, include
from .import  views
urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', views.store, name="store"),
    path('cart', views.cart_detail, name="cart_detail"),
    path('category/<slug:category_slug>', views.store, name="products_bycategory"),
    path('category/<slug:category_slug>/<slug:product_slug>', views.product_detail, name="product_detail"),
    path('cart/add/<int:product_id>', views.add_cart, name="add_cart"),
    path('cart/remove/<int:product_id>', views.cart_remove, name="cart_delete"),
    path('cart/remove_product/<int:product_id>', views.cart_remove_product, name="cart_product_remove"),
    path('thankyou/<int:order_id>', views.thank_you_page, name='thankyou')

]