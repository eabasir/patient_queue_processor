def get_command():
    menu = """
    1- Register patient
    2- Find patient with high priority
    3- Display all patient information
    4- Change status of patient
    5- Show number of patient in queue
    6- Exit
    """
    print(menu)
    return input('Enter the value: ')

def register_new_patient():
    pass

def find_highest_priority():
    pass

def display_all():
    pass

def change_patient_status():
    pass

def show_queue_size():
    pass

def end_program():
    print("Good luck! Bye...")
    exit()


commands = {
    "1": register_new_patient,
    "2": find_highest_priority,
    "3": display_all,
    "4": change_patient_status,
    "5": show_queue_size,
    "6": end_program
}



def main():
    code = get_command()
    while(code not in commands):
        print("You've entered an invalid number. Please choose one from the following list")
        code = get_command()

    commands[code]()
    main()
    


main()