import requests

url="http://127.0.0.1:8000/"
def show_menu():
    print('1. Add Students\n2. Fetch All Students\n3. Update Student\n4. Delete student\n5. Exit')

def show():
    id = input("Enter ID: ")
    name = input("Enter Name: ")
    stream = input("Enter Stream: ")
    return id,name,stream

def add_student():
    id,name,stream=show()
    response = requests.post(url+"create",
                             json={'id': id, 'name': name, 'stream': stream})
    print(response.content)


def update_student():
    id,name,stream=show()
    response = requests.put(url+"update",
                            json={'id': id, 'name': name, 'stream': stream})
    print(response.content)


def delete_student():
    id = input("Enter ID: ")
    response = requests.delete(url+"delete/{}".format(id)
                               )
    print(response.content)


def show_all():
    response = requests.get(url+"read")
    print(response.json())


while(1):
    print("\n")
    show_menu()
    choice = int(input("Enter Your Corresponding Choice\n "))
    if choice == 1:
        print("\n")
        add_student()
    elif choice == 2:
        print("\n")
        show_all()
    elif choice == 3:
        print("\n")
        update_student()
    elif choice == 4:
        print("\n")
        delete_student()
    elif choice == 5:
        break
    else:
        print("Invalid Choice")