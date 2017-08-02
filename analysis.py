import pymongo

# connect to mongo
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to jobs db
db = connection.jobs

# get a handle to dice collection
diceMongoWarren = db.diceMongoWarren


def find_based_on_location(location):
    print("Retrieving jobs in {}".format(location))
    query = {"location": location}
    projection = {"_id": 0, "detailUrl": 0}

    result = diceMongoWarren.find(query, projection)

    for job in result:
        print(job)


def count_jobs_based_on_location(location):
    print("Number of jobs in {}".format(location))
    count = 0
    query = {"location": location}

    result = diceMongoWarren.find(query)

    for job in result:
        count += 1

    return (count)


def group_by_location():
    print("Grouping by location: ")
    query = [{"$group": {
        "_id": "$location",
        "totalJobs": {"$sum": 1}
    }}]

    result = diceMongoWarren.aggregate(query)

    for item in result:
        print(item)

def group_by_location_sorted():
    print("Grouping by location descending job count")
    query = [{"$group": {
        "_id": "$location",
        "totalJobs": {"$sum": 1}
            }
        },
        {"$sort":{
            "totalJobs":-1
            }
        }
    ]

    result = diceMongoWarren.aggregate(query)

    for item in result:
        print(item)

def filter_by_location(location):
    print("Filter jobs based on location")

    query = []

    result = diceMongoWarren.aggregate(query)

    for item in result:
        print(item)

def main():
    # find_based_on_location("New York, NY")
    # print(count_jobs_based_on_location("New York, NY"))
    # group_by_location()
    # group_by_location_sorted()
    filter_by_location()


if __name__ == '__main__':
    main()
