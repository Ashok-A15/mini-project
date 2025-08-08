# 🩺 Diabetic Retinopathy Detection

A deep learning-based web application to detect the severity of **Diabetic Retinopathy** from retinal fundus images.  
The project uses a **Convolutional Neural Network (CNN)** (ResNet50) trained on the **APTOS 2019 Blindness Detection** dataset, with a Flask backend and an interactive frontend.

---

## 📌 Features
- **Automated Image Analysis**: Detects DR severity levels from retinal fundus images.
- **Flask Web App**: User-friendly interface for uploading images.
- **Deep Learning Model**: Uses **ResNet50** with TensorFlow/Keras.
- **Visualization**: Shows prediction confidence and classification chart.
- **Responsive UI**: Designed with HTML, CSS, and JavaScript.

---

## 📂 Project Structure

diabetic-retinopathy-detection

│── app.py # Flask app entry point

│── model/ # Saved model files

│── static/ # CSS, JS, and images

│── templates/ # HTML templates (upload, results, charts)

│── requirements.txt # Python dependencies

│── README.md # Project documentation

│── .gitignore # Ignoring large dataset files


## 📊 Dataset
This project uses the **APTOS 2019 Blindness Detection** dataset.  
Due to its large size (>10GB), it is **not included in this repository**.  
You can download it from:

🔗 **[Kaggle - APTOS 2019 Dataset](https://www.kaggle.com/competitions/aptos2019-blindness-detection/data)**

After downloading, place the dataset in a `data/` folder:
diabetic-retinopathy-detection/data/
├── train_images/
├── test_images/
└── train.csv


## ⚙️ Installation & Usage

### 1️⃣ Clone the Repository
bash
git clone https://github.com/YOUR_USERNAME/diabetic-retinopathy-detection.git
cd diabetic-retinopathy-detection

2️⃣ Install Dependencies
pip install -r Flask
pip install -r Flask-SQLAlchemy
pip install -rmysqlclient
pip install -rpymysql
pip install -rFlask-Migrate
pip install -rpython-dotenv

pip install -r requirements.txt

3️⃣ Download the Dataset
Download from Kaggle and place inside the data/ folder.


4️⃣ Run the Application
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

# Open your browser and go to:
http://127.0.0.1:5000/

🧠 Model Details
Architecture: ResNet50 (pre-trained on ImageNet, fine-tuned for DR detection)

Framework: TensorFlow / Keras

Loss Function: Categorical Crossentropy

Optimizer: Adam

Metrics: Accuracy, Quadratic Weighted Kappa

📈 Output Examples
Prediction Result Page

Displays uploaded image.

Shows predicted DR severity level.

Pie chart for probability distribution.

Severity Classes

0: No DR

1: Mild

2: Moderate

3: Severe

4: Proliferative DR

🚀 Deployment
This app can be deployed on:

Heroku

Render

AWS EC2

PythonAnywhere

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.


## 🤝 Acknowledgements

- **Kaggle** – APTOS 2019 Blindness Detection Dataset  
- **TensorFlow / Keras** – Deep learning model framework  
- **Flask** – Backend web framework  
- **OpenCV & NumPy** – Image preprocessing and manipulation  
- **Matplotlib** – Data visualization  

I can also make you a **`.gitignore` file** that automatically excludes your dataset so GitHub won’t reject the upload due to size.  

Do you want me to prepare that `.gitignore` along with the README so your repo is ready to push without errors?








Ask ChatGPT





