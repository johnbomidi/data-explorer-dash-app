# Data Explorer Dash App

Dash App to explore Time Series or data that has a sequence index

![image](https://user-images.githubusercontent.com/37553132/161395296-2026cd38-3e52-40f3-9d91-0914a5eeee6e.png)


## Running locally

To run a development instance locally, ensure you have the 
requirements from `requirements.txt` and launch `app.py` using the 
Python executable.

## Deploying on ECS

Use `make image` to create a Docker image. Then, follow [these 
instructions](https://www.chrisvoncsefalvay.com/2019/08/28/deploying-dash-on-amazon-ecs/) 
to deploy the image on ECS.
