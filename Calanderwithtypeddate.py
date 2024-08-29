import calendar
import os

# Function to display the calendar of a specific month and year
def display_calendar(year, month):
    print(calendar.month(year, month))

# Function to save a note for a specific date
def save_note_for_date(year, month, day, note):
    filename = f"notes_{year}_{month}_{day}.txt"
    with open(filename, 'w') as file:
        file.write(note)
    print(f"Note saved for {day}/{month}/{year}.")

# Function to retrieve a note for a specific date
def retrieve_note_for_date(year, month, day):
    filename = f"notes_{year}_{month}_{day}.txt"
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            note = file.read()
        print(f"Note for {day}/{month}/{year}: {note}")
    else:
        print(f"No note found for {day}/{month}/{year}.")

def main():
    # Get user input for year and month
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    
    # Display the calendar for the given month and year
    display_calendar(year, month)
    
    # Get user input for the date and action
    day = int(input("Enter day of the month: "))
    action = input("Do you want to (S)ave a note or (R)etrieve a note? ").strip().upper()
    
    if action == 'S':
        note = input("Enter your note: ")
        save_note_for_date(year, month, day, note)
    elif action == 'R':
        retrieve_note_for_date(year, month, day)
    else:
        print("Invalid action. Please enter 'S' to save or 'R' to retrieve.")

if __name__ == "__main__":
    main()
