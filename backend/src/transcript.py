from typing import List
from datetime import date
from course_record import CourseRecord


class Transcript:
    school_name: str = "The University of British Columbia"

    def __init__(self) -> None:
        self.student_surname: str = "N/A"
        self.student_given_name: str = "N/A"
        self.student_number: int = -1
        self.today: str = date.today().strftime("%b %d, %Y")
        self.course_record_list: List[CourseRecord] = []

    def sort_course_records_by_session(self) -> None:
        self.course_record_list.sort(key=lambda x: (x.year, -x.term))
