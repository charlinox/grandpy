from grandpy.api import WikiDownloader, WikiDownloader, GoogleMapsDownloader


def test_find_place(monkeypatch):
    google_maps_downloader = GoogleMapsDownloader()
    expected_result = {
        "address": "une adresse",
        "lat": 12.134,
        "lng": -30.4135,
        "error": False
    }

    class MockRequestsGet:
        def __init__(self, url, params):
            self.status_code = 200

        def json(self):
            return {
                "candidates":[
                    {
                        "formatted_address": expected_result["address"],
                        "geometry": {
                            "location": {
                                "lat": expected_result["lat"],
                                "lng": expected_result["lng"]
                                }
                        }
                    }
                ]
            }
    monkeypatch.setattr('requests.get', MockRequestsGet)
    assert google_maps_downloader.find_place("question") == expected_result


def test_fetch_by_coord(monkeypatch):
    wikiDownloader = WikiDownloader()
    find_by_place_result = {
        "address": "une adresse",
        "lat": 12.134,
        "lng": -30.4135,
        "error": False
    }
    expected_result = {
        "title": "Academy of Art University",
        "pageid": 1,
        "extract": "",
        "fullurl": "",
        "error": False,
    }

    class MockRequestsGet:
        def __init__(self, url, params):
            self.status_code = 200

        def json(self):
            return {
                "query": {
                    "geosearch": [{
                        "title": expected_result["title"],
                        "pageid": expected_result["pageid"]
                    }
                    ]
                }
            }
    monkeypatch.setattr('requests.get', MockRequestsGet)
    assert wikiDownloader.fetch_by_coord(
        find_by_place_result) == expected_result

def test_fetch_by_title(monkeypatch):
    wikiDownloader = WikiDownloader()
    expected_result = {
        "title": "Academy of Art University",
        "pageid": 1,
        "extract": "L'Academy of Art University...",
        "fullurl": "https://fr.wikipedia.org/wiki/Academy_of_Art_University",
        "error": False,
    }
    class MockRequestsGet:
        def __init__(self, url, params):
            self.status_code = 200

        def json(self):
            return {
                "query": {
                    "pages": {
                        expected_result["pageid"]: {
                            "title": expected_result["title"],
                            "extract": expected_result["extract"],
                            "fullurl": expected_result["fullurl"]
                        }
                    }
                }
            }
    monkeypatch.setattr('requests.get', MockRequestsGet)
    assert wikiDownloader.fetch_by_title(expected_result) == expected_result
