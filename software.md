# environment

* Rasbperry Pi running Raspbian or similar
* Python  ≥3.9 (required for type hinting)
  * highly recommended: a virtual environment (like [venv](https://docs.python.org/3/library/venv.html))
* Jupyter Lab notebook for Web UI

# Raspbian setup

```sh
# check current Python version:
python3 --version # we need at least 3.9.

# build Python 3.9 or newer from source:
sudo apt update
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libssl-dev libffi-dev libsqlite3-dev

wget https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tgz # or newer.
tar -xf Python-* && cd Python-*/

# these might take a while.
./configure --enable-optimizations && make -j 5 # ~ number of cores +1.
sudo make altinstall # altinstall leaves the original install alone.

# check if it worked:
python3.9 --version
python3.9 -c 'import ssl;print(ssl.OPENSSL_VERSION)'
```

# cloning and starting the notebooks

Depending on your OS the `python3.9` binary might be called `python3` or
`python`. Check that you have the right version with the `--version` flag.
Similarly `pip3.9` might be called `pip` or `pip3`, again check with the `--version` flag.

```sh
# clone the repo:
git clone 'git@github.com:bmedicke/quantum_cryptography.git' # or via https.

# switch to the notebooks folder:
cd quantum_cryptography/notebooks

# create a virtual Python environment:
python3.9 -m venv env

# source the virtual environment.
source env/bin/activate
# you have to repeat this step for each new terminal.
# you can deactivate the venv with: deactivate

# install requirements.
pip3.9 install wheel
pip3.9 install -r requirements.txt

# start the notebook:
jupyter notebook --ip=0.0.0.0 --no-browser
# the first flag binds the programm to all network interfaces so we
# can connect to the raspberry pi via its public IP address.
# the second flag prevents a browser from popping up.

# now visit the displayed URL with the public IP address
# from any browser running on a device in the same network.
```

**While working with an activated virtual environment you should always
be able to simply use `python` and `pip`.**

---

To update the requirements file (after addding new libraries to the project)
run `pip3 freeze > requirements.txt`.

# libraries

* https://github.com/johnwargo/seeed-studio-relay-board
  * library to control the seeed relay hat
  * updated version: https://github.com/johnwargo/seeed-studio-relay-v2
* https://github.com/jupyter/notebook
  * a web-based notebook environment for interactive computing
  * could be used for our user interface
