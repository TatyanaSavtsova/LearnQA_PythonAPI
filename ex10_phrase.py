class TestPhrase:
    def test_phrase(self):
        phrase = input("Set a phrase shorter 15 characters: ")
        assert len(phrase) < 15, f"The phrase has {len(phrase)} characters"
