# Immo Eliza

![Static Badge](https://img.shields.io/badge/python-3.12-green?logo=python&color=%23FFE873) 
![Static Badge](https://img.shields.io/badge/scikitlearn-1.5.1-blue?logo=scikitlearn&color=%23F7931E) 
![Static Badge](https://img.shields.io/badge/fastapi-0.112-blue?logo=fastapi&color=%23009688) 
![Static Badge](https://img.shields.io/badge/streamlit-1.37.1-blue?logo=streamlit&color=%23FF4B4B) 

![](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExeWdvMHRvaDRwMzB5dHBsODVzMm04bGJxdGo4emwwdWdmMmM3OWp5eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1wrRQfA0DcS7n3zaX0/giphy.gif)
## 📚 Overview

This is a small project about predicting the price of a house in Belgium, as part of a learning journey at [Becode](https://becode.org/).

## 🔍 Pedagogic objective

The goal here was to deploy a model that we previously worked on using `FastAPI` and `Streamlit` to learn about them, and produce an pp usable by anyone without the technical knowledge.

## 🕺 Collaborators
Thank you for your contributions to this project : 

- [Laura](https://github.com/KriszgruberL), for the nice README template.

## ⚒️ Setup

### For local usage

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Jojopanis/immo_eliza.git
    cd immo_eliza
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv #On some OS, it can be 'python3'
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## ⚙️ Usage

### Local

1. Since both the preprocessing and the actual machine learning models are too heavy for github, you will have to regenerate them using these scripts :

```py
python preprocessing.py
python machine_learning.py
```
2. Launch the api and the front-end on 2 separate instances (you can use the `screen` command for that)
```py
fastapi run fastapi.py
```
```py
streamlit run streamlit.py
```
Check the address provided by you streamlit instance, usually http://localhost:8501 and enjoy the app!
### Online
I host this app on my own server at home, accessible via this address `coming soon (I don't want to expose my public IP on a public repo)`
