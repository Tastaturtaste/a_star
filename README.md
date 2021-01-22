# A* Python Extension Module
A c++ extension module for python, implementing a a*-algorithm, to learn how to make c++ python extensions and package them.


## Building
### Optional: Setup virtual environment
In the root directory of this project run ```python -m venv venv-name``` where ```venv-name``` can be any name you like.  
Activate it using ```venv-name/scripts/activate```.  
Read more about it [here](https://docs.python.org/3/tutorial/venv.html).

### Required
In the root directory run ```python make_dist.py```. This will build a wheel and a sdist and store them in ./dist/.
If you did not have the correct compiler installed at this stage the generated error message will tell you which compiler you need and where you can get one.

## Usage
Installing this module requires either a c++-compiler or a platform compatible with the provided wheel distribution.  
Installation with pip should be possible after downloading the ```./dist``` subdirectory with  
```pip install --find-links=relative/path/to/downloaded/dist a_star```.  
A example usage of this module can be seen in the project [mazesolve](https://github.com/Tastaturtaste/mazesolver). 