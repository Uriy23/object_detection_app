from django.db import models
from PIL import Image, UnidentifiedImageError
from transformers import DetrFeatureExtractor, DetrForObjectDetection
import requests
import torch
from image_object_detector.lib.singleton import Singleton

class ImageObjectDetectorModel(metaclass = Singleton):
  def __init__(self):
    print('ImageObjectDetectorModel#17')
    self.feature_extractor = DetrFeatureExtractor.from_pretrained("facebook/detr-resnet-50")
    self.model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50")

  def detect_image(self, url = None, path = None):
    if (url is None or url == '') and (path is None or path == ''):
      return None, [], []

    try:
      image = self.__open_image(url, path)
    except UnidentifiedImageError:
      return None, [], []
    except requests.exceptions.MissingSchema:
      return None, [], []

    inputs = self.feature_extractor(images=image, return_tensors="pt")
    outputs = self.model(**inputs)

    target_sizes = torch.tensor([image.size[::-1]])
    results = self.feature_extractor.post_process(outputs, target_sizes=target_sizes)[0]

    list_box, list_name = self.__filter_predictions(results, minimum_score = 0.8)
    return url or path, list_box, list_name

  # private methods

  def __filter_predictions(self, results, minimum_score):
    list_box = []
    list_name = []

    for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
      box = [round(i, 2) for i in box.tolist()]

      if float(score) > minimum_score:
        print(
          f"Detected {self.model.config.id2label[label.item()]} with confidence "
          f"{round(score.item(), 3)} at location {box}"
        )
        list_box.append(box)
        list_name.append(self.model.config.id2label[label.item()])

    return list_box, list_name

  def __open_image(self, url, path):
    if url is not None:
      return Image.open(requests.get(url, stream = True).raw)

    return Image.open(path)
