from django.urls import path

from .all_views import views


urlpatterns = [
    path(
        '',
        views.new_form,
        name='new_form'),
]
