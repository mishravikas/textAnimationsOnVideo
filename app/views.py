import json
from django.forms.models import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.template import loader
from django.core import serializers
from .models import Video,Animation


def index(request):
    context = {
            'first_text': 'TITLE 1',
            }

    return render(request, 'app/index.html',context)

def video(request, video_id):
    try:
        video = Video.objects.get(pk=video_id)
    except Video.DoesNotExist:
        raise Http404("Video does not exist")
    print (video.filename)
    anims = Animation.objects.filter(video=video)
    animations = []
    for anim in anims:
        animations.append({'time_app': anim.time_app, 'text': anim.text})

    return render(request,'app/video.html',{'video_name':video.filename, 'animations':animations})

def animations(request, video_id):
    video = Video.objects.get(pk=video_id)
    anims = Animation.objects.filter(video=video)
    data_out = get_animations(video_id)
    return JsonResponse(data_out,safe=False)

def get_animations(video_id):
    video = Video.objects.get(pk=video_id)
    anims = Animation.objects.filter(video=video)
    data_out = {'video':video.filename}
    for j,anim in enumerate(anims):
        data_out[j+1] = {}
        for key,value in model_to_dict(anim).items():
            print (key)
            print (value)
            if value:
                if key == 'video':
                    pass
                elif key == 'id':
                    data_out[j+1]['animation'] = value
                else:
                    data_out[j+1][str(key)] = value

    return data_out

