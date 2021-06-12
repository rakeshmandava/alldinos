# alldinos/dinos/urls.py
from django.urls import path
from . import views


app_name = "dinos"
urlpatterns = [
    path(
        route='',
        view=views.DinosaurListView.as_view(),
        name='list'
    ),
    path(
        route='<slug:slug>/',
        view=views.DinosaurDetailView.as_view(),
        name='detail'
        ),
]