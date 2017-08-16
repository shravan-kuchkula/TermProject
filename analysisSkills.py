import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from diceSkillDAO import DiceSkillDAO

class AnalysisSkills:

    def __init__(self, list, country):

        #location, use country
        self._country = country

        # skills, use list of skills
        self._skillset = list

        # Pass the database object, jobType and location
        self.diceJobs = DiceSkillDAO(self._skillset, self._country)

    def displayBarPlot(self, dataFrame):
        # plot a bar plot
        sns.barplot(x="count", y="skill", data=dataFrame, orient="h")
        plt.xlabel("Number of jobs", fontsize=9)
        plt.ylabel("Skill", fontsize=9)
        plt.title("job count by skill")
        plt.yticks(fontsize=9)
        plt.xticks(fontsize=9)
        plt.show()

    def getJobsBySkill(self, barplot=True):

        print("Get jobs by skill")
        cursorDict = self.diceJobs.RetrieveJobTotal()

        df = pd.DataFrame({"skill": self._skillset, "count": cursorDict})
        df = df.sort(['count'], ascending=False)

        if barplot:
            self.displayBarPlot(df)
        else:
            print(df)

        return df
