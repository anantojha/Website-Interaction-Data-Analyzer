import csv
import datetime
import numpy as np 
import matplotlib.pyplot as plt

#from itertools import zip_longest
##### Interaction CSV Data Reader #####

#INSTRUCTIONS:
#Design and implement a software program to process the log data from the two schemes,
#producing a single file in CSV format containing results ready for statistical analysis. For
#this processing, you may use any programming language or environment. Think carefully
#about how to process the log files. In particular, you may wish to re-order the data so that
#you can process the information by user and by site. The new file must contain at least
#the following information for each user of each scheme:


#The userID.
# The password scheme (Text21 or Image21).
# The number of logins, successful logins, and failed logins.
# The time taken to enter a password, recorded separately for successful logins, and
#for failed logins.

#Documentation for your log data processing software, including high-level
#explanation and pseudo-code for your approach, and the documented source code. Also
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


#Create new output csv file
#other options: w = overwrite, r = read, a = append, ab = append binary.
csvFileOut = open(newFileName,'w')
outFile = csv.writer(csvFileOut)


#Header for new file
header=['userID', 'SCHEME', '# of Logins', '# of Success', '# of Failure', 'Average Login Time', 'Average Login Success Time', 'Average Login Failure Time']


# any login times which exceeds this threshold are an out-lier and will not be taken into calculations 
threshold = datetime.timedelta( 
	days=0,
     seconds=0,
     microseconds=0,
     milliseconds=0,
     minutes=10,
     hours=0,
     weeks=0
 )

NullTime = datetime.timedelta( 
	days=0,
     seconds=0,
     microseconds=0,
     milliseconds=0,
     minutes=10,
     hours=0,
     weeks=0
 )


# round time objects to seconds 
def roundToSeconds(delta):
	if(datetime.timedelta(microseconds=delta.microseconds) >= datetime.timedelta(microseconds=500000)):
		return delta - datetime.timedelta(microseconds=delta.microseconds) + datetime.timedelta(seconds=1)
	else:
		return delta - datetime.timedelta(microseconds=delta.microseconds)


# scrape data from file and store into a dictionary 
def fileToDict(myFile):
	list={}
	number_of_login_success = 0
	number_of_login_failure = 0

	#Loop over csv file rows
	for row in myFile:
		split = row.split(",")
		
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

	#  loop through users in a dictionary 
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
				else: # failed attempt
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
		numberOfLoginsPerUser.append(number_of_login_success + number_of_login_failure)
		numberOfSuccessesPerUser.append(number_of_login_success)
		numberOfFailuresPerUser.append(number_of_login_failure)
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



# get data from file and store into a dictionary, Key = userID  ---> Value = list containing all of that user's logs
imageData=fileToDict(myCSVFileImage)
textData=fileToDict(myCSVFileText)

# write the header to file 
outFile.writerow(header)

#numbers of users in Text Scheme
numberOfUsersText = 0;
for b in textData:
	numberOfUsersText = numberOfUsersText + 1

# calculate statistics for text scheme 
allLogins = []
successes = []
failures = []
rows = []
numberOfLoginsPerUser = []
numberOfSuccessesPerUser = []
numberOfFailuresPerUser = []
textDataFormatted = algorithm(textData)
allLoginsText = allLogins
successesText = successes
failuresText = failures
numberOfLoginsText = numberOfLoginsPerUser
numberOfSuccessesText = numberOfSuccessesPerUser
numberOfFailuresText = numberOfFailuresPerUser
textRows = rows
for j in textRows:
	outFile.writerow(j)

# Avg login time of all users -> text
totalLoginTimeAllUsersText = datetime.timedelta()
for q in allLoginsText:
	totalLoginTimeAllUsersText = totalLoginTimeAllUsersText + q
avgLoginTimeAllUsersText = totalLoginTimeAllUsersText / (len(allLoginsText))

# Avg success time of all users -> text
totalSuccessTimeAllUsersText = datetime.timedelta()
for r in successesText:
	totalSuccessTimeAllUsersText = totalSuccessTimeAllUsersText + r
avgSuccessTimeAllUsersText = totalSuccessTimeAllUsersText / (len(successesText))

# Avg failure time of all users -> text
totalFailureTimeAllUsersText = datetime.timedelta()
for s in failuresText:
	totalFailureTimeAllUsersText = totalFailureTimeAllUsersText + s
avgFailureTimeAllUsersText = totalFailureTimeAllUsersText / (len(failuresText))


allLoginsText.sort()
allLoginsTextSeconds = []
for o in allLoginsText:
	allLoginsTextSeconds.append(o.total_seconds())
successesText.sort()
successesTextSeconds = []
for i in successesText:
	successesTextSeconds.append(i.total_seconds())
failuresText.sort()
failuresTextSeconds = []
for v in failuresText:
	failuresTextSeconds.append(v.total_seconds())
numberOfLoginsText.sort()
numberOfSuccessesText.sort()
numberOfFailuresText.sort()


countZeros = 0
for f in numberOfFailuresText:
	if(f == 0):
		countZeros = 1 + countZeros
del numberOfFailuresText[:countZeros]


#numbers of users in Image Scheme
numberOfUsersImage = 0
for c in imageData:
	numberOfUsersImage = numberOfUsersImage + 1

# calculate statistics for image scheme 
allLogins = []
successes = []
failures = []
rows = []
numberOfLoginsPerUser = []
numberOfSuccessesPerUser = []
numberOfFailuresPerUser = []
imageDataFormatted = algorithm(imageData)
allLoginsImage = allLogins
successesImage = successes
failuresImage = failures
numberOfLoginsImage = numberOfLoginsPerUser
numberOfSuccessesImage = numberOfSuccessesPerUser
numberOfFailuresImage = numberOfFailuresPerUser
imageRows = rows
for j in imageRows:
	outFile.writerow(j)

# Avg login time of all users -> Image
totalLoginTimeAllUsersImage = datetime.timedelta()
for t in allLoginsImage:
	totalLoginTimeAllUsersImage = totalLoginTimeAllUsersImage + t
avgLoginTimeAllUsersImage = totalLoginTimeAllUsersImage / (len(allLoginsImage))

# Avg success time of all users -> Image
totalSuccessTimeAllUsersImage = datetime.timedelta()
for u in successesImage:
	totalSuccessTimeAllUsersImage = totalSuccessTimeAllUsersImage + u
avgSuccessTimeAllUsersImage = totalSuccessTimeAllUsersImage / (len(successesImage))

# Avg failure time of all users -> Image
totalFailureTimeAllUsersImage = datetime.timedelta()
for v in failuresImage:
	totalFailureTimeAllUsersImage = totalFailureTimeAllUsersImage + v
avgFailureTimeAllUsersImage = totalFailureTimeAllUsersImage / (len(failuresImage))

allLoginsImage.sort()
allLoginsImageSeconds = []
for n in allLoginsImage:
	allLoginsImageSeconds.append(n.total_seconds())
successesImage.sort()
successesImageSeconds = []
for u in successesImage:
	successesImageSeconds.append(u.total_seconds())
failuresImage.sort()
failuresImageSeconds = []
for l in failuresImage:
	failuresImageSeconds.append(l.total_seconds())
numberOfLoginsImage.sort()
numberOfSuccessesImage.sort()
numberOfFailuresImage.sort()
# write 'average' row
outFile.writerow([" "," "," "," "," "," "," "," "])
outFile.writerow([" "," "," "," "," "," "," "," "])
outFile.writerow(["All Users: "," "," "," "," "," "," "," "])
outFile.writerow([" ||||| "," "," "," "," ","All logins", "All successes", "All Failures"])

outFile.writerow(["Median: ","testtextrandom", numberOfLoginsText[len(numberOfLoginsText)/2],
				 numberOfSuccessesText[len(numberOfSuccessesText)/2], numberOfFailuresText[len(numberOfFailuresText)/2], 
				 allLoginsText[(len(allLoginsText)/2)], successesText[len(successesText)/2], failuresText[len(failuresText)/2]])
outFile.writerow(["Median: ","testpasstiles", numberOfLoginsImage[len(numberOfLoginsImage)/2] ,
				 numberOfSuccessesImage[len(numberOfSuccessesImage)/2], numberOfFailuresImage[len(numberOfFailuresImage)/2], 
				 allLoginsImage[(len(allLoginsImage)/2)], successesImage[len(successesImage)/2], failuresImage[len(failuresImage)/2]])
outFile.writerow([" ||||| "])
outFile.writerow(["Mean: ","testtextrandom",(len(allLoginsText) + numberOfUsersText // 2) // numberOfUsersText, 
				 (len(successesText) + numberOfUsersText // 2) // numberOfUsersText, (len(failuresText) + (numberOfUsersText) // 2) // (numberOfUsersText), 
				 roundToSeconds(avgLoginTimeAllUsersText), roundToSeconds(avgSuccessTimeAllUsersText), roundToSeconds(avgFailureTimeAllUsersText)])
outFile.writerow(["Mean: ","testpasstiles",(len(allLoginsImage) + numberOfUsersImage // 2) // numberOfUsersImage, 
				 (len(successesImage) + numberOfUsersImage // 2) // numberOfUsersImage, (len(failuresImage) + (numberOfUsersImage) // 2) // (numberOfUsersImage),
				 roundToSeconds(avgLoginTimeAllUsersImage), roundToSeconds(avgSuccessTimeAllUsersImage),roundToSeconds(avgFailureTimeAllUsersImage)])
outFile.writerow([" ||||| "])
outFile.writerow(["SD: ","testtextrandom", round(np.std(numberOfLoginsText),2), round(np.std(numberOfSuccessesText),2), round(np.std(numberOfFailuresText),2), 
				 roundToSeconds(datetime.timedelta( days=0,
													seconds=round(np.std(allLoginsTextSeconds),2),
													microseconds=0,
													milliseconds=0,
													minutes=0,
													hours=0,
													weeks=0)),
				 roundToSeconds(datetime.timedelta( days=0,
												    seconds=round(np.std(successesTextSeconds),2),
												    microseconds=0,
												    milliseconds=0,
												    minutes=0,
												    hours=0,
												    weeks=0)),
				 roundToSeconds(datetime.timedelta( days=0,
												   seconds=round(np.std(failuresTextSeconds),2),
												    microseconds=0,
												    milliseconds=0,
												    minutes=0,
												    hours=0,
												    weeks=0))])																																											 
outFile.writerow(["SD: ","testpasstiles", round(np.std(numberOfLoginsImage),2), round(np.std(numberOfSuccessesImage),2), round(np.std(numberOfFailuresImage),2), 
				 roundToSeconds(datetime.timedelta( days=0,
												    seconds=round(np.std(allLoginsImageSeconds),2),
												    microseconds=0,
												    milliseconds=0,
												    minutes=0,
												    hours=0,
												    weeks=0)),
				 roundToSeconds(datetime.timedelta( days=0,
												    seconds=round(np.std(successesImageSeconds),2),
												    microseconds=0,
												    milliseconds=0,
												    minutes=0,
												    hours=0,
											     	weeks=0)), 
				roundToSeconds(datetime.timedelta(  days=0,
												    seconds=round(np.std(failuresImageSeconds),2),
												    microseconds=0,
												    milliseconds=0,
												    minutes=0,
												    hours=0,
											        weeks=0))])
outFile.writerow([" "," "," "," "," "," "," "," "])
outFile.writerow([" "," "," "," "," "," "," "," "])
outFile.writerow([" "," "," "," "," "," "," "," "])
outFile.writerow([" ", " " , " ", " ", "HISTOGRAM &", " ", " ", " "])
outFile.writerow([" ", " " , " ", " ", "BOXPLOT DATA", " ", " ", " "])
outFile.writerow([" ","testtextrandom","testtextrandom","testtextrandom","  ","testpasstiles","testpasstiles","testpasstiles"])
outFile.writerow([" ","All Login Times (s)","All Success Times (s)","All Failure Times (s)"," ","All Login Times (s)","All Success Times (s)","All Failure Times (s)"])

maxLength = max(len(allLoginsTextSeconds),len(successesTextSeconds),len(failuresTextSeconds),len(allLoginsImageSeconds),len(successesImageSeconds),len(failuresImageSeconds))
for a in range(0,maxLength):
	row = [" "]
	if(a < len(allLoginsTextSeconds)):
		row.append(round(allLoginsTextSeconds[a]))
	else:
		row.append(" ")
	if(a < len(successesTextSeconds)):
		row.append(round(successesTextSeconds[a]))
	else:
		row.append(" ")
	if(a < len(failuresTextSeconds)):
		row.append(round(failuresTextSeconds[a]))
	else:	
		row.append(" ")
	row.append(" ")
	if(a < len(allLoginsImageSeconds)):
		row.append(round(allLoginsImageSeconds[a]))
	else:
		row.append(" ")
	if(a < len(successesImageSeconds)):
		row.append(round(successesImageSeconds[a]))
	else:
		row.append(" ")
	if(a < len(failuresImageSeconds)):
		row.append(round(failuresImageSeconds[a]))
	else:	
		row.append(" ")
	outFile.writerow(row)



print(" ")
print("Output.csv file has been created in Project Directory!")
print(" ")

plt.style.use('_classic_test')
plt.hist(allLoginsTextSeconds, bins=[0, 5, 10, 15, 20, 25, 30],alpha=0.5)
plt.gca().set(title='Histogram: All Login Times Text Scheme', ylabel='Frequency', xlabel='Seconds');
plt.savefig("Graphs/TextHistogramAllLogins.png")

plt.clf()

plt.style.use('_classic_test')
plt.hist(successesTextSeconds, bins=[0, 5, 10, 15, 20, 25, 30],alpha=0.5)
plt.gca().set(title='Histogram: All Success Times Text Scheme', ylabel='Frequency', xlabel='Seconds');
plt.savefig("Graphs/TextHistogramSuccesses.png")

plt.clf()

plt.style.use('_classic_test')
plt.hist(failuresTextSeconds, bins=[0, 5, 10, 15, 20, 25, 30],alpha=0.5)
plt.gca().set(title='Histogram: All Failure Times Text Scheme', ylabel='Frequency', xlabel='Seconds');
plt.savefig("Graphs/TextHistogramFailures.png")


plt.clf()

plt.style.use('_classic_test')
plt.hist(allLoginsImageSeconds, bins=[0, 5, 10, 15, 20, 25, 30, 35, 40],alpha=1)
plt.gca().set(title='Histogram: All Login Times Image Scheme', ylabel='Frequency', xlabel='Seconds');
plt.savefig("Graphs/ImageHistogramAllLogins.png")

plt.clf()

plt.style.use('_classic_test')
plt.hist(successesImageSeconds, bins=[0, 5, 10, 15, 20, 25, 30, 35, 40],alpha=1)
plt.gca().set(title='Histogram: All Success Times Image Scheme', ylabel='Frequency', xlabel='Seconds');
plt.savefig("Graphs/ImageHistogramSuccesses.png")

plt.clf()

plt.style.use('_classic_test')
plt.hist(failuresImageSeconds, bins=[0, 5, 10, 15, 20, 25, 30, 35],alpha=1)
plt.gca().set(title='Histogram: All Failure Times Image Scheme', ylabel='Frequency', xlabel='Seconds');
plt.savefig("Graphs/ImageHistogramFailures.png")


print(" ")
print("Histograms have been created in /Graphs !")
print(" ")

print(" ")
print("Boxplots have been created in /Graphs !")
print(" ")

#####CLOSE THE DOCUMENTS####
myCSVFileImage.close()
myCSVFileText.close()
csvFileOut.close()

