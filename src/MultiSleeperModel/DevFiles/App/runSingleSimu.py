"""
This script allows running a simulation from a terminal. It requires a .json parameter 
file in argument (relative path from this script's location). Example:
python3 runSingleSimu.py ./ListOfSimulations/myParameters1.json

Parameter files completely define a simulation and should first be generated using the GUI.
"""

import json
import os
import sys

sys.path.insert(0, './DevFiles/App')
import module_run as mod

dir = os.path.dirname(os.path.realpath(__file__))

try:
    fileName = sys.argv[1]
except:
    print("File name not found.")
    sys.exit()    

if not os.path.exists(fileName):
    print("The file " + fileName + ' was not found.')
    sys.exit()

with open(fileName, 'r') as f:
    txt = f.read()
f.close()

try:
    parameters = json.loads(txt)
except:
    print("The parameters dictionnary could not be defined from the file " + fileName + ".")
    sys.exit()

code = mod.RunSimulation(parameters)

if code != 0:
    if isinstance(code, str):
        print(parameters['name'] + " did not run properly. The error message is:\n" + code)
    elif isinstance(code, int):
        print(parameters['name'] + " did not run properly. Check out Code_Aster message files. Exit code: " + str(code))
    else:
        print("Unknown error; exit code: " + str(code))
        
mod.DeletePycFiles(dir)