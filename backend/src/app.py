from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Hello World"}


@app.post("/upload/file")
async def get_data(file: UploadFile = File(...)):
    tesseract_path = "/opt/homebrew/bin/tesseract"
    pytesseract.pytesseract.tesseract_cmd = tesseract_path

    print("====== File Meta Start =====")
    # print(file.filename)
    print(file.content_type)
    # print(type( file.file ))
    print("====== File Meta End =====")

    # Convert to image if uploaded file is a PDF
    file_type: str = file.content_type

    imgs = []

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
    # print(pytesseract.image_to_string(Image.open('test1.png')))
    for img in imgs:
        print(pytesseract.image_to_string(img))

    return {"file_name": "Testing..."}
