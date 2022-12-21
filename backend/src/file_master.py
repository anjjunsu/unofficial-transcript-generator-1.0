import re
import logging
from fastapi import Response
from db_app import crud
from pdf_writer import generate_transcript_pdf
from sqlalchemy.orm import Session
from typing import List
from transcript import Transcript
from course_record import CourseRecord
from fastapi import UploadFile, File
from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes


async def handle_uploaded_file(db: Session, file: UploadFile = File(...)) -> Response:
    # tesseract_path= "/usr/bin/tesseract"  # Cloud VM dev env path
    tesseract_path = "/opt/homebrew/bin/tesseract"  # Mac dev env path
    pytesseract.pytesseract.tesseract_cmd = tesseract_path

    logging.info("[File Meta] File Name: %s | File Content Type: %s",
                 file.filename, file.content_type)

    imgs = []
    data: str = ""
    data_list: List[str] = []
    transcript = Transcript()

    # Convert to image if uploaded file is a PDF
    file_type: str = file.content_type
    if "pdf" in file_type:
        bytes = file.file.read()
        imgs = convert_from_bytes(bytes)
    # elif "image" in file_type:
    #    imgs.append(Image.open(file.file))
    else:
        #! TODO: Raise error, return 4xx response
        logging.warning("Invalid file type. Current file type: %s", type(imgs))

    logging.warning("Image has been opened")

    for img in imgs:
        data += pytesseract.image_to_string(img)

    data_list = data.splitlines()

    for data in data_list:
        if not data.strip():
            continue
        # If "Name:" is found, then the get substring after "Name:" to "."
        if "Name:" in data or "#:" in data:
            handle_personal_info(data=data, transcript=transcript)
            continue

        num_data: int = len(data.strip().split(" "))
        course_record: CourseRecord
        match num_data:
            case 11:
                course_record = handle_completed_coures(db=db, record=data)
            case 9:
                course_record = handle_pass_fail_course(db=db, record=data)
            case 7:
                course_record = handle_in_progress_coures(db=db, record=data)
            case _:
                continue

        if course_record:
            transcript.course_record_list.append(course_record)

    transcript.sort_course_records_by_session()
    logging.info(transcript)

    return generate_transcript_pdf(transcript)


def handle_personal_info(data: str, transcript: Transcript):

    logging.info("[Info] Handle personal info: %s", data)

    full_name = data.split("Name:")[1].split("#")[0].strip()

    # get surname and given name from full name
    surname: str = full_name.split(",")[0].strip()
    surname = re.sub("[^a-zA-Z]+", "", surname)
    transcript.student_surname = surname

    given_name: str = full_name.split(",")[1].strip()
    given_name = re.sub("[^a-zA-Z]+", "", given_name)
    transcript.student_given_name = given_name

    transcript.student_number = data.split(
        "#:")[1].strip().split(" ")[0].strip()
    logging.info("Student Surname: %s, Given Name: %s, Student #: %s",
                 transcript.student_surname, transcript.student_given_name, transcript.student_number)


def handle_completed_coures(db: Session, record: str) -> CourseRecord:
    course_record = CourseRecord()

    entries = record.strip().split(" ")

    # Combine of first and the second entry is the course code
    course_record.code = entries[0] + " " + entries[1]
    course_record.name = crud.get_course_name(
        db, course_record.code)
    course_record.section = entries[2]
    course_record.grade = entries[3]

    letter = entries[4]
    if len(letter) > 1 and letter[1] != "+":
        letter = letter[0] + "+"
    course_record.letter_grade = letter

    course_record.session = entries[5]
    course_record.term = entries[6]
    course_record.program = entries[7]
    course_record.year = entries[8]
    course_record.credits = entries[9]
    course_record.class_average = entries[10]

    return course_record


def handle_pass_fail_course(db: Session, record: str) -> CourseRecord:
    course_record = CourseRecord()

    entries = record.strip().split(" ")

    course_record.code = entries[0] + " " + entries[1]
    course_record.name = crud.get_course_name(db, course_record.code)
    course_record.section = entries[2]
    course_record.session = entries[3]
    course_record.program = entries[4]
    course_record.year = entries[5]
    course_record.credits = entries[7]
    course_record.grade = entries[8]

    return course_record


def handle_in_progress_coures(db: Session, record: str) -> CourseRecord:
    course_record = CourseRecord()

    entries = record.strip().split(" ")

    course_record.code = entries[0] + " " + entries[1]
    course_record.name = crud.get_course_name(db, course_record.code)
    course_record.section = entries[2]
    course_record.session = entries[3]
    course_record.term = entries[4]
    course_record.program = entries[5]
    course_record.year = entries[6]

    return course_record
