import pymongo
def load(playlist_name, name, data):
    try:
        client = pymongo.MongoClient("mongodb+srv://saimanideep13:Manideep(1312)@atlascluster.avjebmm.mongodb.net/")
        #print("Connected successfully!!!")
        p_name = playlist_name
        print(p_name)
        db = client[p_name]
    except Exception as e:
        print("Error in connecting to the database",e)   
    try:
        if name == 'song':
            collection = db.song
            collection.insert_many(data)
        if name == 'artist':
            collection = db.artist
            collection.insert_many(data)
        if name == 'album':
            collection = db.album
            collection.insert_many(data)
        print("Data inserted successfully")
    except Exception as e:
        print("Error in inserting data",e)
    
