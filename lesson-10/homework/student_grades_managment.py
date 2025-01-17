import csv

def read_grades(file_name):
    """
    Reads the grades from the CSV file and returns a list of dictionaries.
    """
    grades = []
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            grades.append({"Name": row["Name"], "Subject": row["Subject"], "Grade": int(row["Grade"])});
    return grades

def calculate_average_grades(grades):
    """
    Calculates the average grade for each subject.
    """
    subject_totals = {}
    subject_counts = {}
    
    for entry in grades:
        subject = entry["Subject"]
        grade = entry["Grade"]
        if subject not in subject_totals:
            subject_totals[subject] = 0
            subject_counts[subject] = 0
        subject_totals[subject] += grade
        subject_counts[subject] += 1
    
    averages = {}
    for subject in subject_totals:
        averages[subject] = subject_totals[subject] / subject_counts[subject]
    return averages

def write_average_grades(file_name, averages):
    """
    Writes the average grades to a new CSV file.
    """
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Average Grade"])
        for subject, avg_grade in averages.items():
            writer.writerow([subject, round(avg_grade, 2)])

def main():
    # File names
    input_file = "grades.csv"
    output_file = "average_grades.csv"

    # Read, process, and write grades
    grades = read_grades(input_file)
    averages = calculate_average_grades(grades)
    write_average_grades(output_file, averages)

    print("Average grades have been calculated and written to average_grades.csv.")
if  __name__== "__main__":
    main()
