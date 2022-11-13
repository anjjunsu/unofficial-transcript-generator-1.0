import os
from io import BytesIO

from transcript import Transcript

from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
from reportlab.lib.pagesizes import A4

from fastapi import Response


def generate_transcript_pdf(transcript: Transcript):
    file_name = f"UBCTranscript_{transcript.student_surname},{transcript.student_given_name}_{transcript.student_number}.pdf"
    # register Times New Roman font
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

    canvas = Canvas(file_name, pagesize=A4)
    canvas.setFont('Times New Roman', 12)

    canvas.drawString(100, 100, "Hello World")
    print("[Info] Avaialble fonts: ", pdfmetrics.getRegisteredFontNames())

    # Convert canvas to bytes
    canvas.save()

    with open(file_name, "rb") as pf:
        buffer = BytesIO(pf.read())

    # Close the buffer! Important!
    # My cloud VM has the smallese RAM size I ever used so far.
    buffer.seek(0)
    pdf_bytes = buffer.getvalue()
    buffer.close()

    #! Uncomment it
    # os.remove(file_name)

    headers = {'Content-Disposition': 'attachment; filename="' + file_name + '"'}
    return Response(pdf_bytes, headers=headers, media_type="application/pdf")
