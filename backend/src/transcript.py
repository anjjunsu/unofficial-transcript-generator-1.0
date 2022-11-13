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

    def __str__(self) -> str:
        s: str = "=======================================\n" \
            + f"=== Transcript ===\n" \
            + f"{self.school_name}\n" \
            + f"Surname: {self.school_name}, Given name: {self.student_given_name}\n" \
            + f"Student #: {self.student_number}\n" \
            + f"Today: {self.today}\n" \

        for c in self.course_record_list:
            s += c.__str__()

        s += "=======================================\n"

        return s

    def sort_course_records_by_session(self) -> None:
        # Sort course list by session
        # Lower session number comes first, and 'S' comes first and 'W' comes last
        # Then, sort by term
        self.course_record_list.sort()
