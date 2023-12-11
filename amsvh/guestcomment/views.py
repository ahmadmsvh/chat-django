from django.views import generic
from .models import Guest
from colors import Bcolors as C
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect,Http404
from api.sessions import handle_session

class GuestListView(generic.ListView):
    model = Guest
    template_name = 'guestcomment/guestcommentlist.html'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()

        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(
                    self.object_list, "exists"
            ):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                raise Http404(
                    _("Empty list and “%(class_name)s.allow_empty” is False.")
                    % {
                        "class_name": self.__class__.__name__,
                    }
                )
        context = self.get_context_data()
        response = self.render_to_response(context)
        response = handle_session(request, response)["response"]
        return response


class GuestDetailView(generic.DetailView):
    model = Guest
    template_name = 'guestcomment/guestcommentdetail.html'


def create(request,*args, **kwargs):
    data = request.POST
    if data["first_name"] and data["last_name"] and data["comment"]:
        Guesobj = Guest(first_name=data["first_name"], last_name=data["last_name"], comment=data["comment"])
        Guesobj.save()
        print( C.YLW, data, C.ENDC)
        return HttpResponseRedirect(reverse_lazy('guestcomment:guestcommentlist'))
    else:
        return HttpResponseRedirect(reverse_lazy('guestcomment:guestcommentlist'))


def update(request,*args, **kwargs):
    data = request.POST
    guest_obj = Guest.objects.get(id=data["id"])
    guest_obj.first_name = data["first_name"]
    guest_obj.last_name = data["last_name"]
    guest_obj.comment = data["comment"]
    guest_obj.save()
    print(C.YLW, guest_obj , C.ENDC)
    return HttpResponseRedirect(reverse_lazy('guestcomment:guestcommentlist'))

def delete(request,*args, **kwargs):
    data = request.POST
    print(C.YLW, data, C.ENDC)
    guest_obj = Guest.objects.get(id=data["id"])
    guest_obj.delete()
    print(C.YLW, guest_obj , C.ENDC)
    return HttpResponseRedirect(reverse_lazy('guestcomment:guestcommentlist'))




