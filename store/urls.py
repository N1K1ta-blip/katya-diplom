from django.urls import path
from django.urls.conf import include

from store import views

urlpatterns = [
    path('store/', include([
        path('', views.StoreView.as_view()),
        path('admin/', views.AdminView.as_view()),
        path('edit/', views.EditStoreView.as_view()),
        path('table/', views.TableStoreView.as_view()),
        path('cart/', views.CartView.as_view()),
        path('profile/', views.ProfileView.as_view()),
        path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
        path('history/', views.HistoryView.as_view(), name='history'),
        path('history/self/', views.HistoryDetailView.as_view(), name='history-detail'),
    ])),
]
