from lib.track import *

"""
When user adds a track, 
The title and artist are stored to the object
"""

def test_title_and_artist_are_stored():
    track = Track("Teenage Kicks", "The Undertones")
    assert track.title == "Teenage Kicks"
    assert track.artist == "The Undertones"

"""
When user calls #matches with a keyword
And that keyword matches either the artist
Then it will return True 
"""

def test_true_is_returned_if_keyword_matches_artist():
    track = Track("Teenage Kicks", "The Undertones")
    assert track.matches("The Undertones") ==  True

"""
When user calls #matches with a keyword
And that keyword matches either the title or artist
Then it will return True 
"""

def test_true_is_returned_if_keyword_matches_title():
    track = Track("Teenage Kicks", "The Undertones")
    assert track.matches("Teenage Kicks") ==  True

"""
When user calls #matches with a keyword
And that keyword doesn't matches either the title or artist
Then it will return False
"""

def test_false_is_returned_if_keyword_meets_no_matches():
    track = Track("Teenage Kicks", "The Undertones")
    assert track.matches("The Clash") ==  False

"""
When user calls #matches with a keyword
And that keyword partially matches either the title or artist
Then it will return True 
"""

def test_true_is_returned_if_keyword_partially_matches():
    track = Track("Teenage Kicks", "The Undertones")
    assert track.matches("Kicks") ==  True