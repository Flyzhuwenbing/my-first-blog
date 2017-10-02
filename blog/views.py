from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
#连接模型与模板
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # 通过查询集将模型传递到模板中
    return render(request,'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    # 查询集 将模型传递到post_detail.html中
    post = get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})

