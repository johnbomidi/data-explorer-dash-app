# Data Explorer Dash App

Dash App to explore Time Series or data that has a sequence index

![image](https://user-images.githubusercontent.com/37553132/161395361-b8efae32-28c3-466e-9865-6daafdc13fea.png)

![image](https://user-images.githubusercontent.com/37553132/161395433-0863a0cd-f636-4c14-93b0-18d1608735a8.png)


## Running locally

To run a development instance locally, ensure you have the 
requirements from `requirements.txt` and launch `app.py` using the 
Python executable.

## Deploying on ECS

Use `make image` to create a Docker image. Then, follow [these 
instructions](https://www.chrisvoncsefalvay.com/2019/08/28/deploying-dash-on-amazon-ecs/) 
to deploy the image on ECS.
