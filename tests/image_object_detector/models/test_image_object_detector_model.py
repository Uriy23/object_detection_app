from django.conf import settings
from django.test import TestCase
from image_object_detector.models.image_object_detector_model import ImageObjectDetectorModel

class ImageObjectDetectorModelTest(TestCase):
  def setUp(self):
    print('setUp#7')
    self.detector = ImageObjectDetectorModel()

  def test_model_find_two_cats(self):
    image_path = f'{settings.BASE_DIR}/tests/image_object_detector/test_image001.jpg'
    boxes, labels = self.detector.detect_image(path = image_path)
    self.assertEqual(labels, ['cat', 'cat'])
