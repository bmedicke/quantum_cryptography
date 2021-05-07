# environment

* Python 3.9.5
* [venv](https://docs.python.org/3/library/venv.html) virtual environment
* Jupyter Lab notebook for Web UI

# getting started with the playground

* clone the repo
* switch to playground folder
* create a virtual environment with `python3 -m venv env`
* source the virtual environment with `source env/bin/activate`
  * you can deactivate the venv with `venv`
* install dependencies `pip3 install -r requirements.txt`
* to update the requirements file run `pip3 freeze > requirements.txt`

# libraries

* https://github.com/johnwargo/seeed-studio-relay-board
  * library to control the seeed relay hat
* https://github.com/jupyter/notebook
  * a web-based notebook environment for interactive computing
  * could be used for our user interface
