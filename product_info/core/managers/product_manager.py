from core.serializers.product_serializer import ProductSerializer
from core.models.product import Product

class ProductManager(object):

    def __init__(self) -> None:
        pass

    def create(self, data):
        if not data:
            return None
        serialized_data = ProductSerializer(data=data)
        if serialized_data.is_valid():
            serialized_data.save()
            return serialized_data.data
        
        return None
    
    def load_all(self):
        objs = Product.objects.all()
        return objs
        