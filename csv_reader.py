import csv
import datetime

##### Interaction CSV Data Reader #####

#INSTRUCTIONS:
#Design and implement a software program to process the log data from the two schemes,
#producing a single file in CSV format containing results ready for statistical analysis. For
#this processing, you may use any programming language or environment. Think carefully
#about how to process the log files. In particular, you may wish to re-order the data so that
#you can process the information by user and by site. The new file must contain at least
#the following information for each user of each scheme:


#The userid.
# The password scheme (Text21 or Image21).
# The number of logins, successful logins, and failed logins.
# The time taken to enter a password, recorded separately for successful logins, and
#for failed logins.

#Documentation for your log data processing software, including high-level
#explanation and pseudocode for your approach, and the documented source code. Also
#provide the resulting data in CSV format




#DOCUMENTS to read and write
fileName ='text21.csv'
newFileName = 'text21Output.csv'

#Open input csv file
myCSVFile = open(fileName, 'rb')
myFile = csv.reader(myCSVFile)

inFile =csv.reader(myCSVFile)

#Create new csv file and make it appendable
#other options: w = overwrite, r = read, a = append, ab = append binary.
csvFile = open(newFileName,'w')

outFile =csv.writer(csvFile)

#Header for new file
header=['userID', 'SCHEME', '# of Logins', '# of Success', '# of Failure', 'Average Time', 'Average Success Time', 'Average Fail Time']

#write header to new file
outFile.writerow(header)


##### LOOP OVER DOCUMENT ####

#Alternative way to skip first line--pt1
#firstLine= True



list={}
number_of_login_success = 0
number_of_login_failure = 0
#Loop over csv rows
for row in myFile:
	if(list.get(row[1]) == None):
		date_time_obj = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
		data = [date_time_obj,row[1],row[3],row[4],row[5],row[6]]
		value = []
		value.append(data)
		list[row[1]] = value
	else:
		date_time_obj = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
		data = [date_time_obj,row[1],row[3],row[4],row[5],row[6]]
		list.get(row[1]).append(data)
		print(date_time_obj)




for x in list:
	outRow = []
	number_of_login_success = 0
	number_of_login_failure = 0
	outRow.append(list.get(x)[1][1])
	outRow.append(list.get(x)[1][2])
	for k in list.get(x):
		if(k[4] == 'login'):
			if(k[5] == 'success'):
				number_of_login_success = number_of_login_success + 1
				#while():

			else:
				number_of_login_failure = number_of_login_failure + 1
				#while():

	outRow.append(number_of_login_success + number_of_login_failure)
	outRow.append(number_of_login_success)
	outRow.append(number_of_login_failure)
	outRow.append(0)
	outRow.append(0)
	outRow.append(0)
	outFile.writerow(outRow)





#####CLOSE THE DOCUMENTS####

myCSVFile.close()
#csvFile.close()
