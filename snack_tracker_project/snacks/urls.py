from django.urls import path

from snacks.views import SnackCreateView, SnackDeleteView, SnackDetailView, SnackListView, SnackUpdateView 

urlpatterns = [
    path('',SnackListView.as_view(),name='home'),
    path('<int:pk>',SnackDetailView.as_view(), name='snack_detail'),
    path('create/',SnackCreateView.as_view(), name='snack_create'),
    path('delete/<int:pk>',SnackDeleteView.as_view(), name='snack_delete'),
    path('update/<int:pk>',SnackUpdateView.as_view(), name='snack_update'),
    


]
