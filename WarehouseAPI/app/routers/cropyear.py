from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List
from fastapi import Form

from ..database import SessionLocal
from ..models import CropYear, Commoditymaster
from app.schemas import (GetCropYear)
from ..auth import get_current_user
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api", tags=["CropYear"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/GetCropYear", response_model=List[GetCropYear])
def get_questions(db: Session = Depends(get_db)):
    try:
        rows = db.query(CropYear).all()
        return rows
    except Exception as exc:
        logger.exception("Failed to fetch questions: %s", exc)
        return []