from carDetectClassifier import *

listcars = []
listbus = []
listtruck = []
listmotor = []
listperson = []

for i in range(len(label)):

    if label[i] == 'car':
        listcars.append(i)
        vehicle = {f'{label[i]}'+ f'{listcars.index(i)}': bbox[i]}
        my_dict.update(vehicle)

    if label[i] == 'bus':
        listbus.append(i)
        vehicle = {f'{label[i]}'+ f'{listbus.index(i)}': bbox[i]}
        my_dict.update(vehicle)

    if label[i] == 'truck':
        listtruck.append(i)
        vehicle = {f'{label[i]}'+ f'{listtruck.index(i)}': bbox[i]}
        my_dict.update(vehicle)

    if label[i] == 'motorcycle':
        listmotor.append(i)
        vehicle = {f'{label[i]}'+ f'{listmotor.index(i)}': bbox[i]}
        my_dict.update(vehicle)

    if label[i] == 'person':
        listperson.append(i)
        vehicle = {f'{label[i]}'+ f'{listperson.index(i)}': bbox[i]}
        my_dict.update(vehicle)

#print(my_dict)
