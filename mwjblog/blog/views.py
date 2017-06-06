from django.shortcuts import render
from .models import Post,UserInfo

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    userinfo = UserInfo.objects.first()
    return render(request, 'blog/index.html', context={'post_list': post_list,'userinfo': userinfo})
