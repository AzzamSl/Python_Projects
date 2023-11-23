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
print(files[1:33])