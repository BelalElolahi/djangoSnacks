from django.urls import path

from snacks.views import SnackDetailView, SnackListView


urlpatterns = [
    path('',SnackListView.as_view(),name='home'),
    path('<int:pk>',SnackDetailView.as_view(), name='snack_detail')
]
