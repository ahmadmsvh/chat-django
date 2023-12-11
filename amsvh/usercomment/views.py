from django.views import generic
from .models import UserComment, Picture
from colors import Bcolors as C
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from api.serializers import UserCommentSerializer
from home.forms import SampleForm
import time


class UserCommentListView(
        LoginRequiredMixin,
        generic.ListView,
        ):
    model = UserComment
    template_name = 'usercomment/usercommentlist.html'


class UserCommentDetailView(
        LoginRequiredMixin,
        generic.DetailView,
        ):
    model = UserComment
    template_name = 'usercomment/usercommentdetail.html'


def create(request,*args, **kwargs):
    data = request.POST
    print(C.YLW, data, C.ENDC)
    if data["first_name"] and data["last_name"] and data["comment"]:
        user_comment_object = UserComment(first_name=data["first_name"],
                              last_name=data["last_name"],
                              comment=data["comment"],
                              username_id=data["username_id"])
        user_comment_object.save()
        return HttpResponseRedirect(reverse_lazy('usercomment:usercommentlist'))
    else:
        return HttpResponseRedirect(reverse_lazy('usercomment:usercommentlist'))


def update(request,*args, **kwargs):
    data = request.POST
    user_obj = UserComment.objects.get(id=data["id"])
    user_obj.first_name = data["first_name"]
    user_obj.last_name = data["last_name"]
    user_obj.comment = data["comment"]
    user_obj.save()
    print(C.YLW, user_obj, C.ENDC)
    return HttpResponseRedirect(reverse_lazy('usercomment:usercommentlist'))


def delete(request,*args, **kwargs):
    data = request.POST
    print(C.YLW, data, C.ENDC)
    user_obj = UserComment.objects.get(id=data["id"])
    user_obj.delete()
    print(C.YLW, user_obj, C.ENDC)
    return HttpResponseRedirect(reverse_lazy('usercomment:usercommentlist'))


def handy_delete(request,*args, **kwargs):
    data = request.path
    data = data.split("/")[-3]
    print(C.YLW, data, C.ENDC)
    user_obj = UserComment.objects.get(id=data)
    user_obj.delete()
    print(C.YLW, user_obj, C.ENDC)
    return HttpResponseRedirect(reverse_lazy('usercomment:handy'))


def handy(request):
    template_name = "usercomment/handy.html"
    ctx = {
        "usercomment_list": UserComment.objects.all(),
        "pictures": Picture.objects.all(),
        "user": request.user
        }
    return render(request, template_name, ctx)


def handy_chat(request):
    if request.user.is_authenticated:
        print(C.YLW, request.user, C.ENDC)
        template_name = "usercomment/handy_chat.html"
        ctx = {
            "usercomment_list": UserComment.objects.all(),
            "pictures": Picture.objects.all(),
            "user": request.user
             }
        return render(request, template_name, ctx)
    else:
        return HttpResponseRedirect(
            'http://localhost:8000/accounts/login/?next=/usercomment/handy-chat/')


def handy_create(request,*args, **kwargs):
    data = request.POST
    print(C.YLW, data, C.ENDC)
    if data["first_name"] and data["last_name"] and data["comment"]:
        guesobj = UserComment(first_name=data["first_name"],
                              last_name=data["last_name"],
                              comment=data["comment"],
                              username_id=data["username_id"])
        guesobj.save()
        return HttpResponseRedirect(reverse_lazy('usercomment:handy'))
    else:
        return HttpResponseRedirect(reverse_lazy('usercomment:handy'))


def handy_json(request):
    # print(C.YLW, "fuck", C.ENDC)
    # json_data = {
    #     "usercomment_list" : UserComment.objects.first(),
    #     "pictures" : "[Picture.objects.all()]",
    #     "user" : "[request.user]"
    # }
    json_data = UserCommentSerializer(UserComment.objects.all(), many=True)
    return JsonResponse(json_data.data, safe=False)
