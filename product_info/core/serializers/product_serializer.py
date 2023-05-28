from rest_framework import serializers
from core.models.product import Product
from core.serializers.image_serializer import ImageSerializer

class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'discountPercentage', 'rating', 'stock', 'brand', 'category', 'thumbnail', 'images']
    
    def create(self, validated_data):
        images = validated_data.pop('images')
        data_dict = {}
        validated_data['images'] = []
        for url in images:

            url_serial = ImageSerializer(data={
                'url': url
            })
            if url_serial.is_valid():
                url_serial.save()
                
                validated_data['images'].append(url)
        return super().create(validated_data)

