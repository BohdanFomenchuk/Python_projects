#!/usr/bin/env python3


import re
import operator
import csv


error = {}
per_user = {}

with open('syslog.log', 'r') as file:
    Lines = file.readlines()
    for line in Lines:
        match = re.search(r'\((\w+)\)', line)
        if match:
            username = match.group(1)

        if re.search(r'INFO', line):
            if username in per_user:

                per_user[username]['INFO'] += 1

            else:
                per_user[username] = {'INFO': 1, 'ERROR': 0}

            print(per_user[username])

        elif re.search(r'ERROR', line):
            error_name = re.search(r'ERROR ([\w ]*) ', line)[1]
            if error_name in error:
                error[error_name] += 1
                if username in per_user:
                    per_user[username]['ERROR'] += 1
                else:
                    per_user[username] = {'INFO': 0, 'ERROR': 1}


                print(error)
            else:
                error[error_name] = 1
                if username in per_user:
                    per_user[username]['ERROR'] += 1
                else:
                    per_user[username] = {'INFO': 0, 'ERROR': 1}


sort_error = sorted(error.items(), key=operator.itemgetter(0), reverse=True)

sort_per_user = sorted(per_user.items())

sort_error.insert(0, ("Error", "Count"))
sort_per_user.insert(0, ("Username", "INFO", "ERROR"))
print(sort_error)
print(sort_per_user)

with open("error_message.csv", 'w') as error_csv:
    writer = csv.writer(error_csv)
    writer.writerows(sort_error)
error_csv.close()

with open("user_statistics.csv", 'w') as user_csv:
    writer = csv.writer(user_csv)
    writer.writerows(sort_per_user)
error_csv.close()
