from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.CartDetailView.as_view()),
    path('add/<int:product_id>/', views.CartAddView.as_view()),
    path('remove/<int:product_id>/', views.CartRemoveView.as_view()),
]
