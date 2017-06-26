from rest_framework.generics import ListAPIView, RetrieveAPIView
from lowMes.models import Chat, Message
from .serializers import ChatListSerializer, ThisChatSerializer


class ChatListAPIView(ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatListSerializer


class ThisChatAPIView(ListAPIView):
    lookup_field = 'chat'
    queryset = Message.objects.all
    serializer_class = ThisChatSerializer
