import re
from typing import List
from transcript import Transcript
from course_record import CourseRecord
from fastapi import UploadFile, File
from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes


async def handle_uploaded_file(file: UploadFile = File(...)):
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

    for d in data_list:
        if not d.strip():
            continue
        # If "Name:" is found, then the get substring after "Name:" to "."
        if "Name:" in d or "#:" in d:
            full_name = d.split("Name:")[1].split(".")[0].strip()
            # get surname and given name from full name
            transcript.student_surname = full_name.split(",")[0].strip()
            transcript.student_given_name = full_name.split(",")[1].strip()
            print(f"[Info] student surname: { transcript.student_surname }")
            print(
                f"[Info] student given name: { transcript.student_given_name }")

            transcript.student_number = d.split(
                "#:")[1].strip().split(" ")[0].strip()
            print(f"[Info] student number: { transcript.student_number }")

            continue

        # regex to match course code
        # start with four alphabets, followed by a space, followed by three digits, and optional one alphabet
        # Then, extract the course code and course name
        #! TODO: Handle coures with p, and in progress
        if re.match(r"^[A-Z]{4} [0-9]{3}[A-Z]?", d):
            coures_record = CourseRecord()
            # get course code
            coures_record.code = re.search(
                r"^[A-Z]{4} [0-9]{3}[A-Z]?", d).group(0)

            print(f"[Info] course code: { coures_record.code }")

            print(d)
            # Remove course code from current line
            d = d.replace(coures_record.code, "").strip()

            print(d)
            # Next three characters are the course section
            coures_record.section = d[:3].strip()
            print(f"[Info] course section: { coures_record.section }")
            # Remove course section from current line
            d = d[3:].strip()

            print(d)
            # Next two characters are the course grade
            coures_record.grade = d[:2].strip()
            print(f"[Info] course grade: { coures_record.grade }")
            # Remove course grade from current line
            d = d[2:].strip()

            print(d)
            # Next one or two characters are the coures letter grade
            letter_grade = d[:2].strip()
            # Somethimes, postfix "+" is given as "t"
            # Replace "t" with "+"
            if len(letter_grade) == 2 and letter_grade[1] == "t":
                letter_grade = letter_grade[0] + "+"
            coures_record.letter_grade = letter_grade
            print(
                f"[Info] course letter grade: { coures_record.letter_grade }")
            # Remove course letter grade from current line
            d = d[2:].strip()

            print(d)
            # Start with four digits, followed by a alphabet, followed by a space, and followed by a digit is the course session and term
            session_term = re.search(
                r"^[0-9]{4}[A-Z] [0-9]", d).group(0)
            coures_record.session = session_term.split(" ")[0].strip()
            coures_record.term = session_term.split(" ")[1].strip()
            print(f"[Info] course session: { coures_record.session }")
            print(f"[Info] course term: { coures_record.term }")
            # Remove course session and term from current line
            d = d.replace(session_term, "").strip()
            print(d)
