from django.shortcuts import redirect, render
from .models import Post

def index(request):
    return render(request, 'board/index.html')

def list(request):
    postlist = Post.objects.all().order_by('-id')
    return render(request, 'board/list.html', {'postlist':postlist})

def view(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'board/view.html', {'post':post})

def edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method=='POST':
        try:
            post.titles=request.POST['titles']
            post.contents=request.POST['contents']
            post.mainphoto=request.FILES['mainphoto']
        except:
            post.titles=request.POST['titles']
            post.contents=request.POST['contents']
        post.save()
        return redirect('../view/'+str(pk))
    else:
        return render(request, 'board/edit.html', {'post':post})

def write(request):
    if request.method=='POST':
        try :            
            new_article = Post.objects.create(
                titles=request.POST['titles'],
                contents=request.POST['contents'],
                mainphoto=request.FILES['mainphoto'],
            )
        except :
            new_article = Post.objects.create(
                titles=request.POST['titles'],
                contents=request.POST['contents'],
            )       
        return redirect('../list')
    return render(request, 'board/write.html')

def delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method=='GET':
        post.delete()
        return redirect('../list')
    


