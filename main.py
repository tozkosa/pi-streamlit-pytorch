import streamlit as st
from PIL import Image

import style

st.title("Pytorch Style Transfer")

img = st.sidebar.selectbox(
    'Select image',
    ('amber.jpg', 'ring.jpg')
)

style_name = st.sidebar.selectbox(
    'Select Style',
    ('candy', 'mosaic', 'rain_princess', 'udnie')
)

model = "saved_models/" + style_name + ".pth"
input_image = "images/content-images/" + img
output_image = "images/output-images" + style_name + "-" + img

left_column, right_column = st.beta_columns(2)

left_column.write("### Source Image:")
image = Image.open(input_image)
left_column.image(image, width=200)

clicked = left_column.button("Stylize")

if clicked:
    model = style.load_model(model)
    style.stylize(model, input_image, output_image)
    right_column.write("### Output Image:")
    image = Image.open(output_image)
    right_column.image(image, width=200)
