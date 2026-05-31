from src.collectors.remotive_collector import RemotiveCollector
from src.processing.cleaner import JobCleaner
from src.processing.skill_extractor import SkillExtractor
from src.analytics.analytics_engine import AnalyticsEngine
from src.visualization.charts import JobMarketVisualizer
from src.analytics.experience_analyzer import ExperienceAnalyzer


collector = RemotiveCollector()
cleaner = JobCleaner()
extractor = SkillExtractor()
analytics = AnalyticsEngine()
visualizer = JobMarketVisualizer()
experience = ExperienceAnalyzer()

raw_df = collector.fetch_jobs()

clean_df = cleaner.clean_dataframe(raw_df)

skill_df = extractor.process_dataframe(clean_df)

skill_df = experience.analyze(
    skill_df
)

skill_df.to_csv(
    "data/jobs_with_skills.csv",
    index=False
)

skill_counts = extractor.get_skill_frequency(
    skill_df
)


print("\nTop Skills:\n")

for skill, count in skill_counts.most_common(10):
    print(f"{skill}: {count}")

    total_jobs = len(skill_df)

print("\nTop Skills (% of jobs)\n")

for skill, count in skill_counts.most_common(10):

    percentage = (count / total_jobs) * 100

    print(
        f"{skill}: {percentage:.1f}%"
    )

    print("\nTOP COMPANIES\n")

print(
    analytics.top_companies(skill_df)
)

print("\nTOP LOCATIONS\n")

print(
    analytics.top_locations(skill_df)
)

print("\nTOP CATEGORIES\n")

print(
    analytics.top_categories(skill_df)
)

cooccurrence = analytics.skill_cooccurrence(
    skill_df
)

print(
    "\nTOP TECHNOLOGY COMBINATIONS\n"
)

for pair, count in cooccurrence.most_common(10):

    print(
        f"{pair[0]} + {pair[1]}: {count}"
    )

    visualizer.plot_top_skills(
    skill_counts
)

visualizer.plot_top_companies(
    analytics.top_companies(skill_df)
)

visualizer.plot_top_locations(
    analytics.top_locations(skill_df)
)

print("\nEXPERIENCE LEVELS\n")

experience_summary = experience.summary(
    skill_df
)

for level, count in experience_summary.items():

    percentage = (
        count / len(skill_df)
    ) * 100

    print(
        f"{level}: {count} jobs ({percentage:.1f}%)"
    )

print("\nCharts Generated Successfully!")