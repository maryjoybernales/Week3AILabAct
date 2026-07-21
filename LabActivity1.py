print("Aliah's Interactive Library Kiosk")
def check_borrowing(overdue_books, status):
    if overdue_books:
        return "Not allowed: overdue books"
    elif status == "suspended":
        return "Not allowed: suspended account"
    else:
        return "Borrowing allowed"


students_allowed = 0

while True:
    name = input("Enter student name (or 'exit' to stop): ").strip()

    if name.lower() == "exit":
        break

    overdue_input = input("Do you have overdue books? (yes/no): ").strip().lower()
    status = input("Enter your status (active/suspended): ").strip().lower()
    books = int(input("How many books do you want to borrow? "))

    overdue_books = overdue_input == "yes"

    result = check_borrowing(overdue_books, status)
    print(result)

    if result == "Borrowing allowed":

        if books <=0:
            print("Error: Please enter a number greater than 0.")

        elif books > 3:
            print("You can only borrow up to 3 books.")
            print("Borrowing approved for 3 books.")
            students_allowed += 1

        else:
            print("Borrowing approved for", books, "book(s).")
            students_allowed += 1

    print()
print("Total students allowed to borrow books:", students_allowed)
