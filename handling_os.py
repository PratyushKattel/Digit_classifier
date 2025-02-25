import os
print("import os : ", os.getcwd())
os.chdir('E:/3rd sem proj/fds ko project/archive/Images/Images')
folders=os.listdir()
for folder in folders[1:]:
    print(folder)
    if folder=='digits':
        os.chdir(folder)
        digits=os.listdir()
        for digit in digits:
            os.chdir(digit)
            for index,image in enumerate(os.listdir(),1):
                new_name=str(index)+'.png'
                old_path=os.path.join(os.getcwd(),image)
                new_path=os.path.join(os.getcwd(),new_name)
                os.rename(old_path,new_path)
                print(f"{image} is renamed to {new_name}")
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

print("All files are renamed successfully")

    
