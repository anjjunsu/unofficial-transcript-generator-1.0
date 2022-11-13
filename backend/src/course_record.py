from functools import total_ordering


@total_ordering
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

    def __eq__(self, other):
        return self.session == other.session and self.term == other.term

    def __lt__(self, other):
        self_year: int = self.session[:4]
        self_season: str = self.session[4]
        self_term: str = self.term
        other_year: int = other.session[:4]
        other_season: str = other.session[4]
        other_term: str = other.term

        if self_year < other_year:
            return True
        elif self_year > other_year:
            return False
        else:
            if self_season > other_season:
                return False
            elif self_season < other_season:
                return True
            else:
                if self_term < other_term:
                    return True
                else:
                    return False
