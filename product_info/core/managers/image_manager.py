from core.models.image import Image
from core.serializers.image_serializer import ImageSerializer

class ImageManager(object):

    def __init__(self) -> None:
        pass

    def save_images(self, data, product_id):
        if not data:
            return None
        image_obj_list = []
        for image_url in data:
            image_obj = self.create_image(image_url, product_id=product_id)
            image_obj_list.append(image_obj.url)
        

        # res = ImageSerializer(data = image_obj_list, many=True)
        # if res.is_valid():
        #     print("hiiiiiiiiiiiiiiiiiiiii=================")
        #     return res.data
        return image_obj_list

    def create_image(self, url, product_id):
        if not url:
            return None
        image_obj = Image.objects.create(url=url, product_id=product_id)
        image_obj.save

        return image_obj
        