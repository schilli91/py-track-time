import argparse, csv, os.path
from datetime import datetime

parser = argparse.ArgumentParser(description='Track time working on a task.')
parser.add_argument('-s', '--start', help='starts timer', metavar='task')
# parser.add_argument('task', help='specify task working on')
parser.add_argument('-e', '--end', action='store_true', help='end timer')
# action="store_true" assigns True to args.verbose
# parser.add_argument("--verbose", help="increase output verbosity", action="store_true")
# choices specifies valid parameters for an argument
# parser.add_argument("--level", choices=[0, 1, 2])

args = parser.parse_args()
ACTIVITY_CSV = 'activities.csv'

today = datetime.today()
today_string = str(today.day) + '.' + str(today.month) + '.' + str(today.year)
time = today.time()
time_string = time.isoformat(timespec='seconds')

if args.start:
	print(args.start)
	file_exists = os.path.isfile(ACTIVITY_CSV)

	with open(ACTIVITY_CSV, 'a') as csvfile:
	    fieldnames = ['activity', 'date', 'start', 'end', 'hours']
	    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

	    if not file_exists:
	    	writer.writeheader() # if file doesn't exist yet, write a header
	    writer.writerow({'activity': args.start, 'date': today_string, 'start': time_string, 'end': '', 'hours': ''})
elif args.end:
	print('end')
	with open(ACTIVITY_CSV, 'a') as csvfile:
	    fieldnames = ['activity', 'date', 'start', 'end', 'hours']
	    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

	    writer.writerow({'activity': args.start, 'date': 'now', 'start': '', 'end': 'hh:mm:ss', 'hours': ''})
