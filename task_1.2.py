my_favorite_songs = [
['Waste a Moment', 3.03],
['New Salvation', 4.02],
['Staying\' Alive', 3.40],
['Out of Touch', 3.03],
['A Sorta Fairytale', 5.28],
['Easy', 4.15],
['Beatiful Day', 4.04],
['Nowhere to Run', 2.58],
['In This World', 4.02]
]

duration_of_songs = my_favorite_songs[3][1] + my_favorite_songs[5][1] + my_favorite_songs[-1][1]
print(f'Three songs sound {duration_of_songs} minutes')

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation' : 4.02,
    'Staying\' Alive' : 3.40,
    'Out Of Touch' : 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy' : 4.15,
    'Beatiful Day' : 4.04,
    'Nowhere to run' : 2.58,
    'In This World' : 4.02
}

duration = my_favorite_songs_dict['New Salvation'] + my_favorite_songs_dict['Nowhere to run'] + my_favorite_songs_dict['Beatiful Day']
print(f'Three songs sound {duration} minutes')