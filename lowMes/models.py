from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Chat(models.Model):
    members = models.ManyToManyField(User)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class MessagesManager(models.Manager):
    def create_message(self, text, author, chat):
        message = self.create(text=text, author=author, chat=chat)
        return message

def file_upload(filename):
    """
        Как это вообще работает?
    """
    return ('lowMes/messages/files/'+filename)


class Message(models.Model):
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE, null=False)
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    file = models.FileField(upload_to=file_upload, null=True, blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    objects = MessagesManager()

    def publish(self):
        self.created_date = timezone.now()
        self.save()
