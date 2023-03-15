from bs4 import BeautifulSoup
import requests
import nltk
from string import punctuation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity 
import numpy as np

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

class ChatBot():
    def __init__(self):
        self.end_chat = False
        self.got_topic = False
        self.do_not_respond = True
        self.title = None
        self.text_data = []
        self.sentences = []
        self.para_indices = []
        self.current_sent_idx = None
        self.punctuation_dict = str.maketrans({p:None for p in punctuation})
        self.lemmatizer = nltk.stem.WordNetLemmatizer()
        self.stopwords = nltk.corpus.stopwords.words('english')
        self.greeting()

    def greeting(self):
        print("Inicializando...")
        print('Digite "sair" para encerrar a conversa')
        print('-'*50)
        print("Bot >>  Olá, sobre o que deseja conversar?")
        
    def chat(self):
        while not self.end_chat:
            self.receive_input()
            if self.end_chat:
                print('\nEncerrando conversa...')
            elif self.got_topic:
                if not self.do_not_respond:
                    self.respond()
                self.do_not_respond = False
    
    def receive_input(self):
        text = input("Você    >> ")
        if text.lower().strip() in ['sair']:
            self.end_chat=True
        elif text.lower().strip() == 'mais':
            self.do_not_respond = True
            if self.current_sent_idx != None:
                response = self.text_data[self.para_indices[self.current_sent_idx]]
            else:
                response = "Sobre o que deseja conversar?"
            print("Bot >>  " + response)
        elif not self.got_topic:
            self.scrape_wiki(text)
        else:
            self.sentences.append(text)
                
    def respond(self):
        vectorizer = TfidfVectorizer(tokenizer=self.preprocess)
        tfidf = vectorizer.fit_transform(self.sentences)
        scores = cosine_similarity(tfidf[-1],tfidf) 
        self.current_sent_idx = scores.argsort()[0][-2]
        scores = scores.flatten()
        scores.sort()
        value = scores[-2]
        if value != 0:
            print("Bot >>  " + self.sentences[self.current_sent_idx]) 
        else:
            print("Bot >>  Não tenho certeza. Desculpe!" )
        del self.sentences[-1]
        
    def scrape_wiki(self,topic):
        topic = topic.lower().strip().capitalize().split(' ')
        topic = '_'.join(topic)
        try:
            link = 'https://pt.wikipedia.org/wiki/'+ topic
            data = requests.get(link).content
            soup = BeautifulSoup(data, 'html.parser')
            p_data = soup.findAll('p')
            dd_data = soup.findAll('dd')
            li_data = soup.findAll('li')
            p_list = [p for p in p_data]
            dd_list = [dd for dd in dd_data]
            li_list = [li for li in li_data]
            for tag in p_list+dd_list+li_list:
                a = []
                for i in tag.contents:
                    if i.name != 'sup' and i.string != None:
                        stripped = ' '.join(i.string.strip().split())
                        a.append(stripped)
                self.text_data.append(' '.join(a))
            
            for i,para in enumerate(self.text_data):
                sentences = nltk.sent_tokenize(para)
                self.sentences.extend(sentences)
                index = [i]*len(sentences)
                self.para_indices.extend(index)
            
            self.title = soup.find('h1').string
            self.got_topic = True
            print('Bot >>  "{}", ok, vamos conversar!'.format(self.title)) 
        except Exception as e:
            pass

    def preprocess(self, text):
        text = text.lower().strip().translate(self.punctuation_dict) 
        words = nltk.word_tokenize(text)
        words = [w for w in words if w not in self.stopwords]
        return [self.lemmatizer.lemmatize(w) for w in words]
      
b = ChatBot()
b.chat()
