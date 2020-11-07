# import keras
# print(keras.__version__)

from keras.models import load_model
from PIL import Image
import numpy as np

from flasgger import Swagger
from flask import Flask, request

app = Flask(__name__)
swagger = Swagger(app)

# load model form disk
model = load_model('./data/model.h5')

@app.route("/predict_digit", methods = ["POST"])
def predict_digit():
    """Endpoint returning a prediction of mnist
    ---
    parameters:
        - name: image
          in: formData
          type: file
          required: true
    """
    img = Image.open(request.files['image'])
    img2arr = np.array(img).reshape((1, 28, 28, 1))

    pred = model.predict(img2arr)
    pred = np.argmax(pred)

    print("Estimated digit %s " % pred)
    return str(pred)


if __name__ == '__main__':

    app.run(host = '0.0.0.0', port = 5000) 