from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import io
import base64  # Import the base64 module
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
from PIL import Image

app = Flask(__name__)

# Allowed file extensions
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}

# Load the model
model = load_model('model/resnet50_brain_model.h5')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def predict_tumor(image_bytes):
    # Load the image from bytes
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((224, 224))  # Resize according to model input size
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)

    # Predict using the loaded model
    prediction = model.predict(img)
    # Assuming binary classification (0: No Tumor, 1: Tumor)
    return 'No Tumor Detected' if prediction[0][0] > 0.5 else 'Tumor Detected'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            image_bytes = file.read()  # Read the image into memory
            prediction = predict_tumor(image_bytes)  # Make prediction using the image bytes
            
            # Convert image bytes to base64 for inline display
            image_base64 = base64.b64encode(image_bytes).decode('utf-8')  # Convert bytes to base64 string
            
            # Create the image URL as a data URI
            image_url = f"data:image/jpeg;base64,{image_base64}"
            return render_template('index.html', filename=filename, prediction=prediction, image_url=image_url)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
