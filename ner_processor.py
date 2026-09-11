import spacy

nlp = spacy.load("en_core_web_sm")


def extract_entities(text):
    """
    Extract PERSON, ORG and LOCATION entities from text.
    """

    doc = nlp(text)

    entities = []

    for ent in doc.ents:

        if ent.label_ in ["PERSON", "ORG", "GPE", "LOC"]:

            if ent.label_ in ["GPE", "LOC"]:
                entity_type = "LOCATION"
            else:
                entity_type = ent.label_

            entities.append({
                "entity": ent.text.strip(),
                "type": entity_type
            })

    return entities


if __name__ == "__main__":

    text = """
    Narendra Modi visited Ahmedabad.
    Google and Microsoft announced a new project.
    """

    print("INPUT TEXT:")
    print(text)

    print("\nEXTRACTED ENTITIES:")

    result = extract_entities(text)

    for entity in result:
        print(entity)