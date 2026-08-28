import pickle
import os

DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(DIR, "students.pkl")

if os.path.exists(DATABASE):
    try:
        with open(DATABASE, "rb") as file:
            db = pickle.load(file)
            # make sure is dict
            if not isinstance(db, dict):
                db = {}
    except Exception:
        db = {}
else:
    db = {}

def save_data():
    with open(DATABASE, "wb") as file:
        pickle.dump(db, file)
    

while True:
    print(f"\n------ STUDENTS REPORT---------\n")
    print(f"1. Add student score")
    print(f"2. See last students scores")
    print(f"3. See students score resume and promovation status")
    print(f"4. Exit program")

    option = input(f"Choose option (1-4): ").strip()

    if option == "1":
        while True:
            student = input(f"Insert student name: ").strip().title()
            if not student:
                print(f"Student name missing!\n")
                continue
            if not student.replace(" ", "").isalpha():
                print(f"Student name can only contain letters!\n")
                continue
            break

        while True:
            discipline = input(f"Insert student discipline: ").strip().capitalize()
            if not discipline:
                print(f"Student discipline missing!\n")
                continue

            if not discipline.replace(" ", "").isalpha():
                print(f"Discipline must contain only letters!\n")
                continue
            break


        while True:
            raw_score = input(f"Insert student score: ").strip()
            if not raw_score:
                print(f"Student score is missing!\n")
                continue
            if raw_score.isdigit():
                score = int(raw_score)
                                
   

                if 1 <= score <= 10:
                    resume = (discipline, score)

                    if student not in db:
                        db[student] = []
                
                    db[student].append(resume)
                    save_data()

                    print(f"You added student: {student} |Discipline: {discipline} | Score: {score}")
                    break
                else:
                    print(f"Score must be between 1 to 10!\n")

            else:
                print(f"Invalid score!\n")


    elif option == "2":
        while True:
            student = input(f"Insert student name to see last scores: \n").strip()
            if not student:
                print(f"Student name is missing!\n")
                continue

            if not student.replace(" ", "").isalpha():
                print(f"Student name can only contain letters!\n")
                continue

            break

        if student not in db:
            print(f"Student {student} does not exist in students records database!\n")
            db[student] = []

        while True:
            choice = input(f"How many of last student {student} score you wish to view: \n").strip()
            if not choice:
                print(f"Answer is missing!\n")
                continue

            if not choice.isdigit() or not (1 <= int(choice) <= 10):
                print(f"Answer must be a positive number between 1 and 10!\n")
                continue
            

            number = int(choice)
            break


        all_scores = db[student]

        if not all_scores:
            print(f"Student {student} does not have disciplines records!\n")

        else:

            last_scores = all_scores[-number:]

            for discipline, score in last_scores:
                print(f"Student: {student} | Discipline: {discipline} | Score: {score}")


    elif option == "3":
        if not db:
            print(f"Students scores not aavailable!\n")
        

        else:
            print(f"------------SCHOOL RESULTS STUDENTS RESUME-------------")

            for stud, statistic in db.items():
                if len(statistic) > 0:
                    sum = 0
                    for item in statistic:
                        discipline, score = item
                        sum += score

                    average = sum / len(statistic)

                    status = "Promoted" if average > 5 else "Not promoted"

                    print(f"Student: {stud} | Discipline: {discipline} | Average Score: {average} | Status: {status}!")

                else:
                    print(f"Student {stud} does not have discipline records available!\n")

    elif option == "4":
        save_data()
        print(f"Exiting program...!\n")
        break

    else:
        print(f"Invalid Option!\n")
                

