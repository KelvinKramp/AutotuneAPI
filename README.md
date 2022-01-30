# OpenAPS Autotune API

API version of OpenAPS Autotune application. Documentation of the original application can be found over [here](https://openaps.readthedocs.io/en/latest/docs/Customize-Iterate/autotune.html). 


### Installing Project on AWS

Use this tutorial to setup AWS EC2 instance. Stop at the moment that there is a connection with the instance from your local machine. 
https://www.youtube.com/watch?v=MAsp90tQGOA

Once your local machine is connected create SSH key:
  - ```ssh-keygen -t rsa``` 
  - There will be multiple prompts asking you for further configurable options to the SSH key, such as location of the key and a passphrase to greater reduce the risk of key leakage from your local machine.
  - Save the information you enter somewhere save.

Git clone this repository with this command. SSH key could be asked. Generate one according to protocol. 
  - ```git clone https://github.com/KelvinKramp/AutotuneAPI.git``` 

Run install.sh. 
  - ```./install.sh``` 

It could be that you have to change the mode by running:
  - ```chmod +x install.sh``` and  ```chmod +x print.sh``` 

Now continue the tutorial untill the gunicorn activation and use app.py from this repository instead of the app.py from the tutorial.

Extra tips:
https://medium.com/techfront/step-by-step-visual-guide-on-deploying-a-flask-application-on-aws-ec2-8e3e8b82c4f7


### Testing Project

#### Get profile:
  - https://"URL or Public IP HERE"/api/get-profile?--nightscout=https%3A%2F%2F"YOURNIGHTSCOUTURL"%2F&--start-date=2021-12-30&--end-date=2022-01-04

#### Run Autotune
  - https://"URL  or Public IP HERE"/api/run-autotune?--nightscout=https%3A%2F%2F"YOURNIGHTSCOUTURL"%2F&--start-date=2021-12-30&--end-date=2022-01-04
