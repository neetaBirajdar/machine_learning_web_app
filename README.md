# machine_learning_web_application

Machine learning can be more fun when you create a beginners application with it. The magic happening live 🪄 .
So, I have created this basic web-application which detects/predicts the input number provided to it via an image format. More details are : [blog/tech_ml_application/](https://neetabirajdar.github.io/blog/tech_ml_application/)

## How to start running the application: 

- Create a python env, its important to not do any changes within your root python setting, so create a python virtual env, ie with direnv, venv etc.. 
- Use pip to install all the requirements: 
```   
pip install -r requirements.txt
```
- If you have added the trained_model.keras file in your repository then you can use that for predicting your input number. I would recommend you delete that file and let the model train again when you run the application to understand how the model gets trained. 
- Run fast-api application to start the application: 
```
uvicorn main:app --reload   
```
- You can play around. 


## Remember: 
I have added some input images which are not properly predicted as it was not the part of train set, so the accuracy currently is 98.7% . You can add some extra images and try it yourself for fun. 


