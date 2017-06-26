from django.shortcuts import render, redirect, get_object_or_404, Http404
from .models import Chat, Message
from django.contrib import auth
from .forms import MessageForm
from rest_framework.views import APIView


def chat_screen(request):
    args = {}
    args['chats'] = Chat.objects.filter(members=auth.get_user(request))
    return render(request, 'lowMes/ChatScreen/main.html', args)


def this_chat(request, chat_id):
    args = {}
    try:
        args['chat'] = get_object_or_404(Chat, pk=chat_id, members=auth.get_user(request))
    except Http404:
        return render(request, 'ERROR_PERMISSION.html', args)
    args['messages'] = Message.objects.filter(chat__pk=chat_id)
    if auth.get_user(request).username:
        message_form = MessageForm
        args['message_form'] = message_form
    else:
        args['message_form'] = None
    return render(request, 'lowMes/ThisChat/main.html', args)


def new_message(request, chat_id):
    try:
        args['chat'] = get_object_or_404(Chat, pk=chat_id, members=auth.get_user(request))
    except Http404:
        return render(request, 'ERROR_PERMISSION.html')
    if request.POST:
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.chat = Chat.objects.get(id=chat_id)
            comment.author = auth.get_user(request)
            form.save()
    return redirect('/lowmes/chat'+chat_id+'/')
