class CourseRecord:
    def __init__(self) -> None:
        self.code: str = "N/A"
        self.section: str = "N/A"
        self.grade: str = "N/A"
        self.letter_grade: str = "N/A"
        self.session: str = "N/A"
        self.term: str = "N/A"
        self.program: str = "N/A"
        self.year: str = "N/A"
        self.credits: str = "N/A"
        self.class_average: str = "N/A"

    def __str__(self) -> str:
        s: str = "-----------------------------------------------------\n" \
            + f"| code: {self.code} | section: {self.section} |" \
            + f"grade: {self.grade} | letter grade: {self.letter_grade} |" \
            + f"session: {self.session} | term: {self.term} | " \
            + f"program: {self.program} | year: {self.year} | " \
            + f"credits: {self.credits} | class average: {self.class_average} |\n" \
            + "-----------------------------------------------------\n"
        return s
