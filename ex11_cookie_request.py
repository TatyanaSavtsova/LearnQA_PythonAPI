import requests


class TestCookie:
    def test_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        response_dict = dict(response.cookies)

        assert "HomeWork" in response_dict, "There is no cookie 'HomeWork' in the response"
        assert response_dict["HomeWork"] == "hw_value", "The value is incorrect"
