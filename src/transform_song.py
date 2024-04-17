def transform_song(data):
    song_list = []
    for i in data["items"]:
        song_id = i["track"]["id"]
        song_name = i["track"]["name"]
        song_duration_ms = i["track"]["duration_ms"]
        song_url = i["track"]["external_urls"]["spotify"]
        song_popularity = i["track"]["popularity"]
        song_added = i["added_at"]
        album_id = i["track"]["album"]["id"]
        artist_id = i["track"]["artists"][0]["id"]
        song_element = {
            "song_id": song_id,
            "song_name": song_name,
            "song_duration": song_duration_ms,
            "song_url": song_url,
            "song_popularity": song_popularity,
            "song_added": song_added,
            "album_id": album_id,
            "artist_id": artist_id,
        }
        song_list.append(song_element)

    return song_list
