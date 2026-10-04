from dataclasses import asdict, dataclass

@dataclass
class Job:
    id: int
    company: str
    title: str
    location: str
    
    def to_dict(self):
        return asdict(self)
    
class JobCatalog:
    def __init__(self):
        self.jobs = {101: Job(101, "Nova Labs", "Python Developer", "Remote")}
        
    def list(self):
        return list(self.jobs.values())
    
    def get(self, job_id):
        job = self.jobs.get(job_id)
        if not job:
            raise LookupError("Job not found")
        return job
    
# Done