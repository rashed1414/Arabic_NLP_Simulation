import pathlib
import nltk
import qalsadi.lemmatizer
import easygui
import os
import pickle
from statistics import mode



# nltk.download()


class AppWork:

    def create_msg_box(self, text, title):
        return easygui.msgbox(text, title=title)

    def get_file_path(msg="please Choose a TxT file", title="Choose file"):
        file = easygui.fileopenbox(msg=msg, title=title, filetypes='*.txt')
        return file

    def check_file_path(self):
        file_path = self.get_file_path()
        filename, file_extension = os.path.splitext(file_path)
        if file_extension == ".txt":
            return file_path

    def load_file(self):
        file_path = self.check_file_path()
        file = open(file_path, 'r')
        string = " ".join(line.strip() for line in file)
        file.close()
        return string

    def segment_text(self, inp):
        seg = nltk.data.load('tokenizers/punkt/english.pickle').tokenize(inp)
        return seg

    def tokenize_text(self, inp):
        token = nltk.tokenize.wordpunct_tokenize(inp)
        out = []
        for i in token:
            out.append(i)
        return out

    def stem_text(self, inp):
        token = self.tokenize_text(inp)
        out = []
        for i in token:
            out.append(nltk.ISRIStemmer().stem(i))
        return out

    def lemmatize_text(self, inp):
        token = self.tokenize_text(inp)
        out = []
        for i in token:
            out.append(qalsadi.lemmatizer.Lemmatizer().lemmatize(i))
        return out

    def stopword_removal(self, inp):
        arb_stopwords = set(nltk.corpus.stopwords.words("arabic"))
        processed_tokens = self.tokenize_text(inp)
        for i in processed_tokens:
            if i in arb_stopwords:
                processed_tokens.remove(i)
        return processed_tokens

    def decoder(self, val):
        if val == 0:
            return "نص سيئ"
        else:
            return "نص جيد"

    def predict_txt(self, inp):
        pre_txt = self.stopword_removal(inp)
        vectorizer = pickle.load(open(str(pathlib.Path(__file__).parent.parent) + "/models/vectorizer.pickle", 'rb'))
        file_name = open(str(pathlib.Path(__file__).parent.parent) + '/models/Naive_Bayes_model.sav', 'rb')
        loaded_model = pickle.load(file_name)
        result = loaded_model.predict(vectorizer.transform(pre_txt))
        out=mode(result)
        return self.decoder(out)

