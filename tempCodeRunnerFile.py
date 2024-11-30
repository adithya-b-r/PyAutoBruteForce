import pyautogui as auto  # type: ignore
def mouseClick(x, y):
    auto.leftClick(x, y)
    
mouseClick(1400,100)