from src.extract import extract
from src.transform_album import transform_album
from src.transform_artist import transform_artist
from src.transform_song import transform_song
from src.load import load
from dotenv import load_dotenv
import os
load_dotenv('env')

playlist_name = os.getenv('NAME')
print(playlist_name)

if __name__ == "__main__":
    try:
        print("extracting data")
        data = extract()
    except Exception as e:
        print("failed to extract data",e)

    try:
        print("transforming data")
        album_data = transform_album(data)
    except Exception as e:
        print("failed to transform albums data",e)
    
    try:
        print("transforming data")
        artist_data = transform_artist(data)
    except Exception as e:
        print("failed to transform artists data",e)
    
    try:
        print("transforming data")
        song_data = transform_song(data)
    except Exception as e:
        print("failed to transform songs data",e)
    try:
        print("loading albums data")
        load_album = load(playlist_name, 'album', album_data)
    except Exception as e:
        print("failed to load albums data",e)

    try:
        print("loading artists data")
        load_artist = load(playlist_name,'artist', artist_data)
    except Exception as e:
        print("failed to load artists data",e)
    try:
        print("loading songs data")
        load_song = load(playlist_name,'song', song_data)
    except Exception as e:
        print("failed to load songs data",e)

