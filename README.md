JumpHigh
===
Predict how high you will jump.

# Dependencies
### macOS
First of all, you need Homebrew.  
Install python3:  
`brew install python3`  
Install dependencies:  
`pip3 install openpyxl numpy scipy sklearn matplotlib`  

### Ubuntu/Debian
Install python3:  
`apt install python3`  
Install dependencies:  
`pip3 install openpyxl numpy scipy sklearn matplotlib`  

### Windows
Install python3 from the official website.  
From <http://www.lfd.uci.edu/~gohlke/pythonlibs/>, download whl files for numpy, scipy, sklearn.  
After that, run the following command for every whl file:  
`pip install [downloaded-whl-file]`  
Next, install other dependencies using PyPI:  
`pip install openpyxl matplotlib`  

# Run
First, change the working direcory to the project directory. Then, put all the test xlsx files to a subdirectory named `testdata`. Finally, launch the script as following and the program should output a prediction.

### macOS and Ubuntu/Debian
`python3 ./src/machine_learning.py`

### Windows
`python .\src\machine_learning.py`
