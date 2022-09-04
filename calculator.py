def initialize():
    global current_value
    current_value = 0
    # Add memory and previous value = 0
    return current_value

def display_current_value():
    #print("Current Value:", current_value)
    #print(current_value)
    return current_value

def add(to_add):
    global current_value
    global previous_value
    previous_value = current_value
    current_value = current_value + to_add


def subtract(to_subtract):
    global current_value
    global previous_value
    previous_value = current_value
    current_value = current_value - to_subtract


def multiply(to_multiply):
    global current_value
    global previous_value
    previous_value = current_value
    current_value = current_value * to_multiply

def divide(to_divide): # Must make sure you are not dividing by 0
    global current_value
    global previous_value
    if to_divide == 0:
        print("ERROR")
        return None
    else:
        print("Dividing...")
        previous_value = current_value
        current_value = current_value / to_divide


def memory():
    global memory_value
    global current_value
    memory_value = current_value

def recall():
    global previous_value
    global current_value
    global memory_value
    memory_value = 0
    previous_value = current_value
    current_value = memory_value

def undo():
    global current_value
    global previous_value
    current_value, previous_value = previous_value, current_value

if __name__ == "__main__":
    current_value = 0
    print("Welcome to the calcultor program")
    display_current_value()
    print("Adding...")
    add(5)
    display_current_value()
    multiply(2)
    print("Multiplying...")
    display_current_value()
    divide(5)
    display_current_value()
    subtract(4)
    print("Subtracting...")
    display_current_value()
    print("\n")

#Problem 6
    current_value = 0
    memory()
    add(10)
    display_current_value
    recall()
    display_current_value()
    print("================")
    current_value = 0
    add(10)
    display_current_value()
    undo()
    display_current_value()
    undo()
    display_current_value()
    undo()
    display_current_value()