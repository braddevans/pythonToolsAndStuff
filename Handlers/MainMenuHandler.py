from tabulate import tabulate

class MainMenuHandler():
    def __init__(self):
        pass

    def __repr__(self):
        return tabulate([['Product Management', 1], ['exit', 0]], headers=['Menu Options', 'Option Number'], tablefmt="outline")