from rest_framework.serializers import ModelSerializer
from lowMes.models import Chat, Message


class ChatListSerializer(ModelSerializer):
    class Meta:
        model = Chat
        fields = [
            'name',
            'members',
        ]

class ThisChatSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'