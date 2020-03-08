from django.conf.urls import url
from Myapp import views

app_name='Myapp'

urlpatterns=[
    url('relative/', views.relative, name='relative'),
    url('other/', views.other, name='other'),
    url('register/', views.register, name='register'),
    url('user_login/', views.user_login, name='user_login'),
]
