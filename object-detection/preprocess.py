import os
import cv2

file_names = os.listdir('coil-100-original')

train_test_count = 0
def get_class_name(file_name):
    pos = file_name.find('_')
    res = file_name[:pos]
    return res
 
for i in range(1,101):
    os.mkdir(os.path.join('coil-100-BOW\\train','obj'+str(i)))
    os.mkdir(os.path.join('coil-100-BOW\\test','obj'+str(i)))

# phân chia vào folder train/test tỉ lệ 80/20
for file_name in file_names:
    img = cv2.imread(os.path.join('coil-100-original', file_name))
    class_name = get_class_name(file_name)

    if train_test_count < 58:
        cv2.imwrite(os.path.join('coil-100-BOW\\train', class_name, file_name), img)
        train_test_count += 1
    else:
        cv2.imwrite(os.path.join('coil-100-BOW\\test', class_name, file_name), img)
        train_test_count += 1
        if train_test_count == 72:
            train_test_count = 0
    
