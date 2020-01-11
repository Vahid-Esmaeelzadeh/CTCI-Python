'''
Favorite Genres

Given a map Map<String, List<String>> userSongs with user names as keys and a list of all the songs that the user has
listened to as values.

Also given a map Map<String, List<String>> songGenres, with song genre as keys and a list of all the songs within
that genre as values. The song can only belong to only one genre.

The task is to return a map Map<String, List<String>>, where the key is a user name and the value is a list of the
user's favorite genre(s). Favorite genre is the most listened to genre. A user can have more than one favorite genre
if he/she has listened to the same number of songs per each of the genres.

Example 1:

Input:
userSongs = {
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
},
songGenres = {
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}

Output: {
   "David": ["Rock", "Techno"],
   "Emma":  ["Pop"]
}
'''


def favGenres(userSongs: dict, genres: dict):
    song_genre_table = {}
    for x in genres.keys():
        for song in genres[x]:
            song_genre_table[song] = x

    user_genres_table = {}
    for user in userSongs.keys():
        user_genres_table[user] = []
        max_count = 0
        genre_count_table = {}
        for song in userSongs[user]:
            if song in song_genre_table:
                genre_count_table[song_genre_table[song]] = genre_count_table.get(song_genre_table[song], 0) + 1
                max_count = max(genre_count_table[song_genre_table[song]], max_count)

        for genre in genre_count_table.keys():
            if genre_count_table[genre] == max_count:
                user_genres_table[user].append(genre)

    return user_genres_table

songGenres = {
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}

userSongs = {
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
}

userSongs1 = {
   "David": ["song1", "song2"],
   "Emma":  ["song3", "song4"]
}
songGenres1 = {}


print(favGenres(userSongs1, songGenres1))
