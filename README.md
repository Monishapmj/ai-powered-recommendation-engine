COMPANY : CODTECH IT SOLUTIONS 
NAME : MONISHA J 
INTERN ID : CT04DL69
DOMAIN : BACK END DEVELOPMENT 
DURATION : 4 WEEKS 
MENTOR : NEELA SANTHOSH KUMAR

# 🧠 AI-Powered Recommendation Engine

This project is a simple yet powerful AI-powered recommendation system built with **Flask**, **scikit-learn**, and **content-based filtering** techniques like **TF-IDF** and **cosine similarity**. It exposes a RESTful API to fetch similar items (movies, products, etc.) based on their features.

---

## 🚀 Features

- 🔍 Content-based recommendation using text features
- 📊 TF-IDF vectorization and cosine similarity
- ⚙️ Lightweight and fast REST API with Flask
- 📁 CSV-based dataset (easy to extend to databases)
- 🔌 Plug-and-play local development

---

## 🗂️ Folder Structure

recommendation-engine/
│
├── app/
│ ├── init.py # Flask app setup
│ ├── model.py # ML logic (TF-IDF + similarity)
│ └── routes.py # API route definition
│
├── data/
│ └── items.csv # Sample item data
│
├── run.py # Entry point to run Flask app
├── requirements.txt # Required Python packages
└── README.md # Project documentation


---

## 📦 Requirements

- Python 3.9+
- pip

## Install dependencies:

pip install -r requirements.txt

## Running the App

python run.py

Server will start at:
http://127.0.0.1:5000

## API Usage
Endpoint
GET /recommend?id=<item_id>&top=<number_of_results>

Example
http://127.0.0.1:5000/recommend?id=1&top=2

## output

![image](https://github.com/user-attachments/assets/28de7668-de66-4ca0-a5e5-9496d3c67ff7)
![image](https://github.com/user-attachments/assets/ac7acf48-527e-417a-86b0-14715552452a)

## How It Works

Loads items from items.csv

Converts item features into numerical vectors using TF-IDF

Computes cosine similarity between items

Returns the top N most similar items based on content

## 📌 Future Improvements

Switch to collaborative filtering (e.g., using user ratings)

Store data in SQLite or MongoDB

Add user login + history tracking

Build a simple frontend to display recommendations

Add similarity scores to response

Dockerize the app for deployment

## 📃 License
This project is open-source and free to use for educational and prototyping purposes.

## 🙋‍♀️ Author
Monisha J.
Designed and developed as part of AI internship learning journey.





