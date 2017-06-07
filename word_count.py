################################################################################
#### Name: Rishi Raj Singh Chauhan                                          ####
#### Registration Number: 14B00025                                          ####
#### The following program takes a path of the directory from the user.     ####
#### Then scans the whole directory ONLY for ".txt" files and then displays ####
#### words with their frequency in all the files scanned                    ####
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
for f in glob.glob("*.txt"):
    filenames.append(f)

# dictionary to store words and their count
words = {}

for i in filenames:
    f = open(i, "r")
    for j in f.readlines():
        for k in j.split():
            if words.has_key(k):
                words[k] += 1
            else:
                words[k] = 1

print "\n{0:15}{1:5}".format("WORDS", "FREQUENCY")
for i in words:
    print "{0:15}{1:5}".format(i, words[i])

# noting end time
end_time = datetime.datetime.now()

# print time elapsed to run program
print "\nTotal time elapsed for the program to run: ", end_time - start_time, "seconds"
