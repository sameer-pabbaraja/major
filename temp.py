import os
from pathlib import Path


from flask import Flask, render_template, request
#import tensorflow as tf
#model=tf.keras.models.load_model("model/model.h5",compile=False)
IMAGE_SIZE=(256,256)
UPLOAD_FOLDER=os.path.join('static')
app = Flask(__name__)
