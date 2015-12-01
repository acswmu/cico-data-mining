import operator

computers = dict([('a00',-1),('a01',-1),('a02',-1),('a03',-1),('a04',-1),('a05',-1),('a06',-1),('a07',-1),('a08',-1),('a09',-1),('a10',-1),('a11',-1),('a12',-1),('a13',-1),('a14',-1),('a15',-1),('a16',-1),('a17',-1),('a18',-1),('a19',-1),('a20',-1),('a21',-1),('a22',-1),('a23',-1),('a24',-1),('a25',-1),('a26',-1),('a27',-1),('a28',-1),('a29',-1),('a30',-1),('a31',-1),('a32',-1),('a33',-1),('a34',-1),('a35',-1),('a36',-1),('a37',-1),('a38',-1),('a39',-1),('a40',-1),('a41',-1),('a42',-1),('a43',-1),('a44',-1),('a45',-1),('a46',-1),('a47',-1),('a48',-1),('a49',-1),('a50',-1),('a51',-1),('a52',-1),('a53',-1),('a54',-1),('a55',-1),('a56',-1),('a57',-1),('a58',-1),('a59',-1),('a60',-1),('a61',-1),('a62',-1),('a63',-1),('a64',-1),('a65',-1),('a66',-1),('a67',-1),('a68',-1),('a69',-1),('a70',-1),('a71',-1),('a72',-1),('a73',-1),('a74',-1),('a75',-1),('a76',-1),('a77',-1),('a78',-1)])

computerUsage = dict([('a00',0),('a01',0),('a02',0),('a03',0),('a04',0),('a05',0),('a06',0),('a07',0),('a08',0),('a09',0),('a10',0),('a11',0),('a12',0),('a13',0),('a14',0),('a15',0),('a16',0),('a17',0),('a18',0),('a19',0),('a20',0),('a21',0),('a22',0),('a23',0),('a24',0),('a25',0),('a26',0),('a27',0),('a28',0),('a29',0),('a30',0),('a31',0),('a32',0),('a33',0),('a34',0),('a35',0),('a36',0),('a37',0),('a38',0),('a39',0),('a40',0),('a41',0),('a42',0),('a43',0),('a44',0),('a45',0),('a46',0),('a47',0),('a48',0),('a49',0),('a50',0),('a51',0),('a52',0),('a53',0),('a54',0),('a55',0),('a56',0),('a57',0),('a58',0),('a59',0),('a60',0),('a61',0),('a62',0),('a63',0),('a64',0),('a65',0),('a66',0),('a67',0),('a68',0),('a69',0),('a70',0),('a71',0),('a72',0),('a73',0),('a74',0),('a75',0),('a76',0),('a77',0),('a78',0)])


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
					
					#computer was checked out over night need special calculation for these
					if dif < 0:
						print "check out time: " + computers[temp[2]] + " check in time: " + temp[0]
					else:
						computerUsage[temp[2]] += dif
					
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
	
print sorted(computerUsage.items(), key=operator.itemgetter(0))