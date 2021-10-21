from django.urls import path
from rest_framework import routers
from .views import UserCreate, UserList, UserRetrieve, UserUpdate, UserDelete, UserViewSet

router = routers.DefaultRouter()
router.register('cadastrar_usuario', UserViewSet, basename='Cadastrar Usuário')

urlpatterns = [
    path("",  UserList.as_view()),
    path("create/", UserCreate.as_view()),
    path("detail/<int:pk>/", UserRetrieve.as_view()),
    path("update/<int:pk>/", UserUpdate.as_view()),
    path("delete/<int:pk>/", UserDelete.as_view())
]