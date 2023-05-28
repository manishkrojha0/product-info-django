from core.models.comment import Comment
from core.models.product import Product
from core.managers.image_manager import ImageManager
from core.managers.product_manager import ProductManager
from core.serializers.product_serializer import ProductSerializer
from core.managers.comment_manager import CommentManager


class ProductInfoManager(object):

    def __init__(self) -> None:
        self.image_mgr = ImageManager()
        self.product_mgr = ProductManager()
        self.cmt_mgr = CommentManager()

    def parse_and_save_products(self, product_data):
        if not product_data:
            return None
        _list_prod_objs = []
        for _product in product_data:
            title = _product.get('title')
            description = _product.get('description')
            price = _product.get('price')
            discountPercentage = _product.get('discountPercentage')
            rating = _product.get('rating')
            stock = _product.get('stock')
            brand = _product.get('brand')
            category = _product.get('category')
            thumbnail = _product.get('thumbnail')
            images = _product.get('images')
            _obj_product = Product(
                title=title,
                description=description,
                price=price,
                discountPercentage=discountPercentage,
                rating=rating,
                stock=stock,
                brand=brand,
                category=category,
                thumbnail=thumbnail
            )
            _obj_product.save()
            _list_prod_objs.append(_obj_product)

        _image_list = []

        for index, product in enumerate(_list_prod_objs):
            product_id = product.id
            obj = self.image_mgr.save_images(product_id=product_data[index]['id'], data=product_data[index]['images'])


        response = ProductSerializer(data=_list_prod_objs, many=True)
        print(response)
        if response.is_valid():
            return response
        return None
