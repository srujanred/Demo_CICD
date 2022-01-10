# content of test_demo.py
import requests

class TestDemo:
    def test_one(self):
        page = requests.get("https://the-internet.herokuapp.com/context_menu")
        assert "Right-click in the box below to see one called 'the-internet'" in page.text

    def test_two(self):
        page = requests.get("https://the-internet.herokuapp.com/context_menu")
        assert "alibaba" in page.text
