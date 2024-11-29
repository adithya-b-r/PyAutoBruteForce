import pyautogui as auto
from time import sleep

print("Welcome to PyAutoBruteForce!\n")
print("This tool is designed to automate the process of brute-forcing passwords.\n")
print("Please note that this tool is for educational purposes only and should not be used to attack systems")

total_fields = int(input("Enter the number of input fields: "))
action_elements = int(input("Enter the number of action elements (buttons and checkboxes): "))
delay_time = int(input("Enter delay duration (in seconds): "))

inputFieldsPos = {}
actionElementsPos = {}

def getMousePos():
  sleep(3)
  return auto.position()

for field in range(total_fields):
  inputFieldName = input(f"Enter a name for {field+1} input field: ")
  print(f"Place mouse pointer at {inputFieldName}")
  
  x, y = getMousePos()
  inputFieldsPos[inputFieldName] = {"x": x, "y": y}
  print(f"{inputFieldName} position: x={x} y={y}")
  
for actionField in range(action_elements):
  actionFieldName = input(f"Enter a name for {actionField+1} action element:")
  print(f"Place mouse pointer at {actionFieldName}")
  
  x, y = getMousePos()
  actionElementsPos[actionFieldName] = {"x": x, "y": y}
  print(f"{actionFieldName} position: x={x} y={y}")
  
