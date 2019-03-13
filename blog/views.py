from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog

# Create your views here.

def home(request):
    blogs = Blog.objects  # 쿼리셋
    return render(request, 'home.html',{'blogs':blogs})

def detail(request, blog_id): #new.html띄어주는 함수
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html',{'details':details})

def new(request):
    return render(request, 'new.html')

def create(request):#입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))   # 위에거 다 처리하고 url 로 보내세요
