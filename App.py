import streamlit as st #we can call this library as st in the code that we will create.
from PIL import Image, ImageOps #we can call this library for load images and performing operations on load images.
import tensorflow as tf
import numpy as np
st.write("""
          # Malaria Cell Classification
          """
          )
upload_file = st.sidebar.file_uploader("Upload Cell Images", type="png")
Generate_pred=st.sidebar.button("Predict")
model=tf.keras.models.load_model('malaria_cell.h5')
def import_n_pred(image_data, model):
    size = (150,150)
    image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    img = np.asarray(image)
    reshape=img[np.newaxis,...]
    pred = model.predict(reshape)
    return pred
if Generate_pred:
    image=Image.open(upload_file)
    with st.beta_expander('Cell Image', expanded = True):
        st.image(image, use_column_width=True)
    pred=import_n_pred(image, model)
    labels = ['Parasitized', 'Uninfected']
    st.title("Prediction of image is {}".format(labels[np.argmax(pred)]))