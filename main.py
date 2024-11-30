import pyautogui as auto  # type: ignore
from time import sleep

print("Welcome to PyAutoBruteForce!\n")
print("This tool is designed to automate the process of brute-forcing passwords.\n")
print("Please note that this tool is for educational purposes only and should not be used to attack systems.")

action_elements = int(input("Enter the number of elements (inputs, buttons and checkboxes): "))
delay_time = int(input("Enter delay duration (in seconds): "))

actionElementsPos = {}

def getMousePos():
    sleep(3)
    return auto.position()

def mouseClick(x, y):
    auto.leftClick(x, y)
    
def mousePaste(x, y, text):
    ...

def autoBruteForce():
    with open("usernames.csv", "r") as usernames, open("passwords.csv", "r") as passwords:
        username_list = usernames.read().splitlines()
        password_list = passwords.read().splitlines()
        keys = list(actionElementsPos.keys())

        for user in username_list:
            print(f"{keys[0]} : {actionElementsPos[keys[0]]}")
            for password in password_list:
                print("Password: "+ password)

for actionField in range(action_elements):
    actionFieldName = input(f"Enter a name for {actionField+1} element: ")

    while True:
        actionType = int(input("Enter 1 for Input or 2 for Button: "))
        if actionType in [1, 2]:
            break
        print("Invalid input. Please enter 1 or 2.")

    print(f"Place mouse pointer at {actionFieldName}")

    x, y = getMousePos()
    actionElementsPos[actionFieldName] = {"actionType": actionType, "x": x, "y": y}
    print(f"{actionFieldName} position: x={x} y={y}")

autoBruteForce()