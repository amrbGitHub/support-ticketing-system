from django.urls import path
from . import views
from .views import ReplyView
urlpatterns = [
    path("reply/<int:pk>/", ReplyView.as_view(), name="reply"),
]