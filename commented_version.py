#add task----------------------DONE
#mark task complete/delete-----DONE
#see task----------------------DONE
#see number of task------------DONE

#-------------GLOBAL VARS--------------
#creates list, global is so it can be accessed inside and outside of the function
to_do = []

#--------------------------------------


#the menu fo the user to see the options they have to choose from
def main_menu():
    print('''
Enter 'add' to add a task
Enter 'complete' to mark a task complete
Enter 'view' to view your to-do list
Enter 'length' to see how many things you have to do.

''')


#run_program is used to help keep the code clean and see how the code runs
def run_program():

    #calls the main menu first thing when the program starts
    main_menu()

    #sets the function for when a user wants to add a task to the list
    def add(user_adding):
        #gets the to_do list
        global to_do

        #adds the users task to the list, and the end of the list
        to_do.append(user_adding)
        #shows the user what they added
        print(user_adding)
        #brings up the main menu for the user to see options again
        main_menu()
        return user_adding


    def marking_complete(mark_comp):
        global to_do

        #mark_comp is mark complete and it checks to see if the task the user wants to complete is in the list to_do
        if mark_comp in to_do:
            print("That is in your list")
            #finds the index of your item
            #removes the task from the list
            to_do.remove(mark_comp)
            #prints the list with the previous item deleted from it
            print(to_do)

        elif mark_comp not in to_do:
            print("That is not in your list")
            print(to_do)

        else:
            pass

        return mark_comp

    #loops so the user can keep choosing options from the menu
    while True:

        #main input from user
        user_input = input(">")

        #checks to see if the user wants to add a task to the list
        if user_input.upper() == "ADD":
            print("What would you like to add to your list?\n")
            user_adding = input(">")
            #calls the add task function
            add(user_adding)

        #calls to the function marking complete when the user wants to mark a item off the list
        #this method of calling back and structing the code like this is to keep it clean and easy to read
        #and when you have to go and fix a bug you know exactly where it is located
        elif user_input.upper() == "COMPLETE":
            mark_comp = input("What would you like to take off your to-do list")
            marking_complete(mark_comp)
            pass

        #lets user view list
        elif user_input.upper() == "VIEW":
            print(to_do)
            main_menu()

        #lets user see the length of their to do list
        elif user_input.upper() == "LENGTH":
            print(len(to_do))
            main_menu()

        else:
            print("I didnt understand, please try again")



#tells the program to run
run_program()