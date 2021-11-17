# import os
# import time

# from flask import Flask, request
# import pyspark
# from pyspark import SparkContext
# from pyspark.sql import SparkSession
# from pyspark.ml.classification import RandomForestClassificationModel
# from pyspark.ml.linalg import Vectors as ml_vectors

# app = Flask(__name__)
# sc = SparkContext(appName="Research_Notebook")


# model = RandomForestClassificationModel.load('random_forest_model')


# @app.route('/')
# def hello():
    
#     return """
#             <!DOCTYPE html>
# <html>
#     <head>
#         <title>PI Model</title>
#     </head>
#     <body>
#         <header></header>
#           <h1>Purchase Intent Prediction</h1>
#         <div>
#             <form action="/predict" method="POST">
#               <label for="views">Views</label>
#               <input type="number" id="views" name="views">
#               <label for="time">Time after VisitStartTime</label>
#               <input type="number" id="time" name="time">
#               <label for="hitNumber">Number of Hits</label>
#               <input for="hitNumber" id="hitNumber" name="hits">
#               <label for="action">Action Type</label>
#               <select id="action" name="action">
#                   <option value="0">0</option>
#                   <option value="1">1</option>
#                   <option value="2">2</option>
#                   <option value="3">3</option>
#                   <option value="4">4</option>
#                   <option value="5">5</option>
#                   <option value="6">6</option>
#               </select>
#               <label for="isclick">Click?</label>
#               <select id="isclick" name="isclick">
#                   <option value="1">True</option>
#                   <option value="0">Null</option>
#               </select>
#               <br>
#               <input type="submit" value="Submit">
#             </form>
#             <h1> Prediction: { prediction }</h1>
#         </div>
#     </body>
# </html>
    
# """

# @app.route('/predict', methods=['POST'])
# def predict():
#     if request.method == 'POST':
#         predict_list = request.form.to_dict()
#         predict_list = list(predict_list.values())
#         predict_list = list(map(int, predict_list))

#         predicted = model.predict(ml_vectors(predict_list))

#         if int(predicted) == 0:
#             prediction = "Ecommerce User Action: Unknown, Not Transacting"
#         elif int(predicted) == 1:
#             prediction = "Ecommerce User Action: Click Through of Product list, Not Transacting"
#         elif int(predicted) == 2:
#             prediction = "Ecommerce User Action: Cart , Not Transacting"
            
#         else: prediction = "Ecommerce User Action: Purchase, Transacting" 

#         return 'prediction'