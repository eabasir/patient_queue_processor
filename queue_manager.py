queue = {}

def push(patient):

    if patient.national_code in queue:
        print(f"The patient is already in the queue")
        return

    queue[patient.national_code] = patient

def get_highest_priority():
    return sorted(queue.items(), key=lambda item: (-item[1].get_priority(), item[1].entrance_dt))[0][1]
    
def pop(id):
    if id not in queue:
        print("The id is not in the queue. cannot be dropped...")
        return
    
    print(f"The following patient will be popped off the queue: {queue[id]}")
    queue.pop(id)




