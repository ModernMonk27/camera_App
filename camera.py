import streamlit as lt

from PIL import Image

camera = lt.camera_input("Start camera")

if camera:
    img = Image.open(camera)

    image_gray = img.convert("L")

    lt.image(image_gray)