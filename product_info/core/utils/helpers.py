import requests
from rest_framework import serializers
from core.models.product import Product
from core.models.image import Image
from core.models.comment import Comment
import requests

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('url',)

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'discountPercentage', 'rating', 'stock', 'brand', 'category', 'thumbnail', 'images')

# Fetch and save product data
def fetch_and_save_products():
    product_url = "https://dummyjson.com/products?limit=200"
    response = requests.get(product_url)
    if response.status_code == 200:
        product_data = response.json().get('products')
        product_serializer = ProductSerializer(data=product_data, many=True)
        if product_serializer.is_valid():
            product_serializer.save()
        else:
            errors = product_serializer.errors
    else:
        print("Failed to fetch product data")

# Call the function to fetch and save the products
fetch_and_save_products()
