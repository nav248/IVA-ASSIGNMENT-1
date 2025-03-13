import cv2
import numpy as np

# Function to determine the color name based on RGB
def get_color_name(B, G, R):
    if R > 150 and G < 100 and B < 100:
        return "Red"
    elif B > 150 and G < 100 and R < 100:
        return "Blue"
    elif G > 150 and B < 100 and R < 100:
        return "Green"
    else:
        return "Unknown"

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define red color range
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Get the center pixel color
    h, w, _ = frame.shape
    center_x, center_y = w // 2, h // 2
    B, G, R = frame[center_y, center_x]

    color_name = get_color_name(B, G, R)

    # Display the color name
    cv2.putText(result, f"Color: {color_name}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("Webcam Color Detection", result)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
