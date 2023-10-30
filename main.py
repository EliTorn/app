import pymongo
import streamlit as st
# Connect to the MongoDB database
client = pymongo.MongoClient("localhost", 27017)
db = client["my_database"]
collection = db["my_collection"]

# # Insert a document into the collection
# document = {
#   "name": "yoni",
#   "age": 45
# }
# collection.insert_one(document)
st.title("My app")
# Query the collection
results = collection.find()
st.table(results)
for x in results:
  print(x)

# # Update a document in the collection
# collection.update_one({ "name": "John Doe" }, { "$set": { "age": 31 } })
#
# # Delete a document from the collection
# collection.delete_one({ "name": "John Doe" })

# Close the connection to the MongoDB database
client.close()