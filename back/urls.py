from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("buy/<int:item_id>/", views.session_create, name='buy'),
    path("item/<int:item_id>/", views.item, name='item')

]