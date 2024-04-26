#Example Python Code to Insert a Document
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'aac123'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30166 #32067?  
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
# Method for adding new data to the database.  
    def create(self, data):
        if data is not None: #if not null
            successfulInsert = self.database.animals.insert_one(data)  # data should be dictionary
            if successfulInsert is not None: #If inserted successfully, return true
                return True
            else: #if not, return false. 
                return False
        else:#exception for empty data
            raise Exception("Nothing to save, because data parameter is empty")

#Method for reading data from the database.  
    def read(self, findData): #read by the 'findData'
        if findData: #if it exists
            returnData = self.database.animals.find(findData, {"_id": False})
            #return the specified animals by key value pair
        else:
            returnData = self.database.animals.find({}, {"_id": False})
            #return without 'found' findData.  
        return returnData #return regardless, empty list or not.  
    
#Method for updating existing data within the database.  
    def update(self, originalData, updateTag):
        if originalData is not None: #Ensure we aren't receiving empty parameters.  
            updateCount = self.database.animals.update_many(originalData, {"$set": updateTag }) #Update all existing database entries matching the updateTag
            return updateCount.raw_result #Returns the number of updates performed
        else:
            #everything in my brain says python's dynamic return types are wrong
            return "Received data set is Null"

#Method for removing data from existing database.  
    def delete(self, deletionTag):
        if deletionTag is not None:
            deletionCount = self.database.animals.delete_many(deletionTag)
            return deletionCount.raw_result #Return number of objects removed that match the delete tag
        else:
            return "Received data set is Null"