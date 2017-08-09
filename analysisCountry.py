import pymongo
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from diceCountryDAO import DiceCountryDAO

def displayBarPlot(dataFrame):
    # plot a bar plot
    sns.barplot(x="JobCount", y="Company", data=dataFrame, orient="h")
    plt.xlabel("Number of jobs", fontsize=6)
    plt.ylabel("Companies", fontsize=6)
    plt.title("{} jobs in {}".format("Data Scientist", "US"))
    plt.yticks(fontsize=6)
    plt.xticks(fontsize=6)
    plt.show()

# Get a handle to connection object
connection = pymongo.MongoClient("mongodb://localhost")
db = connection.jobs

# Pass the connection object, job type, zipcode
diceJobs = DiceCountryDAO(db, "Data Scientist", "US")

# Retrieve the jobs from dice API and store in mongodb.
diceJobs.retrieveJobs()

# Get the top 20 companies hiring the desired skill
cursor = diceJobs.topCompanies()

# Use pandas to create a dataframe
df = pd.DataFrame(list(cursor))

# print the dataframe
print(df)

displayBarPlot(df)