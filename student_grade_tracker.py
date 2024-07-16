def calculate_average(grades):
  """Calculates the average of a list of grades."""
  return sum(grades) / len(grades)

def calculate_letter_grade(average):
  """Calculates the letter grade based on the average."""
  if average >= 90:
    return 'A'
  elif average >= 80:
    return 'B'
  elif average >= 70:
    return 'C'
  elif average >= 60:
    return 'D'
  else:
    return 'F'

def main():
  student_name = input("Enter student's name: ")
  num_subjects = int(input("Enter number of subjects: "))
  grades = []

  for i in range(num_subjects):
    subject_name = input(f"Enter subject {i+1} name: ")
    grade = float(input(f"Enter grade for {subject_name} (Out of 100): "))
    grades.append(grade)

  average_grade = calculate_average(grades)
  letter_grade = calculate_letter_grade(average_grade)

  print(f"\nStudent Name: {student_name}")
  print(f"Average Grade: {average_grade:.2f}")
  print(f"Overall Grade: {average_grade:.2f}") 
  # Here , Overall grade and Average grade are same because all subjects have equal weight.
  print(f"Letter Grade: {letter_grade}")

if __name__ == "__main__":
  main()