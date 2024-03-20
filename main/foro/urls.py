from django.urls import path
from . import views

app_name = 'foro'

urlpatterns = [
    path('new_thread/', views.new_thread, name='new_thread'),
    path('list_threads/', views.list_threads, name='list_threads'),
    path('thread_detail/<int:thread_id>/', views.thread_detail, name='thread_detail'),
    path('thread/comment/<int:thread_id>/', views.comment, name='comment'),
    path('search_threads/', views.search_threads, name='search_threads'),
    path('order_threads/', views.order_threads, name='order_threads'),
]
