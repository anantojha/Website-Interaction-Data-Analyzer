import sys
import csv
import datetime
import numpy as np 
import matplotlib.pyplot as plt

#----------------------------------------------------------------------------------------------------------
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
#----------------------------------------------------------------------------------------------------------



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

# function used to remove outliers from a list of data
def removeOutliers(list, value):
	new = []
	for x in list:
		if(x <= value):
			new.append(x)
	return new

# get average time from a list of times 
# -- add all time values in listOfTimes then divide by its length
def getAverageTimes(listOfTimes):
	if(len(listOfTimes) == 0):
		return datetime.timedelta(0);
	totalLoginTimeAllUsers = datetime.timedelta()
	for q in listOfTimes:
		totalLoginTimeAllUsers = totalLoginTimeAllUsers + q
	return totalLoginTimeAllUsers / (len(listOfTimes))


# convert a list of datetime objects into integers (seconds)
def getInSeconds(logins, seconds):
	for o in logins:
		seconds.append(o.total_seconds())


# count numb of users in a scheme
def numberOfUsers(data):
	count = 0
	for b in data:
		count = count + 1
	return count


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


# Time-stamp matching algorithm 
# capable of backtracking while looping through log data 
def algorithm(list, rows, allLogins, successes, failures, numberOfLoginsPerUser, numberOfSuccessesPerUser, numberOfFailuresPerUser):
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
		Avg_login_time = datetime.timedelta(0)
		if((number_of_login_success + number_of_login_failure) > 0):
			Avg_login_time = (Avg_login_time_success + Avg_login_time_failure)/(number_of_login_success + number_of_login_failure)
		
		numberOfLoginsPerUser.append(number_of_login_success + number_of_login_failure)
		numberOfSuccessesPerUser.append(number_of_login_success)
		numberOfFailuresPerUser.append(number_of_login_failure)
		row.append(number_of_login_success + number_of_login_failure)
		row.append(number_of_login_success)
		row.append(number_of_login_failure)
		row.append(roundToSeconds(Avg_login_time))
		if(number_of_login_success > 0):
			row.append(roundToSeconds(Avg_login_time_success/number_of_login_success))
		else:
			row.append(0)
		if(number_of_login_failure > 0):
			row.append(roundToSeconds(Avg_login_time_failure/number_of_login_failure))
		else:
			row.append(0)
		rows.append(row)
		# print("User: " + list.get(x)[1][1])
		# print("number of logins: " + str(number_of_login_success + number_of_login_failure))
		# print("number of success: " + str(number_of_login_success))
		# print("number of failure: " + str(number_of_login_failure))
		# print("Average login time: " + str(roundToSeconds(Avg_login_time)))
		# print("Average success time: " + str(roundToSeconds(Avg_login_time_success/number_of_login_success)))
		# if(number_of_login_failure > 0):
		# 	print("Average failure time: " + str(roundToSeconds(Avg_login_time_failure/number_of_login_failure)))
		# print("----------------------------------")


# function which plots a histogram and then saves it into a PNG image (for part A)
def makeHistogram(logins, bins_array, alpha_val, title_str, y, x, name, style, colour):
	plt.style.use(style)
	plt.hist(logins, color=colour,bins=bins_array, alpha=alpha_val)
	plt.gca().set(title=title_str, ylabel=y, xlabel=x)
	plt.savefig(name)
	plt.clf()

# function which plots a histogram and then saves it into a PNG image (for part B)
def makeHistogram2(logins, bins_array, alpha_val, title_str, y, x, name, style, colour):
	plt.style.use(style)
	plt.grid(color='#ADAFAD', linewidth=0.5, linestyle=':')
	plt.hist(logins, color=colour,bins=bins_array, alpha=alpha_val)
	plt.gca().set(title=title_str, ylabel=y, xlabel=x)
	plt.savefig(name)
	plt.clf()

# run program to do work for part A
def doPartA():
	fileNameImage = 'imagept21.csv'
	fileNameText = 'text21.csv'
	newFileName = 'Output_Part_A.csv'
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

	# get data from file and store into a dictionary, Key = userID  ---> Value = list containing all of that user's logs
	imageData=fileToDict(myCSVFileImage)
	textData=fileToDict(myCSVFileText)

	# write the header to file 
	outFile.writerow(header)
	textRows = []
	imageRows = []

	#numbers of users in each Scheme
	numberOfUsersText = numberOfUsers(textData);
	numberOfUsersImage = numberOfUsers(imageData)

	# calculate statistics for text scheme 
	allLoginsText = []
	successesText = []
	failuresText = []
	numberOfLoginsText = []
	numberOfSuccessesText = []
	numberOfFailuresText = []
	textDataFormatted = algorithm(textData, textRows, allLoginsText, successesText, failuresText, numberOfLoginsText, numberOfSuccessesText, numberOfFailuresText)


	allLoginsImage = []
	successesImage = []
	failuresImage = []
	numberOfLoginsImage = []
	numberOfSuccessesImage = []
	numberOfFailuresImage = []
	textDataFormatted = algorithm(imageData, imageRows, allLoginsImage, successesImage, failuresImage, numberOfLoginsImage, numberOfSuccessesImage, numberOfFailuresImage)


	for j in textRows:
		outFile.writerow(j)

	for k in imageRows:
		outFile.writerow(k)

	# Avg login time of all users 
	avgLoginTimeAllUsersText = getAverageTimes(allLoginsText)
	avgLoginTimeAllUsersImage = getAverageTimes(allLoginsImage)
	# Avg success time of all users 
	avgSuccessTimeAllUsersText = getAverageTimes(successesText)
	avgSuccessTimeAllUsersImage = getAverageTimes(successesImage)
	# Avg failure time of all users 
	avgFailureTimeAllUsersText = getAverageTimes(failuresText)
	avgFailureTimeAllUsersImage = getAverageTimes(failuresImage)

	# sort and convert time object to seconds in order to calculate standard deviation 
	allLoginsText.sort()
	allLoginsImage.sort()
	allLoginsTextSeconds = []
	allLoginsImageSeconds = []
	getInSeconds(allLoginsText, allLoginsTextSeconds)
	getInSeconds(allLoginsImage, allLoginsImageSeconds)


	successesText.sort()
	successesImage.sort()
	successesTextSeconds = []
	successesImageSeconds = []
	getInSeconds(successesText, successesTextSeconds)
	getInSeconds(successesImage, successesImageSeconds)


	failuresText.sort()
	failuresImage.sort()
	failuresTextSeconds = []
	failuresImageSeconds = []
	getInSeconds(failuresText, failuresTextSeconds)
	getInSeconds(failuresImage, failuresImageSeconds)


	numberOfLoginsText.sort()
	numberOfLoginsImage.sort()
	numberOfSuccessesText.sort()
	numberOfSuccessesImage.sort()
	numberOfFailuresText.sort()
	numberOfFailuresImage.sort()


	countZeros = 0
	for f in numberOfFailuresText:
		if(f == 0):
			countZeros = 1 + countZeros
	del numberOfFailuresText[:countZeros]



	# write 'average' row
	outFile.writerow([" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "])
	outFile.writerow([" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "])
	outFile.writerow(["All Users: "," _ "," _ "," _ "," _ "," _ "," _ "," _ "])
	outFile.writerow([" ||||| "," _ "," _ "," _ "," _ ","All logins", "All successes", "All Failures"])


	outFile.writerow(["Median: ","testtextrandom", numberOfLoginsText[len(numberOfLoginsText)/2],
					 numberOfSuccessesText[len(numberOfSuccessesText)/2], numberOfFailuresText[len(numberOfFailuresText)/2], 
					 allLoginsText[(len(allLoginsText)/2)], successesText[len(successesText)/2], failuresText[len(failuresText)/2]])
	outFile.writerow(["Median: ","testpasstiles", numberOfLoginsImage[len(numberOfLoginsImage)/2] ,
					 numberOfSuccessesImage[len(numberOfSuccessesImage)/2], numberOfFailuresImage[len(numberOfFailuresImage)/2], 
					 allLoginsImage[(len(allLoginsImage)/2)], successesImage[len(successesImage)/2], failuresImage[len(failuresImage)/2]])


	outFile.writerow([" ||||| "," _ "," _ "," _ "," _ "," _ "," _ "," _ "])


	outFile.writerow(["Mean: ","testtextrandom",(len(allLoginsText) + numberOfUsersText // 2) // numberOfUsersText, 
					 (len(successesText) + numberOfUsersText // 2) // numberOfUsersText, (len(failuresText) + (numberOfUsersText) // 2) // (numberOfUsersText), 
					 roundToSeconds(avgLoginTimeAllUsersText), roundToSeconds(avgSuccessTimeAllUsersText), roundToSeconds(avgFailureTimeAllUsersText)])
	outFile.writerow(["Mean: ","testpasstiles",(len(allLoginsImage) + numberOfUsersImage // 2) // numberOfUsersImage, 
					 (len(successesImage) + numberOfUsersImage // 2) // numberOfUsersImage, (len(failuresImage) + (numberOfUsersImage) // 2) // (numberOfUsersImage),
					 roundToSeconds(avgLoginTimeAllUsersImage), roundToSeconds(avgSuccessTimeAllUsersImage),roundToSeconds(avgFailureTimeAllUsersImage)])


	outFile.writerow([" ||||| "," _ "," _ "," _ "," _ "," _ "," _ "," _ "])


	outFile.writerow(["SD: ","testtextrandom", round(np.std(numberOfLoginsText),2), round(np.std(numberOfSuccessesText),2), round(np.std(numberOfFailuresText),2), 
					 roundToSeconds(datetime.timedelta(seconds=round(np.std(allLoginsTextSeconds),2))),
					 roundToSeconds(datetime.timedelta(seconds=round(np.std(successesTextSeconds),2))),
					 roundToSeconds(datetime.timedelta(seconds=round(np.std(failuresTextSeconds),2)))])																																											 
					 
	outFile.writerow(["SD: ","testpasstiles", round(np.std(numberOfLoginsImage),2), round(np.std(numberOfSuccessesImage),2), round(np.std(numberOfFailuresImage),2),
					 roundToSeconds(datetime.timedelta( seconds=round(np.std(allLoginsImageSeconds),2))),
					 roundToSeconds(datetime.timedelta( seconds=round(np.std(successesImageSeconds),2))), 
					 roundToSeconds(datetime.timedelta(  seconds=round(np.std(failuresImageSeconds),2)))])


	outFile.writerow([" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "])
	outFile.writerow([" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "])
	outFile.writerow([" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "])
	outFile.writerow([" _ ", " _ " , " _ ", " _ ", "HISTOGRAM &", " _ ", " _ ", " _ "])
	outFile.writerow([" _ ", " _ " , " _ ", " _ ", "BOXPLOT DATA", " _ ", " _ ", " _ "])
	outFile.writerow([" _ ","testtextrandom","testtextrandom","testtextrandom"," _ ","testpasstiles","testpasstiles","testpasstiles"])
	outFile.writerow([" _ ","All Login Times (s)","All Success Times (s)","All Failure Times (s)"," ","All Login Times (s)","All Success Times (s)","All Failure Times (s)"])



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

	print("")
	print("Output_Part_A.csv file has been created in Project Directory!")
	print("")
	t1 = removeOutliers(allLoginsTextSeconds, 40)
	i1 = removeOutliers(allLoginsImageSeconds, 40)
	t2 = removeOutliers(successesTextSeconds, 40)
	i2 = removeOutliers(successesImageSeconds, 40)
	t3 = removeOutliers(failuresTextSeconds, 35)
	i3 = removeOutliers(failuresImageSeconds, 40)

	makeHistogram(t1, 10, .9, 'Text Scheme: Login Time', 'Frequency', 'Seconds', "Graphs/TextHistogramAllLogins.png", 'ggplot','#E83A22')
	makeHistogram(t2, 10, .9, 'Text Scheme: Success Time', 'Frequency', 'Seconds', "Graphs/TextHistogramSuccesses.png", 'ggplot','#E83A22')
	makeHistogram(t3, 10, .9, 'Text Scheme: Failure Time', 'Frequency', 'Seconds', "Graphs/TextHistogramFailures.png", 'ggplot','#E83A22')
	makeHistogram(i1, 10, .9, 'Image Scheme: Login Time', 'Frequency', 'Seconds', "Graphs/ImageHistogramAllLogins.png", 'ggplot','#2739EE')
	makeHistogram(i2, 10, .9, 'Image Scheme: Success Time', 'Frequency', 'Seconds', "Graphs/ImageHistogramSuccesses.png", 'ggplot','#2739EE')
	makeHistogram(i3, 10, .9, 'Image Scheme: Failure Time', 'Frequency', 'Seconds', "Graphs/ImageHistogramFailures.png", 'ggplot','#2739EE')
	print("")
	print("Histograms have been created in /Graphs !")
	print("")


	#####CLOSE THE DOCUMENTS####
	myCSVFileImage.close()
	myCSVFileText.close()
	csvFileOut.close()




# run program to do work for part B
def doPartB():
	fileNameDirect = 'database.csv'
	newFileName = 'Output_Part_B.csv'
	
	myCSVFileDirect = open(fileNameDirect, 'rb')
	myFileDirect = csv.reader(myCSVFileDirect)


	
	csvFileOut = open(newFileName,'w')
	outFile = csv.writer(csvFileOut)


	
	header=['userID', 'SCHEME', '# of Logins', '# of Success', '# of Failure', 'Average Login Time', 'Average Login Success Time', 'Average Login Failure Time']

	
	directData=fileToDict(myCSVFileDirect)



	
	outFile.writerow(header)
	directRows = []

	numberOfUsersDirect = numberOfUsers(directData);
	

	
	allLoginsDirect = []
	successesDirect = []
	failuresDirect = []
	numberOfLoginsDirect = []
	numberOfSuccessesDirect = []
	numberOfFailuresDirect = []
	directDataFormatted = algorithm(directData, directRows, allLoginsDirect, successesDirect, failuresDirect, numberOfLoginsDirect, numberOfSuccessesDirect, numberOfFailuresDirect)



	for p in directRows:
		outFile.writerow(p)

	
	avgLoginTimeAllUsersDirect = getAverageTimes(allLoginsDirect)
	
	avgSuccessTimeAllUsersDirect = getAverageTimes(successesDirect)
	
	avgFailureTimeAllUsersDirect = getAverageTimes(failuresDirect)


	allLoginsDirect.sort()
	allLoginsDirectSeconds = []
	getInSeconds(allLoginsDirect, allLoginsDirectSeconds)
	
	successesDirect.sort()
	successesDirectSeconds = []
	getInSeconds(successesDirect, successesDirectSeconds)
	
	failuresDirect.sort()
	failuresDirectSeconds = []
	getInSeconds(failuresDirect, failuresDirectSeconds)
	
	numberOfLoginsDirect.sort()
	numberOfSuccessesDirect.sort()
	numberOfFailuresDirect.sort()

	countZeros = 0
	for f in numberOfFailuresDirect:
		if(f == 0):
			countZeros = 1 + countZeros
	del numberOfFailuresDirect[:countZeros]

	
	outFile.writerow([" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "])
	outFile.writerow([" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "])
	outFile.writerow(["All Users: "," _ "," _ "," _ "," _ "," _ "," _ "," _ "])
	outFile.writerow([" ||||| "," _ "," _ "," _ "," _ ","All logins", "All successes", "All Failures"])



	outFile.writerow(["Median: ","directrandom", numberOfLoginsDirect[len(numberOfLoginsDirect)/2],
					 numberOfSuccessesDirect[len(numberOfSuccessesDirect)/2], numberOfFailuresDirect[len(numberOfFailuresDirect)/2], 
					 allLoginsDirect[(len(allLoginsDirect)/2)], successesDirect[len(successesDirect)/2], failuresDirect[len(failuresDirect)/2]])

	outFile.writerow([" ||||| "," _ "," _ "," _ "," _ "," _ "," _ "," _ "])


	outFile.writerow(["Mean: ","directrandom",(len(allLoginsDirect) + numberOfUsersDirect // 2) // numberOfUsersDirect, 
					 (len(successesDirect) + numberOfUsersDirect // 2) // numberOfUsersDirect, (len(failuresDirect) + (numberOfUsersDirect) // 2) // (numberOfUsersDirect), 
					 roundToSeconds(avgLoginTimeAllUsersDirect), roundToSeconds(avgSuccessTimeAllUsersDirect), roundToSeconds(avgFailureTimeAllUsersDirect)])


	outFile.writerow([" ||||| "," _ "," _ "," _ "," _ "," _ "," _ "," _ "])


	outFile.writerow(["SD: ","directrandom", round(np.std(numberOfLoginsDirect),2), round(np.std(numberOfSuccessesDirect),2), round(np.std(numberOfFailuresDirect),2), 
					 roundToSeconds(datetime.timedelta(seconds=round(np.std(allLoginsDirectSeconds),2))),
					 roundToSeconds(datetime.timedelta(seconds=round(np.std(successesDirectSeconds),2))),
					 roundToSeconds(datetime.timedelta(seconds=round(np.std(failuresDirectSeconds),2)))])	

	outFile.writerow([" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "])
	outFile.writerow([" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "])
	outFile.writerow([" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "])
	outFile.writerow([" _ ", " _ " , " _ ", " _ ", "HISTOGRAM &", " _ ", " _ ", " _ "])
	outFile.writerow([" _ ", " _ " , " _ ", " _ ", "BOXPLOT DATA", " _ ", " _ ", " _ "])
	outFile.writerow([" _ ","directrandom","directrandom","directrandom"," _ "," _ "," _ "," _ "])
	outFile.writerow([" _ ","All Login Times (s)","All Success Times (s)","All Failure Times (s)"," "," _ "," _ "," _ "])

	maxLength = max(len(allLoginsDirectSeconds),len(successesDirectSeconds),len(failuresDirectSeconds))
	for a in range(0,maxLength):
		row = [" "]
		if(a < len(allLoginsDirectSeconds)):
			row.append(round(allLoginsDirectSeconds[a]))
		else:
			row.append(" ")
		if(a < len(successesDirectSeconds)):
			row.append(round(successesDirectSeconds[a]))
		else:
			row.append(" ")
		if(a < len(failuresDirectSeconds)):
			row.append(round(failuresDirectSeconds[a]))
		else:	
			row.append(" ")
		row.append(" ")
		row.append(" ")
		row.append(" ")
		row.append(" ")
		outFile.writerow(row)




	print("")
	print("Output_Part_B.csv file has been created in Project Directory!")
	print("")
	d1 = removeOutliers(allLoginsDirectSeconds, 30)
	d2 = removeOutliers(successesDirectSeconds, 35)
	d3 = removeOutliers(failuresDirectSeconds, 30)
	
	makeHistogram2(d1, 6, 1, 'Direction Scheme: Login Time', 'Frequency', 'Seconds', "Graphs/DirectHistogramAllLogins.png", 'seaborn-poster', '#4DB755')
	makeHistogram2(d2, 6, 1, 'Direction Scheme: Success Time', 'Frequency', 'Seconds', "Graphs/DirectHistogramSuccesses.png", 'seaborn-poster', '#4DB755')
	makeHistogram2(d3, 6, 1, 'Direction Scheme: Failure Time', 'Frequency', 'Seconds', "Graphs/DirectHistogramFailures.png", 'seaborn-poster', '#4DB755')
	print("")
	print("Histograms have been created in /Graphs !")
	print("")
	


# which job? Part A or B
arguments = len(sys.argv) - 1

if(arguments != 1):
	print("incorrect # of arguments")
	sys.exit()
else:
	if(sys.argv[1] == "A"):
		#print(sys.argv[1])
		doPartA()
	elif(sys.argv[1] == "B"):
		#print(sys.argv[1])
		doPartB()
	else:
		print("incorrect argument")
		sys.exit()
