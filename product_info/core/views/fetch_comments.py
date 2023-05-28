from core.managers.comment_manager import CommentManager
from rest_framework.views import APIView, Response, status
import requests
from core.managers.product_manager import ProductManager
from core.utils.constants import PRODUCT_COMMENTS_URL
from core.serializers.comment_serializer import CommentSerializer

class FetchCommentsViews(APIView):

    def __init__(self) -> None:
        self.comment_mgr = CommentManager()
        self.product_mgr = ProductManager()
    
    def post(self, request):
        product_objs = self.product_mgr.load_all()
        print(len(product_objs))
        
        response_parse = []
        # Check the response status code
        for _product in product_objs:
            url = PRODUCT_COMMENTS_URL.format(product_id=_product.id)
            response = requests.get(url=url)
            if response.status_code != status.HTTP_200_OK:
                return Response({'error': 'Failed to fetch comments'}, status=response.status_code)

            try:
                json_body = response.json()
                comments = json_body.get('comments')
                if not comments:
                    continue
                _comment_resultants = self.comment_mgr.create_in_bulk(comments)

                dumy_check = CommentSerializer(data=_comment_resultants, many=True)
                if dumy_check.is_valid():
                    print(dumy_check.data)

                response_parse.append(_comment_resultants)

                if not _comment_resultants:
                    return Response({'error': 'Failed to fetch comments'}, status=status.HTTP_404_NOT_FOUND)        
            except ValueError:
                return Response({'error': 'Invalid response from comments API'}, status=status.HTTP_404_NOT_FOUND)
            
        result = []

        for _data in response_parse:
            for data in _data:
                result.append({
                    'id': data.id,
                    'body': data.body
                })
        
        if not result:
            return Response({'error': 'Invalid response from comments API'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(result, status=status.HTTP_201_CREATED)
        
