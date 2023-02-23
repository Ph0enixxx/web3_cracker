import cv2
from PIL import ImageGrab
import numpy as np
import pyautogui
 
def match_template_via_cv2_in_screenshot(path_to_template, threshold=0.9):
    # Get the screenshot
    screenshot = ImageGrab.grab()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)
 
    # Load the template
    template = cv2.imread(path_to_template)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2RGB)
 
    # Match the template
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    (yCoords, xCoords) = np.where(result >= threshold)
    print(yCoords, xCoords)
    for i in range(len(yCoords.tolist())):
        cv2.rectangle(screenshot, (xCoords[i], yCoords[i]), (xCoords[i]+template.shape[1], yCoords[i]+template.shape[0]), (0, 0, 255), 2)
    # # Get the top left position of the matched area
    # top_left = max_loc
    # # Get the bottom right position of the matched area
    # bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
 
    # # Draw a rectangle around the matched area
    # print(top_left, bottom_right)
    # cv2.rectangle(screenshot, top_left, bottom_right, (0, 0, 255), 2)
 
    # Display the screenshot with the rectangle around the matched area
    cv2.imshow('Matches', screenshot)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

match_template_via_cv2_in_screenshot('assets/chrome/test.png')