from django.views import generic
from colors import Bcolors as C
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

from .models import Picture
from .forms import CreateForm


class PictureListView(OwnerListView):
    model = Picture
    template_name = "usercomment/list.html"


class PictureDetailView(OwnerDetailView):
    model = Picture
    template_name = "usercomment/detail.html"


class PictureCreateView(LoginRequiredMixin, View):
    template_name = 'usercomment/form.html'
    success_url = reverse_lazy('pics:all')

    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        pic = form.save(commit=False)
        pic.owner = self.request.user
        pic.save()
        return redirect(self.success_url)


class PictureUpdateView(LoginRequiredMixin, View):
    template_name = 'usercomment/form.html'
    success_url = reverse_lazy('usercomment:all')

    def get(self, request, pk):
        pic = get_object_or_404(Picture, id=pk, owner=self.request.user)
        form = CreateForm(instance=pic)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        pic = get_object_or_404(Picture, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=pic)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        pic = form.save(commit=False)
        pic.save()

        return redirect(self.success_url)


class PictureDeleteView(OwnerDeleteView):
    model = Picture
    template_name = "usercomment/delete.html"


def stream_file(request, pk):
    pic = get_object_or_404(Picture, id=pk)
    response = HttpResponse()
    response['Content-Type'] = pic.content_type
    response['Content-Length'] = len(pic.picture)
    response.write(pic.picture)
    return response