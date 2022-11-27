import math
from datetime import datetime, date

from pymongo import MongoClient

# MongoDB Connection URL
connectionString = "mongodb+srv://team7:sid12345@cluster0.4qs77z7.mongodb.net/test"
client = MongoClient(connectionString)

# Get Current Date and time
currentMonth = datetime.now().strftime("%b")
currentYear = datetime.now().strftime("%Y")
currentDay = datetime.now().strftime("%d")
currentTime = datetime.now().strftime("%H:%M:%S")

# Creating a Database for boba ordering
db = client['glamping']

# The current collection we are working on which calculated based on current month and year
collection_name = currentMonth + " " + currentYear
collection = db["nov/2022"]

list_of_collections = db.list_collection_names()  # Return a list of collections in db

bot_name = "glamping"


def insertDocument(Date, Package, Name, PhoneNo, No_Room, No_people, Total):
    # if collection_name in list_of_collections:
    Bookingid = collection.count_documents({}) + 1
    orderDetails = {"BookingId": Bookingid,
                    "Date": Date,
                    "Name": Name,
                    "package": Package,
                    "Phone": PhoneNo,
                    "No_Room": No_Room,
                    "noOfPeople": No_people,
                    "Total": Total}
    collection.insert_one(orderDetails)

    print(
        f"Booking is confirmed for {No_people} people on {Date} with booking id {Bookingid} .\nTotal Amount to be paid is {Total} which is to be "
        f"paid once you reach to the camp")
    print("\nThank you for booking with us :)")

    # collection.update_one({"OrderId": int(Bookingid)}, {"$set": {"Date": Date}})
    #
    # specificOrder = collection.find_one({"BookingId": int(Bookingid)}, {'_id': 0, 'OrderId': 1,
    #                                                                     'Date': 1, 'Name': 1, 'package': 1,
    #                                                                     'Phone': 1,
    #                                                                     'No_Room': 1,
    #                                                                     'noOfPeople': 1, 'Total': 1})


def bookRoom():
    available_rooms = 0
    occupied_rooms = 0
    noRoom = 0
    name = input("Enter Your Name: ")
    phone = input("Enter Your Phone No: ")
    noOFPeople = int(input("Enter No of People "))
    package = int(
        input("1. Basic Package (Max 2 people) - 1499/-\n2. Deluxe Package(Max 4 people) - 1999 (Enter 1 or 2)"))
    if package == 1:
        price = 1499 * noOFPeople
    elif package == 2:
        price = 1999 * noOFPeople
    else:
        print("Invalid choice. Please re-enter the details")
        bookRoom()
    if noOFPeople <= 2:
        if package == 1:
            noRoom = 1
        else:
            noRoom = 1

    elif noOFPeople > 2:
        if package == 1:
            noRoom = math.ceil(noOFPeople / 2)
        elif package == 2:
            noRoom = math.ceil(noOFPeople / 4)

    day = int(input('Enter a day: '))
    month = int(input('Enter a month: '))
    d = date(date.today().year, month, day)


    occupied_room_details = collection.find({"Date": str(d), "package": package}, {"_id": 0, "No_Room": 1})
    for item in occupied_room_details:
        occupied_rooms += item["No_Room"]

    #print(f"Occupied Rooms: {occupied_rooms}")
    available_rooms = 5 - occupied_rooms
    print(f"Available Rooms: {available_rooms}")
    print(f"Occupied Rooms: {occupied_rooms}")
    if noRoom <= available_rooms:
        if d <= date.today():
            print("This date isn't available for booking. Please try again")
        else:
            insertDocument(str(d), package, name, phone, noRoom, noOFPeople, price)
    else:
        print("This date isn't available for booking. Please try again")


def bookingDetails():
    bookingId = int(input("Enter your Booking id"))

    if collection.count_documents({"BookingId": bookingId}) == 1:

        bookingDetails = collection.find_one({"BookingId": int(bookingId)}, {'_id': 0, 'BookingId': 1,
                                                                             'Date': 1, 'Name': 1, 'package': 1,
                                                                             'Phone': 1,
                                                                             'No_Room': 1,
                                                                             'noOfPeople': 1, 'Total': 1})
        print(bookingDetails)
    else:
        print("This booking id does not exist")



