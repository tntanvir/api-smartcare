from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('list', views.PatientViewSerializer)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('registration/',views.PatientRegistration.as_view(),name='registration'),
    path('login/',views.PatientLogin.as_view(),name='login'),
    path('logout/',views.logoutView.as_view(),name='logout'),
    path('active/<uid64>/<token>/',views.activate )
]