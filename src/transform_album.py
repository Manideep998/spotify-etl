def transform_album(data):
    album_list = []
    for i in range(len(data['items'])):
        album_id = data["items"][i]["track"]["album"]["id"]
        album_name = data["items"][i]["track"]["album"]["name"]
        album_release_date = data["items"][i]["track"]["album"]["release_date"]
        album_total_tracks = data["items"][i]["track"]["album"]["total_tracks"]
        album_url = data["items"][i]["track"]["album"]["external_urls"]["spotify"]
        album_element = {
            "album_id": album_id,
            "name": album_name,
            "release_date": album_release_date,
            "total_tracks": album_total_tracks,
            "url": album_url,
        }
        album_list.append(album_element)

    return album_list