from django.urls import path
from . import views


app_name = 'chat'


urlpatterns = [
    path('room/<int:chat_id>/', views.chat_room, name='chat_room'),
    path('send_chat_request/<int:cuidador_id>/<int:offer_id>/', views.send_chat_request, name='send_chat_request'),
    path('requests/', views.chat_requests_for_caregiver, name='chat_requests_for_caregiver'),
    path('accept_chat_request/<int:chat_request_id>/', views.accept_chat_request, name='accept_chat_request'),
    path('reject_chat_request/<int:chat_request_id>/', views.reject_chat_request, name='reject_chat_request'),
]