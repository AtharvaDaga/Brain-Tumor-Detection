# Brain-Tumor-Detection
🧠 **Brain Tumor Detection using Fused MRI & CT Images**

📌 **Project Overview**

This project presents a deep learning–based brain tumor detection system that combines MRI and CT scan images using advanced image fusion techniques.  
By leveraging the complementary strengths of MRI (soft tissue contrast) and CT (structural details), the model improves tumor identification accuracy and robustness.

The system evaluates multiple pre-trained CNN models (VGG-19, Densenet121, and ResNet-50) using transfer learning to determine the most effective model for binary brain tumor classification.

🎯 **Objectives**

- Combine MRI and CT images to enhance diagnostic information  
- Apply image fusion using wavelet transforms  
- Compare performance of pre-trained deep learning models  
- Identify the most accurate model for brain tumor detection  
- Support early and reliable diagnosis using AI-assisted analysis  

✨ **Key Highlights**

- Multi-modal image fusion using wavelet transforms  
- Transfer learning with VGG-19  
- Tumor boundary refinement with Watershed Algorithm  
- Data augmentation to improve generalization  
- Independent validation on real patient images  

🖼️ **Outputs**

📊 **Plots**

- **Snapshot of Accuracy plot showing model performance over epochs:**  
![Accuracy over epochs](https://github.com/AtharvaDaga/Brain-Tumor-Detection/blob/238bb09a8affcbed83532e6d023bbf05736087ea/Images/plots/Plot_accuracy_over_epochs.jpg)  

- **Snapshot of Loss plot showing how loss decreases over epochs:**  
![Loss over epochs](https://github.com/AtharvaDaga/Brain-Tumor-Detection/blob/238bb09a8affcbed83532e6d023bbf05736087ea/Images/plots/Plot_Loss_over_epochs.jpg)  

💻 **System Snapshots**

- **Snapshot of Image Upload interface:**  
![Image Upload](https://github.com/AtharvaDaga/Brain-Tumor-Detection/blob/238bb09a8affcbed83532e6d023bbf05736087ea/Images/system/Snapshots%20of%20Image%20upload.jpg)  

- **Snapshot of Image Registration interface:**  
![Image Registration](https://github.com/AtharvaDaga/Brain-Tumor-Detection/blob/238bb09a8affcbed83532e6d023bbf05736087ea/Images/system/Snapshot%20of%20Image%20Registeration.jpg)  

- **Snapshot of Registered Image:**  
![Registered Image](https://github.com/AtharvaDaga/Brain-Tumor-Detection/blob/238bb09a8affcbed83532e6d023bbf05736087ea/Images/system/Snapshot%20of%20Registered%20Image.jpg)  

- **Snapshot of Fused Image combining MRI and CT scans:**  
![Fused Image](https://github.com/AtharvaDaga/Brain-Tumor-Detection/blob/238bb09a8affcbed83532e6d023bbf05736087ea/Images/system/Snapshot%20of%20Fused%20Image.jpg)  

- **Snapshot of Segmented Image:**  
![Segmented Image 1](https://github.com/AtharvaDaga/Brain-Tumor-Detection/blob/238bb09a8affcbed83532e6d023bbf05736087ea/Images/system/Snapshot%20of%20Segmented%20Image.jpg)  

- **Snapshot of  Tumor Detection:**  
![Segmented Image 2](https://github.com/AtharvaDaga/Brain-Tumor-Detection/blob/238bb09a8affcbed83532e6d023bbf05736087ea/Images/system/Snapshot%20of%20Segmented%20Image.jpg)  

🛠️ **Tech Stack**

- Languages: Python, HTML, CSS  
- Libraries: TensorFlow, Keras, PyTorch, OpenCV, NumPy, Matplotlib  
- Techniques: Image fusion, Transfer learning, CNNs, Watershed segmentation  
- Framework: Flask  

📄 **Research Paper**

Comparative Evaluation of Pre-Trained Models for Brain Tumor Identification based on MRI and CT Image  
[Read the full paper here](https://ijsret.com/wp-content/uploads/IJSRET_V11_issue5_108.pdf)
