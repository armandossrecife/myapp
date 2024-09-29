from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import banco
from app import seguranca
from app.processamento import jobs as processamento_jobs

router = APIRouter()

@router.get("/users/{user_id}/jobs", dependencies=[Depends(seguranca.get_current_user)])
async def get_user_jobs(user_id: int, db: Session = Depends(banco.get_db)):
    try: 
        user_dao = banco.UserDAO(db)
        user = user_dao.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        jobs = [
            {"task": "Job A", "start": "2009-01-01", "finish": "2009-02-28"},
            {"task": "Job B", "start": "2009-03-01", "finish": "2009-03-28"},
            {"task": "Job C", "start": "2009-04-01", "finish": "2009-04-28"},
            {"task": "Job D", "start": "2009-05-01", "finish": "2009-05-28"}
        ]

        jobs_DTO_exemplo = processamento_jobs.criar_registros_job_DTO(jobs)
        return jobs_DTO_exemplo

    except Exception as ex:
      raise HTTPException(status_code=500, detail=f"Internal server error. {str(ex)}")