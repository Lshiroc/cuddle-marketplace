from django.urls import path
from . import views

app_name = 'conversation'

urlpatterns = [
    path('messages/<int:pk>', views.messages, name='messages'),
    path('contact/<int:pk>', views.index, name='contact'),
]
