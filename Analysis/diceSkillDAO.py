import requests

class DiceSkillDAO:
	def __init__(self, list, country):
	
		# location, use country
		self._country = country
		
		# skills, use list of skills
		self._skillset = list
		
	def RetrieveJobTotal(self):
	
		# initialize job_total list
		job_total = []
		
		# get job total for each skill in list
		for skill in self._skillset:		
			# construct the URL
			url = "http://service.dice.com/api/rest/jobsearch/v1/simple.json?text={}&Country={}".format(self._skillset[skill],self._country)
			
			print("Retrieving job total from URL:")
			print(url)
			
			r = requests.get(self._url)
			json_data = r.json()
			
			c = json_data['count']
			job_total = job_total.append(int(c))
			
			# print("Job total requiring {} skill is {}".format(self._skillset[skill],c)
			
		return job_total