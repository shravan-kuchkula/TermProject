import requests

class DiceCountryDAO:
    def __init__(self, db, jobType, country):
        self._db = db

        # Clean jobType
        # 1. replace spaces with '+'
        # 2. convert to lower case
        self._jobType = jobType.replace(" ", "+").lower()

        # location, use zipcode
        self._country = country

        # Derive the collection name as
        # collectionName = jobType + location
        # eg: datascientistUS
        self._collection = getattr(self._db, jobType.replace(" ", "").lower() + country)

        # Construct the URL
        self._url = "http://service.dice.com/api/rest/jobsearch/v1/simple.json?text={}&country={}".format(self._jobType,
                                                                                                       self._country)

    def retrieveJobs(self):
        print("Retrieving jobs from URL:")
        print(self._url)

        # Drop the collection to start fresh
        print("Dropping collection {}".format(getattr(self._collection, 'name')))
        self._collection.drop()

        # Retrieve jobs from the url and store them into mongodb
        # Handle pagination and store all of the docs in one collection

        r = requests.get(self._url)
        json_data = r.json()

        for item in json_data['resultItemList']:
            self._collection.insert_one(item)

        while json_data['count'] != json_data['lastDocument']:

            # get nextUrl for paginated results
            nextURL = json_data['nextUrl']
            r = requests.get("http://service.dice.com" + nextURL)

            json_data = r.json()
            for item in json_data['resultItemList']:
                self._collection.insert_one(item)


    def countJobs(self):
        return self._collection.count()

    def topCompanies(self):

        print("Printing top companies")

        query = [
        {
            "$match": {
                "location": {"$exists": "true", "$ne": ""}
                }
        },
        {
            "$project": {
                "jobTitle": 1,
                "company": 1,
                "location": 1,
                "state": {
                    "$toUpper": {"$substrCP": ["$location", {"$subtract": [{"$strLenCP": "$location"}, 2]}, 2]}
                    }
                }
        },
        {
            "$group": {
                "_id": "$state",
                "count": {"$sum":1}
            }

        },
        {
            "$project": {
                "_id":0,
                "state": "$_id",
                "jobcount": "$count"
            }

        },
        {
            "$sort": {
                "jobcount":-1
            }

        },
        {
            "$limit":20

        }
        ]

        return(self._collection.aggregate(query))


    def topCompanyWithinState(self):
        print("Display the top company with every state")

        query = [
            {
                "$match": {
                    "location": {"$exists": "true", "$ne": ""}
                }
            },
            {
                "$project": {
                    "jobTitle": 1,
                    "company": 1,
                    "location": 1,
                    "state": {
                        "$toUpper": {"$substrCP": ["$location", {"$subtract": [{"$strLenCP": "$location"}, 2]}, 2]}
                    }
                }
            },
            {
                "$match": {
                    "state": {
                        "$in": ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
                                "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                                "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
                                "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
                                "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
                    }
                }

            },
            {
                "$group": {
                    "_id": {"company": "$company", "state":"$state"},
                    "count": {"$sum": 1}
                }

            },
            {
                "$sort": {
                    "count": -1
                }

            },
            {
                "$group": {
                    "_id": {"state": "$_id.state"},
                    "topCompany": {
                        "$first": "$_id.company"
                    }
                }
            },
            {
                "$project": {
                    "_id":0,
                    "state": "$_id.state",
                    "company": "$topCompany"
                }

            },
            {
                "$sort": {
                    "state": 1
                }

            }
        ]

        return(self._collection.aggregate(query))


