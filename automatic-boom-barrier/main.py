import cv2
import pytesseract
import time
import threading
import csv
import pandas

width = 800
height = 400

# Create a VideoCapture object to access the camera (index 0 by default camera)
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not open camera.")
    exit()

# Load the number plate detector
n_plate_detector = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")

# Configure Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

saved_letter = "0123456789ZXCVBNMASDFGHJKLQWERTYUIOP";

# Define the target plate
target_plate = "KLO7CP7235"

# Thread event to signal the gate opening
gate_event = threading.Event()

csv_filename = "detected_plates.csv"


def save_to_csv(data):
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def detect_plate(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    detections = n_plate_detector.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=7)

    detected_plates = []

    for (x, y, w, h) in detections:
        number_plate = gray[y:y + h, x:x + w]
        extracted_text = pytesseract.image_to_string(number_plate)
        plate = extracted_text.strip()

        string = plate
        new_string = ""
        for char in string:
            if char in saved_letter:
                new_string += char
        result = "".join(new_string)

        print("Detected Number Plate:", result)

        if result.upper() == target_plate:
            detected_plates.append((x, y, w, h))
            save_to_csv([time.strftime("%Y-%m-%d %H:%M:%S"), result.upper(), "Detected"])  # Save detected plate to CSV

    return detected_plates


def open_gate_thread():
    global gate_event
    while True:
        gate_event.wait()
        print("Gate opened")
        save_to_csv([time.strftime("%Y-%m-%d %H:%M:%S"), "Gate Opened"])  # Save gate opening event to CSV
        time.sleep(2)  # Keep the gate open for 2 seconds
        print("Gate closed")
        save_to_csv([time.strftime("%Y-%m-%d %H:%M:%S"), "Gate Closed"])  # Save gate closing event to CSV
        gate_event.clear()


gate_thread = threading.Thread(target=open_gate_thread)
gate_thread.daemon = True
gate_thread.start()

while True:
    ret, frame = camera.read()

    if not ret:
        print("Error reading frame.")
        break

    frame = cv2.resize(frame, (width, height))
    detected_plates = detect_plate(frame)

    for (x, y, w, h) in detected_plates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255),
                      2)  # Draw a blue rectangle around the detected plate
        save_to_csv([time.strftime("%Y-%m-%d %H:%M:%S"), "", "Plate Detected"])  # Save plate detection event to CSV

    cv2.imshow("Number plate detection", frame)

    # Check if the detected plates match the target plate
    if detected_plates:
        gate_event.set()

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()

user_input = input("Do you want to see the details of vehicle, type 'y' >> ")
if user_input == "y":
    data = pandas.read_csv("detected_plates.csv")
    print(data)