import nibabel as nib #handles the .nii.gz file
import numpy as np #for handling the image data as an array
from pathlib import Path
from sklearn.model_selection import train_test_split
from heart_utils import helper
import torch 

def helper():
    print("This is a helper function for heart disease analysis.")
    return 0

def dataLoader():
   
    #load the image
    img = nib.load('/home/thomas/Downloads/heartDisease/imagesTr/la_003.nii.gz')

    #get image data 
    data = img.get_fdata()

    #check shape
    print(data.shape)

    #get the needed paths
    training_path = Path('/home/thomas/Downloads/heartDisease/imagesTr')
    labels_path = Path('/home/thomas/Downloads/heartDisease/labelsTr')
    test_path = Path('/home/thomas/Downloads/heartDisease/imagesTs')

    #split into test/val
    train_images, val_images = train_test_split(list(training_path.glob('*.nii.gz')), test_size=0.2, random_state=42)
    train_labels, val_labels = train_test_split(list(labels_path.glob('*.nii.gz')), test_size=0.2, random_state=42)

    #populate the test set
    train_images = [str(path) for path in train_images]

    #print the number of images in each set
    print(f'Training images: {len(train_images)}')
    print(f'Validation images: {len(val_images)}')
    print(f'Training labels: {len(train_labels)}')
    print(f'Validation labels: {len(val_labels)}')
    print(f'Test images: {len(list(test_path.glob("*.nii.gz")))}')
    
