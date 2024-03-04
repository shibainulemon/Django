from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("<int:reply_id>", views.index, name="index"),
    path("<int:page>", views.index, name="index"),
    # path("<int:reply_id>/<int:page>", views.index, name="index"),
    path("post", views.post, name="post"),
    path("goods", views.goods, name="goods"),
    path("good/<int:good_id>", views.good, name="good"),
    path("edit/<int:num>", views.edit, name="edit"),
    path("delete/<int:num>", views.delete, name="delete"),
    path("find/<int:id>", views.find, name="find"),
    path("find/<int:id>/<int:page>", views.find, name="find"),
]