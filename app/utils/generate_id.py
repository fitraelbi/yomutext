import bson # type: ignore

def generate_id():
    return str(bson.ObjectId())