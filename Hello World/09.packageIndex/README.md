** Package installation **

- To install packages use `pip3 install packageName`
- To upgrade packages use `pip3 install --upgrade packageName`
- To list packages currently installed on your maching `pip3 list`
- To install a specific version package `pip3 install packageName==versionNumber`
- To install a latest compatible version `pip3 install packageName==major.minor.*` or `pip install packageName~=major.minor.0` or `pip install packageName==major.*`
- To uninstall a package globally `pip3 uninstall packageName`

** Virtual Environment **

- To create virtual environment `python3 -m venv env` where env is the directory name
- Once the environment is created, to activate it, run `source env/bin/activate`
- Now install the required packages in the specific activated environment
- To deactivate the environment once it is done, run `deactivate`

** Virtual Environment (Pipenv - new projects) **

- To combine pip3 and venv, we can use pipenv
- To install pipenv, run `pip3 install pipenv`
- To install a package using pipenv, run `pipenv install packageName`
  - The above step creates 2 files - Pipfile and Pipfile.lock, if they don't exist already
- To activate the pipenv environment, run `pipenv shell`. This will activate the shell in which we can run the commands.
- To deactivate the pipenv environment, run `exit`

** Virual Environment (Pipenv - from pipfiles) **

- To check if the pipenv virtual environment is created for this project, hit `pipenv --venv`. If virtual environment is not created for this project, you'll get an error.
- To create the virtual environment using the Pipfile, hit `pipenv install`. Once create, it can be verified using `pipenv --venv`.
- To craete the virtual environment using the Pipfile.lock, hit `pipenv install --ignore-pipfile`. Once create, it can be verified using `pipenv --venv`.

** Pipenv commands **

- To see list of all installed dependencies, `pipenv graph`
- To update the outdated packages, `pipenv update --outdated`
- To update a specific package, `pipenv update packageName`
