from typing import Optional
import PyPDF2
from pydantic import BaseModel

class Option (BaseModel):
    FileName: str
    FileDesc: str
    FileType: Optional[str]
