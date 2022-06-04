# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.

def make_album(artist_name='', album_title='',number_of_songs=None):
    """Return dictionary of album"""
    album_info = {'Artist':artist_name, 'Album': album_title}
    if number_of_songs:
        album_info['Number of tracks'] = number_of_songs
    return album_info

while True:
    print("Enter 'q' at any time to quit")

    artist_n = input("Artiste name: ")
    if artist_n == 'q':
        break
    album_n = input("Album name: ")
    if artist_n == 'q':
        break
    else:
        print(make_album(artist_n, album_n))
        break