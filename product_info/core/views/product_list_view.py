from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.paginator import Paginator
from core.models.product import Product
from core.serializers.product_serializer import ProductSerializer
from django.db.models import Q

class ProductListAPIView(APIView):
    def get(self, request):

        filters = {}
        for key, value in request.query_params.items():
            filters[key] = value.split(',')
        print(filters)

        query_set = Product.objects.all()
        print(len(query_set))

        for key, values in filters.items():

            query_set = query_set.filter(**{key + '__in': values})

        print(len(query_set))


        page = request.query_params.get('page', 1)
        limit = request.query_params.get('limit', 10)

        # Apply pagination
        paginator = Paginator(query_set, limit)
        paginated_products = paginator.get_page(page)

        print(paginated_products)

        # Serialize the paginated products
        serializer = ProductSerializer(paginated_products, many=True)

        return Response(serializer.data)
