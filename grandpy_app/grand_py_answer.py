import random

def grand_py_answer(error):
    """  grand py response  """

    if error:
        grandpy_answer1 = random.choice(
            [
            "Ah non mon ptit gars. Là je vois pas de quoi tu parles !",
            "Tu sais je suis un sourd. Tu peux répéter en articulant ?",
            "Je ne connais pas. Tu es sur que ce lieu existe ?"
            ]
        )
        grandpy_answer2 = ""
    else:
        grandpy_answer1 = random.choice(
            [
            "J'ai bien trouvé le lieu que tu cherchais. L'adresse est : ",
            "Ouaip poussin, je connais ! L'adresse, c'est : ",
            "Effectivement mon petit. C'est ici : "
            ]
        )

        grandpy_answer2 = random.choice(
            [
            "Et mais je connais ce quartier ! Dans le coin tu as un endroit que je connais bien. J'habitais juste en face ! ",
            "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? ",
            "Je pourrais t'en raconter de belles sur ce coin. Tiens par exemple. "
            ]
        )
    return grandpy_answer1, grandpy_answer2
