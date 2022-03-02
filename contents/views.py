from django.shortcuts import render, redirect
from .models import PostModel, ScrapModel, CommentModel
from users.models import UserModel
# Create your views here.
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def upload_view(request, id):

    user = request.user.is_authenticated
    user_id = request.user
    if user:
        if request.method == 'GET':
            return render(request, 'contents/upload.html',{'user_id':user_id})

        elif request.method == 'POST':

            photo = request.POST.get('styled_url')
            writing = request.POST.get('writing')
            postdate = request.POST.get('postdate')

            upload = PostModel(user_id=user_id, photo=photo, writing=writing, postdate=postdate)
            upload.save()
            print('post', str(id))
            return redirect('upload',id)

def index(request):
    # user = request.user.is_authenticated
    # if user:
    #     if request.method == 'GET':
    #         posts = PostModel.objects.all()
    #         return render(request, 'contents/index.html', {'posts': posts})
    return render(request, 'contents/index.html')


def detail(request, postid):
    user = request.user.is_authenticated
    if user:
        # post_id = request.POST.get('post_id')

        if request.method == 'GET':
            post = PostModel.objects.get(pk=postid)

            return render(request, 'contents/detail.html', {'post': post})
            # return render(request, 'contents/detail.html', {'post_id': post.id})


def post_delete(request, postid):
    post = PostModel.objects.get(pk=postid)
    post.delete()
    return redirect('/')

def post_edit(request, postid):
    user = request.user.is_authenticated
    if user:
        post = PostModel.objects.get(pk=postid)
        if request.method == 'GET':
            return render(request, 'contents/post_edit.html', {'post':post})

        elif request.method == 'POST':
            writing = request.POST.get('writing')
            post.writing = writing
            post.save()
            return render(request, 'contents/detail.html', {'post':post})
