from collections import Counter
import pandas as pd


class SkillExtractor:

    SKILLS = [
        "Python",
        "Java",
        "JavaScript",
        "TypeScript",
        "React",
        "Angular",
        "Vue",
        "Node.js",
        "Express",
        "Django",
        "Flask",
        "FastAPI",
        "SQL",
        "PostgreSQL",
        "MySQL",
        "MongoDB",
        "Redis",
        "AWS",
        "Azure",
        "GCP",
        "Docker",
        "Kubernetes",
        "Terraform",
        "Git",
        "Linux",
        "TensorFlow",
        "PyTorch",
        "Pandas",
        "NumPy",
        "Spark",
        "Hadoop",
        "Machine Learning",
        "Deep Learning",
        "NLP"
    ]

    def extract_skills(self, text):

        if pd.isna(text):
            return []

        text = text.lower()

        found_skills = []

        for skill in self.SKILLS:
            if skill.lower() in text:
                found_skills.append(skill)

        return found_skills

    def process_dataframe(self, df):

        df = df.copy()

        df["skills"] = df["description"].apply(
            self.extract_skills
        )

        return df

    def get_skill_frequency(self, df):

        counter = Counter()

        for skills in df["skills"]:
            counter.update(skills)

        return counter