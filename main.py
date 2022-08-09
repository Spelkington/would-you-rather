import os
import yaml
import random
from surveysort.scenario import Scenario
from surveysort.quicksorter import QuickSorter

os.system("clear")

with open("config/sex_survey.yaml") as f:
    scenario_dict_list = yaml.load(f, yaml.SafeLoader)

# Scenarios
scenarios = [Scenario(e) for e in scenario_dict_list]

random.shuffle(scenarios)

# Initialize sorter
sorter = QuickSorter(
    scenarios,
    verbose=True
)
sorted = sorter.sort()
sorted.reverse()

Scenario.compile_list(sorted, "outputs/test.csv")