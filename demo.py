import csv
import time

symptomdict={"Yes":"\nWARNING: Your symptoms may be related to a more serious cause.\n\nIf your symptoms persist, do not wait more than 5 minutes before seeking help.","No":"\nOK, thanks for telling us.\n\nRemember, even 20 minutes of brisk walking a day can significantly reduce your risk of heart disease.","Intermediate":"\nCAUTION: Your symptoms could be signs of heart disease.\n\nPlease follow up with your doctor if your symptoms do not completely resolve."}

events={"RR":3,"HR":4,"Sleep":5,"Nausea":2,"Upper":2,"Chest":9, "Sweats": 0, "Fatigue":1, "Breath":3}

def checker(data_file):
    reader = csv.reader(data_file)
    print(type(reader))
    minute=0
    for row in reader:
        print("Minute: "+str(minute)+". Respiration rate is "+row[1]+" breaths per minute. Heart rate is "+row[2]+" beats per minute.")
        minute+=1
        time.sleep(.1)
        if ((float(row[1])/float(row[2]))>1.5):
                print("\nCardia Alert! We have detected an anomaly in your respiration rate.\n")
                raw_input("Please hit Enter to view the alert.\n")
                symptoms=raw_input("List which, if any, of the following symptoms you are experiencing: chest pain, upper extremity pain, nausea, cold sweats, shortness of breath, extreme fatigue. Or type \"none\" if none.\n\n")
                symptoms=str.split(symptoms,", ")
                normal_alert(symptoms)
                break

def normal_alert(symptom_list):
    if ("chest pain" in symptom_list) or len(symptom_list)>1:
        print symptomdict["Yes"]
    elif "none" in symptom_list:
        print symptomdict["No"]
    else:
        print symptomdict["Intermediate"]
    raw_input("\nPress enter to view your Weekly Report.")
    weekly_alert()

def weekly_alert():
        print("\nThis week, you had "+str(events["RR"])+" respiration rate anomalies, "+str(events["HR"])+" heart rate anomalies, and "+str(events["Sleep"])+" sleep disruptions. You reported "+str(events["Nausea"])+" instances of nausea/indigestion, "+str(events["Upper"])+" instances of upper extremity pain, "+str(events["Chest"])+" instances of chest pain, "+str(events["Breath"])+" instances of shortness of breath, "+str(events["Fatigue"])+" instances of extreme fatigue, and "+str(events["Sweats"])+" instances of cold sweats.\n\nYou had 4 more events this week than last week. Consider speaking to your doctor. You can sync this data directly with your personal health record by clicking the button below.\n\n***Sync Button***\n") 
 
if __name__ == "__main__":
    csv_path = "testdata.csv"
    with open(csv_path, "rb") as data_file:
        checker(data_file)
