from flask import Flask, render_template
from jinja2 import Environment, PackageLoader, select_autoescape
from keras.models import load_model
import numpy as np
from keras.preprocessing import image
import cv2
from keras.optimizers import SGD

app = Flask(__name__)

env = Environment(
    loader=PackageLoader('app', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

@app.route('/')
def index():
    template = env.get_template('index.html')
    model = load_model('.\model\CNN_2_category_picdoc_model.h5')
    #replace this picture path with the path to any image
    #on your system that you'd like the model to classify
    picturePath = '.\model\\facepalm.png'
    test_image = cv2.imread(picturePath)
    output = test_image.copy()
    test_image = cv2.resize(test_image, (32, 32)).flatten()
    test_image = test_image.reshape((1, test_image.shape[0]))
    result = model.predict(np.array(test_image), batch_size=1, verbose=1)

    return template.render(username='Alla', prediction=result)
