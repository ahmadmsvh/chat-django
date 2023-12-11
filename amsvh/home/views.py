from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.views import View, generic
from .forms import *

class Home(View):
    template = 'home/home.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template)

class SampleFormView(View):

    def get(self, request):
        # init_data = {
        #     "user_name":"amadmsvh",
        #     "password":"password"
        # }
        # form = SampleForm(init_data)
        form = SampleForm()

        ctx = {'form' : form}
        return render(request, 'home/sample_form.html', ctx)

    def post(self,request):
        form = SampleForm(request.POST)
        pass
