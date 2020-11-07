# MNIST Image Recognition API with Docker
Production grade version of a image recognition application. The MNIST data is one of the most common toy data sets for image classification. Here a CNN was trained to classify handwritten digits with Keras.


## API
The API serves with two endpoints:
 1. localhost:5000/predict_digit [POST] [Key = `image`]

The api based on `flask`. 

## Docker
For launching the application  with docker use the following commands:

 `cd api`   
 `docker build --tag img_predict .`  
 `docker run -p 0.0.0.0:5000:5000/tcp --name img_predict img_predict`  

*The last command starts a new docker container*


***
**Credentials**  
This project based on the udemy course Deploy Machine Learning & NLP Models with Dockers (DevOps): https://www.udemy.com/course/deploy-data-science-nlp-models-with-docker-containers/
