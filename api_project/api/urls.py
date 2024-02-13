from django.urls import path
from .views import UserListAPIView, UserRetrieveUpdateAPIView, ClientCreateAPIView

urlpatterns = [
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserRetrieveUpdateAPIView.as_view(), name='user-detail'),
    path('clients/create/', ClientCreateAPIView.as_view(), name='client-create'),
]
