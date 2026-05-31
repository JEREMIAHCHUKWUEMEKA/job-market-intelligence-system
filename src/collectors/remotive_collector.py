import requests
import pandas as pd


class RemotiveCollector:
    URL = "https://remotive.com/api/remote-jobs"

    def fetch_jobs(self):
        response = requests.get(self.URL)

        if response.status_code != 200:
            raise Exception(
                f"API Request Failed: {response.status_code}"
            )

        data = response.json()

        jobs = []

        for job in data["jobs"]:
            jobs.append({
                "job_id": job.get("id"),
                "job_title": job.get("title"),
                "company": job.get("company_name"),
                "location": job.get("candidate_required_location"),
                "salary": job.get("salary"),
                "job_type": job.get("job_type"),
                "category": job.get("category"),
                "publication_date": job.get("publication_date"),
                "description": job.get("description"),
                "url": job.get("url")
            })

        return pd.DataFrame(jobs)