import nltk
import qalsadi.lemmatizer
import easygui
import os
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle


# nltk.download()
def create_msg_box(text, title):
    return easygui.msgbox(text, title=title)


def get_file_path(msg="please Choose a TxT file", title="Choose file"):
    file = easygui.fileopenbox(msg=msg, title=title, filetypes='*.txt')
    return file


def check_file_path():
    file_path = get_file_path()
    filename, file_extension = os.path.splitext(file_path)
    if file_extension == ".txt":
        return file_path


def load_file():
    file_path = check_file_path()
    file = open(file_path, 'r')
    string = " ".join(line.strip() for line in file)
    file.close()
    return string


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


def predict_txt(inp):
    vectorizer = TfidfVectorizer()
    inp_tfidf = vectorizer.fit_transform([inp])
    file_name = open('models/Naive_Bayes_model.sav', 'rb')
    loaded_model = pickle.load(file_name)
    result = loaded_model.predict(inp_tfidf)
    print(result)


predict_txt("كيف حالك يا صديقي")
