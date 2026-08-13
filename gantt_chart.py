from datetime import date

import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator

ACTIVITIES = [
    ("Topic selection and proposal",            date(2026, 5, 18), date(2026, 5, 27)),
    ("Ethics application and approval",         date(2026, 5, 25), date(2026, 6, 10)),
    ("Literature review",                       date(2026, 6, 1),  date(2026, 7, 5)),
    ("Dataset acquisition",                     date(2026, 6, 22), date(2026, 7, 5)),
    ("Data preparation and cleaning",           date(2026, 7, 5),  date(2026, 7, 20)),
    ("Exploratory data analysis",               date(2026, 7, 18), date(2026, 7, 28)),
    ("Model development and evaluation",        date(2026, 7, 26), date(2026, 8, 6)),
    ("Decision-support tool build and testing", date(2026, 8, 1),  date(2026, 8, 10)),
    ("Dissertation writing",                    date(2026, 7, 20), date(2026, 8, 15)),
    ("Review, corrections and submission",      date(2026, 8, 10), date(2026, 8, 17)),
]

fig, ax = plt.subplots(figsize=(12, 6))

# Put activity names on the y axis so labels never clip the bars.
labels = [name for name, _, _ in ACTIVITIES]
for i, (name, start, end) in enumerate(reversed(ACTIVITIES)):
    duration = (end - start).days
    ax.barh(i, duration, left=start, height=0.55,
            color="#4C72B0", edgecolor="black", alpha=0.9)

ax.set_yticks(range(len(ACTIVITIES)))
ax.set_yticklabels(list(reversed(labels)), fontsize=9)
ax.set_ylim(-0.5, len(ACTIVITIES) - 0.5)

ax.xaxis.set_major_locator(WeekdayLocator(byweekday=0))
ax.xaxis.set_major_formatter(DateFormatter("%d %b"))
ax.set_xlim(date(2026, 5, 15), date(2026, 8, 20))
plt.xticks(rotation=45, ha="right")

ax.set_title("Project Timeline, 18 May to 17 August 2026", fontsize=13, pad=15)
ax.set_xlabel("Week commencing")
ax.grid(axis="x", alpha=0.3)

ax.axvline(date(2026, 8, 17), color="red", linestyle="--", linewidth=1)
ax.text(date(2026, 8, 17), len(ACTIVITIES) - 0.4, " Submission",
        color="red", ha="left", va="top", fontsize=8)

plt.tight_layout()
plt.savefig("outputs/figures/gantt_chart.png", dpi=120, bbox_inches="tight")
print("Saved outputs/figures/gantt_chart.png")