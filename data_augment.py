import os
from PIL import Image
from torchvision import transforms
import kagglehub


# Download dataset from kaggle
path = kagglehub.dataset_download("deeptrial/miniimagenet")

print("Path to dataset files:", path)


#Transformation to generate more data

augmentation_transforms = transforms.Compose([
    transforms.RandomApply([
        transforms.RandomHorizontalFlip(p=1.0),
        transforms.RandomVerticalFlip(p=1.0)
    ], p=0.7),  # Randomly apply flips with a combined probability

    transforms.RandomApply([
        transforms.RandomRotation(degrees=(-30, 30)),  # Larger range for rotation
    ], p=0.6),  # Apply rotation randomly

    transforms.RandomApply([
        transforms.ColorJitter(
            brightness=(0.5, 1.5),  # Larger range for brightness
            contrast=(0.5, 1.5),    # Larger range for contrast
            saturation=(0.5, 1.5),  # Larger range for saturation
            hue=(-0.2, 0.2)         # Larger range for hue
        ),
    ], p=0.5),  # Randomly apply color jitter with reduced probability

    transforms.RandomPerspective(distortion_scale=0.5, p=0.4),  # Add perspective distortion randomly

    transforms.RandomApply([
        transforms.RandomAffine(
            degrees=0,
            translate=(0.1, 0.2),  # Random translation
            scale=(0.8, 1.2),      # Random scaling
            shear=(-10, 10)        # Random shearing
        )
    ], p=0.5),

    transforms.RandomResizedCrop(
        size=(224, 224),
        scale=(0.6, 1.0),  # Allow smaller crop sizes for more variability
        ratio=(0.75, 1.33)  # Aspect ratio variations
    ),

    transforms.ToTensor()
])


def generate_augmented_data(input_directory= "D:/yogi/shoppin/ImageNet-Mini/images",
                            output_directory= "D:/yogi/shoppin/ImageNet-Mini/augmented_images",
                            transform= augmentation_transforms,
                            num_augmentations= 50):
    
    '''
    Applies transform to generate augmented data for the images in the input_directory 
    and saves them to output_directory.
    num_augmentations is the number of augmentations generated per image
    '''

    os.makedirs(output_directory, exist_ok=True)

    for dir, folder, files in os.walk(input_directory):

        for filename in files:

            file_path = os.path.join(dir, filename)
            image = Image.open(file_path)

            
            for i in range(num_augmentations):
                augmented_image = transform(image)
                augmented_image = transforms.ToPILImage()(augmented_image)  # Convert back to PIL for saving

                # Convert to RGB if the image is in RGBA mode
                if augmented_image.mode == 'RGBA':
                    augmented_image = augmented_image.convert('RGB')
                
                # Save augmented image
                base_name, ext = os.path.splitext(filename)
                augmented_filename = f"{base_name}_aug_{i}{ext}"
                output_folder= os.path.join(output_directory, os.path.basename(dir))
                print(output_folder)

                os.makedirs(output_folder, exist_ok=True)
                augmented_image.save(os.path.join(output_folder, augmented_filename))


    print(f"Augmented images saved to {output_directory}")
