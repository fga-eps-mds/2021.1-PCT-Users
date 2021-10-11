from django.urls import path
from .views import UserCreate, UserList, UserRetrieve, UserUpdate, UserDelete

urlpatterns = [
    path("",  UserList.as_view()),
    path("create/", UserCreate.as_view()),
    path("detail/<int:pk>/", UserRetrieve.as_view()),
    path("update/<int:pk>/", UserUpdate.as_view()),
    path("delete/<int:pk>/", UserDelete.as_view())
]