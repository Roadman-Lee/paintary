from django.shortcuts import render
from contents.models import PostModel
# Create your views here.
def search(request):
    if request.method == 'POST':
        search_post = request.POST.get('search')

        find_post = PostModel.objects.filter(post_title__contains=search_post)  # 전부가져와서 search_post를 포함한 것을 출력
        # find_post = [post for post in result_post if search_post in post.post_title]
        return render(request, 'contents/index.html', {'post_list': find_post})
        # return render(request, 'contents/category.html', {'find_post': find_post})
    else:
        return render(request, 'contents/category.html')