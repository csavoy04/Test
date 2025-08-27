""" Python random number matrix generator

"""

# Importing required modules
import csv
import random

# Function for checking the file extension given by user
def extCheck(file):
    if len(file)<5:
        file+='.csv'
    elif file[len(file)-4:len(file)]!='.csv' and file[len(file)-4]!='.':
        file+='.csv'
    elif file[len(file)-4]=='.':
        file = file[0:len(file)-4]
        file+='.csv'
    else:
        pass
    return file
    
file = input('Enter name for matrix file: ')
file = extCheck(file)

# Try: Except: statement to obtain matrix size
try:
    x = int(input('Enter matrix X dimension: '))
    y = int(input('Enter matrix Y dimension: '))
except TypeError:
    print('Invalid input, required integer')
    
# Try: Except: statement to write to the .csv file (list is temp number storage)
try:
    # Remember to use newline='' to prevent every other line from being blank
    with open(file, 'x', newline='') as f:
        writer = csv.writer(f)
        
        # Repeats for y value of matrix
        j=0
        while j<y:
            list=[]
            i=0
            # Generating row x numbers
            while i<x:
                list.append(random.randint(0,100))
                i+=1
            writer.writerow(list)
            j+=1
except FileExistsError:
    print('The file name you have chosen is already in use!')
finally:
    print('File succesfully made')