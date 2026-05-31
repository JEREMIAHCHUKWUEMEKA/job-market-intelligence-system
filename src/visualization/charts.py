import matplotlib.pyplot as plt
import os


class JobMarketVisualizer:

    def plot_top_skills(self, skill_counts, top_n=10):

        top_skills = skill_counts.most_common(top_n)

        skills = [skill for skill, _ in top_skills]
        counts = [count for _, count in top_skills]

        plt.figure(figsize=(10, 6))

        plt.bar(skills, counts)

        plt.title("Top Skills")
        plt.xlabel("Skills")
        plt.ylabel("Number of Jobs")

        plt.xticks(rotation=45)

        plt.tight_layout()

        os.makedirs(
        "data/analytics",
        exist_ok=True
        )

        plt.savefig(
            "data/analytics/top_skills.png"
        )

        plt.close()

    def plot_top_companies(self, companies):

        plt.figure(figsize=(10, 6))

        companies.plot(kind="bar")

        plt.title("Top Hiring Companies")
        plt.xlabel("Company")
        plt.ylabel("Number of Jobs")

        plt.tight_layout()

        os.makedirs(
        "data/analytics",
        exist_ok=True
        )

        plt.savefig(
            "data/analytics/top_companies.png"
        )

        plt.close()

    def plot_top_locations(self, locations):

        plt.figure(figsize=(10, 6))

        locations.plot(kind="bar")

        plt.title("Top Locations")
        plt.xlabel("Location")
        plt.ylabel("Number of Jobs")

        plt.tight_layout()

        os.makedirs(
        "data/analytics",
        exist_ok=True
        )

        plt.savefig(
            "data/analytics/top_locations.png"
        )

        plt.close()