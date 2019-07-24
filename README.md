# 60daysofudacity_challenge
60 days of Udacity challenge: federated leaning and differential privacy mini-projects

# KeyStone Project overview
Basic idea: implement the federated learning and differential privacy with a real web and mobile app, using a trained model in Pytorch.

## day 7
- implemented a post API with Flask for the model of house price prediction in Keras from the book Mobile Artificial Intelligence Project. 
I have also implemented the mobile app but could not get to work it properly in Kotlin code. 

## day 8
- finished to code my first mobile app with flask api and keras model!
See Predict real estate prices with Keras

## day 11-12
Step 1: Train a Pytorch model with flower dataset. 
I have trained two models during the Pytorch Challenge and the Bossom Challenge during the Private AI course

## day 15
Step 2: Create a Web app
I have created a basic web app with Flask with a post API which is in the Flower_AppAPI folder

## day 16
Step 3: Create a mobile app 
create a simple app that loads an image and predict the flower name
a. create the app in kotlin
b. load the model in the mobile app to show the prediction
     how to convert the pytorch model for Android, after some research these are my options:
    - convert the pytorch model to Caffe2 and load the model in the app
	https://github.com/onnx/tutorials/blob/master/tutorials/Caffe2OnnxExport.ipynb
	https://heartbeat.fritz.ai/transferring-machine-learning-models-from-pytorch-to-caffe2-and-mobile-using-onnx-10eb266eaacb
    - convert the image to tensor and send it to the API
    - try Pytorch Lite but it looks as the dev it is not finished
	 https://github.com/cedrickchee/pytorch-lite
Step 4: implement PySyft and Federated learning
	  https://github.com/OpenMined/AndroidWorker


## day 18
Step 3b: convert Pytorch model to Onnx and Caffe2
The converting to onnx was easy, the Caffe2 part was a bit more work, the dependencies were not installed.
Error: No module name past
was resolved by installing future package in conda (dit not work in pip)
See result in Convert Pytorch model to ONNIX notebook!
Todo: try it out in the Android app

## day 19
Step 3b, option 1: converting pytorch to .pb for Android was not difficult but then there is no info on how to use this model in Android itself.
Tried a lot of tutorials, nothing worked really
New solution: convert .onnix to Tensorflow, it seems like an easier option.
The conversion seems to work.
