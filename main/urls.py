from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('portfolio/', views.PortfolioView.as_view()),
    path('work/<int:pk>/', views.WorkDetailView.as_view(), name='work-detail'),
    path('aboutUs/', views.AboutUsView.as_view()),
]
