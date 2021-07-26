def getdate():
    import datetime
    return datetime.datetime.now()

def client():
    if pref == 1:
        with open(name + "Diet.txt", "a+") as f:
            a = input("Tell me what did " + name + " eat today?")
            date = str(getdate()) + " "
            f.write(date)
            f.write(a)
            f.write("\n")
            print("Your data has been successfully updated.")
        print("To show " + name + "'s Diet data press 1")
        try:
            x = int(input())
        except Exception as e:
            e = ValueError
            print("Entered the wrong key.")
            exit()
        if x == 1:
            retrieve(name , 1)
        else:
            exit()
    elif pref == 2:
        with open(name + "Exercise.txt", "a+") as f:
            a = input("Tell me what did " + name + " train today?")
            date = str(getdate()) + " "
            f.write(date)
            f.write(a)
            f.write("\n")
            print("Your data has been successfully updated.")
        print("To show " + name + "'s Exercise data press 1")
        try:
            x = int(input())
        except Exception as e:
            e = ValueError
            print("Entered the wrong key.")
            exit()
        if x == 1:
            retrieve(name , 2)
        else:
            exit()

def retrieve(name, pref):
    if pref == 1:
        with open(name + "Diet.txt") as f:
            print(f.read())
    if pref == 2:
        with open(name + "Exercise.txt") as f:
            print(f.read())

x = int(input("Press 0 to log data and 1 to retrieve data."))
name = input("Enter Client's name.")
name = name.capitalize()
pref = int(input("Enter \n 1 for Diet \n 2 for Exercise. \n"))
if x == 0:
    client()
if x == 1:
    retrieve(name, pref)
