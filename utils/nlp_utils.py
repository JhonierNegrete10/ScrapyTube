import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class PreprocessingData:

    def __init__(self):
        self.stop_words_es = set(stopwords.words('spanish')) 
        self.stop_words_en = set(stopwords.words('english'))
        self.stop_words = set(["cómo"])
        # print(self.stop_words)
        self.stop_words = self.stop_words.union( self.stop_words_en )
        # print(self.stop_words)
        self.stop_words = self.stop_words.union( self.stop_words_es )
        # print(self.stop_words)
        
        

    def process_text(self, text: str, lngs):
        lng = None 
        words = word_tokenize(text.lower())
        
        # Determinar el idioma del título basado en las stopwords restantes
        if any(token in self.stop_words_es for token in words):
            lng=  "es"
        elif any(token in self.stop_words_en for token in words):
            lng = "en"
        lngs.append(lng)
        words = [word for word in words if word.isalnum() and word not in self.stop_words]
        return words, lng 
    
data = PreprocessingData()  
"""
        
        import nltk
        nltk.download(‘omw’)
        nltk.download(‘wordnet’)
        nltk.download(‘omw-1.4’)
        from nltk.corpus import wordnet as wn

        # bettering tokens with nltk
        pattern = r'''(?x)                  # Flag para iniciar el modo verbose
                    (?:[A-Z]\.)+          # Hace match con abreviaciones como U.S.A.
                    | \w+(?:-\w+)*        # Hace match con palabras que pueden tener un guión interno
                    | \$?\d+(?:\.\d+)?%?  # Hace match con dinero o porcentajes como $15.5 o 100%
                    | \.\.\.              # Hace match con puntos suspensivos
                    | [][;"'?():-_`]      # Hace match con signos de puntuación
        '''
        tokens2 = nltk.regexp_tokenize(raw, pattern)
        print(tokens2[:50]) 
"""