import os

cmd = "conda env create -f environment.yml"

try:    
    os.system(cmd)
except:
    print("Could not install the specidied environment!")