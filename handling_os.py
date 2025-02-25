import os
print("import os : ", os.getcwd())
# changing the current directory to the directory where the images are stored
os.chdir('E:/3rd sem proj/fds ko project/archive/Images/Images')
folders=os.listdir()
for folder in folders[1:]:
    print(folder)
    if folder=='digits':
        os.chdir(folder)
        digits=os.listdir()
        for index,digit in enumerate(digits,0):
            os.chdir(digit)
            os.rename(os.getcwd(),str(index))
            print(f"{digit} is renamed to {index}")
            for index,image in enumerate(os.listdir(),1):
                new_name=str(index)+'.png'
                old_path=os.path.join(os.getcwd(),image)
                new_path=os.path.join(os.getcwd(),new_name)
                os.rename(old_path,new_path)
                print(f"{image} is renamed to {new_name}")
            os.chdir('..')
        os.chdir('..')


    os.chdir(folder)
    images=os.listdir()
    for index,image in enumerate(images,1):
        new_name=str(index)+'.png'
        old_path=os.path.join(os.getcwd(),image)
        new_path=os.path.join(os.getcwd(),new_name)
        os.rename(old_path,new_path)
        print(f"{image} is renamed to {new_name}")
    os.chdir('..')



#fixing the error with the digit folder
os.chdir('E:/3rd sem proj/fds ko project/archive/Images/Images')
#fixing the error with the digit folder
folders=os.listdir()
for folder in folders[1:]:
    print(folder)
    if folder=='digits':
        os.chdir('digits')
        digits=os.listdir()
        for digit in digits:
           true_label=((int(digit)+8)%10)
           os.rename(digit,"digit_"+str(true_label))



#making the data uniform by renaming the digits folder starting from 1 instead of 0
os.chdir('E:/3rd sem proj/fds ko project/archive/Images/Images/digits')
digits=os.listdir()
for digit in digits:
    os.chdir(digit)
    images=os.listdir()
    for image in images:
        image_name=image.split('.')[0]
        image_name_new=str((image_name))+'.png'
        print(image_name," is renamed to ",image_name_new)
        os.rename(image,image_name_new)
    os.chdir('..')
        
    
print("All files are renamed successfully")

    
