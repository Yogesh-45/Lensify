import os
from PIL import Image
from torchvision import transforms

# # Define augmentation transformations
# augmentation_transforms = transforms.Compose([
#     transforms.RandomHorizontalFlip(p=0.5),
#     transforms.RandomVerticalFlip(p=0.2),
#     transforms.RandomRotation(degrees=15),
#     transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),
#     transforms.RandomResizedCrop(size=(224, 224), scale=(0.8, 1.0)),
#     transforms.ToTensor()
# ])


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


# Directory paths
input_dir = "D:/yogi/shoppin/ImageNet-Mini/images"  # Replace with the path to your original images
output_dir = "D:/yogi/shoppin/ImageNet-Mini/augmented_images"  # Replace with the desired output directory
os.makedirs(output_dir, exist_ok=True)

# # Number of augmentations per image
num_augmentations = 50

for dir, folder, files in os.walk(input_dir):

    for filename in files:

        file_path = os.path.join(dir, filename)
        image = Image.open(file_path)
        # print(output_dir)
        # print(dir)
        # print(os.path.basename(dir))
        # break
        
        for i in range(num_augmentations):
            augmented_image = augmentation_transforms(image)
            augmented_image = transforms.ToPILImage()(augmented_image)  # Convert back to PIL for saving

            # Convert to RGB if the image is in RGBA mode
            if augmented_image.mode == 'RGBA':
                augmented_image = augmented_image.convert('RGB')
            
            # Save augmented image
            base_name, ext = os.path.splitext(filename)
            augmented_filename = f"{base_name}_aug_{i}{ext}"
            output_folder= os.path.join(output_dir, os.path.basename(dir))
            print(output_folder)

            os.makedirs(output_folder, exist_ok=True)
            augmented_image.save(os.path.join(output_folder, augmented_filename))


print(f"Augmented images saved to {output_dir}")


# # Directory paths
# input_dir = "D:/yogi/shoppin/ImageNet-Mini/images/n15075141"  # Replace with the path to your original images
# output_dir = "D:/yogi/shoppin/ImageNet-Mini/augmented_images/n15075141"  # Replace with the desired output directory

# # Augment and save images
# for filename in os.listdir(input_dir):
#     print(filename)
#     if filename.endswith(('.jpg', '.png', '.JPEG')):  # Check for image files
#         file_path = os.path.join(input_dir, filename)
#         image = Image.open(file_path)
        
#         for i in range(num_augmentations):
#             augmented_image = augmentation_transforms(image)
#             augmented_image = transforms.ToPILImage()(augmented_image)  # Convert back to PIL for saving

#             # Convert to RGB if the image is in RGBA mode
#             if augmented_image.mode == 'RGBA':
#                 augmented_image = augmented_image.convert('RGB')

#             # Save augmented image
#             base_name, ext = os.path.splitext(filename)
#             augmented_filename = f"{base_name}_aug_{i}.jpg"  # Save as JPEG
#             print(output_dir)
#             os.makedirs(output_dir, exist_ok=True)
#             augmented_image.save(os.path.join(output_dir, augmented_filename))

# print(f"Augmented images saved to {output_dir}")
