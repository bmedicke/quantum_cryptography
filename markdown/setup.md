# setup instructions

<!-- vim-markdown-toc GFM -->

* [environment](#environment)
* [Raspberry Pis](#raspberry-pis)
  * [Alice, Bob & Eve](#alice-bob--eve)
    * [Python 3](#python-3)
    * [cloning and initial setup](#cloning-and-initial-setup)
    * [starting the notebook](#starting-the-notebook)
  * [Alice](#alice)
    * [Docker & MQTT broker](#docker--mqtt-broker)
* [configuring the code formatter](#configuring-the-code-formatter)
* [used libraries](#used-libraries)

<!-- vim-markdown-toc -->

## environment

* Rasbperry Pis running Raspbian
* Python  ≥3.9 (required for type hinting)
  * highly recommended: a virtual environment (like [venv](https://docs.python.org/3/library/venv.html))
* [JupyterLab](https://jupyter.org/) for running the notebooks
* an MQTT broker running in Docker

## Raspberry Pis

### Alice, Bob & Eve

#### Python 3

```sh
# check current Python version:
python3 --version # we need at least 3.9.

# build a newer Python version from source.
sudo apt update
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libssl-dev libffi-dev libsqlite3-dev

wget https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tgz # or newer.
tar -xf Python-* && cd Python-*/

# these steps might take a while.
./configure --enable-optimizations && make -j 5 # ~ number of cores +1.
sudo make altinstall # altinstall leaves the original install alone.

# check if it worked:
python3.9 --version
python3.9 -c 'import ssl;print(ssl.OPENSSL_VERSION)'
```

#### cloning and initial setup

```sh
# clone the repo:
git clone 'git@github.com:bmedicke/quantum_cryptography.git' # or via https.

# switch to the repo folder:
cd quantum_cryptography

# create a virtual Python environment with the new Python:
python3.9 -m venv env

# activate the virtual environment.
source env/bin/activate
  # while working in an activated virtual environment you can
  # simply use `python` and `pip` and  skip the postfixes.

# install requirements.
pip install wheel
pip install -r requirements.txt

# enable the I2C interface for the relay shield:
sudo raspi-config
  # Interfacing options → I2C → yes.
```

#### starting the notebook

```sh
# activate the virtual environment if its not still active.
source env/bin/activate # you can deactivate the venv with: deactivate
jupyter-lab --ip=0.0.0.0 --no-browser notebooks/ # start JupyterLab.
  # the first flag binds the programm to all network interfaces so we
  # can connect to the raspberry pi via its public IP address.
  # the second flag prevents a browser from popping up.

# now visit the displayed URL with the public IP address
# from any browser running on a device in the same network.
```

All required libraries are installed into the virtual environment.<br>
**You have to activate the virtual environment before starting JupyterLab.**

### Alice

#### Docker & MQTT broker

```sh
# install docker:
curl -fsSL https://get.docker.com | sh

# install docker-compose outside of venv:
sudo pip3 install docker-compose

# start the MQTT broker:
sudo docker-compose up -d

# check if it's running:
sudo docker-compose ps

# to stop it:
sudo docker-compose down
```

## configuring the code formatter

Set the default code formatter to black:

*Settings* → *Advanced Code Formatter* → *Jupyterlab Code Formatter* → *User Preferences*

```json
{
    "preferences": {
        "default_formatter": {
            "python": "black"
        }
    },
    "black": {
         "line_length": 79
    }
}
```

## used libraries

* [jupyterlab_code_formatter](https://github.com/ryantam626/jupyterlab_code_formatter)
  * and [black](https://github.com/psf/black) as a formatter
* [paho-mqtt](https://pypi.org/project/paho-mqtt/)
* [seeed-studio-relay-board](https://github.com/johnwargo/seeed-studio-relay-board)
  * library to control the seeed relay hat
  * updated version: [seeed-studio-relay-v2](https://github.com/johnwargo/seeed-studio-relay-v2)
    * supports stacked hats 🎩
  * [smbus](https://pypi.org/project/smbus/)

Installation without `requirements.txt`:

```sh
pip install paho-mqtt jupyterlab black jupyterlab-code-formatter
```
