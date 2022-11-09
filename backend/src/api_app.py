import requests


def fetch_course_info_request(cousre_code: str) -> str:
    formatted_code: str = cousre_code.replace(" ", "%20")
    ubc_explore_url: str = "https://ubcexplorer.io/api/getCourseInfo/" + formatted_code

    # Fetch course info to ubc explorer
    print(f"[Info] Fetching course info for {cousre_code} from ubc explorer")
    course_name: str = requests.get(ubc_explore_url)
    print(course_name)
    print(f"[Info] Course name received: {course_name}")
