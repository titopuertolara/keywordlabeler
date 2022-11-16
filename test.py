from keybert import KeyBERT

doc = """
        Soy un experto en derecho con especialización en derechoi laboral.
      """
kw_model = KeyBERT(model='paraphrase-multilingual-mpnet-base-v2')
keywords = kw_model.extract_keywords(doc)