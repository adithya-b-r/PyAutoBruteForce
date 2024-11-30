import pyautogui as auto #type: ignore
from time import sleep

print("Welcome to PyAutoBruteForce!\n")
print("This tool is designed to automate the process of brute-forcing passwords.\n")
print("Please note that this tool is for educational purposes only and should not be used to attack systems.")

with open("usernames.csv", "r") as users:
  print(users.read())

action_elements = int(input("Enter the number of elements (inputs, buttons and checkboxes): "))
delay_time = int(input("Enter delay duration (in seconds): "))

actionElementsPos = {}

def getMousePos():
  sleep(3)
  return auto.position()
  
for actionField in range(action_elements):
  actionFieldName = input(f"Enter a name for {actionField+1} action element:")
  actionType = int(input("Type Input[1] or Button[2]: "))
  print(f"Place mouse pointer at {actionFieldName}")
  
  x, y = getMousePos()
  actionElementsPos[actionFieldName] = {"actionType": actionType,"x": x, "y": y}
  print(f"{actionFieldName} position: x={x} y={y}")