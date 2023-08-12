from django.shortcuts import render
from .models import Message

# Create your views here.
def index(request):
    message_list = Message.objects.all()

    return render(request, 'message/index.html', {'message_list': message_list})


def message_input(request):
    if request.method == 'POST':
        message_writer = request.POST['message_writer']
        message_content = request.POST['message_content']

        message = Message(message_writer=message_writer, message_content=message_content)
        message.save()

        return render(request, 'message/message_input.html', {'result': "메시지가 성공적으로 등록되었습니다.", 'message_writer': message_writer, 'message_content': message_content})
    return render(request, 'message/message_input.html')