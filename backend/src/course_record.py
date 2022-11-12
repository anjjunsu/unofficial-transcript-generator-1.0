class CourseRecord:
    def __init__(self) -> None:
        self.code: str = ""
        self.name: str = ""
        self.section: str = ""
        self.grade: str = ""
        self.letter_grade: str = ""
        self.session: str = ""
        self.term: str = ""
        self.program: str = ""
        self.year: str = ""
        self.credits: str = ""
        self.class_average: str = ""

    def __str__(self) -> str:
        s: str = "-----------------------------------------------------\n" \
            + f"| code: {self.code} | name: {self.name} |section: {self.section} | " \
            + f"grade: {self.grade} | letter grade: {self.letter_grade} | " \
            + f"session: {self.session} | term: {self.term} | " \
            + f"program: {self.program} | year: {self.year} | " \
            + f"credits: {self.credits} | class average: {self.class_average} |\n" \
            + "-----------------------------------------------------\n"
        return s
