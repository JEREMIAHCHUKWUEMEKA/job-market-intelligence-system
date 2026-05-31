import pandas as pd
import re
from bs4 import BeautifulSoup


class JobCleaner:

    def remove_html(self, text):
        if pd.isna(text):
            return ""

        return BeautifulSoup(text, "html.parser").get_text(separator=" ")

    def clean_salary(self, salary):
        if pd.isna(salary):
            return None

        salary = str(salary).strip()

        if salary == "":
            return None

        return salary

    def normalize_location(self, location):
        if pd.isna(location):
            return "Unknown"

        location = location.strip()

        location_map = {
            "Worldwide": "Remote",
            "Anywhere": "Remote",
            "Remote": "Remote"
        }

        return location_map.get(location, location)

    def clean_dataframe(self, df):

        df = df.copy()

        # Remove duplicates
        df.drop_duplicates(
            subset=["job_id"],
            inplace=True
        )

        # Clean descriptions
        df["description"] = df["description"].apply(
            self.remove_html
        )

        # Clean salary
        df["salary"] = df["salary"].apply(
            self.clean_salary
        )

        # Normalize location
        df["location"] = df["location"].apply(
            self.normalize_location
        )

        # Parse publication date
        df["publication_date"] = pd.to_datetime(
            df["publication_date"],
            errors="coerce"
        )

        return df