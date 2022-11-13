import os
from io import BytesIO
from reportlab.pdfgen.canvas import Canvas
from transcript import Transcript
from fastapi import Response


def generate_transcript_pdf(transcript: Transcript):
    file_name = f"UBCTranscript_{transcript.student_surname},{transcript.student_given_name}_{transcript.student_number}.pdf"
    canvas = Canvas(file_name)
    canvas.drawString(100, 100, "Hello World")

    # Convert canvas to bytes
    canvas.save()

    with open(file_name, "rb") as pf:
        buffer = BytesIO(pf.read())

    # Close the buffer! Important!
    # My cloud VM has the smallese RAM size I ever used so far.
    buffer.seek(0)
    pdf_bytes = buffer.getvalue()
    buffer.close()
    os.remove(file_name)

    headers = {f'Content-Disposition': 'attachment; filename="{file_name}"'}
    return Response(pdf_bytes, headers=headers, media_type="application/pdf")
