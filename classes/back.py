"""
File Name: back.py
Contained Classes: AppWork
AppWork class used by main.py file to implement the processing of NLP

"""

import pathlib
import sys

import nltk
import pandas as pd
from qalsadi import lemmatizer, analex
import easygui
import os
import pickle
from statistics import mode
from awesometkinter.bidirender import render_text


# nltk.download()


class AppWork:
    """
    This Class had 11 Function
    """

    def create_msg_box(self, text, title):
        """
        This Function is used to create a message box
        :param text: the message that will be shown to the user in the message box (string)
        :param title: the title of the message box (string)
        :used by: main.py
        :return: easygui.msgbox contain the text and title
        """
        return easygui.msgbox(text, title=title)

    def get_file_path(self, msg="please Choose a TxT file", title="Choose file"):
        """
        This Function is used to get the file path
        :param msg: the message that will be shown to the user in the message box
        :param title: the title of the message box
        :used by: check_file_path()
        :return: path of the file that the user chose (string)
        """
        file = easygui.fileopenbox(msg=msg, title=title, filetypes='*.txt')
        return file

    def check_file_path(self):
        """
        This Function is used to check if the file path is valid (.txt)
        :used by: load_file()
        :uses: get_file_path()
        :return: file path (string) if it is valid
        """
        file_path = self.get_file_path()
        filename, file_extension = os.path.splitext(file_path)
        if file_extension == ".txt":
            return file_path

    def load_file(self):
        """
        This Function is used to load the file
        :used by: main.py
        :uses: check_file_path()
        :return: content of the file (string)
        """
        file_path = self.check_file_path()
        file = open(file_path, 'r')
        string = " ".join(line.strip() for line in file)
        file.close()
        return string

    def segment_text(self, inp):
        """
        This Function is used to segment the text
        :param inp: should be a string
        :used by: main.py
        :return: segments of the text (list)
        """
        seg = nltk.data.load('tokenizers/punkt/english.pickle').tokenize(inp)
        return seg

    def tokenize_text(self, inp):
        """
        This Function is used to tokenize the text
        :param inp: should be a string
        :used by: main.py
        :return: tokens of the text (list)
        """
        token = nltk.tokenize.wordpunct_tokenize(inp)
        return token

    def stem_text(self, inp):
        """
        This Function is used to stem the text
        :param inp: the text that will be stemmed (string)
        :used by: main.py
        :uses: tokenize_text()
        :return: the stemmed text (list)
        """
        token = self.tokenize_text(inp)
        stem = []
        for i in token:
            stem.append(nltk.ISRIStemmer().stem(i))
        return stem

    def lemmatize_text(self, inp):
        """
        This Function is used to lemmatize the text
        **This Function takes time more than the-> stem_text() <-due searching in the dictionary
        :param inp: the text that will be lemmatized (string)
        :used by: main.py
        :uses: tokenize_text()
        :return: the lemmatized text (list)
        """
        token = self.tokenize_text(inp)
        lemma = []
        for i in token:
            lemma.append(lemmatizer.Lemmatizer().lemmatize(i))
        return lemma

    def stopword_removal(self, inp):
        """
        This Function is used to remove the stopwords from the text
        :param inp: the text that will be stopword removed (string)
        :used by: main.py
        :uses: tokenize_text()
        :return: the stopword removed text (list)
        """
        arb_stopwords = set(nltk.corpus.stopwords.words("arabic"))
        processed_tokens = self.tokenize_text(inp)
        for i in processed_tokens:
            if i in arb_stopwords:
                processed_tokens.remove(i)
        return processed_tokens

    def decoder(self, val):
        """
        This Function is used to decode the predicted value
        :param val: Number that will be decoded (int)
        :return: the decoded value (string)
        """
        if val == 0:
            return "نص سيئ"
        else:
            return "نص جيد"

    def predict_txt(self, inp):
        """
        This Function is used to predict the text
        :param inp: the text that will be predicted (string)
        :used by: main.py
        :uses: stopword_removal()
        :used file: vectorizer.pickle ,Naive_Bayes_model.sav
        :return: predicted value (int)
        """
        pre_txt = self.stopword_removal(inp)
        vectorizer = pickle.load(open(str(pathlib.Path(__file__).parent.parent) + "/models/vectorizer.pickle", 'rb'))
        file_name = open(str(pathlib.Path(__file__).parent.parent) + '/models/Naive_Bayes_model.sav', 'rb')
        loaded_model = pickle.load(file_name)
        result = loaded_model.predict(vectorizer.transform(pre_txt))
        out = mode(result)
        return self.decoder(int(out))

    def morph_analysis_txt(self, inp):
        """
        This Function is used to morph the text
        :param inp: the text that will be morphed (string)
        :used by: main.py
        :uses: tokenize_text()
        :return: the morph dataframe (dataframe)
        """
        text = inp
        print(text)

        analyzer = analex.Analex()
        analyzer.set_debug(False)
        result = analyzer.check_text(text)
        word_list = []
        for word in result:
            for description in word:
                desc_list = [description.word, description.vocalized, description.type, description.affix,
                             description.root,
                             description.tags, description.stem, description.affix_key, description.type,
                             description.tag_original_number, description.tag_original_gender, description.word]

                if sys.platform == 'linux':
                    word_list.append(map(render_text, desc_list))
                else:
                    word_list.append(desc_list)

        return pd.DataFrame(word_list)
