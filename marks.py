Maths = 0
Science = 0
Computers = 0
History = 0
Arts = 0
list = []
bool=True
while(bool):
    
    
    print("1:Input")
    print("2:Cal")
    print("3:Exit")
    
    def Input():
        global Maths, Science, Computers, History, Arts
        global list
        Maths = float(input("Enter The Marks In Mathematics ="))
        list.append(Maths)
        Science = float(input("Enter The Marks In Science ="))
        list.append(Science)
        Computers = float(input("Enter The Marks In Computers ="))
        list.append(Computers)
        History = float(input("Enter The Marks In History ="))
        list.append(History)
        Arts = float(input("Enter The Marks In Arts ="))
        list.append(Arts)
        display()


    def display():
        print("\n")
        print("Marks In Mathematics are :", Maths)
        print("Marks In Science are :", Science)
        print("Marks In Computers are :", Computers)
        print("Marks In History are :", History)
        print("Marks In Arts are :", Arts)
        print("\n")


    def cal():
        sum = 0
        for i in list:
            sum = sum + i
            percentage = sum / 5
        print(percentage)
    def out():
        global bool
        print("Exiting")
        bool=False
        exit()
    def boundary():
        print("Invalid Option,Please Enter the choice in Range ")


    dic = {

        1: Input,
        2: cal,
        3: out

    }
    choice = int(input("enter the choice"))
    dic.get(choice,boundary)()
