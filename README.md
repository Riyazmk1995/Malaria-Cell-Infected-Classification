# Malaria-Cell-Infected-Classification

A GUI based application which uses a custom CNN model(Accuracy: 100%) to predict if an uploaded cell image is parasitized or uninfected. At first a CNN- Deep learning model was trained and tested in jupyter notebook then in order to give it a user interface, streamlit module in Python is used.

Dataset: https://www.kaggle.com/iarunava/cell-images-for-detecting-malaria

System will read the image uploaded by the user, augment it and will use the saved custom model to detect whether the disease is present or not in the patient and thus display the result in a user-friendly language.

Below are the steps:-
Upload Image: The user can upload the medical test image through a workstation running on Windows OS. The image should be in jpeg, png or jpg format.
Read Image: The image will be scanned before augmentation takes place.
Transform Image: The scanned image is then transformed into a format that is needed by the saved custom model.
Evaluate image using saved model: The saved custom model creates a feature map of the uploaded medical test image and predicts the output.
Determine and Analyze the Output: The predicted output is then analyzed and converted to a user friendly language.
Display the Output: The analyzed result is then displayed to the user.
