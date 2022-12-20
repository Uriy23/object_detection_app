# !pip install torch
# !pip install transformers
# !pip install timm
from django.db import models

import torch
from transformers import DetrFeatureExtractor, DetrForObjectDetection
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import requests

url = "http://images.cocodataset.org/val2017/000000039769.jpg"


def rectanagle_image(list_box, list_name):
    for box, label_figure in zip(list_box, list_name):
        # plt.figure(figsize=(10,10))
        plt.imshow(image)

        ax = plt.gca()
        for k in range(len(list_box)):
            plt.text(box[0], box[1], label_figure)
            rect = patches.Rectangle(
                (box[0], box[1]),
                box[2],
                box[3],
                linewidth=2,
                edgecolor='cyan',
                fill=False
            )
            ax.add_patch(rect)
    plt.savefig('image_detecion.png')


def detiction_image(url):
    image = Image.open(requests.get(url, stream=True).raw)

    feature_extractor = DetrFeatureExtractor.from_pretrained("facebook/detr-resnet-50")
    model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50")

    inputs = feature_extractor(images=image, return_tensors="pt")
    outputs = model(**inputs)

    target_sizes = torch.tensor([image.size[::-1]])
    results = feature_extractor.post_process(outputs, target_sizes=target_sizes)[0]

    list_box = []
    list_name = []

    for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
        box = [round(i, 2) for i in box.tolist()]
        # let's only keep detections with score > 0.9
        if score > 0.9:
            print(
                f"Detected {model.config.id2label[label.item()]} with confidence "
                f"{round(score.item(), 3)} at location {box}"
            )
        list_box.append(box)
        list_name.append(model.config.id2label[label.item()])
    rectanagle_image(list_box, list_name)

