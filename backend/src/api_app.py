import logging
import requests
import re


def fetch_course_info_request(course_code: str) -> str:
    if re.match(r"^[A-Z]{4} [0-9]{3}[A-Z]$", course_code):
        course_code = re.match(r"^[A-Z]{4} [0-9]{3}", course_code).group(0)

    formatted_code: str = course_code.replace(" ", "%20")
    ubc_explore_url: str = "https://ubcexplorer.io/getCourseInfo/" + formatted_code

    # Fetch course info to ubc explorer
    logging.info("Fetching course info for %s from ubc explorer", course_code)
    try:
        course_name: str = requests.get(ubc_explore_url).json()["name"]
    except:
        logging.warning(
            "Failed to fetch course info for %s from ubc explorer", course_code)
        return None

    logging.info(
        "Course name has been fetched from UBC Explorer: %s", course_name)

    return course_name
