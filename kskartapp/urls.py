from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('registration/',views.registration,name='registration'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('userlogout/',views.userlogout,name='userlogout'),
    path('password_reset/',auth_view.PasswordResetView.as_view(template_name='registration/password_reset.html'),name='password_reset'),
    path('password_reset_done/',auth_view.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete/',auth_view.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),

    path('userhome/',views.userhome,name='userhome'),

    path('adminhome/',views.adminhome,name='adminhome'),

    path('sample/',views.sampleview,name='sample'),
]
