from django.urls import path

from . import views

urlpatterns = [
    path ("", views.index, name="index"),
    path("<int:email>/", views.detail, name="detail"),
]