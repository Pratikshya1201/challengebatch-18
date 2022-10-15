# AI Challenge Batch-18

## 💁 Description

The goal of this challenge is to create an AI model to **predict the number of accidents** based on parameters like category, accident-type, year and month and then deploy it. The model is trained using Machine Learning algorithms such as Linear Regression, XGB Regression model, Random Forest Model and LightGBM model and predicted the values for number of accidents. **XGB Regression** ensemble learning algorithm gave R2 score as **0.98**, therefore I chose this algorithm for prediction purpose.

## 💻 Demo

## Project Setup

- `Step 1:`

```bash
git clone https://github.com/Pratikshya1201/challengebatch-18.git
```

- `Step 2:`

```bash
cd challengebatch-18
```

- `Step 3:`

```bash
pip install -r requirements.txt
```

- `Step 4:`

```bash
python app.py
```

## 🛠 Built with

<li><a href="https://flask.palletsprojects.com/en/2.2.x/">Flask</a> : Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.</li>

## 📦 Packages

<li><a href="https://pandas.pydata.org/">pandas</a> : pandas is a software library written for the Python programming language for data manipulation and analysis.</li>
<li><a href="https://matplotlib.org/">Matplotlib</a> : Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.</li>
<li><a href="https://scikit-learn.org/stable/">Sklearn</a> : Scikit-learn is probably the most useful library for machine learning in Python. The sklearn library contains a lot of efficient tools for machine learning and statistical modeling including classification, regression, clustering and dimensionality reduction.</li>
<li><a href="https://seaborn.pydata.org/">Seaborn</a> : Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.</li>
<li><a href="https://numpy.org/">NumPy</a> : NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. </li>
<li><a href="https://xgboost.readthedocs.io/en/stable/">XGBoost</a> : XGBoost, which stands for Extreme Gradient Boosting, is a scalable, distributed gradient-boosted decision tree (GBDT) machine learning library.</li>
<li><a href="https://practicaldatascience.co.uk/machine-learning/how-to-save-and-load-machine-learning-models-using-pickle#:~:text=Pickle%20is%20a%20useful%20Python,for%20serializing%20and%20deserializing%20objects">pickle</a> : Pickle is a useful Python tool that allows you to save your models, to minimise lengthy re-training and allow you to share, commit, and re-load pre-trained machine learning models.</li>

## 📈 Data Visualization

### Number of accidents per category for month 'Summe':

![stacked-bar](https://user-images.githubusercontent.com/74849723/195918880-6e23156f-e96e-4ba8-a46e-a27b1c95bae1.png)

![area](https://user-images.githubusercontent.com/74849723/195919024-0db3449e-f393-4bb8-b0a5-fade1fded475.png)

![bar](https://user-images.githubusercontent.com/74849723/195919286-ae7d206e-0598-4948-a89d-c26cfa0890f9.png)

![line](https://user-images.githubusercontent.com/74849723/195919466-365a1056-12bc-4b19-b6ee-0052fab61777.png)

### Number of accidents per category :

![pie](https://user-images.githubusercontent.com/74849723/195919969-015e6cda-9778-4cc9-bcb9-d4bbd126cac5.png)

![barplot](https://user-images.githubusercontent.com/74849723/195920063-289ea70c-9428-4831-98a0-ff260bdd540f.png)
