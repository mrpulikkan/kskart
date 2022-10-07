
import email
from symbol import parameters
from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Group

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


from .models import sample
from .forms import CreateUserForm


# Create your views here.

#-------index page------------------#
def index(request):
    items = sample.objects.order_by('-id')[:6]
    last_three = sample.objects.order_by('-id')[:3]
    context = {'items':items,'last_three':last_three}
    return render(request,'index.html',context)

#-------index ends here------------------#

#############################################
#             AUTHENTICATION                # 
#############################################

#-------registration --------------------#
def registration(request):

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='user')
            user.groups.add(group)
            
            txt = """<script>alert('Account is succesfully created !');window.location='/index/';</script>"""
            return HttpResponse(txt)
    else:
        form = CreateUserForm
    return render(request,'registration/register.html',{"form":form})


#-------registration ends------------------#


#-------userlogin starts --------------------#
def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #authenticating user
        try:
            user = authenticate(username=User.objects.get(email=username),password=password)
        except:
            user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            group = None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
        
            if group =='user':
                return redirect('/userhome')

            if group == 'admin':
                return redirect('/adminhome')

            if group == 'shg':
                return redirect('shghome')

            return redirect('/userhome')

        else:
            messages.info(request,"Username or Password is incorrect ! ")
            return redirect('/userlogin')

    return render(request,'registration/login.html')

#-------userlogin ends------------------#

def userlogout(request):
    logout(request)
    return redirect('/userlogin')


# ---------------Password reset starts ----------------#

# def password_reset_request(request):
#     if request.method == 'POST':
#         password_form = PasswordResetForm(request.POST)
#         if password_form.is_valid():
#             data = password_form.cleaned_data['email']
#             user_email = User.objects.filter(Q(email=data))
#             if user_email.exists():
#                 for user in user_email:
#                     subject = 'Password Reset'
#                     email_template_name = 'registration/password_message.txt'
#                     parameters = {
#                         'email' : user.email,
#                         'domaian':'http://127.0.0.1:7000/',
#                         'site_name':'KS_Kart',
#                         'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
#                         'token':default_token_generator.make_token(user),
#                         'protocol':'http'
#                     }
#                     email = render_to_string(email_template_name)
#                     try:
#                         send_mail(subject, parameters,email,'',[user.email],fail_silently=False)
#                     except:
#                         txt = """<script>alert('Invalid Header !');window.location='/password_request/';</script>"""
#                         return HttpResponse("ERROR 504")
#                     redirect('')
#     else:
#         password_form = PasswordResetForm()
#     context ={'password_form':password_form}
#     return render(request, 'registration/password_reset.html',context)


#############################################
#                 USER                      # 
#############################################

#-------userhome starts --------------------#
def userhome(request):
    return render(request,'user/userhome.html')

#-------userhome ends --------------------#


#############################################
#           ADMIN                          # 
#############################################

#---------Admin Home starts here------------#
def adminhome(request):
    return render(request,'admin/adminhome.html')
#---------Admin Home ends here--------------#


# ---------------sample function------------#
def sampleview(request):
    items = sample.objects.all()
    context = {'items':items}
    return render(request,'sampleview.html',context)





