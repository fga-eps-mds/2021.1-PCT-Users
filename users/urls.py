from django.urls import path
from users import views

urlpatterns = [
    path("", views.list),
    path("",  views.create),
    path("<int:pk>", views.edit),
    path("<int:pk>", views.detail),
    path("<int:pk>", views.delete)
]