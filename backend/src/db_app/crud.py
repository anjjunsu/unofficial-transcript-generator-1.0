from sqlalchemy.orm import Session
from . import models
import api_app


def get_total_requests(db: Session) -> float:
    instance = db.query(models.SystemSettings).with_for_update(of=models.SystemSettings).filter(
        models.SystemSettings.name == "Total Requests").first()

    if instance:
        db.commit()
        return instance.value
    else:
        instance = models.SystemSettings(name="Total Requests", value=0)
        db.add(instance)
        db.commit()
        return instance.value


def increment_total_requests(db: Session):
    instance = db.query(models.SystemSettings).with_for_update(of=models.SystemSettings).filter(
        models.SystemSettings.name == "Total Requests").first()

    if instance:
        instance.value += 1
    else:
        instance = models.SystemSettings(name="Total Requests", value=1)
        db.add(instance)

    db.commit()


def insert_course_info(db: Session, code: str, name: str):
    instance = db.query(models.Course).with_for_update(
        of=models.Course).filter(models.Course.code == code).first()

    if not instance:
        db_course = models.Course(code=code, name=name, deleted=False)
        db.add(db_course)
        db.commit()
        print(f"[Info] New coure {code}: {name} is added to courses table\n")
    else:
        print(f"[Info] Coure {code}: {name} already exists in courses table\n")


def get_course_name(db: Session, code: str) -> str:
    instance = db.query(models.Course).filter(
        models.Course.code == code).first()

    if instance:
        return instance.name
    else:
        course_name = api_app.fetch_course_info_request(code)
        print("+++++")
        print(course_name)
        print("+++++")
        if course_name:
            insert_course_info(db, code, course_name)
            return course_name
