import yaml
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os
import matplotlib.image as mpimg
import numpy as np
import cv2
import numpy as np

test_filename="./dataset_test_rgb/trial.yaml"
test_dict = yaml.load(open(test_filename))
image_path="./dataset_test_rgb/rgb/test/"

#print(Dict)

# Define a function to draw bounding boxes
def draw_boxes(img, bboxes, color=(0, 0, 255), thick=6):
    # Make a copy of the image
    imcopy = np.copy(img)
    # Iterate through the bounding boxes
    for bbox in bboxes:
        # Draw a rectangle given bbox coordinates
        cv2.rectangle(imcopy, bbox[0], bbox[1], color, thick)
    # Return the image copy with boxes drawn
    return imcopy

#opecv 0-255, implot 0-1
def draw_single_box(img, box, color=(1, 0, 0), thick=6):
    # Make a copy of the image
    imcopy = np.copy(img)
    cv2.rectangle(imcopy, bbox[0], bbox[1], color, thick)
    # Return the image copy with boxes drawn
    return imcopy

#with open(test_filename, mode='rb') as f:
#    test = pickle.load(f)
print(len(test_dict))
##change file path of the read dictionary
for i in range(len(test_dict)):
    path=test_dict[i]['path']
    #print(path)
    path2 = path.split('/')
    #print(path2[-1])
    test_dict[i]['path']=newpath=image_path+path2[-1]

#new box in x dir is 16 pixel, -8,+8
pix_x_max=1280
pix_y_max=720
for i in range(len(test_dict)):
    box=test_dict[i]['boxes']
    '''print(box[0])
    {'occluded': False, 'y_max': 
    355.125, 'x_min': 749.0, 'y_min': 
    345.125, 'label': 'Green', 'x_max': 752.25}
    '''
    #print("box ",box)
    x_min=box[0]['x_min']
    x_max=box[0]['x_max']
    xmid=(x_max+x_min)/2
    x_min=xmid-8
    x_max=xmid+8
    if(x_max > pix_x_max):
        x_max=pix_x_max
    box[0]['x_min'] = int(x_min)
    box[0]['x_max'] = int(x_max)
    #
    y_min = box[0]['y_min']
    y_max = box[0]['y_max']
    ymid = (y_max + y_min) / 2
    y_min = ymid - 16
    y_max = ymid + 16
    if(y_max > pix_y_max):
        y_max=pix_y_max
    box[0]['y_min'] = int(y_min)
    box[0]['y_max'] = int(y_max)
    test_dict[i]['boxes']=box
    #print(test_dict[i]['boxes'])

#now read the image file

img = mpimg.imread(test_dict[0]["path"])
box=test_dict[0]['boxes']
x_min = box[0]['x_min']
x_max = box[0]['x_max']
y_min = box[0]['y_min']
y_max = box[0]['y_max']
addto=0
bbox=[(x_min-addto,y_min-addto), ( x_max+addto,y_max+addto) ]
print(bbox)
imgboxed=draw_single_box(img, bbox)
imgplot = plt.imshow(imgboxed)
plt.show()

