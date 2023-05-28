from typing import Any
from rest_framework.views import APIView, status, Response
from core.managers.product_manager import ProductManager
from core.models.product import Product
from core.models.image import Image

class ProductFiltersView(APIView):

    def __init__(self, **kwargs: Any) -> None:
        self.product_mgr = ProductManager()

    def get(self, request):

        product_objs = self.product_mgr.load_all()

        unique_values = {}
        
        for field in Product._meta.fields:
            field_name = field.name
            values = product_objs.values_list(field_name, flat=True).distinct()
            unique_values[field_name] = list(values)

    
        image_list = Image.objects.all().values_list('url', flat=True)

        
        unique_values['images'] = list(image_list)

        if not unique_values:
            return Response({"error": "Please try again"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(unique_values, status=status.HTTP_200_OK)