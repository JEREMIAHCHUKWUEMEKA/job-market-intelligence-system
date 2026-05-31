from collections import Counter


class ExperienceAnalyzer:

    LEVELS = {
        "Junior": [
            "junior",
            "entry level",
            "graduate",
            "intern"
        ],

        "Mid": [
            "mid",
            "mid-level"
        ],

        "Senior": [
            "senior",
            "sr."
        ],

        "Lead": [
            "lead"
        ],

        "Staff": [
            "staff"
        ],

        "Principal": [
            "principal"
        ]
    }

    def detect_level(self, text):

        text = str(text).lower()

        for level, keywords in self.LEVELS.items():

            for keyword in keywords:

                if keyword in text:
                    return level

        return "Unknown"

    def analyze(self, df):

        levels = []

        for title in df["job_title"]:

            levels.append(
                self.detect_level(title)
            )

        df = df.copy()

        df["experience_level"] = levels

        return df

    def summary(self, df):

        return Counter(
            df["experience_level"]
        )