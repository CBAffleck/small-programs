import operator

filename = 'netflix.txt'

#Read from file
with open(filename) as f:
	data = f.readlines()

#Finds nth appearance of element in string
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

tvshow_dict = {}	#Format: {[name: [views, type, minutes]]}
watch_dates = []	#List of all dates (can have duplicates)
shows = []			#List of shows (can have duplicates)
for line in data:
	if not line[0].isalpha():	#Checks if line is a date
		watch_dates.append(line.rstrip())
	if "\"" in line and line[0].isalpha():	#Checks if line is a TV Show
		line = line.rstrip()	#Strips return off of line
		if 'Pok\xc3\xa9mon' in line or 'Star Wars' in line:	#These shows have extra ":" in them
			show_name = line[:find_nth(line, ":", 2)]
			shows.append(show_name)
		else:
			show_name = line[:line.find(":")]
			shows.append(show_name)
		if show_name not in tvshow_dict:	#Add show to dict if not already there
			tvshow_dict[show_name] = [1, "TV Show", 0]
		else:
			tvshow_dict[show_name][0] += 1	#Increase count for views
	elif ":" in line and line[0].isalpha():	#Checks if line is a Movie with a ":"
		line = line.rstrip()
		show_name = line
		shows.append(show_name)
		if show_name not in tvshow_dict:
			tvshow_dict[show_name] = [1, "Movie", 0]
		else:
			tvshow_dict[show_name][0] += 1
	elif ":" not in line and line[0].isalpha():	#Checks if line is a Movie
		name = line.rstrip()
		shows.append(name)
		if name not in tvshow_dict:
			tvshow_dict[name] = [1, "Movie", 0]
		else:
			tvshow_dict[name][0] += 1

## Show run times ##
duration = {'Arrow':42, 'Captain America: Civil War':150, 'Chuck':45, "DC's Legends of Tomorrow":42, 
			'Dear Frankie':105, 'Gotham':42, 'Hitch':118, 'Home':94, 'How I Met Your Mother':22, 
			'Love Actually':145, "Marvel's Daredevil":54, "Marvel's Jessica Jones":52, 
			"Marvel's Luke Cage":55, "Marvel's The Defenders":50, "Marvel's The Punisher":52, 
			'New Girl':22, 'One-Punch Man':24, 'Orange Is the New Black':54, 
			'Pok\xc3\xa9mon: Indigo League':22, 'Psych':45, 'Serenity':120, 'Sherlock':86, 
			'Spotlight':128, 'Star Wars: The Clone Wars':22, 'Stranger Things':50, 
			'The Blacklist':45, 'The IT Crowd':24, 'The Office (U.S.)':22, 'White Collar':45}

# Adds run times to tvshow_dict
for x in tvshow_dict:
	if x in duration:
		tvshow_dict[x][2] = tvshow_dict[x][0] * duration[x]

#Matches shows with the dates they were watched on
show_per_date = {}
for i, j in zip(watch_dates, shows):
	show_per_date[i] = j

#Finds number of episodes watched per date, date with most episodes, highest watched episode per that
#date, and the time spent on Netflix on that date
date_counts = {}
for x in watch_dates:
	if x not in date_counts:
		date_counts[x] = [1]
	else:
		date_counts[x][0] += 1
top_date = max(date_counts.iteritems(), key=operator.itemgetter(1))[0]
most_watched_one_day = show_per_date[top_date]
top_date_time = duration[most_watched_one_day] * date_counts[top_date][0]

#Finds show that has the most viewing time
top_show = ""
top_min = 0
for x in tvshow_dict:
	if tvshow_dict[x][2] > top_min:
		top_show = x
		top_min = tvshow_dict[x][2]

#Returns the total time spent on Netflix for the dataset
def total_time(tvshow_dict):
	total = 0
	for x in tvshow_dict:
		total += tvshow_dict[x][2]
	return total/60 + float(total%60)/60

#Print out all of the stats and shows/movies seen with corresponding statistics
print "==Stats=="
print "Total watch time: %f hours" % (total_time(tvshow_dict))
print "Most active date: %s -- %d episodes -- %s -- %f hours" % (top_date, date_counts[top_date][0], 
		most_watched_one_day, top_date_time/60 + float(top_date_time%60)/60)
print "Show with most watch time: %s -- %d.%d hours" % (top_show, top_min/60, 
		(float(top_min%60)/60)*100), "\n"
print "==SHOWS/MOVIES=="
for key in sorted(tvshow_dict):
	print "%s - Views: %d, Type: %s, Watch time: %d.%d hours" % (key, tvshow_dict[key][0], 
			tvshow_dict[key][1], tvshow_dict[key][2]/60, (float(tvshow_dict[key][2]%60)/60)*100)


