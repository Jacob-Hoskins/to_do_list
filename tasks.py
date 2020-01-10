#add task----------------------DONE
#mark task complete/delete-----
#see task----------------------DONE
#see number of task------------

#-------------GLOBAL VARS--------------
to_do = []

#--------------------------------------

def main_menu():
    print('''
Enter 'add' to add a task
Enter 'complete' to mark a task complete
Enter 'view' to view your to-do list
Enter 'length' to see how many things you have to do.

''')


def run_program():

    main_menu()

    def add(user_adding):
        global to_do

        to_do.append(user_adding)
        print(user_adding)
        main_menu()
        return user_adding


    def marking_complete(mark_comp):
        global to_do

        if mark_comp in to_do:
            print("That is in your list")
            #finds the index of your item
            to_do.remove(mark_comp)
            print(to_do)

        elif mark_comp not in to_do:
            print("That is not in your list")
            print(to_do)

        else:
            pass

        return mark_comp


    while True:

        user_input = input(">")

        if user_input.upper() == "ADD":
            print("What would you like to add to your list?\n>")
            user_adding = input(">")
            add(user_adding)

        elif user_input.upper() == "COMPLETE":
            mark_comp = input("What would you like to take off your to-do list")
            marking_complete(mark_comp)
            pass

        elif user_input.upper() == "VIEW":
            print(to_do)
            main_menu()

        elif user_input.upper() == "LENGTH":
            print(len(to_do))
            main_menu()

        else:
            print("I didnt understand, please try again")











run_program()