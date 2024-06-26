import os
import re

contacts = {

"Person1": 
{
    "Name":"Grant",
    "Phone Number": "972-375-4664",
    "Email Address": "grantbcopeland@gmail.com",
    "Company": "DJO",
    "Birthday": "12-24-1994",
    "Anniversary": "",
    "Group": "Friend"
}, 

"Person2": 
{
    "Name":"Grace",
    "Phone Number": "512-643-8127",
    "Email Address": "",
    "Company": "LandDev",
    "Birthday": "",
    "Anniversary": "",
    "Group": ""
}

}


def display_contacts():
    print("\nContact List:")
    for x, obj in contacts.items():
        print()
        for y in obj:
            print(y + ":", obj[y])

def display_contact(c):
    for x, obj in contacts.items():
        if contacts[x]["Name"].lower() == c.lower():
            for y in obj:
                print(y + ":", obj[y])

def display_info():
    for y in contacts["Person1"]:
        print(y)
            
def edit_contacts(c): #fix function bugs to return error messages properly (see delete funct)
    display_contact(c)
    for x, obj in contacts.items():
        if contacts[x]["Name"].lower() == c.lower():
            while True:
                b = input(f"Which of {c}'s contact information would you like to change?\n'Back' to return to contact selection. \n >> ")
                if b.lower() == "back":
                    break
                i=0
                for y in obj:
                    if y.lower() == b.lower():
                        i+=1
                        d = input(f"Enter information for {b.lower()}:\n >> ")
                        contacts[x][y] = d
                        if b.lower() == "name":
                            c = d
                        break
                if i == 0:
                    print("Input not recognized. Please try again.")
                print()
                display_contact(c)

def search():
    while True:
        print()
        display_info()
        j=0
        info = input("Which of the above options would you like to search for a contact by?\n'Back' to return home.\n >> ")
        if info.lower() == "back":
            break
        s = input("Input search criteria:\n'Back' to return home.\n >> ")
        if s.lower() == "back":
            break
        for x, obj in contacts.items():
            for y in obj:
                if obj[y].lower() == s.lower():
                    print(f"Match found for {obj[y]}!\n")
                    j+=1
                    name = contacts[x]["Name"]
                    display_contact(name)
                    break
        if j == 0:
            print("No matches found. Please try again.\n")
        r = input("Run again?\n >> ")
        if r.lower() != "yes":
            break

def add():
    print("Enter information for the following prompts. Enter blank if you have no information for that item.")
    name = input("Input name:\n >> ")
    pn = input("Input phone number:\n >> ")
    ea = input("Input email address: \n >> ")
    comp = input("Input company: \n >> ")
    bd = input("Input birthday: \n >> ")
    av = input("Input anniversary: \n >> ")
    g = input("Enter group (work, friend, family):\n >> ")

    for x in contacts.keys():
        k = int(x[6])
    
    contacts["Person"+(str(k+1))] = {
    
    "Name":name,
    "Phone Number": pn,
    "Email Address": ea,
    "Company": comp,
    "Birthday": bd,
    "Anniversary": av,
    "Group": g

    }
    display_contact(name)

def delete():
    while True:
        v=0
        de = input("Enter the name of the contact to remove or enter 'display' to view contact list.\n'Back' to return home. \n >> ")
        if de.lower() == "display":
            display_contacts()
            v+=1
        if de.lower() == "back":
            break
        for x, obj in contacts.items():
            z=0
            if contacts[x]["Name"].lower() == de.lower():
                z+=1
                break
        if z==1:
            contacts.pop(x)
            display_contacts()
            r = input("Run again?\n >> ")
            if r.lower() != "yes":
                v+=1
                break
        if v==0:
            print("No match found for name to delete.")

def export():
    f = open("Export.txt", "w")
    f.write("*Exported contacts:*\n")

    with open("Export.txt", "a") as f:
        for x, obj in contacts.items():
            f.write("\n")
            for y in obj:
                f.write('%s:%s\n' % (y, obj[y]))

    q = input("Read and display exported file?\n >> ")
    if q.lower() == "yes":
        f = open("Export.txt", "r")
        print(f.read())

def import_file():

    e = [" "]
    while True:
        try:
            imp = input("Enter a file to import contact info from:\n >> ")
            f = open(imp, "r")
            if f.name.lower() == 'corrupt.txt':
                raise Exception
        except FileNotFoundError:
            print("Error. File not found. Please try again.")
        except Exception:
            print("Error! Corrupt file!")
        else:
            print(f"Importing data from {imp}.")
            break
        
    
    for line in f:

        name = re.findall(r"Name: (.*?);", line)
        if name == []:
            name = e
        pn = re.findall(r"Phone Number: ([0-9]{3}+[-]+[0-9]{3}+[-]+[0-9]{4});", line)
        if pn == []:
            pn = e
        ea = re.findall(r"Email Address: ([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,});", line)
        if ea == []:
            ea = e
        comp = re.findall(r"Company: (.*?);", line)
        if comp == []:
            comp = e
        bd = re.findall(r"Birthday: ([0-9]{2}+[/|-]+[0-9]{2}+[/|-]+[0-9]{4});", line)
        if bd == []:
            bd = e
        av = re.findall(r"Anniversary: ([0-9]{2}+[/|-]+[0-9]{2}+[/|-]+[0-9]{4});", line)
        if av == []:
            av = e
        g = re.findall(r"Group: (.*?);", line)
        if g == []:
            g = e

        for x in contacts.keys():
            k = int(x[6])

        
        contacts["Person"+(str(k+1))] = {

        "Name": name[0],
        "Phone Number": pn[0],
        "Email Address": ea[0],
        "Company": comp[0],
        "Birthday": bd[0],
        "Anniversary": av[0],
        "Group": g[0]
        }

    print("\nContact List:")
    for x, obj in contacts.items():
        print()
        for y in obj:
            print(y + ":", obj[y])

while True:
    try:
        display = input("\n Welcome to the Contact Management System! \n Menu: \n 1. Add a new contact \n 2. Edit an existing contact \n 3. Delete a contact \n 4. Search for a contact \n 5. Display all contacts \n 6. Export all contacts to a text file \n 7. Import contacts from a text file \n 8. Quit \n Please input from the menu above with a number or action: \n >> ")
    
    except ValueError:
        print("Input not recognized. Please try again.")
   

    if display == "1" or display.lower() == "add" or display.lower() == "add a new contact":
        add()
    elif display == "2" or display.lower() == "edit" or display.lower() == "edit an existing contact": #fix function bugs to return error messages properly (see delete funct)
        while True:
            prompt = input("Enter the name of the contact to edit or enter 'display' to view contact list.\n'Back' to return home. \n >> ")
            e=0
            for x in contacts:
                if contacts[x]["Name"].lower() == prompt.lower():
                    edit_contacts(prompt)
                    e+=1
            if prompt.lower() == "display":
                display_contacts()
            elif e == 1:
                continue
            elif prompt.lower() == "back":
                break
            else:
                print("Input not recognized. Please try again.")
    elif display == "3" or display.lower() == "delete" or display.lower() == "delete a contact":
        delete()
    elif display == "4" or display.lower() == "search" or display.lower() == "search for a contact":
        search()
    elif display == "5" or display.lower() == "display" or display.lower() == "display all contacts":
        display_contacts()
    elif display == "6" or display.lower() == "export" or display.lower() == "export contacts to a text file":
        export()
    elif display == "7" or display.lower() == "import" or display.lower() == "import contats from a text file":
        import_file()
    elif display == "8" or display.lower() == "quit":
        print("Thank you for using the Contact Management System! Have a great day!")
        break
    else:
        print("Input not recognized. Please try again.")