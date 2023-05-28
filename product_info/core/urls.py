
from django.urls import path
from core.views.fetch_product_info import ProductInfoViews
from core.views.fetch_comments import FetchCommentsViews
from core.views.product_filters_view import ProductFiltersView
from core.views.product_list_view import ProductListAPIView

urlpatterns = [
    path('fetch-products/', ProductInfoViews.as_view(), name='fetch_products'),
    path('fetch-comments/', FetchCommentsViews.as_view(), name='fetch_comments'),
    path('product-filters/', ProductFiltersView.as_view(), name='product_list'),
    path('product-list/', ProductListAPIView.as_view(), name='product_filters'),
]