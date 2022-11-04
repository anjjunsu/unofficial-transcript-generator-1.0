from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import PyPDF2

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
    print(file.filename)
    print(file.content_type)
    print(type( file.file ))
    pdf = PyPDF2.PdfFileReader(file.file)
    print( pdf.documentInfo )
    print( pdf.numPages )
    print( "=== Let the page begin!!! ===" )
    print(pdf.getPage(0).extract_text )
    return { "file_name": file.filename }
