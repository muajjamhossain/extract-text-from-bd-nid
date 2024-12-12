import easyocr

IMAGE_PATH = 'nid_2.jpg'

reader = easyocr.Reader(['en', 'bn'], gpu=True)

result = reader.readtext(IMAGE_PATH)

text = []

with open("nid.txt", 'w', encoding='utf-8') as f:
    for detection in result:
        detected_text = detection[1]
        text.append(detected_text)
        f.write(detected_text)
        f.write('\n')
        print(detected_text)
