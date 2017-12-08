import sys
import yaml
import pickle

test_filename="./dataset_test_rgb/trial.yaml"
Dict = yaml.load(open(test_filename))
image_path="./dataset_test_rgb/rgb/test/"

#print(Dict)

#with open(test_filename, mode='rb') as f:
#    test = pickle.load(f)
print(len(Dict))


label_list=[];
for line in Dict:
    boxes=line['boxes']
    print(boxes)
    path=line['path']
    print(path)
    path2 = path.split('/')
    print(path2[-1])
    newpath=image_path+path2[-1]
    print(newpath)
    mydict=boxes[0]
    print(mydict)
    print(mydict['x_max'])
#    print(line['y_max']

#/net/pal-soc1.us.bosch.com/ifs/data/Shared_Exports/deep_learning_data/traffic_lights/university_run1/
print("dictionary")
print(mydict[0])
#print(mydict[1])

