'''
Auther-: White-Programmer
Date-: 9 May 2020
This Program Help To Remind The Things That User Wants To Get Remind
'''

from plyer import notification
from datetime import datetime
import json
import os


def Fun(Print):
    print(f"---------------------------- {Print}----------------------------")


def write_reminder_to_json(reminder, date, time, duration):
    date = date.split("-")
    time = time.split(":")
    files = os.listdir()
    if ".Remind.json" not in files:
        with open(".Remind.json", "w") as f:
            f.write("")
    with open(".Remind.json", "r") as f:
        try:
            data = json.load(f)
            Data = {reminder: [date[0], date[1],
                               date[2], time[0], time[1], duration, []]}
            data["Reminder"].append(Data)
        except Exception as e:
            data = {"Reminder": [
                {reminder: [date[0], date[1], date[2],  time[0], time[1], duration, []]}]}
        with open(".Remind.json", "w") as f:
            json.dump(data, f, indent=3)
        Logger(f"You Created Reminder For {reminder}", "Created")


def Logger(Event, Type):
    with open(".RemindLog", "a") as f:
        f.write("[" + Type + "] " + "At " +
                datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        f.write(" " + Event + "\n")


def notify(text):
    notification.notify(title="Reminder", message=text, timeout=10)
    Logger(f"Reminder Notification Confirmed For {text}", "Notified")


def get_reminder():
    try:
        with open(".Remind.json", "r") as f:
            data = json.load(f)
            reminder_list = []
            for i in data["Reminder"]:
                for o in i.keys():
                    reminder_list.append(o)
        return reminder_list
    except:
        return "No Reminder So Far"


def get_time_of_reminder(reminder_index):
    with open(".Remind.json", "r") as f:
        data = json.load(f)
        value = []
        for i in data["Reminder"][reminder_index].values():
            for o in i:
                value.append(o)
        value.pop(-1)
        value.pop(-1)
        value = list(map(int, value))
        date = f"{value[0]}-{value[1]}-{value[2]}"
        time = f"{value[3]}:{value[4]}"
        return date, time


def delete_reminder():
    for i, j in enumerate(get_reminder()):
        date, time = get_time_of_reminder(i)
        print(f"{i + 1}. {j}\n[Reminder Will Activate On {date} At {time}]\n")
    try:
        with open(".Remind.json", "r") as f:
            data = json.load(f)
            if len(data["Reminder"]) != 0:
                index = int(input("\nWhich One You Want To Delete\n>>> "))
                reminder = data["Reminder"][index - 1]
                data["Reminder"].pop(index - 1)
                if index > 0:
                    with open(".Remind.json", "w") as f:
                        json.dump(data, f, indent=3)
                Logger(f"You Deleted Reminder {j}", "Deleted")
    except Exception as e:
        print((str(e)) + ">>> Reminder Not Found")


def Main():
    print("1.Set Reminder\n2.Delete Reminder\n3.Reminder Log\n4.Exit")
    user = int(input(">> "))
    if user == 1:
        yn = 'n'
        while yn == 'n':
            Fun("Set Reminder")
            '''When User Select This And Enter Some Reminder It Store In Json File'''
            Remind = input("Enter Your Reminder\n>>> ")
            print("\nEnter Your Time For Reminder\nNote-: Enter In This Format 'Month Date Year Hour Min' Just Seperate By Space And Enter Full Year Like '20XX'\nTo Set Reminder For Every Day Only Press 'd'")
            time = input(">>> ")
            try:
                if 'd' in time.lower():
                    Hour = int(input("Enter Hour\n>>> "))
                    Min = int(input("Enter Min\n>>> "))
                    date = datetime.now().strftime("%d-%m-%Y")
                    time = f"{Hour}:{Min}"
                    duration = "Every Day"
                else:
                    time = list(map(int, time.split()))
                    Month, Date, Year, Hour, Min = time[0], time[1], time[2], time[3], time[4]
                    m = [1, 3, 5, 7, 8, 10, 12]
                    if Month > 12:
                        print("\n(ERROR)>>Invalid Month")
                        continue
                    if Month in m and Date > 31:
                        print(
                            "\n(ERROR)>>Invalid Date\n(ERROR TYPE)>>>Date Limit Is 31 ")
                        continue
                    if len(str(Year)) < 4 or Year < int(datetime.now().strftime("%Y")):
                        print("\n(ERROR)>>Invalid Year")
                        continue
                    if Month not in m and Date > 30:
                        print("\n(ERROR)>>Invalid Date\n(ERROR TYPE)>>>Date Limit Is 30")
                    time = f"{Hour}:{Min}"
                    date = f"{Date}-{Month}-{Year}"
                    print(f"\nYou Entered This Time-: {time}\nYou Entered This Date-: {date}")
                    if 'd' not in time.lower():
                        d = input("(QUESTION)>>>Do You Want This Reminder Every Year y(es) n(o)> ")
                        if d == 'y':
                            duration = "Every Year"
                        else:
                            duration = "Day"
                yn = input(
                    "\n(QUESTION)>>> Do You Want To Edit The Entered Details Press y(es) or n(o)> ")
                if yn == 'y':
                    yn = 'n'
                    continue
                else:
                    yn = 'y'
                    write_reminder_to_json(Remind, date, time, duration)
                    print()
                    Fun("Reminder Saved")
            except:
                print("\n(ERROR)>>Invalid Entry")
                continue

    elif user == 2:
        Fun("Delete Reminder")
        delete_reminder()
        Fun("Reminder Deleted")

    elif user == 3:
        Fun("Activity")
        with open(".RemindLog", "r") as f:
            data = f.readlines()
            for i, j in enumerate(data):
                print(f"{i + 1}. {j}")
            print(f"Total Activity-: {len(data)}")
        Fun("Activity Log Ends Here")
    elif user == 4:
        exit()

    else:
        print("\n>> Invalid Operation\n")


if __name__ == "__main__":
    while 1:
        try:
            Main()
        except Exception as e:
            Fun("Some Error")
            print(f"(Error_Name)>>> {str(e)}\n")
