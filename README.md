# Lensify

Lensify is a project aimed at creating an alternative to Google Lens by demonstrating different feature extraction approaches. The effectiveness of Lensify lies in its ability to extract highly discriminative features, making it versatile for tasks such as image classification, object detection, and other computer vision applications.

# 🎯 Objective
The core idea behind Lensify is to explore the impact of various feature extraction techniques on the performance of tasks typically associated with Google Lens. By experimenting with different approaches, this project highlights the strengths and limitations of each method.

# 🔧 Approaches Used
Lensify demonstrates the following five approaches for feature extraction:

# CNN-Based Feature Extractor

Convolutional Neural Networks (CNNs) are used to extract spatial and hierarchical features from images.

# YOLO-Based Feature Extractor

YOLO (You Only Look Once) is employed for its real-time object detection and feature extraction capabilities.

# Transformer-Based Feature Extractor

Leveraging the attention mechanism in Transformers to capture global context and relationships within the image.

# Autoencoder-Based Feature Extractor

A self-supervised learning approach that reconstructs input images to learn latent representations.
Segmentation Mask + CNN-Based Feature Extractor

Combines segmentation masks with CNNs to focus feature extraction on specific regions of interest in an image.

# Attention-Based Feature Extractor (Optional/Additional)

Uses advanced attention mechanisms for fine-grained feature extraction, enhancing the ability to capture intricate relationships.
📂 Repository Structure
plaintext
Copy code
Lensify/
├── checkpoints
├── demo1.ipynb              # CNN-based feature extractor
├── demo2.ipynb             # YOLO-based feature extractor
├── demo3.ipynb      # Transformer-based feature extractor
├── demo4.ipynb      # Autoencoder-based feature extractor
├── demo5.ipynb     # Segmentation mask + CNN approach
├── utils/                   # Utility functions
└── README.md                # Documentation (this file)


# 🧠 Working of Lensify
The core functionality of Lensify depends on the quality of the feature extractor. A good feature extractor generates highly discriminative inter-class features, improving task performance. For detailed understanding see the flowchart in Lensify.docx

Key insights:

The effectiveness of the feature extractor increases with the number of classes used during training.
The problem is inherently open-ended, meaning improvements in the extractor directly enhance the overall system.

# ✨ Results:
The approaches which gave me promising results are Transformer based and CNN based.
Transformer:
Average Precision- 1   |   Average Recall- 0.365
CNN Based:
Average Precision- 0.99 | Average Recall- 0.365
