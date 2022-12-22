from django.urls import path
from .views import *

urlpatterns=[
    path('', home,name='home'),
    path('concurent/<slug>',concurent,name='concurent'),
    path('question/<slug>',question,name='question'),
    path('questions',questions,name='questions'),
    path('dedicaces',dedicaces,name='dedicaces'),
    path('remerciments',remerciments,name='remerciments'),
    path('notifications',notifications,name='notifications'),
    path('programme',programme,name='programme'),
    path('dedicace',dedicace,name='dedicace'),
    path('vote/<slug>',vote,name='vote'),
    path('like/<slug>',like,name='like'),
    path('get_question/<slug>',get_question,name='get_question'),
    path('reponse',reponse,name='reponse'),
    path('next_prog/', next_prog, name='next_prog'),
    path('cadeau',Cadeau,name='cadeau'),
    path('envellope',envellope, name='envellope'),
    path('redeem/<slug>',redeem, name='redeem')
]