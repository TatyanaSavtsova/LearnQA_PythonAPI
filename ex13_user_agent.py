import pytest
import requests
import json

class TestUserAgent:
    data = [
        ({"User-Agent": "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "expected_platform": "Mobile",
        "expected_browser": "No",
        "expected_device": "Android"}),
        ({"User-Agent": 'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1',
        "expected_platform": "Mobile",
        "expected_browser": "Chrome",
        "expected_device": "iOS"}),
        ({"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "expected_platform": "Googlebot",
        "expected_browser": "Unknown",
        "expected_device": "Unknown"}),
        ({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
        "expected_platform": "Web",
        "expected_browser": "Chrome",
        "expected_device": "No"}),
        ({"User-Agent": "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
        "expected_platform": "Mobile",
        "expected_browser": "No",
        "expected_device": "iPhone"})
    ]

    @pytest.mark.parametrize('data', data)
    def test_user_agent(self, data):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        user_agent = data["User-Agent"]
        response = requests.get(url, headers={"User-Agent": user_agent})

        result = json.loads(response.text)
        print(result)
        useragent = result['user_agent']

        assert "platform" in result, "There is no 'platform' field"
        assert "browser" in result, "There is no 'browser' field"
        assert "device" in result, "There is no 'device' field"

        assert result["platform"] == data["expected_platform"], f"User Agent: {useragent}. The platform is not correct"
        assert result["browser"] == data["expected_browser"], f"User Agent: {useragent}. The browser is not correct"
        assert result["device"] == data["expected_device"], f"User Agent: {useragent}. The device is not correct"
