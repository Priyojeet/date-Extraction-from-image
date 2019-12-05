#!/usr/bin/env python
#title           :accuracy.py
#description     :Finding the accuracy of the date extraction.
#author          :Priyojeet Bhunia
#date            :03/12/2019
#version         :0.0
#usage           :python accuracy.py
#python_version  :3.7.5  
#==============================================================================





# importing libraries
from forAccuracy import result # local module
import os


path = '/home/lucifer/acadgild/project/fyle_assignment/Receipts/'
l = os.listdir(path)
images = [i for i in l if i.endswith('.jpeg')]
print(images)
print(len(images))
print(images.index('379efbfc.jpeg'))
count = 0
for image in images:
	if result(path+image)!=None:
		if len(result(path+image))!=0:
			count+=1
print(count)

accuracy = "{0:.2f}".format((count/len(images))*100)
print("accuracy is:-",accuracy+"%") # 495 out of 595