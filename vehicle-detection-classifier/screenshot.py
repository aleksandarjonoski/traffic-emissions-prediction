# This is the file that crops all of the individual cars/vehicles
from PIL import Image
from carDetectClassifier import *
from dict import *

# trafic_image = Image.open('/home/stefan/personal/traffic-emissions-prediction/vehicle-detection-classifier/traffic2.jpeg') # from which image to open and take the contents
trafic_image = Image.open('./traffic.png')
my_dict_value = list(my_dict.values())
my_dict_key = list(my_dict.keys())
for i in range(len(my_dict_key)):
    crop_car = trafic_image.crop(my_dict_value[i]) # coordinates where to crop
    crop_car.save(f'./images/{my_dict_key[i]}.jpeg')# where to save the images



