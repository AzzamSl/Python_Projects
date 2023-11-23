<<<<<<< HEAD
import sys
def load(file):
    try:
        with open(file) as in_file:
            txt = in_file.read().strip().split('\n')
            txt = [x.lower() for x in txt]
            return txt
    except IOError as e:
        print(f"{e}Could not open the file {file}")
        sys.exit(1)
    
files = load("2of4brif.txt")
=======
import sys
def load(file):
    try:
        with open(file) as in_file:
            txt = in_file.read().strip().split('\n')
            txt = [x.lower() for x in txt]
            return txt
    except IOError as e:
        print(f"{e}Could not open the file {file}")
        sys.exit(1)
    
files = load("2of4brif.txt")
>>>>>>> c083aa8ab0ba4b8d208fc48210652776074dfe5d
print(files[1:33])