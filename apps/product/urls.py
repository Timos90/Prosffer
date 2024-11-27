from django.urls import path
from .views import ProductListView, product_search, product_list_ajax


app_name = 'product-urls'
urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('products/search/', product_search, name='product-search'),
    path('product-list-ajax/', product_list_ajax, name='product_list_ajax'),
]