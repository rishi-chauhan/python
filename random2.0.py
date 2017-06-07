################################################################################
#### Name: Rishi Raj Singh Chauhan                                          ####
#### Registration Number: 14B00025                                          ####
#### The following program takes a path of the directory from the user.     ####
#### Then scans the whole directory ONLY for ".txt" files with name         ####
#### containing "company" and then calculates the total sale by adding the  ####
#### sales value written after each company's name                          ####
################################################################################

import datetime
import glob
import os

# noting the start time
start_time = datetime.datetime.now()

# list to store all filenames in the directory
filenames = []

path = input("Enter the path(in double qoutes): ")

# opening directory
os.chdir(path)

# mamking a list of all the files
for f in glob.glob("company*.txt"):
    filenames.append(f)

# company dictionary
com = {}

for i in filenames:
    f = open(i, "r")
    for j in f.readlines():
        for k in range(len(j.split())):
            if k <=1:
                if com.has_key(j.split()[0]):
                    com[j.split()[0]] += int(j.split()[1])
                else:
                    com[j.split()[0]] = 0

# printing company and it's sales value
print "\n{0:10}{1:10}".format("Company", "Sales")
for company in com:
    print "{0:10}{1:5d}".format(company, com[company])

# noting end time
end_time = datetime.datetime.now()

# print time elapsed to run program
print "\nTotal time elapsed for the program to run: ", end_time - start_time, "seconds"
