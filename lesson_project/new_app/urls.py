from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('post',views.post, name="post"),
    # path('find',views.find, name="find"),
    # path("update",views.update, name="update"),
]