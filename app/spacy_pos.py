from typing import List, Dict
from spacy import Language


class SpacyPOS:
    """
    class SpacyPOS encapsulates logic to pipe Records with an id and text body
    through a spacy model and return text separated by part of speech
    """

    pos_friendly_names = {
        "nouns": ["PROPN", "NOUN",],
        "pronouns": [ "PRON"],
        "verbs": ["VERB", "AUX"],
        "adjectives":["ADJ"],
        "adverbs": ["ADV", "PART",],
        "prepositions": ["ADP"],
        "conjunctions": ["CCONJ",],
        "interjections": ["INTJ"],
        "articles": ["DET"]
    }


    def __init__(
            self, nlp: Language, input_id_col: str = "id", input_text_col: str = "text"
    ):
        """Initialize the SpacyPOS pipeline.

        nlp (spacy.language.Language): pre-loaded spacy language model
        input_text_col (str): property on each document to run the model on
        input_id_col (str): property on each document to correlate with request

        """
        self.nlp = nlp
        self.input_id_col = input_id_col
        self.input_text_col = input_text_col

    def extract_pos(self, records: List[Dict[str, str]]):
        """
        Applies the pre-trained model to a batch of records.

        RETURNS (list): List of responses containing the document id and a categorizing of all words by part of speech.
        """

        ids = (doc[self.input_id_col] for doc in records)
        texts = (doc[self.input_text_col] for doc in records)

        res = {}

        for doc_id, spacy_doc in zip(ids, self.nlp.pipe(texts)):
            pos = {
                "articles": [],
                "pronouns": [],
                "nouns": [],
                "interjections": [],
                "conjunctions": [],
                "verbs": [],
                "adverbs": [],
                "prepositions": [],
                "adjectives": []
            }

            for token in spacy_doc:
                print(f"${token} - ${token.pos_}")
                for count, fn in enumerate(self.pos_friendly_names.keys()):
                    if token.pos_ in self.pos_friendly_names[fn]:
                        pos[fn].append(str(token))

            res[doc_id] = pos

        return res

