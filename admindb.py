from pymongo import MongoClient

# MongoDB Connection URL
connectionString = "mongodb+srv://team7:sid12345@cluster0.4qs77z7.mongodb.net/test"
client = MongoClient(connectionString)

db = client['glamping']
list_of_collections = db.list_collection_names()


def chooseCollection():
    i = 0
    print("Choose a collection from the given list")
    for c in list_of_collections:
        i = i + 1
        print(f"{i}. {c}")
    choice = int(input()) - 1
    collection_name = list_of_collections[choice]
    collection = db[collection_name]
    return collection


def displayAll():
    collection = chooseCollection()
    allOrder = collection.find()
    for order in allOrder:
        print(f"{order}\n")
    print(f"---------------------------------------------------------------------------------------")


def calculateRevenue():
    collection = chooseCollection()
    revenue = collection.aggregate([{"$group": {"_id": "null", "Revenue": {"$sum": "$Total"}}}])
    for r in revenue:
        print(f"The revenue for the chosen collection is {r['Revenue']}\n")
        print(f"---------------------------------------------------------------------------------------")


def AverageOrderValue():
    collection = chooseCollection()
    output = collection.aggregate([{"$group": {"_id": "null", "AverageOrderValue": {"$avg": "$Total"}}}])
    for o in output:
        print(f"Average booking value is {o['AverageOrderValue']}\n")
        print(f"---------------------------------------------------------------------------------------")



def minMaxValue():
    collection = chooseCollection()
    output = collection.aggregate(
        [{"$group": {"_id": "null", "MinOrderValue": {"$min": "$Total"}, "MaxOrderValue": {"$max": "$Total"}}}])
    for o in output:
        print(f"Min booking value is {o['MinOrderValue']}")
        print(f"Max booking value is {o['MaxOrderValue']}\n")
        print(f"---------------------------------------------------------------------------------------")

while True:
    choice = int(input(
        "1. Display all Bookings\n2. Calculate Revenue\n3. Average Booking Value\n4. Minimum and Maximum Booking "
        "Values\n5. "
        "Exit\n"))

    if choice == 1:
        displayAll()
    elif choice == 2:
        calculateRevenue()
    elif choice == 3:
        AverageOrderValue()
    elif choice == 4:
        minMaxValue()
    else:
        exit()
