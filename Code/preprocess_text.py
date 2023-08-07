import Sastrawi
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.tokenize import word_tokenize

def preprocess_data(text):
    # Lowercasing
    text = text.lower()
    
    # Remove punctuation
    separator = '|'
    hapus_tandabaca = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{}~'
    delete =str.maketrans(dict.fromkeys(hapus_tandabaca,''))
    text = text.translate(delete)
    
    # Stemming
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    tokens = word_tokenize(text)
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    
    # Tokenizing
    tokens = ' '.join(stemmed_tokens).split()
    
    return tokens
