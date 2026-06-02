def add_notes():
    note = input("Enter your note : ")
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
        print("Note added successfully")

def view_notes():
    try:
        with open("notes.txt","r") as f:
            print("\n Your notes :")
            print(f.read())

    except FileNotFoundError:
        print("No notes found : ")

def search_note():
    keyword = input("enter keyword :")

    try:
        with open("notes.txt" "r") as f:
            found = False

            for line in f:
                if keyword.lower() in line.lower():

                    if not found:
                        print("Note npt found : ")

    except FileNotFoundError:
        print("No notes found ")

while True:
    print("\n1 Add note")
    print("2. View Notes")
    print("3. Search Notes")
    print("4. exit")

    choice = input("Enter choice : ")

    if choice == "1":
        add_notes()

    elif choice == "2":
        view_notes()

    elif choice == "3":
        search_note()

    elif choice == "4":
       break

    else:
        print("invalid choice")


