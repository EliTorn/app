import pymongo

url = "mongodb+srv://eli:DxhkMWiiylHIq3eB@atlascluster.m6tavxq.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(url)

# Create a database
db: object = client["gama"]

# Create a collection
collection: object = db["java"]


def connect(name: str, question: bytes) -> None:
    """
    the fanc get the name and picture and int of amount and insert this into the database
    """
    d: object = {"topic": name, 'question': question}

    collection.insert_one(d)


def show() -> object:
    """
    the func return the all date the in database
    \n
    -> return object :
    """

    data: object = collection.find()
    return data


def search(value: str) -> object:
    """
    the function get the value and search into the database and return the object
    :param value:
    :return:
    """
    data: object = collection.find({"name": value})
    return data


def update(name: str, value: int) -> None:
    """
    the function get the name and value and update the amount of item into the database
    :param name:
    :param value:
    :return:
    """
    collection.update_one(
        {"name": name},
        update={"$set": {"amount": value}}, )


def upload_image(question, image):
    collection: object = db["image"]
    d: object = {"question": question, "image": image}

    collection.insert_one(d)


def show_image():
    collection: object = db["image"]
    data: object = collection.find()
    return data
