class ApplicationService:
    def __init__(self, jobs):
        self.jobs, self.applications = jobs, []
        
    def submit(self, job_id, name, email, resume_url):
        self.jobs.get(job_id)
        if any(a["job_id"] == job_id and a["email"] == email for a in self.applications):
            raise ValueError("Application already submitted")
        
        application = {"id": f"APP-{len(self.applications)+1:04}", "job_id": job_id, "name": name, "email": email, "resume_url": resume_url, "status": "received"}
        self.applications.append(application)
        return application
    
# Done