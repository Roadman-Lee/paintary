from django.shortcuts import render
from rest_framework.views import APIView
from content.models import Feed, Bookmark
from rest_framework.response import Response
from user.models import UserModel
from rest_framework.response import Response
import os
from config.settings import MEDIA_ROOT
from uuid import uuid4
from datetime import datetime


class UploadFeed(APIView):
    def post(self, request):
        file = request.FILES['file']
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        content = request.data.get('content')
        image = uuid_name
        profile_image = request.data.get('profile_image')
        nickname = request.data.get('nickname')
        email = request.data.get('email')
        Feed.objects.create(content=content, image=image, profile_image=profile_image, nickname=nickname, email=email,
                            like_count=0)
        return Response(status=200)



class BookmarkFeed(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id')
        email = request.data.get('email')
        is_bookmarked = request.data.get('is_bookmarked', 'True')

        if is_bookmarked.lower() == 'false':
            is_bookmarked = False
        else:
            is_bookmarked = True
        bookmark = Bookmark.objects.filter(feed_id=feed_id, email=email).first()

        if bookmark is None:
            Bookmark.objects.create(feed_id=feed_id,
                                    email=email,
                                    is_bookmarked=is_bookmarked,
                                    )
        else:
            bookmark.is_bookmarked = is_bookmarked
            bookmark.save()

        return Response(status=200, data=dict(message='북마크 설정 완료.'))