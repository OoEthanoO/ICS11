student = int(input("How many students: "))
people_per_table = int(input("How many people per table: "))

tables = student // people_per_table + 1

print(f"You need {student} chairs and {tables} tables.")