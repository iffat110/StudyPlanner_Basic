import random
import pandas as pd
import calendar

def generate_study_schedule(name, num_subjects, hours_per_day, study_days_per_week, subjects_per_day, off_days):
    study_hours_per_subject_per_day = hours_per_day // subjects_per_day
    total_study_hours_per_subject_per_week = study_hours_per_subject_per_day * study_days_per_week

    subjects = [input(f"Enter the name of Subject {i}: ") for i in range(1, num_subjects + 1)]

    days_of_week = list(calendar.day_name)

    schedule_data = {'Day': [], 'Subjects': [], 'Study Hours Per Subject': []}

    for day in range(7):
        selected_subjects = random.sample(subjects, subjects_per_day)
        day_name = days_of_week[day % 7]
        if day_name in off_days:
            schedule_data['Day'].append(day_name)
            schedule_data['Subjects'].append('Rest')
            schedule_data['Study Hours Per Subject'].append('Rest')
        else:
            schedule_data['Day'].append(day_name)
            schedule_data['Subjects'].append(", ".join(selected_subjects))
            schedule_data['Study Hours Per Subject'].append(study_hours_per_subject_per_day)

    study_schedule_df = pd.DataFrame(schedule_data)

    # Print the study schedule table
    print(f"\nStudy Schedule for {name}:\n")
    print(study_schedule_df)

    print(f"\nTotal Study Hours per subject per week: {total_study_hours_per_subject_per_week:.2f} hours")
    return


def start():
    continue_play = True
    while continue_play:
        try:
            q1 = input("Enter Your Name: ")
            q2 = int(input("How many subjects you want to study: "))
            q3 = int(input("How many Hours you can study every day: "))
            q4 = int(input("How many days in a week you want to study: "))
            q5 = int(input("How many subjects you can study each day: "))
            q6 = int(input("Do you want any day off from the week (enter the number of days off, 0 to <= 7): "))

            if q4 == 0:
                new = input("Do you even want to study? (Yes/No): ").lower()
                if new == 'yes':
                    continue
                elif new == 'no':
                    continue_play = False
                else:
                    new = input('Invalid Input. Please enter "Yes" or "No": ').lower()
                    if new == 'yes':
                        continue
                    else:
                        continue_play = False
            else:
                off_days = []
                if 0 <= q4 <= 7 and 0 <= q6 <= 7 and q4 + q6 <= 7:
                    if q4 == 0:
                        print("You have chosen to take all days off. Do you want to study?")
                        new = input("(Yes/No): ").lower()
                        if new == 'yes':
                            continue
                        else:
                            continue_play = False
                    elif q6 == 0:
                        print("You have chosen to study every day. Happy studying!")
                        generate_study_schedule(q1, q2, q3, q4, q5, 0)
                    else:
                        print("Choose the days off (enter the day names, e.g., Monday, Tuesday, Wednesday, etc.): ")
                        for i in range(q6):
                            off_day_input = input(f"Day {i + 1}: ").strip().title()
                            try:
                                off_days.append(off_day_input)
                            except ValueError:
                                print(f"Invalid input for day {i + 1}. Please enter a valid day name. e.g. Monday, Tuesday")
                                continue
                else:
                    print("Invalid input. Please ensure the sum of study days and days off is less than or equal to 7.")
                    continue

                # Generate and display the study schedule using pandas
                generate_study_schedule(q1, q2, q3, q4, q5, off_days)

                q7 = input("Do you want to reschedule the routine? Yes/No: ").lower()
                if q7 == 'yes':
                    continue_play = True
                else:
                    print('Happy Study!')
                    continue_play = False

        except ValueError:
            print("Invalid input! Please enter a valid value.")


start()


