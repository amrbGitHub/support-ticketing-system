from django.urls import path
from . import views
from .views import ReplyView
urlpatterns = [
    #path ("", views.index, name="index"),
    #path("<int:email>/", views.detail, name="detail"),
    path("reply/<int:pk>/", ReplyView.as_view(), name="reply"),
    # path("complete/<int:pk>/", mark_complete, name="mark-complete"),
]