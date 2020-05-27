import main
import json
from datetime import datetime


def check_is_every(index):
    with open(".Remind.json", "r") as f:
        data = json.load(f)
        for i in data["Reminder"][index].values():
            return i[-2]
        
def update_reminder(n, Type):
    with open(".Remind.json", "r") as f:
        data = json.load(f)
        dataf = list(data["Reminder"][index].values())
        try:
            if dataf[0][-1][-1] < int(datetime.now().strftime("%Y")) and Type == "year":
                dataf[0][-1].clear()
            if dataf[0][-1][-1] < int(datetime.now().strftime("%d")) and Type == "date":
                dataf[0][-1].clear()
        except:
            pass
        dataf[0][-1].append(n)
    with open(".Remind.json", "w") as f:
        json.dump(data, f, indent=3)

def check(index):
    with open(".Remind.json", "r") as f:
        data = json.load(f)
        dataf = list(data["Reminder"][index].values())
    return dataf[0][-1]

while True:
    try:
        reminder_list = main.get_reminder()
        for i in reminder_list:
            index = reminder_list.index(i)
            date,time = main.get_time_of_reminder(index)
            date = list(map(int, date.split("-")))
            time = list(map(int, time.split(":")))
            ctime = datetime.now().strftime("%H:%M")
            cdate = datetime.now().strftime("%d-%m-%Y")
            ctime = list(map(int, ctime.split(":")))
            cdate = list(map(int, cdate.split("-")))
            Checkup = check_is_every(index)
            if  Checkup == "Every Year" and cdate[0] == date[0] and cdate[1] == date[1] and ctime[0] \
               == time[0] and ctime[1] == time[1] and cdate[2] not in check(index):
                main.notify(i)
                update_reminder(cdate[2], "year")
            if Checkup == "Every Day" and time[0] == ctime[0] and time[1] == ctime[1] and cdate[0] not in check(index):
                main.notify(i)
                update_reminder(cdate[0], "date")
            if Checkup == 'Day' and date[0] == cdate[0] and date[1] == cdate[1] \
              and date[2] == cdate[2] and time[0] == ctime[0] and time[1] == ctime[1]:
                main.notify(i)
                with open(".Remind.json", "r") as f:
                    data = json.load(f)
                    data["Reminder"].pop(index)
                    with open(".Remind.json", "w") as f:
                        json.dump(data, f, indent=3)
    except:
        continue
