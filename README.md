# ml

create venv
````
    conda create --name venv python=3.9
    conda activate venv
    conda env list
    conda deactivate venv
````

### create license file
from https://opensource.org/license/mit/

### requirements.txt

````
numpy
scipy
gradeio
sphinx
````

in command line 
````
    pip install -r requiremnts.txt
````

### Makefile
Help in code automation <br>
if make command not work 
install cmake
````
install:
    pip install -r requirements.txt

in command line 
    make install
````

### README.md

````
    A short description
    ## description
        comprehensive description
    ## Installation

    ## Contributers

    ## License

````

## Documentation
comment in code like below
````
def hello():
    """
    This function print a hello message from file 2

    Args:
    No arguments

    Returns:
    Returns void
    """
    print("Hello from file 2")

````

**install package**
````
    pip install sphinx
    pip install sphinx-rtd-theme
````

**In docs folder**
````
    sphinx-quickstart
````
