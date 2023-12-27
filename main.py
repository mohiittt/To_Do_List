import os, time 

ToDoList = []

def add():
  time.sleep(1)
  os.system("clear")
  name = input("Task Name : ").lower()
  DueDate = input("Due Date : ")
  priority = input("Priority : ").lower()
  row = [name, DueDate, priority]
  ToDoList.append(row)
  print("Added")
  print()

def view():
  time.sleep(1)
  os.system("clear")
  options = input("1 : View All\n2 : By Priority\nChoose(1/2): ")
  if options == "1":
    for row in ToDoList:
      for item in row:
        print(item, end=" | ")
      print()
    print()
  elif options == "2":
    priority = input("What priority : ").lower()
    for row in ToDoList:
      if priority in row:
        for item in row:
          print(item, end=" | ")
        print()
    print()
  else:
    print("Please choose 1 or 2 ! ")
  time.sleep(1)

def edit():
  change = input("Name of the record to edit : ").lower()
  for row in ToDoList:
    if change in row:
      ToDoList.remove(row)
      name = input("Task Name : ").lower()
      DueDate = input("Due Date : ")
      priority = input("Priority : ").lower()
      row = [name, DueDate, priority]
      ToDoList.append(row)
      print("Added")
      print()
    else:
      print("Couldn't find the record")
  print()

def remove():
  time.sleep(1)
  os.system("clear")
  find = input("Record you want to remove : ").lower()
  for row in ToDoList:
    if find in row:
      ToDoList.remove(row)
      print("Record removed")
    else:
      print("No such record exist.")
  print()

while True:
  print("LIFE ORGANIZER")
  option = input("Welcome to your To Do List. \nDo you want to add, view, edit or remove in list : ").lower()
  if option == "add":
    add()
    print()
  elif option == "view":
    view()
    print()
  elif option == "edit":
    edit()
    print()
  else:
    remove()
    print()
  time.sleep(1)
  os.system("clear")