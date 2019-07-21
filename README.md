# 60daysofudacity_challenge
60 days of Udacity challenge: federated leaning and differential privacy mini-projects

# KeyStone Project overview
Basic idea: implement the federated learning and differential privacy with a real web and mobile app, using a trained model in Pytorch.

## day 11-12
Step 1: Train a Pytorch model with flower dataset. 
I have trained two models during the Pytorch Challenge and the Bossom Challenge during the Private AI course

## day 15
Step 2: Create a Web app
I have created a basic web app with Flask with a post API which is in the Flower_AppAPI folder

## day 16
Step 3: Create a mobile app 
create a simple app that loads an image and predict the flower name
- create the app in kotlin
- load the model in the mobile app to show the prediction
    - now I need to convert the pytorch model for Android, after some research these are my options:
    - convert the pytorch model to Caffe2 and load the model in the app
    - convert the image to tensor and send it to the API
    - implement PySyft
    - try Pytorch Lite but it looks as the dev it is not finished



## day 18
Step 3a: convert Pytorch model to Onnx and Caffe2
The converting to onnx was easy, the Caffe2 part was a bit more work, the dependencies were not installed.
Error: No module name past
was resolved by installing future package in conda (dit not work in pip)
See result in Convert Pytorch model to ONNIX notebook!
