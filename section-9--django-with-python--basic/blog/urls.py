from django.urls import path

from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("example", views.example_view, name="example"),
    path("post/<int:post_id>", views.post, name="post"),
]
