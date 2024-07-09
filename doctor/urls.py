from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('list', views.DoctorViewSerializer)
router.register('specialization', views.SpecializationViewSerializer)
router.register('designation', views.DesignationViewSerializer)
router.register('available_time', views.AvailableTimeViewSerializer)
router.register('review', views.ReviewViewSerializer)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]