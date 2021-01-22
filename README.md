# A*-Mazesolver
This is my attempt at solving mazes with an A*-Algorithm using a combination of c++ and python.



## Building
### Optional: Setup virtual environment
In the root directory of this project run ```python -m venv venv-name``` where ```venv-name``` can be any name you like.  
Activate it using ```venv-name/scripts/activate```.  
Read more about it [here](https://docs.python.org/3/tutorial/venv.html).

### Required
For this step a compatible c++-compiler is likely necessary, since the c++-binary extension has to interact with the python interpreter. Linux users should have one by default while windows users may have to install one. But first proceed as follows.
In the root directory run ```python make_dist.py```. This will build a wheel and a sdist.
If you did not have the correct compiler installed at this stage the generated error message will tell you which compiler you need and where you can get one.
