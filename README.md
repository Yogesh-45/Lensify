# Lensify

Lensify is a project aimed at creating an alternative to Google Lens by demonstrating different feature extraction approaches. The effectiveness of Lensify lies in its ability to extract highly discriminative features, making it versatile for tasks such as image classification, object detection, and other computer vision applications.

# 🎯 Objective
The core idea behind Lensify is to explore the impact of various feature extraction techniques on the performance of tasks typically associated with Google Lens. By experimenting with different approaches, this project highlights the strengths and limitations of each method.

# 🔧 Approaches Used
Lensify demonstrates the following five approaches for feature extraction:

### CNN-Based Feature Extractor

Convolutional Neural Networks (CNNs) are used to extract spatial and hierarchical features from images.

### YOLO-Based Feature Extractor

YOLO (You Only Look Once) is employed for its real-time object detection and feature extraction capabilities.

### Transformer-Based Feature Extractor

Leveraging the attention mechanism in Transformers to capture global context and relationships within the image.

### Autoencoder-Based Feature Extractor

A self-supervised learning approach that reconstructs input images to learn latent representations.

### Segmentation Mask + CNN-Based Feature Extractor

Combines segmentation masks with CNNs to focus feature extraction on specific regions of interest in an image.

# 📂 Repository Structure

Lensify/

├── checkpoints

├── demo1.ipynb     &nbsp; &nbsp; &nbsp;  # CNN-based feature extractor

├── demo2.ipynb     &nbsp; &nbsp; &nbsp;        # YOLO-based feature extractor

├── demo3.ipynb    &nbsp; &nbsp; &nbsp;           # Transformer-based feature extractor

├── demo4.ipynb          &nbsp; &nbsp; &nbsp;     # Autoencoder-based feature extractor

├── demo5.ipynb            &nbsp; &nbsp; &nbsp;   # Segmentation mask + CNN approach


└── README.md                 


# 🧠 Working of Lensify
The core functionality of Lensify depends on the quality of the feature extractor. A good feature extractor generates highly discriminative inter-class features, improving task performance. For detailed understanding see the flowchart in Lensify.docx


# ✨ Results:
The approaches which gave me promising results are Transformer based and CNN based.

### Transformer:
Average Precision @ k=10- 1     |   Average Recall @ k=50- 0.365

### CNN Based:
Average Precision @ k=10- 0.99  |   Average Recall @ k=50- 0.365

### YOLO Based:
Average Precision @ k=10- 0.869 |   Average Recall @ k=50- 0.277

### Autoencoder Based:
Average Precision @ k=10- 0.6 |   Average Recall @ k=50- 0.113

# Checkpoints:
Checkpoints can be downloaded from the following link: https://drive.google.com/drive/folders/134FOh28aqSnUlUdXsGOoIBBn9taLvg1l?usp=drive_link
