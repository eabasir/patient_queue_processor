import queue_manager
from patient import Patient
from utils.status import PATIENT_STATUS

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
    name = input("Enter the first name: ")
    surname = input("Enter the surname: ")
    national_code = input("Enter the national code: ")
    disease = input("Enter the disease: ")
    patient = Patient(name, surname, national_code, disease)
    queue_manager.push(patient)


def find_highest_priority():
    highest = queue_manager.get_highest_priority()
    print(f"The patient with the highest priority is: {highest}")

def display_all():
    for key in queue_manager.queue:
        print(queue_manager.queue[key])

def change_patient_status():
    highest = queue_manager.get_highest_priority()
    inp = input(f"Enter the new status for {highest.name} {highest.surname} - {highest.national_code}: ")

    if inp == PATIENT_STATUS.BEDRID.value or inp == PATIENT_STATUS.DISCHARGE.value:
        queue_manager.pop(highest.national_code)
    elif inp == PATIENT_STATUS.REVISIT.value:
        new_disease = input("Enter the new disease for which the patient will be revisited")
        highest.set_new_disease(new_disease)
    else:
        print("Invalid status code")
        change_patient_status()





def show_queue_size():
    print(f"There are {len(queue_manager.queue)} patient(s) in the queue.")
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
    
if __name__ == '__main__':
    main()