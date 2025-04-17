from lib.music_library import MusicLibrary
from lib.track import Track

""" 
When a user calls #add for a track
The track is added to the tracks list in MusicLibrary
"""

def test_track_is_stored_in_tracks_in_library():
    jukebox = MusicLibrary()
    track_1 = Track("Human Fly", "The Cramps")
    jukebox.add(track_1)
    assert jukebox.tracks == [track_1]

"""
When a user adds multiple tracks to the Library
They will all be stored in tracks
"""

def test_multiple_tracks_are_stored_in_tracks_in_library():
    jukebox = MusicLibrary()
    track_1 = Track("Human Fly", "The Cramps")
    track_2 = Track("Spread Your Love", "Black Rebel Motorcycle Club")
    track_3 = Track("Dog House Blues", "Seasick Steve")
    jukebox.add(track_1)
    jukebox.add(track_2)
    jukebox.add(track_3)
    assert jukebox.tracks == [track_1, track_2, track_3]

"""
When a user calls #search
And the keyword matches either the title or artist of a track
Then that track instance will be returned in a list
"""
def test_search_returns_matching_track_with_one_match():
    jukebox = MusicLibrary()
    track_1 = Track("Human Fly", "The Cramps")
    track_2 = Track("Spread Your Love", "Black Rebel Motorcycle Club")
    track_3 = Track("Dog House Blues", "Seasick Steve")
    jukebox.add(track_1)
    jukebox.add(track_2)
    jukebox.add(track_3)
    assert jukebox.search("Spread Your Love") == [track_2]

"""
When a user calls #search
And the keyword matches either the title or artist on multiple tracks
Then all matching track instances will be returned in a list
"""
def test_search_returns_matching_tracks_where_multiple_matches():
    jukebox = MusicLibrary()
    track_1 = Track("Human Fly", "The Cramps")
    track_2 = Track("Spread Your Love", "Black Rebel Motorcycle Club")
    track_3 = Track("Dog House Blues", "Seasick Steve")
    track_4 = Track("Goo Goo Muck", "The Cramps")
    jukebox.add(track_1)
    jukebox.add(track_2)
    jukebox.add(track_3)
    jukebox.add(track_4)
    assert jukebox.search("The Cramps") == [track_1, track_4]

"""
When a user calls #search
And the keyword does not match either the title or artist held in tracks
Then an empty list will be returned
"""
def test_search_returns_empty_list_where_no_matches():
    jukebox = MusicLibrary()
    track_1 = Track("Human Fly", "The Cramps")
    track_2 = Track("Spread Your Love", "Black Rebel Motorcycle Club")
    track_3 = Track("Dog House Blues", "Seasick Steve")
    track_4 = Track("Goo Goo Muck", "The Cramps")
    jukebox.add(track_1)
    jukebox.add(track_2)
    jukebox.add(track_3)
    jukebox.add(track_4)
    assert jukebox.search("The Clash") == []