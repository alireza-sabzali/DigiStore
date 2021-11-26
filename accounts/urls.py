from django.urls import path

from .views import RegistrationAPIView, UserRetrieveUpdateAPIView, LoginAPIView

app_name = 'account'

urlpatterns = [
    path('retrieve/', UserRetrieveUpdateAPIView.as_view()),
    path('register/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
]
