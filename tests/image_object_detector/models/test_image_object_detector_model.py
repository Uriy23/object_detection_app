from django.conf import settings
from django.test import TestCase
from image_object_detector.models.image_object_detector_model import ImageObjectDetectorModel
from PIL import Image


class ImageObjectDetectorModelTest(TestCase):
  def setUp(self):
    self.detector = ImageObjectDetectorModel()

  def test_model_wont_work_with_empty_path(self):
    ''' Проверяет, что если не передать модели пустую ссылку на изображение, то ничего не будет распознано. '''
    boxes, labels = self.detector.detect_image(path='')
    self.assertEqual(labels, [])

  def test_model_find_two_cats(self):
    ''' Проверяет, что на тестовом изображении будет найдено два cat '''
    image_path = f'{settings.BASE_DIR}/tests/image_object_detector/test_image001.jpg'
    boxes, labels = self.detector.detect_image(path=image_path)
    self.assertEqual(labels, ['cat', 'cat'])

  def test_format(self):
    ''' Проверяет, что передан допустимый формат '''
    image_path = f'{settings.BASE_DIR}/tests/image_object_detector/test_pdf.pdf'
    boxes, labels = self.detector.detect_image(path=image_path)
    self.assertEqual(labels, [])
