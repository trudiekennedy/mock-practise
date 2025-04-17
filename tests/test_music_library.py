from lib.music_library import *
from unittest.mock import Mock

"""
Initially, music library list is an empty list
"""

def test_library_begins_with_empty_list():
    jukebox = MusicLibrary()
    assert jukebox.tracks == []

"""
When user adds tracks
They show up in the tracks list
"""
def test_tracks_get_added_and_listed_out():
    jukebox = MusicLibrary()
    track_1 = Mock()
    track_2 = Mock()
    track_3 = Mock()
    jukebox.add(track_1)
    jukebox.add(track_2)
    jukebox.add(track_3)
    assert jukebox.tracks == [track_1, track_2, track_3]

"""
When a user adds multiple tracks
And they search for a keyword
I get tracks that match that keyword
"""
def test_searches_by_keyword_with_fakes():
    jukebox = MusicLibrary()
    fake_matching = FakeMatchingTrack()
    jukebox.add(fake_matching)
    fake_not_matching = FakeNotMatchingTrack()
    jukebox.add(fake_not_matching)
    assert jukebox.search("hello") == [fake_matching]

class FakeMatchingTrack:
    def matches(self, keyword):
        return True

class FakeNotMatchingTrack:
    def matches(self, keyword):
        return False

def test_searches_by_keyword_with_mocks():
    jukebox = MusicLibrary()
    fake_matching = Mock()
    fake_matching.matches.return_value = True
    jukebox.add(fake_matching)
    fake_not_matching = Mock()
    fake_not_matching.matches.return_value = False
    jukebox.add(fake_not_matching)
    assert jukebox.search("hello") == [fake_matching]