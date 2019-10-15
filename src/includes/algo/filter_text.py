def suppCarSpec(Tweet):
    caractereSpeciaux = {}
    temp = {
        "áâäàáâä": "a",
        "èéêëèéêë": "e",
        "ìíîïìíîï": "i",
        "òóôöòóôö": "o",
        "ùúûüùúûüµ": "u",
        "ñ": "n",
        "ç": "c",
        "œ": "oe",
        "#": "",
        "-": " "
    }
    for key, value in temp.items():
        for c in key:
            caractereSpeciaux[c] = value

    for x in Tweet:
        if (x in caractereSpeciaux):
            Tweet=Tweet.replace(x, caractereSpeciaux[x])

    return Tweet

def filter_text(text):
    text = text.lower()
    text=suppCarSpec(text)
    # Tweet=changeCar(Tweet)
    return text
