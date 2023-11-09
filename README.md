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
Help in code automation

````
install:
    pip install -r requirements.txt

in command line 
    make install
````
