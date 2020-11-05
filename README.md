# Distorted-Integers
Software to aid in the exploration of certain discrete mathematical structures, so-called "distorted integers".

### Execution
It should suffice to call the following on a lab machine if tutors’ permissions are equally restrictive:

cd
/usr/bin/python3 -m venv venv_cs2006

source ~/venv_cs2006/bin/activate

pip install coverage

cd <project_code_directory>

coverage run -m unittest discover

coverage report

coverage html

The last two points are only necessary to check the coverage – the third last command will run the
tests. Once finished with the virtual environment, call:

deactivate

to deactivate it.
If a virtual environment is not required to install packages, then simply ignore the first three
commands (i.e. start at “pip install coverage”).
