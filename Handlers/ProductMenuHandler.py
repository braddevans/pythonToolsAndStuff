from tabulate import tabulate


class ProductMenuHandler():
    def __init__(self, dcm):
        self.dcm = dcm

        self.defaultlist = [['Return to Main Menu', 0],['PRINT products list', 1],['CREATE new product', 2],['UPDATE existing product', 3],['DELETE product', 4]]
        self.prodictlist = []
        self.kvdict = {}
        print(tabulate(self.defaultlist, headers=['Menu Options', 'Option Number'], tablefmt="outline"))

        # print(self.dcm.getDB())
        for item in self.dcm.getDB()["products"]:
            index = self.dcm.getDB()["products"].index(item)
            index += 1
            self.kvdict[index] = item
            # print(f"Adding: k:{index}, v:{item}")
            self.prodictlist.append([item, index])

        self.open_menu(int(input("please input your product option: ")))


    def open_menu(self, _input):
        if _input == 4:
            # STRETCH GOAL - DELETE product
            # PRINT products list
            # GET user input for product index value
            # DELETE product at index in products list
            self.recreate_list()
            print(tabulate(self.prodictlist, headers=['Menu Options', 'Option Number'], tablefmt="outline"))
            self.remove_from_list(int(input("please input your product you want to delete: ")))
            print(tabulate(self.defaultlist, headers=['Menu Options', 'Option Number'], tablefmt="outline"))
            self.open_menu(int(input("please input your product option: ")))
            pass
        elif _input == 3:
            # STRETCH GOAL - UPDATE existing product
            # PRINT product names with its index value
            # GET user input for product index value
            # GET user input for new product name
            # UPDATE product name at index in products list
            self.recreate_list()
            print(tabulate(self.prodictlist, headers=['Menu Options', 'Option Number'], tablefmt="outline"))
            self.update_list(int(input("please input your updated product id: ")), input("please input your updated product name: "))
            print(tabulate(self.defaultlist, headers=['Menu Options', 'Option Number'], tablefmt="outline"))
            self.open_menu(int(input("please input your product option: ")))
            pass
        elif _input == 2:
            # CREATE new product
            # GET user input for product name
            # APPEND product name to products list
            self.add_to_list(input("please input your product name: "))
            print(tabulate(self.prodictlist, headers=['Menu Options', 'Option Number'], tablefmt="outline"))
            print(tabulate(self.defaultlist, headers=['Menu Options', 'Option Number'], tablefmt="outline"))
            self.open_menu(int(input("please input your product option: ")))
            pass
        elif _input == 1:
            # PRINT products list
            self.recreate_list()
            print(tabulate(self.prodictlist, headers=['Menu Options', 'Option Number'], tablefmt="outline"))
            print(tabulate(self.defaultlist, headers=['Menu Options', 'Option Number'], tablefmt="outline"))
            self.open_menu(int(input("please input your product option: ")))
        elif _input == 0:
            # RETURN to main menu
            return 0

    def add_to_list(self, item):
        self.dcm.getDB()["products"].append(item)
        self.dcm.writeFile()
        self.recreate_list()
        pass

    def update_list(self, index, item):
        self.dcm.getDB()["products"][index-1] = item
        self.dcm.writeFile()
        self.recreate_list()
        pass

    def remove_from_list(self, index):
        print(f"index: {index-1}, removedItem: {self.dcm.getDB()['products'][index-1]}")
        self.dcm.getDB()["products"].pop(index-1)
        self.dcm.writeFile()
        self.recreate_list()
        pass

    def recreate_list(self):
        self.prodictlist.clear()
        self.kvdict = {}
        # print(self.dcm.getDB())
        for item in self.dcm.getDB()["products"]:
            index = self.dcm.getDB()["products"].index(item)
            index += 1
            self.kvdict[index] = item
            # print(f"Adding: k:{index}, v:{item}")
            self.prodictlist.append([item, index])

    def __repr__(self):
        return 0
