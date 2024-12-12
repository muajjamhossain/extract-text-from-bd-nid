import easyocr
from datetime import datetime

# Define the image path
IMAGE_PATH = 'nid_2.jpg'

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en', 'bn'], gpu=True)

# Perform text detection
result = reader.readtext(IMAGE_PATH)

# Initialize variables for storing text and name
text = []
user_name = None

# Parse the extracted text
for detection in result:
    detected_text = detection[1]
    text.append(detected_text)

    # Check for the name in the text (adjust if necessary based on actual format)
    if "Name" in detected_text or "নাম" in detected_text:
        try:
            user_name_index = result.index(detection) + 1  # Name is often the next line
            user_name = result[user_name_index][1].strip()
        except IndexError:
            pass

# Use a default name if no user name is detected
user_name = user_name if user_name else "user"

# Generate the file name with the current date
current_date = datetime.now().strftime('%d-%m-%y')
file_name = f"{user_name}-{current_date}.txt"

# Write the extracted text to the file
with open(file_name, 'w', encoding='utf-8') as f:
    for line in text:
        f.write(line)
        f.write('\n')

print(f"Text saved to {file_name}")
