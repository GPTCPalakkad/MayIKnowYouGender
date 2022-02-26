import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
mycol =  mydb["names"]


# value = input("Enter your name : ")
# mycol.insert_one({"name":value})



# x =  list(mycol.find({},{"_id":0}))
# # print(type(x))

# for i in x:
#     print(i["name"])


# print(x)

x=mycol.find_one({"name":"sana"})

print(type(x))