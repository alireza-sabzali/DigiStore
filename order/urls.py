from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.OrderCreateView.as_view()),
    path('<int:order_id>/', views.OrderListView.as_view()),
]
