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
fieldnames = ['activity', 'date', 'start', 'end', 'hours']

today = datetime.today()
today_string = today.strftime("%d.%m.%Y")
time_string = today.strftime("%H:%M:%S")

task = "unknown"
hours = -1

if args.start:
    print(args.start)
    file_exists = os.path.isfile(ACTIVITY_CSV)

    with open(ACTIVITY_CSV, 'a') as csvfile: # with takes care of closing the file properly (best practice)
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader() # if file doesn't exist yet, write a header
        writer.writerow({'activity': args.start, 'date': today_string, 'start': time_string, 'end': '', 'hours': ''})

elif args.end:
    temp = []
    with open(ACTIVITY_CSV, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            temp.append(row)

    # clear old file        
    with open(ACTIVITY_CSV, 'w') as csvfile:
        csvfile.write("")

    with open(ACTIVITY_CSV, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for rowIndex in range(0, len(temp) - 1):
            row = {
                'activity': temp[rowIndex]['activity'], 
                'date': temp[rowIndex]['date'], 
                'start': temp[rowIndex]['start'], 
                'end': temp[rowIndex]['end'], 
                'hours': temp[rowIndex]['hours']
            }
            writer.writerow(row)
        
        lastIndex = len(temp) - 1

        start = datetime.strptime(temp[lastIndex]['date'] + " " + temp[lastIndex]['start'], "%d.%m.%Y %H:%M:%S");
        hours = round(((today - start).total_seconds() / 60 / 60), 2)
        task = temp[lastIndex]['activity']

        lastRow = {
            'activity': temp[lastIndex]['activity'], 
            'date': temp[lastIndex]['date'], 
            'start': temp[lastIndex]['start'], 
            'end': time_string, 
            'hours': hours
        }

        writer.writerow(lastRow)
    print("You have worked on the task " + task + " for " + str(hours) + " hours.")
