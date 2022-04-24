from preprocess.utils import imresize
import os
import torch.utils.data
import yaml
import utils
from PIL import Image
import torchvision.transforms.functional as TF

for file in os.listdir("../datasets/test_imgs/"):
	input_img = Image.open("../datasets/test_imgs/" + file)
	input_img = TF.to_tensor(input_img)
	resize_img = imresize(input_img, 1.0 / 4, True)
	TF.to_pil_image(resize_img).save("../datasets/test_imgs_ds/" + file, 'PNG')