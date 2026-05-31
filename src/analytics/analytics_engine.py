from collections import Counter


class AnalyticsEngine:

    def top_skills(self, skill_counts, top_n=10):
        return skill_counts.most_common(top_n)

    def top_companies(self, df, top_n=10):
        return (
            df["company"]
            .value_counts()
            .head(top_n)
        )

    def top_locations(self, df, top_n=10):
        return (
            df["location"]
            .value_counts()
            .head(top_n)
        )

    def top_categories(self, df, top_n=10):
        return (
            df["category"]
            .value_counts()
            .head(top_n)
        )

    def skill_cooccurrence(self, df):

        pair_counter = Counter()

        for skills in df["skills"]:

            skills = sorted(set(skills))

            for i in range(len(skills)):
                for j in range(i + 1, len(skills)):

                    pair = (
                        skills[i],
                        skills[j]
                    )

                    pair_counter[pair] += 1

        return pair_counter