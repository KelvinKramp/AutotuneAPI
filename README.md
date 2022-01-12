# OpenAPS Autotune

This is a diabetic focused SaaS service created to...

## Run the project from scratch

### Setup GCP
- Open a new GCP Account and create a new project within your preferred organisation.
- Once the project has been initialised, open the Cloud Shell console located in the toolbar towards the top right of the page.
- This will spawn a new window featuring a feature rich terminal anchored at the bottom of the browser.
- It will take upwards of a minute to warm up.
- When completed, you will need to run the following command:
  - As this is likely a new fresh Cloud Shell, it will only come with the default configuration served by Google.
- Within this shell, we want to pull files from a remote Github/Bitbucket Repository onto the shell.

### Create SSH Key
  - This is so that we can prepare the projet for Google Cloud App Deployment for enabling a more efficient workflow when the service is live.
- To achieve this, run the following command within the warmed up Cloud Shell terminal:

  - ```ssh-keygen -t rsa``` // This is a base configuration command. If greater security and future proofing is required, you can use ED25519 although it is not yet universally configurable on all platforms. Also if you want to increase the key length/strength of the ssh key produced from the standard rsa option, you can define using -s 4096 or something higher (ideally in multiples of 1024).
  - There will be multiple prompts asking you for further configurable options to the SSH key, such as location of the key and a passphrase to greater reduce the risk of key leakage from your local machine.
  - As this is a test, I am leaving the options blank by clicking enter on all of them.
  - Once completed, I will be returned to the base command prompt with my new SSH key stored within my home directory's .ssh folder.
- Upon creation of the new SSH key, you will need to retrieve the SSH key's public file (.pub) from your local machine and copy it. 
  - This can be achieved by using the cat command and copying the content to your clipboard using CTRL/CMD + C keyboard shortcuts.
- Having retrieved your key, you can then go to your Github account and load the new SSH key as a trusted host. This is done by navigating to your profile picture at the top right, clicking the "Settings" menu and selecting the "SSH and GPC Keys" option in the left navigation pane. 
  - When loaded, a green button can be seen at the top of the page asking to create a "New Key". 
  - Click on the button and paste into the newly loaded textbox the content of your key.
  - Click "Submit" and now your Google Cloud Shell will have access to your Github repositories. (Reminder that explicit permissions can be set to deny this SSH key from performing actions on certain repositories/branches).

### Make Github Repository
- Create a Github Repository containing the project folders and files.
- Copy the URL of the Github Repository 
- Within the Cloud Shell, run the following command:
  - git clone <AUTOTUNE PROJECT GIT URL>
- If done correctly, your project files will be within your Cloud Shell user's home directory.

### Setup Project
- To setup the project, you will need to firstly make the installation file and executable.
- To do this, run the following:
  - chmod +x ~/<AUTOTUNE PROJECT DIR NAME>/install.sh
- Then you can run:
  - ~/<AUTOTUNE PROJECT DIR NAME>/install.sh
- Let it run the script and install the required dependencies. This could take anywhere from 15-30 minutes.
- When completed, you should have most of the required dependencies required to install.
- Next run the following command from the root of the project directory:
  - ```source ./venv/bin/activate```
  - This will source the environment variables from the virtual environment already setup for this project.
- Finally, run the last few commands:
  - pip3 install flask_restful as this was not included in the initial requirements.txt (This has been added to requirements.txt with camel-case)

### Testing Project
- If the steps has been followed, you should be able to successfully run the test scripts within the test folder in the project directory.
- This can be done using the following command:
  - ```python3 test/req-get-profile.py```
  - ```python3 test/req-run-autotune.py```
### Deploying Project
- Right now the project exists only locally on the google shell with the server only locally accessible. 
- To allocate a dedicated host to serve this content independently of the server, we will need to make it remote.
- To do this, you will need to run the following command in the root of the project directory: 
  - ```gcloud app create```

- Once executed, a prompt will show asking to select the region and availability zone that the server should be located in.
- This is important in cloud engineering as latency, costs and legal jurisdiction (Data Protection Act specifically) are affected by this choice especially if your application contains a user's sensitive/medical data.
- In this example, you can choose  the London region (europe-west2).
- Once picked, your app container will be created.
- Next, we will need to deploy the application. To do this, run the following command:
  - ```gcloud app deploy``` 
  - Another prompt will show asking to confirm your decision. You will need to enter "y".
application will begin the upload process to the Google Cloud Storage service where your service can be accessible on the browser as a seperate gcloud url address.
- Deployment will be executed.

### Adding Continuous Delivery
- An effective workflow will typically accomodate a Pipeline that allows for the continous delivery of new builds to the production environment.
- To add this feature to this project, we will need to do the following:
  - ```touch cloudbuild.yaml```
- Next, you will need to first enable certain APIs. To do this, you will need to go to this URL:
  - https://console.cloud.google.com/flows/enableapi?apiid=appengine.googleapis.com,cloudbuild.googleapis.com
  - Click the "ENABLE" button.
- Then go to:
  - https://console.cloud.google.com/cloud-build/settings
  - And for the GCP service "App Engine", change the status to "Enabled".
- Finally, you can set up the Cloud Build Triggers that will deliver changes to your production environment.
- To do this, go to: 
  - https://console.cloud.google.com/cloud-build/triggers
  - You will be asked to "Connect your Repository".
  - You will need to follow the on-screen steps to complete this.
  - Upon asking about the rules for trigger, it gives the option of pushing based on a certain branch. You will need to change this so changes only made in the main branch are deployed to GCP.
  - And that is all setup. 
  - Any changes pushed to the main branch will trigger the Cloud Pipeline setup through Cloud Build and push those changes to the Google App Service.

  ### Routes
  #### Get Profile 
  - https://<URL HERE>/api/get-profile?--nightscout=https%3A%2F%2Ftig-diab.herokuapp.com%2F&--start-date=2021-12-30&--end-date=2022-01-04

   #### Run Autotune
  - https://<URL HERE>/api/run-autotune?--nightscout=https%3A%2F%2Ftig-diab.herokuapp.com%2F&--start-date=2021-12-30&--end-date=2022-01-04