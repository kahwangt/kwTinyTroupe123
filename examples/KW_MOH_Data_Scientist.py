"""
KW - MOH Data Scientist
Demonstrates loading KW and running a sample interaction around public health sentiment analysis.
"""

import sys
sys.path.insert(0, '..')

import tinytroupe
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld

# Load KW and apply the MOH health sentiment analyst fragment
kw = TinyPerson.load_specification("./agents/KW.agent.json")
kw + "./fragments/moh_health_sentiment_analyst.fragment.json"

print("=" * 60)
print("KW loaded. Starting interaction.\n")

# Simulate a policy briefing scenario
world = TinyWorld("MOH Policy Analysis Session", [kw])
world.make_everyone_accessible()

world.broadcast_internal_goal(
    "You are preparing to brief a senior policy officer on public sentiment "
    "towards Singapore's upcoming mental health awareness campaign. You have "
    "access to social media data, survey results, and past campaign engagement "
    "metrics. You will walk through your analysis from descriptive findings "
    "through to prescriptive recommendations."
)

# Ask KW to walk through his analytical approach
kw.listen(
    "KW, we're about to launch a new mental health awareness campaign. "
    "Can you walk me through how you would analyse public sentiment data "
    "to help us make this campaign as effective as possible? "
    "Please cover what data you would source and how you would approach "
    "descriptive, diagnostic, predictive, and prescriptive analysis."
)

world.run(2, parallelize=False)

print("\n" + "=" * 60)
print("KW's response:")
kw.pp_current_interactions()
