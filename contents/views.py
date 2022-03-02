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
            print(user_id.id)
            return render(request, 'contents/upload.html',{'user_id':user_id})

        elif request.method == 'POST':

            photo = request.POST.get('image_url')
            print(photo)
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
        post_id = request.POST.get('post_id')
        if request.method == 'GET':
            post = PostModel.objects.get(post_id=post_id)
            print(post_id.id)
            return render(request, 'contents/detail.html', {'post_id': post.id})



