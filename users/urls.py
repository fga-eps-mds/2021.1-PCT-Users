from django.urls import include, path
from rest_framework import routers
from users import views

app_name = 'users'
router = routers.DefaultRouter()


urlpatterns = [
    path(r'', include(router.urls)),
    path('test', views.UserTestViewSet.as_view(), name='user-test'),
]
