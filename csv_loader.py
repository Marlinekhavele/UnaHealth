import sys
import csv
from pathlib import Path

path = Path(sys.argv[1]) # contains sample data
files_list =  list(path.iterdir()) # list  all files in the directory
 

with open(file_path, "+r") as file:


