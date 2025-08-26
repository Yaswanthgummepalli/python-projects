 class Grocery:
    def __init__(self):
        self.list=[]

    def add(self,data):
        if data in self.list:
            print("already exist")
        else:
            self.list.append(data)
            print(self.list)

    def remove(self,data):
        if data in self.list:
            self.list.remove(data)
            print(self.list)
        else:
            print(f"{data}not exist")

    def view(self):
        print("milk")
        print("water")
        print("curd")
        print("oil")
        print("lemon")

    def exit(self):
        print("your list:",*self.list,sep=",")
if __name__=="__main__":
    g = Grocery()
    print("1.view menu")
    print("2.add")
    print("3.remove")
    print("4.exit")
    

    while True:
        print("choose your option")
        option = int(input("enter the number:"))
        if option == 1:
            g.view()
        elif option == 2:
            item = input("enter the item:")

            g.add(item)
        elif option == 3:
            item1 = input("enter the item:")
            g.remove(item1)
        else:
            g.exit()
            if option==4:
                break
    print("welcome again")
