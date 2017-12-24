import pymongo

class MongoDB(object):
    """ Electronics Ninja custom MongoDB initiation and worker function
    :param auth: <boolean> (required) True = MongoDB auth enabled
    :param mongodb_creds: <dict> (required if auth set)
        :param server: <str> MongoDB server - defaults to localhost
        :param port: <int> MongoDB server - defaults to 27017
        :param username: <str> MongoDB username
        :param password: <str> MongoDB user password
        :param database: <str> Database to authenticate against and subsequently use

        Call via mDB = en_mongodb.MongoDB(auth=True, mongodb_creds=credsDict)
                 myColl = mDB.collection(coll_name='myCollection')
    """
    def __init__(self, auth, mongodb_creds):
        server = mongodb_creds['server']
        port = mongodb_creds['port']
        username = mongodb_creds['username']
        password = mongodb_creds['password']
        database = mongodb_creds['database']

        self.client = pymongo.MongoClient(server, port=port, username=username, password=password, authSource=database)
        self.db = self.client['{}'.format(database)]

    def collection(self, coll_name):
        """ Create or attach to a collection
        :param coll_name: <str> (Required) Name of the collection

        Returns the collection object => make sure you assign to a variable in your program
        """
        self.coll_name = self.db['{}'.format(coll_name)]
        return self.coll_name

    def insert_one(self, coll_name, data):
        coll_name.insert_one(data)
