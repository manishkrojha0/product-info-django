from core.models.comment import Comment
from core.serializers.user_serializer import UserSerializer
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'body', 'postId', 'user']
    

    # def create(self, validated_data):
    #     print(validated_data)
    #     return
    #     user_data = validated_data.pop('user')
    #     user_serializer = UserSerializer(data=user_data)
    #     if user_serializer.is_valid():
    #         user_instance = user_serializer.save()
    #         validated_data['user'] = user_instance
    #         return super().create(validated_data)
    #     else:
    #         # Handle invalid user data if needed
    #         pass


    # def create_in_bulk(self, data):
    #     user_data = {(item['user']['id'], item['user']['username']): item['user'] for item in data}
    #     print(user_data)
        # user_instances = {}
        # print(user_data, "jiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
        # for user_key, user_info in user_data.items():
        #     user_serializer = UserSerializer(data=user_info)
        #     if user_serializer.is_valid():
        #         user_instances[user_key] = user_serializer.save()
        #     else:
        #         # Handle invalid user data if needed
        #         pass

        # comments_data = []
        # for item in data:
        #     user_key = (item['user']['id'], item['user']['username'])
        #     user_instance = user_instances.get(user_key)
        #     if user_instance:
        #         item['user'] = user_instance
        #         comments_data.append(item)

        # serializer = CommentSerializer(data=comments_data, many=True)
        # if serializer.is_valid():
        #     serializer.save()
        #     return serializer.data

        # return None
