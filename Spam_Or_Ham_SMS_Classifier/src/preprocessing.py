import spacy

nlp = spacy.load("en_core_web_sm", disable=["parser", "ner", "textcat"])

def preprocess_texts(texts):
    processed_texts = []
    for text in texts:
        doc = nlp(text)
        tokens = [
            token.lemma_
            for token in doc
            if token.is_alpha and not token.is_stop and token.pos_ in {"NOUN", "VERB", "ADJ", "PRON"}
        ]
        processed_texts.append(" ".join(tokens))  # join tokens as string for vectorizer
    return processed_texts