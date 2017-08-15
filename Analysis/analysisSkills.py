import pymongo
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from diceSkillDAO import DiceSkillDAO

class AnalysisSkills:

	def __init__(self, list, country):

		# location, use country
		self.country = country
		
		# skills, use list of skills
		self.skillset = list

		# Pass the database object, jobType and location
		self.diceJobs = DiceSkillDAO(self.skillset, self.country)   
    
	def displayBarPlot(self, dataFrame):
	    # plot a bar plot
		sns.barplot(x="job_total", y="skillset", data=dataFrame, orient="h")
		plt.xlabel("Number of jobs", fontsize=6)
		plt.ylabel("Skill", fontsize=6)
		plt.title("Jobs in the US by Skillset")
		plt.yticks(fontsize=6)
		plt.xticks(fontsize=6)
		plt.show()
        
	def getJobsBySkill(self, barplot=True):

		print("Group job by skill required")
		cursor = self.diceJobs
        
		# Use pandas to create a dataframe
		df = pd.DataFrame({"skillset":self.skillset,"job_total":cursor})
		print(df.values)

		if barplot:
			self.displayBarPlot(df)
		else:
			print(df.to_string(index=False))
        
		return df        