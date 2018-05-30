import re
from gensim.corpora import Dictionary
from gensim.models.ldamodel import LdaModel

class TopicModelPipeline:
    def __init__(self, tf_file, model_file):
        self.tf = Dictionary.load(tf_file)
        self.lda = LdaModel.load(model_file)

    def _sanitize(self, text):
        return re.split(r'\W+', text.strip().lower())

    def infer(self, text):
        """
        First, convert text to vector using gensim's Dictionary doc2bow after simple
        sanitisation.

        Return the inferred topics
        """
        tf = self.tf.doc2bow(self._sanitize(text))

        return self.lda.get_document_topics(tf)