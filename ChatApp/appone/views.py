from .models import PhoneNumber, Message
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PhoneNumber,Receive
# Create your views here.
# myapp/views.py

from rest_framework import generics
from .models import Message
from .Serializer import MessageSerializer
from .consumers import ChatConsumer

def fun(request):
    if request.method == "POST":
        phone = request.POST.get('phone')
        if phone and len(phone) >= 10:
            obj, created = PhoneNumber.objects.get_or_create(phone=phone)
            if created:
                print("Login successful")
            else:
                print("You are already logged in")
            return redirect('chat')

    return render(request, "index.html")


# views.py


def send(request):
    print("sajdbajkfn")
    if request.method == "POST":
        msg = request.POST.get('msg')
        if msg and len(msg) > 1:
            message = Message(msg=msg)
            message.save()
            print("Message stored successfully:", msg)
    return redirect('chat')


def chat(request):
    
    messages = Message.objects.all()
    g=ChatConsumer.receive.data 
    
    return render(request, 'main.html', {'messages': messages,"data":g})

class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
# myapp/views.py


# def my_view(request):
#     text_input = request.GET.get('text_input', '')
#     return HttpResponse(f"Received text input: {text_input}")

# def fun(request):
#     if request.method == "POST":
#         phone=request.POST['phone']
#         if len(phone) >=10: 
#             obj=PhoneNumber.objects.all()
#             a=[]
#             for i in obj:
#                 a.append(i.phone)
#             msg=""
#             if phone not in a:
#                 obj=PhoneNumber(phone=phone)
#                 obj.save()
#                 print("login successfully")
                
#             else:
#                 print("your are not login")
#             return render(request, 'main.html')
#     return render(request,"index.html")
 # views.py

def main(request):
    messages = Message.objects.all()
    return render(request, 'main.html', {'messages': messages})

        
