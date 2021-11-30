from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductListView.as_view()),
    path('<int:pk>/', views.ProductDetailView.as_view()),

    path('comment/create/<int:product_id>/', views.CommentCreateView.as_view()),
    path('comment/delete/<int:pk>/', views.CommentDeleteView.as_view()),

    path('color/delete/<int:pk>/', views.ColorDeleteView.as_view()),

    path('image/delete/<int:pk>/', views.ImageDeleteView.as_view()),
]
