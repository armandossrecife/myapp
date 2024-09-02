from app import dtos

def criar_job_DTO(job):
    job_DTO = dtos.JobDTO(
                task=job['task'], 
                start=job['start'], 
                finish=job['finish']
            )
    return job_DTO

def criar_registros_job_DTO(jobs):
    registros = []
    for job in jobs:
        job_DTO = criar_job_DTO(job)
        registros.append(job_DTO)
    return registros