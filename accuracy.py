from get_date import result
import os


path = '/home/lucifer/acadgild/project/fyle_assignment/Receipts/'
l = os.listdir(path)
images = [i for i in l if i.endswith('.jpeg')]
#print(images)
print(len(images))
count = 0
for image in images:
	if result(path+image)!=None:
		if len(result(path+image))!=0:
			count+=1
print(count)

accuracy = "{0:.2f}".format((count/len(images))*100)
print("accuracy is:-",accuracy+"%")