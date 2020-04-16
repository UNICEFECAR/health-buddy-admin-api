from .views import *
from django.urls import path

urlpatterns = [
    path("", UserListView.as_view(), name="list_user"),
    path("add", UserCreateView.as_view(), name="add_user"),
    path("delete/<int:pk>", UserAccessManagementView.as_view(), name="delete_user"),
    path("detail/<int:pk>", UserDetailView.as_view(), name="detail_user"),
    path("update/<int:pk>", UserUpdateView.as_view(), name="update_user"),
]
