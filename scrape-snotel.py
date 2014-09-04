import csv
import urllib2
import StringIO
import os

# SNOTEL stations
stations = {'zirkel': 1033, 'columbine' : 408, 'never-summer': 1031, 'rawah': 1032, 'roach': 718, 'blackhall-mtn': 1119, 'webber-springs': 852, 'old-battle': 673, 'sage-creek-basin': 1015, 'south-brush-creek': 772, 'north-french-creek': 668, 'cinnabar-park': 1046, 'brooklyn-lake': 367, 'med-bow': 1196, 'sand-lake': 731, 'windy-peak': 872, 'laprele-creek': 571, 'reno-hill': 716, 'casper-mtn': 389, 'larsen-creek': 1134}

#s = station name, i = station ID
for s,i in stations.items():
	# Open webpage and read data
	# webpage contains snow water equivalency (swe) actual vs 1981-2010 median swe
	url = "http://www.wcc.nrcs.usda.gov/reportGenerator/view_csv/customChartReport/monthly/" + str(s) + "%3ACO%3ASNTL%7Cid%3D%22%22%7Cname/-409%2C0/WTEQ%3A%3Avalue%2CWTEQ%3A%3Amedian_1981"
	print "reading webpage on " + str(s)
	page = urllib2.urlopen(url)
	cr = csv.reader(page)
	
	# Check for subdirectory and/or make subdirectory
	path = "data/" + str(s)
	if not os.path.exists(path):
		os.makedirs(path)
		
	# Create file and write data
	filename = str(s) + "-monthly-data.tsv"
	file = open(os.path.join(path, filename), "wb")
	cw = csv.writer(file, delimiter='\t')
	print "writing file of " + str(s)
	for row in cr:
		cw.writerow(row)
		
	# Close file
	print "closing file " + path + "/" + filename
	file.close()

print "DONE!"
