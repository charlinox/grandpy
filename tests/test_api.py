from grandpy.api import WikiDownloader, WikiDownloader, GoogleMapsDownloader


def test_find_place(monkeypatch):
    expected_result = {
        "address": "une adresse",
        "latitude": 12.134,
        "longitude": -30.4135
    }
    class MockRequestsGet:
        def __init__(self, url, params):
            pass
        def json(self):
            return {
                "formated_address": expected_result["address"],
                "candidates": [{
                        "geometry": {
                            "location": {
                                "lat": expected_result["latitude"],
                                "lng": expected_result["longitude"]
                            }
                        }
                    }
                ]
            }
    monkeypatch.setattr('requests.get', MockRequestsGet)
    assert find_place("question") == expected_result


def test_fetch_by_coord(monkeypatch):
    expected_result = {"Academy of Art University"}
    class MockRequestsGet:
        def __init__(self, url, params):
            pass
        def json(self):
            return {
                "query": {
                    "geosearch": [{
                        "title": expected_result
                        }
                    ]
                }
            }
    monkeypatch.setattr('requests.get', MockRequestsGet)
    assert fetch_by_coord({"lat" : -33.859, "lng" : 151.209}) == expected_result


def test_fetch_by_title(monkeypatch):
    expected_result = {
        "title": "Academy of Art University",
        "extract": "L\u2019Academy of Art University...",
        "fullurl": "https://fr.wikipedia.org/wiki/Academy_of_Art_University"
    }
    class MockRequestsGet:
        def __init__(self, url, params):
            pass
        def json(self):
            return {
                "query": {
                        "pages": {
                            "pageid": {
                                "title": expected_result["title"],
                                "extract": expected_result["extract"],
                                "fullurl": expected_result["fullurl"]
                        }
                    }
                }
            }
    monkeypatch.setattr('requests.get', MockRequestsGet)
    assert fetch_by_title("title", 6422233) == expected_result
