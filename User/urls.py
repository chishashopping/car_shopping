from django.urls import path

# from user.views import login, index, SmsViewSET, LogoutView
from User.views import index, login, SmsViewSET, RegisterSerializer

app_name = 'user'
urlpatterns = [
    path('index/',index),
    path('login/',login),
    # # path('register/',RegisterView.as_view(),name='register'),
    path('code/',SmsViewSET.as_view(actions={
        "post": "create"
    }),name='code'),
    # path('logout/',LogoutView.as_view(),name ='login'),
    #
    path('register/',RegisterSerializer.as_view(actions={
        "post": "create"
    }),name='register'),
    # path('change_pwd/', views.ChangePwd.as_view(), name='change_pwd'),


]





