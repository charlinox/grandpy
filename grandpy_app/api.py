3# coding: utf-8

import requests
from requests.exceptions import ConnectionError


class GoogleMapsDownloader:
    """ Download location of site on Googlemaps API"""

    def find_place(self, question):
        """ Find location of site """
        info = {
            "address": "",
            "lat": None,
            "lng": None,
            "error": True
        }
        if not question or not isinstance(question, str):
            return info
        payload = {
            "key": "AIzaSyC0o3amaUK69TJd7GOTQKiUQ-2Rlu1uex8",
            "input": question,
            "inputtype": "textquery",
            "fields": "formatted_address,geometry",
        }
        url = (
            "https://maps.googleapis.com"
            "/maps/api/place/findplacefromtext/json"
        )
        try:
            response = requests.get(url, params=payload)
            if response.status_code == 200:
                data = response.json()
                if data['candidates']:
                    info['address'] = (
                        data['candidates'][0]["formatted_address"]
                    )
                    info['lat'] = (
                        data['candidates'][0]['geometry']['location']["lat"]
                    )
                    info['lng'] = (
                        data['candidates'][0]['geometry']['location']["lng"]
                    )
                    info['error'] = False
                elif data["status"] == "INVALID_REQUEST":
                    info["error"] = "INVALID_REQUEST"
                elif data["status"] == "ZERO_RESULTS":
                    info["error"] = "ZERO_RESULTS"
        except ConnectionError:
            pass
        return info


class WikiDownloader:
    """ Download coordinates and summary on Wikipedia API """

    def fetch_by_coord(self, location):
        """ Fetch place data by location on Wikipedia """
        info = {
            "title": "",
            "pageid": None,
            "extract": "",
            "fullurl": "",
            "error": True,
        }
        if (
            not location
            or not isinstance(location, dict)
            or "lat" not in location
            or "lng" not in location
            or location['error']
        ):
            return info
        payload = {
            "action": "query",
            "list": "geosearch",
            "gsradius": 200,
            "gscoord": f"{location['lat']}|{location['lng']}",
            "gslimit": 1,
        }

        try:
            response = requests.get(
                "https://fr.wikipedia.org/w/api.php", params=payload
            )
            if response.status_code == 200:
                data = response.json()
                if data['query']['geosearch']:
                    info['title'] = data['query']['geosearch'][0]['title']
                    info['pageid'] = data['query']['geosearch'][0]['pageid']
                    info['error'] = False
        except ConnectionError:
            pass
        return info

    def fetch_by_title(self, info):
        """ Fetch summary and url by title on Wikipedia """
        if (
            not info
            or not isinstance(info, dict)
            or info['error']
            or "title" not in info
        ):
            return info
        payload = {
            "action": "query",
            "prop": "extracts|info",
            "exchars": 1200,
            "titles": info['title'],
            "inprop": "url",
            "explaintext": "",
        }
        
        try:
            response = requests.get(
                "https://fr.wikipedia.org/w/api.php", params=payload)
            if response.status_code == 200:
                data = response.json()
                pageid = str(info['pageid'])
                if pageid in data['query']['pages']:
                    info['extract'] = data['query']['pages'][pageid]['extract']
                    info['fullurl'] = data['query']['pages'][pageid]['fullurl']
                else:
                    info['error'] = True

        except ConnectionError:
            pass
        return info