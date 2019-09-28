# coding: utf-8

import requests
from requests.exceptions import ConnectionError


class GoogleMapsDownloader:

    def find_place(self, question):
        # -tc- Plutôt que de retourner toute la réponse, on va juste retourner
        # -tc- les infos qui nous intéresse.
        # -tc- On part du principe qu'il y a une erreur et on l'annule si la
        # -tc- requête est un succès.
        info = {
            "address": "",
            "lat": None,
            "lng": None,
            "error": True
        }
        # -tc- Si la question est une chaine vide ou que la question n'est pas
        # -tc- une chaine de caractère, on retourne les infos vides.
        if not question or not isinstance(question, str):
            return info
        # -tc- début de la requête
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
            # -tc- Utiliser try-except pour capturer les erreurs de connexion
            response = requests.get(url, params=payload)
            # -tc- S'assurer que le status de la réponse est 200 (OK)
            if response.status_code == 200:
                data = response.json()
                # -tc- S'assurer que Google Maps a trouvé quelque chose
                if data['candidates']:
                    info['address'] = (
                        data['candidates'][0]["formatted_address"]
                    )
                    info['latitude'] = (
                        data['candidates'][0]['geometry']['location']["lat"]
                    )
                    info['longitude'] = (
                        data['candidates'][0]['geometry']['location']["lng"]
                    )
                    info['error'] = True
        except ConnectionError:
            pass
        return info


class WikiDownloader:

    def fetch_by_coord(self, location):
        # -tc- Plutôt que de retourner toute la réponse, on va juste retourner
        # -tc- les infos qui nous intéresse.
        # -tc- On part du principe qu'il y a une erreur et on l'annule si la
        # -tc- requête est un succès.
        info = {
            "title": "",
            "pageid": None,
            "extract": "",
            "fullurl": "",
            "error": True,
        }
        # On vérifie que location est bien ce à quoi on s'attend
        if (
            not location
            or not isinstance(location, dict)
            or "latitude" not in location
            or "longitude" not in location
            or location['error']
        ):
            return info
        # -tc- début de la requête
        payload = {
            "action": "query",
            "list": "geosearch",
            "gsradius": 200,
            # "gscoord": str(location['lat']) + "|" + str(location['lng']),
            # -tc- tu peux utiliser une f-string ici
            "gscoord": f"{location['latitude']}|{location['longitude']}",
            "gslimit": 1,
        }

        # -tc- Utiliser try-except pour capturer les erreurs de connexion
        try:
            response = requests.get(
                "https://fr.wikipedia.org/w/api.php", params=payload
            )
            # -tc- On vérifie que la requête a été un succès
            if response.status_code == 200:
                data = response.json()
                # -tc- On vérifie que wiki a trouvé quelque chose. Si ce n'est pas
                # -tc- le cas, la liste retournée est vide. On décide ici de
                # -tc- le premier article retourné.
                if data['query']['geosearch']:
                    info['title'] = data['query']['geosearch'][0]['title']
                    info['pageid'] = data['query']['geosearch'][0]['pageid']
                    # -tc- la requête a fonctionné, pas d'erreur
                    info['error'] = False
        except ConnectionError:
            # -tc- Si il y a eu une erreur de connection, le dictionnaire info
            # -tc- indique déjà l'erreur. Rien à faire.
            pass
        # -tc- On retourne finalement le dictionnaire avec les infos obtenues
        return info

    # def fetch_by_title(self, title, pageid):
    def fetch_by_title(self, info):
        # -tc- On s'assure qu'info est ce à quoi on s'attend et qu'il ne 
        # -tc- signale pas d'erreur
        if (
            not info
            or not isinstance(info, dict)
            or info['error']:
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
        
        # -tc- On vérifie qu'il n'y a pas d'erreur de connextion avec un try
        try:
            response = requests.get(
                "https://fr.wikipedia.org/w/api.php", params=payload)
            # -tc- On vérifie que la requête a bien renvoyé un status 200
            if response.status_code == 200:
                data = response.json()
                # On vérifie que l'article a été trouvé
                pageid = str(info['pageid'])
                if pageid in data['query']['pages']:
                    info['extract'] = data['query']['pages'][pageid]['extract']
                    info['fullurl'] = data['query']['pages'][pageid]['fullurl']
                else:
                    info['error'] = True

        except ConnectionError:
            pass
        return info