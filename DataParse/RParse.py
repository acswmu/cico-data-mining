computers = dict([('a00',-1),('a01',-1),('a02',-1),('a03',-1),('a04',-1),('a05',-1),('a06',-1),('a07',-1),('a08',-1),('a09',-1),('a10',-1),('a11',-1),('a12',-1),('a13',-1),('a14',-1),('a15',-1),('a16',-1),('a17',-1),('a18',-1),('a19',-1),('a20',-1),('a21',-1),('a22',-1),('a23',-1),('a24',-1),('a25',-1),('a26',-1),('a27',-1),('a28',-1),('a29',-1),('a30',-1),('a31',-1),('a32',-1),('a33',-1),('a34',-1),('a35',-1),('a36',-1),('a37',-1),('a38',-1),('a39',-1),('a40',-1),('a41',-1),('a42',-1),('a43',-1),('a44',-1),('a45',-1),('a46',-1),('a47',-1),('a48',-1),('a49',-1),('a50',-1),('a51',-1),('a52',-1),('a53',-1),('a54',-1),('a55',-1),('a56',-1),('a57',-1),('a58',-1),('a59',-1),('a60',-1),('a61',-1),('a62',-1),('a63',-1),('a64',-1),('a65',-1),('a66',-1),('a67',-1),('a68',-1),('a69',-1),('a70',-1),('a71',-1),('a72',-1),('a73',-1),('a74',-1),('a75',-1),('a76',-1),('a77',-1),('a78',-1)])

output = open("../Data/ParsedData.csv", 'w')

output.write("Start Date, Start Time, Computer Number, Time Used in Mins\n")

with open('../Data/cicolog-bymachine.csv') as file:
	for line in file:
		#data is in the following format
		#	['MM/DD/YYYY HH:MM', 'CheckIn' or 'CheckOut', 'a??\n']
		temp = line.split(',')		
		
		#we have 4 cases 
		#Currently checked out --> checked in read
		#	This case means that someone is done with their computer we should record the time used and update time to -1
		#Currently checked in --> checked in read
		#	Ignore this case
		#Currently checked in --> checked out read
		#	This case means someone is using a computer update -1 to the time stamp
		#Currently checked out --> checked out read
		#	Update timestamp with new checked out value
		
		#remove the extra \n
		temp[2] = temp[2][:3]
		
		if len(temp) == 3:
			#read in Checked in
			if temp[1] == 'CheckIn':
				#Computer was checked out
				if computers[temp[2]] != -1:
					minsOne = int(computers[temp[2]][-5:][3:]) + int(60 * int(computers[temp[2]][-5:][:2]))
					minsTwo = int(temp[0][-5:][3:]) + int(60 * int(temp[0][-5:][:2]))
					
					dif = minsTwo - minsOne
					
					if (dif < 0):
						minsTwo += 1440
						dif = minsTwo - minsOne
					
					#computer was checked out over night need special calculation for these
					if(dif != 0):
						output.write(computers[temp[2]][:-5].strip() + ',' + computers[temp[2]][-5:].lstrip(' ') + ',' + temp[2] + ',' + str(dif) + "\n")
					
					computers[temp[2]] = -1;
				#Computer was Checked in
				else:
					print 'double check in ' + temp[2] + " " + temp[0]
			#read in Checked out
			else:
				#computer was checked in
				if computers[temp[2]] == -1:
					computers[temp[2]] = temp[0]
				#computer was checked out
				else:
					print 'double check out ' + temp[2] + " " + temp[0]

output.close()