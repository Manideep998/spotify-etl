def transform_artist(data):
    artist_list = []
    for i in data["items"]:
        for key, value in i.items():
            if key == "track":
                for artist in value["artists"]:
                    artist_dict = {
                        "artist_id": artist["id"],
                        "artist_name": artist["name"],
                        "external_urls": artist["href"],
                    }
                    artist_list.append(artist_dict)
    return artist_list
