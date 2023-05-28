from core.models.comment import Comment
from core.serializers.comment_serializer import CommentSerializer
from core.serializers.user_serializer import UserSerializer
from core.models.custom_user import CustomUser


class CommentManager(object):
    """"Class of comment manager."""


    def create_in_bulk(self, data):
        """create comments"""
        # serializer = CommentSerializer(data=data, many=True)
        # if serializer.is_valid():
        #     serializer.save()
        #     return serializer.data
        _list = []
        for _data in data:
            _list.append(self.create_comment(_data))
            
        return _list
    
    def create_comment(self, data):
        user = data.get('user')
        user_id = user.get('id')
        username = user.get('username')
        obj = CustomUser(username=username)
        obj.save()
        _comment_obj = Comment(user=obj, postId_id=data.get('postId'), body=data.get('body'))
        _comment_obj.save()
        return _comment_obj
        # id = Pr
        # user_dict = {
        #     'id': user_id,
        #     'username': username
        # }

        # serializer_user = UserSerializer(data=user_dict)
        # if serializer_user.is_valid():
        #     serializer_user.save()
        # serializer_comment = CommentSerializer(data=data)
        # if serializer_comment.is_valid():
        #     serializer_comment.save()
        #     return serializer_comment.data
        
        return None
            



