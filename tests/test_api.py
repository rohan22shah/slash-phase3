import requests
import unittest
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',  # noqa: E501
    'Accept-Encoding': 'gzip, deflate',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'DNT': '1',
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1'
}

class TestAPI(unittest.TestCase):
    searchTerm = "dell laptops"
    def test_server(self):
        self.assertEqual(requests.get("https://slash-app.azurewebsites.net/", headers=headers).status_code, 200, "Server is not up and running")

    def test_amazon(self):
        self.assertEqual(len(json.loads(requests.get("https://slash-app.azurewebsites.net/az/" + self.searchTerm, headers = headers).text))>0, True, "Didn't get any responses from the API")

    def test_walmart(self):
        self.assertEqual(len(json.loads(requests.get("https://slash-app.azurewebsites.net/wm/" + self.searchTerm, headers = headers).text))>0, True, "Didn't get any responses from the API")

    def test_bestbuy(self):
        self.assertEqual(len(json.loads(requests.get("https://slash-app.azurewebsites.net/bb/" + self.searchTerm, headers = headers).text))>0, True, "Didn't get any responses from the API")

    def test_target(self):
        self.assertEqual(len(json.loads(requests.get("https://slash-app.azurewebsites.net/tg/" + self.searchTerm, headers = headers).text))>0, True, "Didn't get any responses from the API")

    def test_costco(self):
        self.assertEqual(len(json.loads(requests.get("https://slash-app.azurewebsites.net/cc/" + self.searchTerm, headers = headers).text))>0, True, "Didn't get any responses from the API")

    def test_ebay(self):
        self.assertEqual(len(json.loads(requests.get("https://slash-app.azurewebsites.net/eb/" + self.searchTerm, headers = headers).text))>0, True, "Didn't get any responses from the API")

if __name__ == '__main__':
    unittest.main()