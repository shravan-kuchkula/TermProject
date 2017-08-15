from analysisState import AnalysisState
from analysisCountry import AnalysisCountry
from analysisSkills import AnalysisSkills

# Create analysis object and pass the jobtype and zip code
# state = AnalysisState("Data Scientist", "48067")

# retrieve jobs from api and store them in mongodb
# state.retrieveAndStoreJobs()

# get top20 companies hiring jobtype around the zipcode
# state.getTop20Companies(barplot=False)
# state.getTop20Companies()


# Create country-level analysis object and pass the jobtype and zip code
# country = AnalysisCountry("Data Scientist", "US")

# retrieve jobs from the api and store them in mongodb
# country.retrieveAndStoreJobs()

# get top company by state
# country.getTopCompanyByState()

# get number of jobs per state
# country.getJobsByState(barplot=False, heatmap=False)
# country.getJobsByState()

# Create skills analysis object and pass a list of skills
list = ["r", "python", "java", "sas", "mongodb"]
skills = AnalysisSkills(list, "US")

# get number of jobs per skill
skills.getJobsBySkill(barplot=False)
skills.getJobsBySkill()
