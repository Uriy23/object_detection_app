import json
from django.shortcuts import render, redirect
from django.views import generic
from .image_object_detector_model import ImageObjectDetectorModel

class IndexView(generic.View):
  def get(self, request):
    template_name = 'image_object_detector/index.html'
    default_image_url = 'https://sun9-82.userapi.com/impf/c855620/v855620359/b9d9f/wGfL4G-rfi4.jpg?size=670x430&quality=96&sign=90a452c26f7194150f3f92ee53a77548&type=album'
    image_url = request.GET.get("image_url", False) or default_image_url
    locals = { 'image_url': image_url }
    return render(request, template_name, locals)

class ShowView(generic.View):
  def post(self, request, *args, **kwargs):
    template_name = 'image_object_detector/show.html'
    image_url = request.POST["image_url"]
    detector = ImageObjectDetectorModel()
    list_box, list_name = detector.detection_image(image_url)
    locals = {
      'image_url': image_url,
      'list_box': json.dumps(list_box),
      'list_name': json.dumps(list_name)
    }
    return render(request, template_name, locals)

  def get(self, request, *args, **kwargs):
    template_name = 'image_object_detector/index.html'
    print(f'#18{kwargs=}')
    return render(request, template_name, {})
