 # Establish Python version
 PY_VER="3.8.12"
 
 # Install Python 3.8 through pyenv
 curl https://pyenv.run | bash
 echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
 echo 'eval "$(pyenv init -)"' >> ~/.bashrc
 echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
 source ~/.bashrc
 pyenv install ${PY_VER}
 pyenv global ${PY_VER}

 # save profile local
 mkdir ~/myopenaps
 mkdir ~/myopenaps/settings
# python3 googlecloud-autotune/get_profile.py -> im going this via the API now

 # install dependencies
 echo "STEP 1"
 sudo apt-get -o Acquire::ForceIPv4=true install -y
 echo "STEP 2"
 sudo apt-get -o Acquire::ForceIPv4=true update && sudo apt-get -o Acquire::ForceIPv4=true -y upgrade
 echo "STEP 3"
 sudo apt-get -o Acquire::ForceIPv4=true install -y git python-dev software-properties-common python-numpy python-pip nodejs-legacy npm watchdog strace tcpdump screen acpid vim locate jq lm-sensors bc
 echo "STEP 4"
 sudo apt-get install bc
 echo "STEP 5"
 sudo pip install -U openaps
 echo "STEP 6"
 sudo pip install -U openaps-contrib
 echo "STEP 7"
 sudo openaps-install-udev-rules
 echo "STEP 8"
 sudo activate-global-python-argcomplete
 echo "STEP 9"
 npm install -g json oref0
 echo "STEP 10"
 sudo apt-get install bc
 echo "STEP 11"
 sudo apt-get install jq

 # download javascript autotune pacakage and install node
 echo "STEP 12"
 mkdir ~/src
 cd ~/src && git clone -b dev git://github.com/openaps/oref0.git || (cd oref0 && git checkout dev && git pull)
 echo "STEP 13"
 cd ~/src/oref0
 sudo apt-get install -y npm
 sudo npm run global-install
 cd ~/

# run autotune -> *** THIS IS THE STEP THATS NOT WORKING
source venv/bin/activate
pip3 install -r requirements.txt
# python3 main.py # -> the API should be able to call oref0-autotune now
#sudo oref0-autotune --dir=~/myopenaps  --ns-host=https://tig-diab.herokuapp.com --start-date=2021-12-30
