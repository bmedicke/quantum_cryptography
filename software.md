# environment

* Rasbperry Pi running Raspbian or similar
* Python  ≥3.9 (required for type hinting)
  * [venv](https://docs.python.org/3/library/venv.html) virtual environment
* Jupyter Lab notebook for Web UI

# Raspbian setup

```sh
# check current Python version:

python3 --version

# get Python 3.9 or newer:

sudo apt update
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libssl-dev libffi-dev

wget https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tgz # or newer.
tar -xf Python-*
rm Python-*.tgz

cd Python-*/

# these might take a while.
./configure --enable-optimizations && make -j 5 # ~ number of cores +1.
sudo make altinstall # altinstall leaves the original install alone.

# check if it worked:
python3.9 --version
python3.9 -c 'import ssl;print(ssl.OPENSSL_VERSION)'
```

# getting started with the notebooks

Depending on your OS the `python3.9` binary might be called `python3` or
`python`. Check that you have the right version with the `--version` flag.
Similarly `pip3.9` might be called `pip` or `pip3`, again check with the `--version` flag.

* clone the repo
* switch to `notebooks` folder
* create a virtual environment with `python3.9 -m venv env`
* source the virtual environment with `source env/bin/activate`
  * you can deactivate the venv with `venv`
* install dependencies `pip3.9 install -r requirements.txt`
* start the notebook with `jupyter notebook`

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
