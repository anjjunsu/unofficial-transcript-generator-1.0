from sqlalchemy.orm import Session
from . import models


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
    db_course = models.Course(code=code, name=name, deleted=False)
    db.add(db_course)
    db.commit()
