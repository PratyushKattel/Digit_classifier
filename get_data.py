import os
import numpy as np
import pandas as pd
from PIL import Image

data_iden=[]
data=[]
os.chdir('E:/3rd sem proj/fds ko project/archive/Images/Images')
folders=os.listdir()[1:37]
for folder in folders:
    current_label=folder
    os.chdir(folder)
    images=os.listdir()
    #taking 1000 images from each of the folder
    for image in images:
        image_path=os.path.join(os.getcwd(),image)
        img=Image.open(image_path).convert('L')
        img_array=np.array(img).flatten()/255
        data.append(img_array) #appending the image data to the data list
        data_iden.append(current_label) #append int the current label to the data_iden list
    os.chdir('..')
    print(f"{folder} is done")    
    
    
print(np.array(data))
print(np.array(data_iden))

#saving the data to a csv file
data_frame=pd.DataFrame(data)
data_frame['label']=data_iden
data_frame.to_csv('E:\\3rd sem proj\\fds ko project\\archive\\training_images\\training_images.csv',index=False)

#saving the data to a csv file

data.clear()
data_iden.clear()
os.chdir('E:/3rd sem proj/fds ko project/archive/Images/Images/digits')
digits=os.listdir()
for digit in digits:
    os.chdir(digit)
    images=os.listdir()
    for image in images:
        image_path=os.path.join(os.getcwd(),image)
        img=Image.open(image_path).convert('L')
        img_array=np.array(img).flatten()/255
        data.append(img_array)
        data_iden.append(digit)

    os.chdir('..')

data_frame_digit=pd.DataFrame(data)
data_frame_digit['label']=data_iden
data_frame_digit.to_csv('E:\\3rd sem proj\\fds ko project\\archive\\training_images\\training_images_digit.csv',index=False)
print('done')

        

            


