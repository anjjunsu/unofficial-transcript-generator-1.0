import requests
import re


def fetch_course_info_request(cousre_code: str) -> str:
    if re.match(r"^[A-Z]{4} [0-9]{3}[A-Z]$", cousre_code):
        cousre_code = re.match(r"^[A-Z]{4} [0-9]{3}", cousre_code).group(0)

    formatted_code: str = cousre_code.replace(" ", "%20")
    ubc_explore_url: str = "https://ubcexplorer.io/getCourseInfo/" + formatted_code

    # Fetch course info to ubc explorer
    print(f"[Info] Fetching course info for {cousre_code} from ubc explorer")
    try:
        course_name: str = requests.get(ubc_explore_url).json()["name"]
    except:
        print(f"[Error] Failed to fetch course info for {cousre_code}")
        return None

    print(course_name)
    print(f"[Info] Course name received: {course_name}")

    return course_name
