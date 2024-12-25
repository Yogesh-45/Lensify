import os
import shutil
from sklearn import preprocessing

from math import floor
import random


root_folder= 'D:/yogi/shoppin/ImageNet-Mini/augmented_images'
img_paths= []
labels= []
labels_set= set()


for dir, folder, files in os.walk(root_folder):
  
  if len(labels_set) >= 200:
    break

  for file in files:
    labels_set.add(os.path.basename(dir))
    img_path= os.path.join(dir, file)
    img_paths.append(img_path)
    labels.append(os.path.basename(dir))


label_encoder= preprocessing.LabelEncoder()
img_ids= label_encoder.fit_transform(labels)


def split_data(img_paths, img_ids):

    # Combine data and labels into a list of tuples
    combined = list(zip(img_paths, img_ids))

    # Shuffle the combined list
    random.shuffle(combined)

    # Split the shuffled combined list into two lists
    split_index1 = floor(len(combined) * 0.8)
    split_index2 = floor(len(combined) * 0.9)

    train_combined  = combined[:split_index1]
    test_combined   = combined[split_index1:split_index2]
    enroll_combined = combined[split_index2:]

    # Unpack the combined tuples into separate paths and labels
    train_img_paths, train_img_ids   = zip(*train_combined)
    test_img_paths, test_img_ids     = zip(*test_combined)
    enroll_img_paths, enroll_img_ids = zip(*enroll_combined)

    return train_img_paths, train_img_ids, test_img_paths, test_img_ids, enroll_img_paths, enroll_img_ids


train_img_paths, train_img_ids, test_img_paths, test_img_ids, enroll_img_paths, enroll_img_ids= split_data(img_paths, img_ids)



def organize_images(train_image_paths, val_image_paths, enroll_image_paths, output_folder="./ImageNet-Mini/dataset"):
    # Create train and test directories inside the output folder
    train_folder = os.path.join(output_folder, "train")
    val_folder = os.path.join(output_folder, "val")
    test_folder = os.path.join(output_folder, "test")
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)
    os.makedirs(val_folder, exist_ok=True)
    
    # Copy train images
    for image_path in train_image_paths:
        train_fold= os.path.join(train_folder, os.path.basename(os.path.dirname(image_path)))
        print(train_fold)
        os.makedirs(train_fold, exist_ok=True)
        if os.path.exists(image_path):  # Check if the image file exists
            shutil.copy(image_path, train_fold)
        else:
            print(f"Train image not found: {image_path}")
    
    # Copy test images
    for image_path in val_image_paths:
        val_fold= os.path.join(val_folder, os.path.basename(os.path.dirname(image_path)))
        os.makedirs(val_fold, exist_ok=True)
        if os.path.exists(image_path):  # Check if the image file exists
            shutil.copy(image_path, val_fold)
        else:
            print(f"Test image not found: {image_path}")

    # Copy test images
    for image_path in enroll_image_paths:
        test_fold= os.path.join(test_folder, os.path.basename(os.path.dirname(image_path)))
        os.makedirs(test_fold, exist_ok=True)
        if os.path.exists(image_path):  # Check if the image file exists
            shutil.copy(image_path, test_fold)
        else:
            print(f"Test image not found: {image_path}")
    
    print("Images organized into 'train' and 'test' folders.")


def copy_images(train_image_paths, val_image_paths, enroll_image_paths, output_folder="./ImageNet-Mini/augmented_images_200"):
    # Create train and test directories inside the output folder
    # train_folder = os.path.join(output_folder, "train")
    # val_folder = os.path.join(output_folder, "val")
    # test_folder = os.path.join(output_folder, "test")
    # os.makedirs(train_folder, exist_ok=True)
    # os.makedirs(test_folder, exist_ok=True)
    # os.makedirs(val_folder, exist_ok=True)
    
    # Copy train images
    for image_path in train_image_paths:
        train_fold= os.path.join(output_folder, os.path.basename(os.path.dirname(image_path)))
        print(train_fold)
        os.makedirs(train_fold, exist_ok=True)
        if os.path.exists(image_path):  # Check if the image file exists
            shutil.copy(image_path, train_fold)
        else:
            print(f"Train image not found: {image_path}")
    
    # Copy test images
    for image_path in val_image_paths:
        val_fold= os.path.join(output_folder, os.path.basename(os.path.dirname(image_path)))
        os.makedirs(val_fold, exist_ok=True)
        if os.path.exists(image_path):  # Check if the image file exists
            shutil.copy(image_path, val_fold)
        else:
            print(f"Test image not found: {image_path}")

    # Copy test images
    for image_path in enroll_image_paths:
        test_fold= os.path.join(output_folder, os.path.basename(os.path.dirname(image_path)))
        os.makedirs(test_fold, exist_ok=True)
        if os.path.exists(image_path):  # Check if the image file exists
            shutil.copy(image_path, test_fold)
        else:
            print(f"Test image not found: {image_path}")
    
    print("Images organized into 'train' and 'test' folders.")


copy_images(train_img_paths, test_img_paths, enroll_img_paths)
