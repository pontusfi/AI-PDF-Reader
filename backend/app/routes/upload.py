from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.pdf_service import pdf_text_extraction

router = APIRouter()


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    
    # Validate file type
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    try:
        # Extract text from PDF
        extracted_text = pdf_text_extraction(file.file)

        return {
            "filename": file.filename,
            "content": extracted_text
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"PDF processing failed: {str(e)}"
        )