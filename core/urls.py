
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    NotificationViewSet,
    MessageViewSet,
    EventViewSet,
    UserPreferenceViewSet,
    UploadAttachmentView
)

router = DefaultRouter()
router.register(r'notifications', NotificationViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'events', EventViewSet)
router.register(r'user-preferences', UserPreferenceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload-attachment/', UploadAttachmentView.as_view(), name='upload-attachment'),
]
