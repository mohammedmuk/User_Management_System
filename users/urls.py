from django.urls import path
from . import views

urlpatterns = [
    path('create', views.CreateUserView.as_view({'post' : 'create'}), name='create-user'),
    path('retrieve', views.GetUserView.as_view(), name='retrieve-user'),
    path('update', views.UpdateUserView.as_view(), name='update-user'),
    path('delete', views.DeleteUserView.as_view(), name='delete-user'),
]