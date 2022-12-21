import logging
from file_master import handle_uploaded_file
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, UploadFile, File
from sqlalchemy.orm import Session
from db_app.database import SessionLocal, engine
from db_app import models, crud

OFFICIAL_TRANSCRIPT_FEE: float = 11.56

app = FastAPI()

# Logger
logging.basicConfig(filename='app.log', encoding='utf-8',
                    level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.info("Server started")

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/total-requests")
def read_total_requets(db: Session = Depends(get_db)):
    total_dollar_savings: float = crud.get_total_requests(
        db) * OFFICIAL_TRANSCRIPT_FEE

    return f"{total_dollar_savings:,.2f}"


@app.post("/upload/file")
async def get_data(db: Session = Depends(get_db), file: UploadFile = File(...)):
    crud.increment_total_requests(db)

    return await handle_uploaded_file(file=file, db=db)
