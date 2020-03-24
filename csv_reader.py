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
fileNameImage = 'imagept21.csv'
fileNameText = 'text21.csv'
newFileName = 'Output.csv'


#Open input csv file
myCSVFileImage = open(fileNameImage, 'rb')
myCSVFileText = open(fileNameText, 'rb')
myFileImage = csv.reader(myCSVFileImage)
myFileText = csv.reader(myCSVFileText)


#Create new csv file and make it appendable
#other options: w = overwrite, r = read, a = append, ab = append binary.
csvFileOut = open(newFileName,'w')


outFile = csv.writer(csvFileOut)



#Header for new file
header=['userID', 'SCHEME', '# of Logins', '# of Success', '# of Failure', 'Average Login Time', 'Average Login Success Time', 'Average Login Failure Time']



threshold = datetime.timedelta( 
	days=0,
     seconds=0,
     microseconds=0,
     milliseconds=0,
     minutes=10,
     hours=0,
     weeks=0
 )



def roundToSeconds(delta):
	if(datetime.timedelta(microseconds=delta.microseconds) >= datetime.timedelta(microseconds=500000)):
		return delta - datetime.timedelta(microseconds=delta.microseconds) + datetime.timedelta(seconds=1)
	else:
		return delta - datetime.timedelta(microseconds=delta.microseconds)



def fileToDict(myFile):
	list={}
	number_of_login_success = 0
	number_of_login_failure = 0
	#Loop over csv rows
	for row in myFile:
		split = row.split(",")
		#print(split[0])
		if(list.get(split[1]) == None):
			date_time_obj = datetime.datetime.strptime(split[0], '%Y-%m-%d %H:%M:%S')
			data = [date_time_obj,split[1],split[3],split[4],split[5],split[6]]
			value = []
			value.append(data)
			list[split[1]] = value
		else:
			date_time_obj = datetime.datetime.strptime(split[0], '%Y-%m-%d %H:%M:%S')
			data = [date_time_obj,split[1],split[3],split[4],split[5],split[6]]
			list.get(split[1]).append(data)

	return list;









def algorithm(list):
	 



	for x in list:
		row = []
		number_of_login_success = 0
		number_of_login_failure = 0
		Avg_login_time = datetime.timedelta()
		Avg_login_time_success = datetime.timedelta()
		Avg_login_time_failure = datetime.timedelta()
		divisors = 0


		row.append(x)
		row.append(list.get(x)[0][2])

		for k in range(0,len(list.get(x))):
			if(list.get(x)[k][4] == 'login'):	# login attempt
				if(list.get(x)[k][5] == 'success'): 	# successful attempt
					number_of_login_success = number_of_login_success + 1
					currIndex = k - 1 # back track counter
					# iterate backwards to find a matching 'start' time-stamp for a successful attempt
					while(list.get(x)[currIndex][5] != 'start'):
						currIndex = currIndex - 1
					# list.get(x)[currIndex][0] ---> login attempt starts  |   list.get(x)[k][0] ---> login attempt ends
					if((list.get(x)[k][0] - list.get(x)[currIndex][0]) <  threshold):
						Avg_login_time_success = Avg_login_time_success + (list.get(x)[k][0] - list.get(x)[currIndex][0])	
						allLogins.append((list.get(x)[k][0] - list.get(x)[currIndex][0]))
						successes.append((list.get(x)[k][0] - list.get(x)[currIndex][0]))
				else:
					number_of_login_failure = number_of_login_failure + 1
					currIndex = k - 1 # back track counter
					# iterate backwards to find a matching 'start' time-stamp for a failure attempt
					while(list.get(x)[currIndex][5] != 'start'):
						currIndex = currIndex - 1
					# list.get(x)[currIndex][0] ---> login attempt starts  |   list.get(x)[k][0] ---> login attempt ends
					if((list.get(x)[k][0] - list.get(x)[currIndex][0]) <  threshold):
						Avg_login_time_failure = Avg_login_time_failure + (list.get(x)[k][0] - list.get(x)[currIndex][0])
						allLogins.append((list.get(x)[k][0] - list.get(x)[currIndex][0])) 
						failures.append((list.get(x)[k][0] - list.get(x)[currIndex][0]))
		Avg_login_time = (Avg_login_time_success + Avg_login_time_failure)/(number_of_login_success + number_of_login_failure)
		#print(list.get(x)[1][1])
		#print("number of logins: " + str(number_of_login_success + number_of_login_failure))
		#print("number of success: " + str(number_of_login_success))
		#print("number of failure: " + str(number_of_login_failure))
		#print("Average login time: " + str(roundToSeconds(Avg_login_time)))
		#print("Average success time: " + str(roundToSeconds(Avg_login_time_success/number_of_login_success)))
		#if(number_of_login_failure > 0):
			#print("Average failure time: " + str(roundToSeconds(Avg_login_time_failure/number_of_login_failure)))
		#print("----------------------------------")
		row.append(number_of_login_success + number_of_login_failure)
		row.append(number_of_login_success)
		row.append(number_of_login_failure)
		row.append(roundToSeconds(Avg_login_time))
		row.append(roundToSeconds(Avg_login_time_success/number_of_login_success))
		if(number_of_login_failure > 0):
			row.append(roundToSeconds(Avg_login_time_failure/number_of_login_failure))
		else:
			row.append(0)
		rows.append(row)



		


imageData=fileToDict(myCSVFileImage)
textData=fileToDict(myCSVFileText)


outFile.writerow(header)
numberOfUsersText = 0;
for b in textData:
	numberOfUsersText = numberOfUsersText + 1

allLogins = []
successes = []
failures = []
rows = []
textDataFormatted = algorithm(textData)
allLoginsText = allLogins
successesText = successes
failuresText = failures
textRows = rows
for j in textRows:
	outFile.writerow(j)

# Avg login time of all users -> text
totalLoginTimeAllUsersText = datetime.timedelta()
for q in allLoginsText:
	totalLoginTimeAllUsersText = totalLoginTimeAllUsersText + q
avgLoginTimeAllUsersText = totalLoginTimeAllUsersText / (len(allLoginsText))
print(avgLoginTimeAllUsersText)
# Avg success time of all users -> text
totalSuccessTimeAllUsersText = datetime.timedelta()
for r in successesText:
	totalSuccessTimeAllUsersText = totalSuccessTimeAllUsersText + r
avgSuccessTimeAllUsersText = totalSuccessTimeAllUsersText / (len(successesText))
print(avgSuccessTimeAllUsersText)
# Avg failure time of all users -> text
totalFailureTimeAllUsersText = datetime.timedelta()
for s in failuresText:
	totalFailureTimeAllUsersText = totalFailureTimeAllUsersText + s
avgFailureTimeAllUsersText = totalFailureTimeAllUsersText / (len(failuresText))
print(avgFailureTimeAllUsersText)
print()


outFile.writerow(["Average: ","testtextrandom",len(allLoginsText)/numberOfUsersText, len(successesText)/numberOfUsersText, 
				 len(failuresText)/(numberOfUsersText-8),roundToSeconds(avgLoginTimeAllUsersText),
				 roundToSeconds(avgSuccessTimeAllUsersText),roundToSeconds(avgFailureTimeAllUsersText)])
outFile.writerow([" "," "," "," "," "," "," "," "])


numberOfUsersImage = 0
for c in imageData:
	numberOfUsersImage = numberOfUsersImage + 1

allLogins = []
successes = []
failures = []
rows = []
imageDataFormatted = algorithm(imageData)
allLoginsImage = allLogins
successesImage = successes
failuresImage = failures
imageRows = rows
for j in imageRows:
	outFile.writerow(j)

# Avg login time of all users -> Image
totalLoginTimeAllUsersImage = datetime.timedelta()
for t in allLoginsImage:
	totalLoginTimeAllUsersImage = totalLoginTimeAllUsersImage + t
avgLoginTimeAllUsersImage = totalLoginTimeAllUsersImage / (len(allLoginsImage))
print(avgLoginTimeAllUsersImage)
# Avg success time of all users -> Image
totalSuccessTimeAllUsersImage = datetime.timedelta()
for u in successesImage:
	totalSuccessTimeAllUsersImage = totalSuccessTimeAllUsersImage + u
avgSuccessTimeAllUsersImage = totalSuccessTimeAllUsersImage / (len(successesImage))
print(avgSuccessTimeAllUsersImage)
# Avg failure time of all users -> Image
totalFailureTimeAllUsersImage = datetime.timedelta()
for v in failuresImage:
	totalFailureTimeAllUsersImage = totalFailureTimeAllUsersImage + v
avgFailureTimeAllUsersImage = totalFailureTimeAllUsersImage / (len(failuresImage))
print(avgFailureTimeAllUsersImage)
print()

outFile.writerow(["Average: ","testpasstiles",len(allLoginsImage)/numberOfUsersImage, len(successesImage)/numberOfUsersImage, 
				 len(failuresImage)/(numberOfUsersImage-2),roundToSeconds(avgLoginTimeAllUsersImage),
				 roundToSeconds(avgSuccessTimeAllUsersImage),roundToSeconds(avgFailureTimeAllUsersImage)])
outFile.writerow([" "," "," "," "," "," "," "," "])

outFile.writerow([""])
outFile.writerow([])
outFile.writerow([])


print(len(failuresText)/(numberOfUsersText-8))



#####CLOSE THE DOCUMENTS####
myCSVFileImage.close()
myCSVFileText.close()
csvFileOut.close()

