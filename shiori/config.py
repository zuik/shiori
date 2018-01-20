from pymongo import MongoClient


def config_mongo(mongo_address, database):
    """
    :param str mongo_address: The address to mongoDB server.
    :param str database: The database to put stuff in.
    :return: mongoDB database
    """
    if not mongo_address:
        client = MongoClient()
    else:
        client = MongoClient(mongo_address)

    return client[database]


DB = config_mongo("", "shiori")
