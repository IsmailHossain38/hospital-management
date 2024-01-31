from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register(r'list', views.DoctorViewset)
router.register(r'Specialization', views.SpecializationViewset)
router.register(r'Designation', views.DesignationViewset)
router.register(r'AvailableTime', views.AvailableTimeViewset)
router.register(r'Review', views.ReviewViewset)
urlpatterns = [
    path('', include(router.urls)),
]