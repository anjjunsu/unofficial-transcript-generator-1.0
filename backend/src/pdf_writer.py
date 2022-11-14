import os
from io import BytesIO
from typing import Final

from transcript import Transcript

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

from fastapi import Response

LEFT: Final = 0
MIDDLE: Final = 1
RIGHT: Final = 2
SPACE: Final = '\u00A0'
TWO_SPACE: Final = '\u00A0\u00A0'
TAB: Final = '\u00A0\u00A0\u00A0\u00A0'
SIX_TAB: Final = '\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0'


def generate_transcript_pdf(transcript: Transcript):
    # region PDF font registration
    pdfmetrics.registerFont(TTFont('Times New Roman', 'Times New Roman.ttf'))
    pdfmetrics.registerFont(
        TTFont('Times New Roman Bold', 'Times New Roman Bold.ttf'))
    pdfmetrics.registerFont(
        TTFont('Times New Roman Italic', 'Times New Roman Italic.ttf'))
    pdfmetrics.registerFont(
        TTFont('Times New Roman Bold Italic', 'Times New Roman Bold Italic.ttf'))

    addMapping('Times New Roman', 0, 0, 'Times New Roman')
    addMapping('Times New Roman', 0, 1, 'Times New Roman Italic')
    addMapping('Times New Roman', 1, 0, 'Times New Roman Bold')
    addMapping('Times New Roman', 1, 1, 'Times New Roman Bold Italic')
    # endregion

    file_name = f"UBCTranscript_{transcript.student_surname},{transcript.student_given_name}_{transcript.student_number}.pdf"

    # Holding a pdf in memory instaed of writing to disk
    #! Replace with buffer: for testing
    pdf = SimpleDocTemplate(
        filename=file_name,
        pagesize=A4,
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
    heading1_text: str = "TRANSCRIPT OF ACADEMIC RECORD"
    heading1_style = style_sheet['Heading1']
    heading1_style.fontName = 'Times New Roman Bold'
    heading1_style.fontWeight = 'bold'
    heading1_style.alignment = MIDDLE
    heading1 = Paragraph(heading1_text, heading1_style)
    flowables.append(heading1)
    # endregion

    # region Student Info
# "A <b>bold</b> word.<br /> An <i>italic</i> word."
    student_info_style = style_sheet['Normal']
    student_info_style.fontName = 'Times New Roman'
    student_info_style.fontSize = 12
    student_info_style.alignment = MIDDLE
    student_info_text: str = "<b>Surname:</b>" + TWO_SPACE + transcript.student_surname + SIX_TAB \
        + "<b>Given Name:</b>" + TWO_SPACE + transcript.student_given_name + SIX_TAB \
        + "<b>Student Number:</b>" + TWO_SPACE + transcript.student_number
    student_info = Paragraph(student_info_text, student_info_style)
    flowables.append(student_info)
    # endregion

    #! Remove: for testing
    # Save as file in disk
    pdf.build(
        flowables,
        onFirstPage=add_page_number,
        onLaterPages=add_page_number
    )
    print(f"[Info] PDF file saved to {file_name}")

    # Close the buffer! Important!
    # My cloud VM has the smallese RAM size I ever used so far.
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
