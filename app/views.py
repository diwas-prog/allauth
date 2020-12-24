from django.views.generic import TemplateView
from django.shortcuts import render
from django.urls import reverse
from django.core.mail import send_mail
from app.forms import NewUserForm 

# def index(request):
#     return render(request,'index.html')

# def contact(request):
#     if request.method == "POST":
#         message_name = request.POST['message-name']
#         message_email = request.POST['message-email']
#         message_phone = request.POST['message-phone']
#         message = request.POST['message']
#         send_mail(
#             message_name,                #subject
#             message,                     #email body
#             message_email,               #from 
#             ['visions1890@gmail.com'],   #to
#             fail_silently = False)
#         subject_user = 'Welcome to FINSENTIAL!'
#         message_user = 'Thanks for writing to us, we will get back to you soon!' 
#         send_mail(
#             subject_user, 
#             message_user, 
#             'visions1890@gmail.com', 
#             [message_email], 
#             fail_silently = False)

#         return render(request,'contact.html', {'message_name': message_name})
#     else:
#         return render(request,'contact.html', {})


# def users(request):
#     form = NewUserForm()

#     if request.method == "POST":
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#             return index(request)
#         else:
#             print('ERROR FORM INVALID')

#     return render(request,'users.html',{'form':form})
 