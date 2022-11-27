import datetime
from datetime import datetime
import speech_recognition as sr
import pyttsx3
import pymongo
from pymongo import MongoClient

connectionString = "mongodb+srv://parthpoladiya:Parth28poladiya@cluster0.jd6ydhb.mongodb.net/test"


def insertDocument():
    # Inserting a document
    order_details = {"Id": 1,
                     "CustomerName": "Pooja1",
                     "OrderName": "Thick Cold Coffee",
                     "OrderDay": datetime.now().strftime("%d"),
                     "OrderTime": datetime.now().strftime("%H:%M:%S")
                     }
    order_id = collection.insert_one(order_details).inserted_id
    print(order_id, " has been created")


def readDocument():
    # Read
    allOrder = collection.find()
    for order in allOrder:
        print(order)

    specificOrder = collection.find_one({"CustomerName": "Parth Poladiya"})
    print(specificOrder)




if __name__ == '__main__':
    client = MongoClient(connectionString)

    # Creating a Database for boba ordering
    db = client['boba-tea']

    # Creating a collection in format month year
    currentMonth = datetime.now().strftime("%b")
    currentYear = datetime.now().strftime("%Y")
    collection_name = currentMonth + " " + currentYear
    collection = db[collection_name]

    #insertDocument()

    readDocument()
    # Update
    collection.update_many({}, {'$inc': {'Id': 100}})

    # Delete
    collection.delete_many({"CustomerName": "Pooja"})

