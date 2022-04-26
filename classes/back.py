import nltk
import qalsadi.lemmatizer


# nltk.download()

def load_file():
    pass

def segment_text(inp):
    seg = nltk.data.load('tokenizers/punkt/english.pickle').tokenize(inp)
    return seg


def tokenize_text(inp):
    token = nltk.tokenize.wordpunct_tokenize(inp)
    out = []
    for i in token:
        out.append(i)

    return out


def stem_text(inp):
    token = tokenize_text(inp)
    out = []
    for i in token:
        out.append(nltk.ISRIStemmer().stem(i))
    return out


def lemmatize_text(inp):
    token = tokenize_text(inp)
    out = []
    for i in token:
        out.append(qalsadi.lemmatizer.Lemmatizer().lemmatize(i))

    return out


def stopword_removal(inp):
    arb_stopwords = set(nltk.corpus.stopwords.words("arabic"))
    processed_tokens = tokenize_text(inp)
    for i in processed_tokens:
        if i in arb_stopwords:
            processed_tokens.remove(i)

    return processed_tokens
