import re
from db_app import crud
from sqlalchemy.orm import Session
from typing import List
from transcript import Transcript
from course_record import CourseRecord
from fastapi import UploadFile, File
from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes


async def handle_uploaded_file(db: Session, file: UploadFile = File(...)):
    tesseract_path = "/opt/homebrew/bin/tesseract"
    pytesseract.pytesseract.tesseract_cmd = tesseract_path

    print("[Info] ====== File Meta Info Start =====")
    print(file.filename)
    print(file.content_type)
    print(type(file.file))
    print("[Info] ====== File Meta Info End =====")

    imgs = []
    data: str = ""
    data_list: List[str] = []
    transcript = Transcript()

    # Convert to image if uploaded file is a PDF
    file_type: str = file.content_type
    if "pdf" in file_type:
        bytes = file.file.read()
        imgs = convert_from_bytes(bytes)
        print("+++++++++")
        print(type(imgs))
    # elif "image" in file_type:
    #    imgs.append(Image.open(file.file))
    else:
        #! TODO: Raise error, return 4xx response
        print("Invalid file type")

    print("Opend image")

    for img in imgs:
        data += pytesseract.image_to_string(img)

    # Remove
    print(data)

    data_list = data.splitlines()

    for data in data_list:
        if not data.strip():
            continue
        # If "Name:" is found, then the get substring after "Name:" to "."
        if "Name:" in data or "#:" in data:
            full_name = data.split("Name:")[1].split(".")[0].strip()
            # get surname and given name from full name
            transcript.student_surname = full_name.split(",")[0].strip()
            transcript.student_given_name = full_name.split(",")[1].strip()
            print(f"[Info] student surname: { transcript.student_surname }")
            print(
                f"[Info] student given name: { transcript.student_given_name }")

            transcript.student_number = data.split(
                "#:")[1].strip().split(" ")[0].strip()
            print(f"[Info] student number: { transcript.student_number }")

            continue

        num_data: int = len(data.strip().split(" "))
        course_record: CourseRecord
        # remove
        match num_data:
            case 11:
                print("Completed course")
                course_record = handle_completed_coures(db=db, record=data)
            case 9:
                continue
            case 7:
                continue
            case _:
                continue

        if course_record:
            transcript.course_record_list.append(course_record)

    print(transcript)


def handle_completed_coures(db: Session, record: str) -> CourseRecord:
    course_record = CourseRecord()

    entries = record.strip().split(" ")

    # Combine of first and the second entry is the course code
    course_record.course_code = entries[0] + " " + entries[1]
    course_record.course_name = crud.get_course_name(
        db, course_record.course_code)
    course_record.section = entries[2]


def handle_in_progress_coures(record: str) -> CourseRecord:
    pass
