import spacy
import re

nlp = spacy.load('en_core_web_sm')


def common_word_swaps(tokens):
    words = {
        'entertain':'entertaining',
        'enjoy':'enjoyable',
        'provoke':'provoking',
        'joyous':'joyful',
        'amuse':'amusing',
        'gre':'grey',
        'ok':'okay',
        '""""':''
        # 'fee':'',
        # 'fhjhffhjkhhh':''
    }
    for key in words.keys():
        tokens = [words[key] if token==key else token for token in tokens]
    return tokens


def tokenize(text: str) -> list:
    
    # process string with spacy
    doc = nlp(text)
    tokens = [token for token in doc]
    tokens = [token for token in tokens if re.search(r'\S', token.text)]
    tokens = [token for token in tokens if re.search(r'\D', token.text)]
    tokens = [token.lemma_ for token in tokens]

    # Combine negations
    for i in range(len(tokens)-2, -1, -1):
        if tokens[i] == 'not':
            tokens[i] = tokens[i] + '_' + tokens.pop(i+1)

    # remove stopwords
    all_stopwords = nlp.Defaults.stop_words
    all_stopwords |= {'f','c','sp','""""','ir','d','_','b','fhjhffhjkhhh','fee','fhjfdcccvgjjhvvfddtghjjjjmmk','hhikjjhyyhjjj','"'}
    tokens = [token for token in tokens if not token in all_stopwords]

    # Remove pronouns
    tokens = [token for token in tokens if token!='-PRON-']
    tokens = common_word_swaps(tokens)

    return tokens