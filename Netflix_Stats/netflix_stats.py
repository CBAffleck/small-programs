import operator
from datetime import datetime

filename = 'netflixinfo.txt'

#Finds nth appearance of element in string
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

#Read from file
show_dict = {}	#Format: [title: [views, type, total time in minutes]]
watch_dates = {}	#Format: [date : [show/movie title, view count]]
dates = []
with open(filename, 'r') as input_f:
	lineNumber = 0
	for line in input_f:
		if lineNumber == 2:
			accountName = line.strip('\n')
		lineNumber += 1
		if "/" not in line:
			continue
		index = line.find("Report a problem")
		line = line[:index]
		date = " ".join(line.split()[:1])
		dates.append(date)
		show = " ".join(line.split()[1:])
		if "\"" in show:	#Checks if line is a TV Show
			if 'Pok\xc3\xa9mon' in line or 'Star Wars' in line:	#These shows have extra ":" in them
				show_name = show[:find_nth(show, ":", 2)]
			else:
				show_name = show[:show.find(":")]
			if date in watch_dates:
				watch_dates[date][1] += 1
			else:
				watch_dates[date] = [show_name, 1]
			if show_name not in show_dict:	#Add show to dict if not already there
				show_dict[show_name] = [1, "TV Show", 0]
			else:
				show_dict[show_name][0] += 1	#Increase count for views
		elif ":" in show:	#Checks if line is a Movie with a ":"
			show_name = show
			if date in watch_dates:
				watch_dates[date][1] += 1
			else:
				watch_dates[date] = [show_name, 1]
			if show_name not in show_dict:
				show_dict[show_name] = [1, "Movie", 0]
			else:
				show_dict[show_name][0] += 1
		elif ":" not in show:	#Checks if line is a Movie
			if date in watch_dates:
				watch_dates[date][1] += 1
			else:
				watch_dates[date] = [show, 1]
			if show not in show_dict:
				show_dict[show] = [1, "Movie", 0]
			else:
				show_dict[show][0] += 1

## Show run times ##
duration = {'50 First Dates':106, 'Arrow':42, 'Batman':126, 'Bones':40,
			'Captain America: Civil War':150, 'Chuck':45, "DC's Legends of Tomorrow":42, 
			'Dear Frankie':105, 'Europa Report':97, 'Family Guy':22, 'Fargo':98, 'Firefly':44, 
			'Gotham':42, 'Hitch':118, 'Home':94, 'How I Met Your Mother':22, 'Kate & Leopold':123, 
			'Love Actually':145, "Marvel's Daredevil":54, "Marvel's Jessica Jones":52, 
			"Marvel's Luke Cage":55, "Marvel's The Defenders":50, "Marvel's The Punisher":52, 
			'New Girl':22, 'One-Punch Man':24, 'Orange Is the New Black':54, 
			'Pok\xc3\xa9mon: Indigo League':22, 'Psych':45, 'Red Dawn':116, 'Revolution':43, 
			'Serenity':120, 'Sherlock':86, 'Spotlight':128, 'Star Wars: The Clone Wars':22, 
			'Stranger Things':50, 'The Avengers':143, 'The Blacklist':45, 'The Croods':98, 
			'The Firm':154, 'The Hunger Games':142, 'The IT Crowd':24, 'The Nut Job':100, 
			'The Office (U.S.)':22, 'The Walking Dead':44, 'Tomorrow, When The War Began':104, 
			'White Collar':45}

# Adds run times to show_dict
for x in show_dict:
	if x in duration:
		show_dict[x][2] = show_dict[x][0] * duration[x]

#Find most watched episodes in one day and the day it occurred on
views = 0
top_date = ""
top_date_watch_time = 0
for x in watch_dates:
	if watch_dates[x][1] > views:
		top_date = x
		views = watch_dates[x][1]
most_watched_one_day = watch_dates[top_date][0]
top_date_watch_time = duration[most_watched_one_day] * watch_dates[top_date][1]

noDupeDates = []
[noDupeDates.append(i) for i in dates if not noDupeDates.count(i)]
date_ints = [datetime.strptime(d, "%m/%d/%y") for d in noDupeDates]
print date_ints
max_consecutive_dates = 0
max_start_date = None
max_end_date = None
startDate = None
tmp = 0
prevDate = None
for d in date_ints:
	if prevDate == None:
		prevDate = d
	elif d - prevDate == -(datetime(2000,1,2,1,1,1) - datetime(2000,1,1,1,1,1)):
		print "Current date: ", d
		print "Previous date: ", prevDate
		tmp += 1
		if startDate == None:
			startDate = prevDate
	else:
		print d - prevDate
		if max_consecutive_dates < tmp:
			max_consecutive_dates = tmp
			max_start_date = startDate
			max_end_date = prevDate
		prevDate = d
		startDate = None
		tmp = 0
print "Most consecutive days of Netflix: ", max_consecutive_dates
print datetime(2000,1,2,1,1,1) - datetime(2000,1,1,1,1,1)
print "Start date: ", max_start_date, "End date: ", max_end_date


#Finds show that has the most viewing time
top_show = ""
top_min = 0
for x in show_dict:
	if x == "White Collar":
		show_dict[x][2] = show_dict[x][0] * duration[x] * 2
		show_dict[x][0] *= 2
	if show_dict[x][2] > top_min:
		top_show = x
		top_min = show_dict[x][2]

#Returns the total time spent on Netflix for the dataset
def total_time(show_dict):
	total = 0
	for x in show_dict:
		total += show_dict[x][2]
	return total/60 + float(total%60)/60

# print "==Stats for %s==" % accountName
# print "Total watch time: %f hours" % (total_time(show_dict))
# print "Most active date: %s -- %d episodes -- %s -- %f hours" % (top_date, views, 
# 		most_watched_one_day, top_date_watch_time/60 + float(top_date_watch_time%60)/60)
# print "Show with most watch time: %s -- %d.%d hours" % (top_show, top_min/60, 
# 		(float(top_min%60)/60)*100), "\n"
# print "==SHOWS/MOVIES=="
# for key in sorted(show_dict):
# 	print "%s - Views: %d, Type: %s, Watch time: %d.%d hours" % (key, show_dict[key][0], 
# 			show_dict[key][1], show_dict[key][2]/60, (float(show_dict[key][2]%60)/60)*100)

#Write to output file
with open('netflix_out.txt', 'w') as output_f:
	output_f.write("==Stats for %s== \n" % accountName)
	output_f.write("Total watch time: %f hours \n" % (total_time(show_dict)))
	output_f.write("Most active date: %s -- %d episodes -- %s -- %f hours \n" % (top_date, views, 
			most_watched_one_day, top_date_watch_time/60 + float(top_date_watch_time%60)/60))
	output_f.write("Show with most watch time: %s -- %d.%d hours \n" % (top_show, top_min/60, 
			(float(top_min%60)/60)*100))
	output_f.write("==SHOWS/MOVIES== \n")
	for key in sorted(show_dict):
		output_f.write("%s - Views: %d, Type: %s, Watch time: %d.%d hours \n" % (key, show_dict[key][0], 
				show_dict[key][1], show_dict[key][2]/60, (float(show_dict[key][2]%60)/60)*100))




