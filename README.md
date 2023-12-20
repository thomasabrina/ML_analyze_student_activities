This repository contains all the documents for this Machine Learning course project, the purpose of the project is to analyse student semester activities and based on that predict student marks and classify students.

The Data folder holds the raw and cleaned data, Docs file is used to hold the project progress and meeting minutes and project requirements and other related documents, Slides folder holds the slides for the mid-term and final debriefing, Src file holds the machine learning code that implements the various functions, and the web application code.

We deployed the trained model using Flask and made a web page where we can upload a csv file with student data and get the predicted results on the web page by clicking the page button.

Packaging to save and load the trained model was done using joblib and pickle, Flask route was used to render and change the html page, Ajax and json were used to pass the data from the front end to the model and return the model data to the front end.

Download the project file, in the command line into the /Src/Web-app folder, use python app.py command can start Flask, successful start can be seen in the command line to the corresponding address: http://127.0.0.1:5000/, in the browser to access the address can be uploaded need to use and fill in the template, otherwise the model can not be processed! data, the template in /Src/Web-app/Upload_Templates folder.

This version of the web application is just a preliminary version, there are many places that can be improved, such as adding abnormal data processing functions in the front-end, the data uploaded by the user for the first check, if there is a problem with the corresponding processing, but also in the web page design of the input box, by the user to enter the data and automatically generate a csv file, so that you do not need to upload the user file. In addition, the output of the prediction results should also be modifiable to be more readable.
