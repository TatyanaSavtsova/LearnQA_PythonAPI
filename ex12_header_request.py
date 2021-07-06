import requests


class TestCookie:
    def test_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        response_dict = dict(response.headers)

        assert "x-secret-homework-header" in response_dict, "There is no header 'x-secret-homework-header' in the response"
        assert response_dict["x-secret-homework-header"] == "Some secret value", "The value is incorrect"