from django.urls import path
from . import views

urlpatterns = [
    path("",views.landing_page,name="landing_page"),
    path("posts", views.posts,name="posts_page"),
    path("posts/<slug:slug>", views.single_post,name="single_post_page")
]