from django.http import Http404
from django.shortcuts import render
saved_posts={
    'first-post':{"post_name":'first-post',"post_image":"blog/images/ecasp42vjzr61.png","post_title":'My first post!',"post_body":"This is the body of my first post."},
    'second-post':{"post_name":'second-post',"post_image":"blog/images/ecasp42vjzr61.png","post_title":'My second post!',"post_body":"This is the body of my second post."},
    'third-post':{"post_name":'third-post',"post_image":"blog/images/ecasp42vjzr61.png","post_title":'My third post!',"post_body":"This is the body of my third post."},
}

def landing_page(request):
    return render(request, "blog/index.html",{"post":list(saved_posts.values())[-1]})

def posts(request):
    return render(request, "blog/all-posts.html",{"post_list":list(saved_posts.values())})

def single_post(request,slug):
    if slug not in saved_posts:
        raise Http404
    post = saved_posts[slug]
    return render(request,"blog/individual-post.html",{"post":post})