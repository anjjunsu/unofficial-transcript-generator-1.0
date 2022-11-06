from fastapi import UploadFile, File
from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes


async def handle_uploaded_file(file: UploadFile = File(...)):
    tesseract_path = "/opt/homebrew/bin/tesseract"
    pytesseract.pytesseract.tesseract_cmd = tesseract_path

    print("====== File Meta Info Start =====")
    print(file.filename)
    print(file.content_type)
    print(type(file.file))
    print("====== File Meta Info End =====")

    imgs = []

    # Convert to image if uploaded file is a PDF
    file_type: str = file.content_type
    if "pdf" in file_type:
        bytes = file.file.read()
        imgs = convert_from_bytes(bytes)
        print("+++++++++")
        print(type(imgs))
    elif "image" in file_type:
        imgs.append(Image.open(file.file))
    else:
        print("Invalid file type")

    print("Opend image")

    for img in imgs:
        print(pytesseract.image_to_string(img))
