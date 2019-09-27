#!/usr/bin/python3
# coding: utf-8

import requests

class GoogleMapsDownloader:

    def find_place(self, question):
        payload = {
            "key": "AIzaSyC0o3amaUK69TJd7GOTQKiUQ-2Rlu1uex8",
            "input": question,
            "inputtype": "textquery",
            "fields": "formatted_address,geometry",
        }
        response = requests.get(
            "https://maps.googleapis.com/maps/api/place/findplacefromtext/json", params=payload)
        data = response.json()
        return {
            "formatted_address": data['candidates'][0]["formatted_address"],
            "candidates": [{
                    "geometry": {
                        "location": {
                            "lat": data['candidates'][0]['geometry']['location']["lat"],
                            "lng": data['candidates'][0]['geometry']['location']["lng"]
                        }
                    }
                }
            ]
        }

class WikiDownloader:

    def fetch_by_coord(self, location):
        payload = {
            "action": "query",
            "list": "geosearch",
            "gsradius": 200,
            "gscoord": str(location['lat']) + "|" + str(location['lng']),
            "gslimit": 1,
        }
        response = requests.get(
            "https://fr.wikipedia.org/w/api.php", params=payload)
        data = response.json()
        return {
            "query": {
                "geosearch": [{
                    "title": data
                    }
                ]
            }
        }
        

    def fetch_by_title(self, title, pageid):
        payload = {
            "action": "query",
            "prop": "extracts%7Cinfo",
            "exchars": 1200,
            "titles": title,
            "inprop": "url",
            "explaintext": "",
        }
        response = requests.get(
            "https://fr.wikipedia.org/w/api.php", params=payload)
        data = response.json()
        return {
            "query": {
                    "pages": {
                        pageid: {
                            "title": data["title"],
                            "extract": data["extract"],
                            "fullurl": data["fullurl"]
                    }
                }
            }
        }
