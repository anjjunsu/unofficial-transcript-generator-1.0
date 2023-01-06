import os
import logging
from io import BytesIO
from typing import Final, List

from transcript import Transcript
from course_record import CourseRecord

from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle, Table, PageBreak
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
from reportlab.lib.pagesizes import A4, LETTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors

from fastapi import Response

LEFT: Final = 0
MIDDLE: Final = 1
RIGHT: Final = 2
SPACE: Final = '\u00A0'
TWO_SPACE: Final = '\u00A0\u00A0'
TAB: Final = '\u00A0\u00A0\u00A0\u00A0'
SIX_TAB: Final = '\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0'


def groupBySession(course_records: List[CourseRecord]) -> dict[str, List[List[str]]]:
    name_style = getSampleStyleSheet()['Normal']
    name_style.fontName = 'Times New Roman'
    name_style.fontSize = 11
    name_style.alignment = LEFT
    sessions = {}
    for course in course_records: 
        data = [
            course.term, 
            course.code, 
            Paragraph(course.name if course.name else course.code, name_style), 
            course.grade, 
            course.letter_grade, 
            course.credits,
            course.class_average
            ]
        if course.session not in sessions:
            sessions[course.session] = [data]
        else:
            sessions[course.session].append(data)
    return sessions


def toExplicitSession(session: str) -> str:
    
    if session[4] == 'W':
        year = int(session[0:4]) 
        return "Winter Session " + str(year) + " - " + str(year+1)
    elif session[4] == "S":
        year = int(session[0:4]) 
        return "Summer Session " + str(year)
    else:
        logging.warning("Invalid session info for: " + session)
        return ""


def generate_transcript_pdf(transcript: Transcript):
    # region PDF font registration
    pdfmetrics.registerFont(TTFont('Times New Roman', 'times.ttf'))
    pdfmetrics.registerFont(
        TTFont('Times New Roman Bold', 'timesbd.ttf'))
    #pdfmetrics.registerFont(
    #    TTFont('Times New Roman Italic', 'Times New Roman Italic.ttf'))
    #pdfmetrics.registerFont(
    #    TTFont('Times New Roman Bold Italic', 'Times New Roman Bold Italic.ttf'))
    addMapping('Times New Roman', 0, 0, 'Times New Roman')
    #addMapping('Times New Roman', 0, 1, 'Times New Roman Italic')
    addMapping('Times New Roman', 1, 0, 'Times New Roman Bold')
    #addMapping('Times New Roman', 1, 1, 'Times New Roman Bold Italic')
    # endregion

    file_name = f"UBCTranscript_{transcript.student_surname},{transcript.student_given_name}_{transcript.student_number}.pdf"

    # Holding a pdf in memory instaed of writing to disk
    #! Replace with buffer: for testing
    pdf = SimpleDocTemplate(
        filename=file_name,
        pagesize=LETTER,
        topMargin=10,
        leftMargin=10,
        rightMargin=10,
        bottomMargin=10
    )

    buffer = BytesIO()
    # pdf = SimpleDocTemplate(buffer, pagesize=A4)
    # pdf = SimpleDocTemplate(
    #     buffer,
    #     pagesize=A4,
    #     topMargin=10,
    #     leftMargin=10,
    #     rightMargin=10,
    #     bottomMargin=10
    # )
    flowables = []
    style_sheet = getSampleStyleSheet()

    # region Title
    heading1_text: str = "TRANSCRIPT OF" +"<br/>" + "ACADEMIC RECORD"
    heading1_style = style_sheet['Heading1']
    heading1_style.fontName = 'Times New Roman Bold'
    heading1_style.fontWeight = 'bold'
    heading1_style.alignment = MIDDLE
    heading1 = Paragraph(heading1_text, heading1_style)
    flowables.append(heading1)
    # endregion

    # region Student Info
# "A <b>bold</b> word.<br /> An <i>italic</i> word."
    logging.info("Printing Student Info")
    student_info_style = style_sheet['Normal']
    student_info_style.fontName = 'Times New Roman'
    student_info_style.fontSize = 11
    student_info_style.alignment = MIDDLE
    student_info_text: str = "<b>Surname:</b>" + TWO_SPACE + transcript.student_surname + SIX_TAB \
        + "<b>Given Name:</b>" + TWO_SPACE + transcript.student_given_name + SIX_TAB \
        + "<b>Student Number:</b>" + TWO_SPACE + transcript.student_number + "<br/> <br/>"
    student_info = Paragraph(student_info_text, student_info_style)
    flowables.append(student_info)
    logging.info("Done Student Info")
    # endregion

    # region Course Listing
    inner_table_header = ["Term", "Course", "Course Title", "%\nGrade", "Letter\nGrade", "Credit\nRec'd", "Class\nAvg"]

    inner_table_style = TableStyle(
        [
            ('FONT', (0,0), (6,0), 'Times New Roman Bold'),
            ('FONT', (0,1), (-1,-1), 'Times New Roman'),
            ('VALIGN', (0,0), (6,0), 'BOTTOM'),
            ('VALIGN', (0,1), (-1,-1), 'TOP')
        ]
    )

    table_style = TableStyle(
        [
            ('FONT', (0,0), (-1,0), 'Times New Roman Bold'),
            ('FONT', (1,0), (-1,-1), 'Times New Roman'),
            ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
            ('BOX', (0,0), (-1,-1), 0.25, colors.black),
        ]
    )

    logging.info("Parsing by course session")
    coursesBySession = groupBySession(transcript.course_record_list)

    logging.info("Printing Course Listing")
    

    for session in coursesBySession:
        explicitSession = toExplicitSession(session)
        course_data = coursesBySession[session]
        course_data.insert(0,inner_table_header)
        
        
        data_table = [
            [explicitSession],
            [Table(course_data, colWidths=(0.52*inch, 0.9*inch, 3.4*inch,0.52*inch,0.52*inch,0.52*inch,0.52*inch ), style=inner_table_style)]
        ]

        table = Table(data_table, colWidths=7*inch, style=table_style)

        flowables.append(table)
        
    # endregion


    #! Remove: for testing
    # Save as file in disk
    pdf.build(
        flowables,
        onFirstPage=add_page_number,
        onLaterPages=add_page_number
    )
    logging.info("PDF file saved to %s", file_name)

    # Close the buffer! Important!
    # My cloud VM has the smallest RAM size I ever used so far.
    buffer.seek(0)
    pdf_bytes = buffer.getvalue()
    buffer.close()

    #! Uncomment it
    # os.remove(file_name)

    headers = {'Content-Disposition': 'attachment; filename="' + file_name + '"'}
    return Response(pdf_bytes, headers=headers, media_type="application/pdf")


def add_page_number(canvas: Canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 9)
    page_num_text = "Page %d" % (doc.page)
    canvas.drawCentredString(
        20,
        20,
        page_num_text
    )
    canvas.restoreState()
