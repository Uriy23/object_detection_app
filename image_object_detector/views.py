from django.shortcuts import render, redirect
from django.views import generic

class IndexView(generic.View):
  def get(self, request):
    template_name = 'image_object_detector/index.html'
    return render(request, template_name, {})

class ShowView(generic.View):

  def post(self, request, *args, **kwargs):
    template_name = 'image_object_detector/show.html'
    image_url = request.POST["image_url"]
    return render(request, template_name, { 'image_url': image_url })

  def get(self, request, *args, **kwargs):
    template_name = 'image_object_detector/index.html'
    print(f'#18{kwargs=}')
    return render(request, template_name, {})
