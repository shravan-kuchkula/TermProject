import pymongo
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from diceCountryDAO import DiceCountryDAO

class AnalysisCountry:

    def __init__(self, jobtype, country):

        self.jobtype = jobtype
        self.country = country

        # Get a handle to connection object
        connection = pymongo.MongoClient("mongodb://localhost")
        db = connection.jobs

        # Pass the database object, job type, country
        self.diceJobs = DiceCountryDAO(db, self.jobtype, self.country)

    def displayBarPlot(self, dataFrame):
        # plot a bar plot
        sns.barplot(x="jobcount", y="state", data=dataFrame, orient="h")
        plt.xlabel("Number of jobs", fontsize=9)
        plt.ylabel("State", fontsize=9)
        plt.title("{} jobs in {} by state".format(self.jobtype, self.country))
        plt.yticks(fontsize=9)
        plt.xticks(fontsize=9)
        plt.show()

    def retrieveAndStoreJobs(self):

        self.diceJobs.retrieveJobs()

        # Print the number of jobs inserted
        print("Retrieved {} jobs and stored them in MongoDB".format(self.diceJobs.countJobs()))

    def getJobsByState(self, barplot=True):

        print("Group jobs by state and list top 20 states")
        cursor = self.diceJobs.topCompanies()

        # Use pandas to create a dataframe
        df = pd.DataFrame(list(cursor))
        print(df.values)

        if barplot:
            self.displayBarPlot(df)
        else:
            print(df.to_string(index=False))

        return df


    def getTopCompanyByState(self):

        print("Group jobs by state and company, display the top company per state")
        cursor = self.diceJobs.topCompanyWithinState()

        # Use pandas to create a dataframe
        df = pd.DataFrame(list(cursor))

        print(df.to_string(index=False))

        return df
