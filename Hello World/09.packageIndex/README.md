- To install packages use `pip3 install packageName`
- To upgrade packages use `pip3 install --upgrade packageName`
- To list packages currently installed on your maching `pip3 list`
- To install a specific version package `pip3 install packageName==versionNumber`
- To install a latest compatible version `pip3 install packageName==major.minor.*` or `pip install packageName~=major.minor.0` or `pip install packageName==major.*`
- To uninstall a package globally `pip3 uninstall packageName`


- To create virtual environment `python3 -m venv env` where env is the directory name 
- Once the environment is created, to activate it, run `source env/bin/activate`
- Now install the required packages in the specific activated environment
- To deactivate the environment once it is done, run `deactivate`

- To combine pip3 and venv, we can use pipenv
- To install pipenv, run `pip3 install pipenv`
- To install a package using pipenv, run `pipenv install packageName`
- The above step creates 2 files - Pipfile and Pipfile.lockpi
- To activate the pipenv environment, run `pipenv shell`. This will activate the shell in which we can run the commands.
- To deactivate the pipenv environment, run `exit`