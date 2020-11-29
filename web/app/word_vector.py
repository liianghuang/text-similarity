from app import app
from app import document
import wikipedia2vec as wiki
import numpy as np

class WordVec(document.Doc):
    def __init__(self, path):
        super().__init__()
        self.file_path = path
        self.wiki2vec = wiki.Wikipedia2Vec.load(path)
    
    def vect_doc(self, document):
        """
        represent document with word vectors
        """
        words_set = self.pre_process(document)
        word_vectors = []
        for w in words_set:
            try:
                vec = self.wiki2vec.get_word_vector(w)
                word_vectors.append(vec)
            except:
                pass
        
        vector = np.mean(word_vectors, axis=0)
        return vector
    
    def cosine_sim(self, vec1, vec2):
        c_sim = np.dot(vec1, vec2)/(np.linalg.norm(vec1)*np.linalg.norm(vec2))
        if np.isnan(np.sum(c_sim)):
            return 0
        return c_sim
    
    def get_similiarity(self, doc1, doc2):
        doc1_vec = self.vect_doc(doc1)
        doc2_vec = self.vect_doc(doc2)
        score = 0
        score = self.cosine_sim(doc1_vec, doc2_vec)
        if score:
            return score.astype(float)
        else:
            return 0
