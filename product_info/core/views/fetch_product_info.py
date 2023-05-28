from typing import Any
from rest_framework.views import APIView, Response, status
import requests
from core.utils.constants import FETCH_PRODUCTS_DATA_URL, PRODUCT_COMMENTS_URL
from core.managers.product_info_view_manager import ProductInfoManager


class ProductInfoViews(APIView):
    """Class for product infor request and response."""
    
    def __init__(self, **kwargs: Any) -> None:
        self.product_view_mgr = ProductInfoManager()

    def post(self, request):
        response = requests.get(FETCH_PRODUCTS_DATA_URL)
        json_data = response.json()

        # print(product_data)
        data = self.product_view_mgr.parse_and_save_products(product_data=json_data['products'])
        return Response(data=data, status=status.HTTP_201_CREATED)

    
