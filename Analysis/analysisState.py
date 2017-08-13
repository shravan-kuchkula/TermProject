import pymongo
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from diceStateDAO import DiceStateDAO

class AnalysisState:

    def __init__(self, jobtype, location):

        self.jobtype = jobtype
        self.location = location

        # Get a handle to connection object
        connection = pymongo.MongoClient("mongodb://localhost")
        db = connection.jobs

        # Pass the database object, jobType and location
        self.diceJobs = DiceStateDAO(db, self.jobtype, self.location)


    def displayBarPlot(self, dataFrame):
        # plot a bar plot
        sns.barplot(x="JobCount", y="Company", data=dataFrame, orient="h")
        plt.xlabel("Number of jobs", fontsize=6)
        plt.ylabel("Companies", fontsize=6)
        plt.title("{} jobs in a 40 mile radius of {}".format(self.jobtype, self.location))
        plt.yticks(fontsize=6)
        plt.xticks(fontsize=6)
        plt.show()


    def retrieveAndStoreJobs(self):

        # Retrieve the jobs from dice API and store in mongodb.
        self.diceJobs.retrieveJobs()

        # Print the number of jobs inserted
        print("Retrieved {} jobs and stored them in MongoDB".format(self.diceJobs.countJobs()))

    def getTop20Companies(self, barplot=True):

        # Get the top 20 companies hiring the desired skill
        cursor = self.diceJobs.topCompanies()

        # Use pandas to create a dataframe
        df = pd.DataFrame(list(cursor))

        if barplot:
            self.displayBarPlot(df)
        else:
            print(df.to_string(index=False))

        return df
