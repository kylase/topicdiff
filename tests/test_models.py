import os
import pytest
from gensim.models.ldamodel import LdaModel
from gensim.corpora.dictionary import Dictionary

from flask import current_app
from app.common.topic_model import TopicModelPipeline

def test_load_models(app):
    MODELS_DIR = app.config.get('MODELS_DIR')
    MODEL_TYPE = 'wikipedia'
    model_files = {
        'tf': os.path.join(MODELS_DIR, MODEL_TYPE, 'tf'),
        'lda': os.path.join(MODELS_DIR, MODEL_TYPE, 'lda')
    }

    pipeline = TopicModelPipeline(model_files['tf'], model_files['lda'])

    assert isinstance(pipeline.tf, Dictionary)
    assert isinstance(pipeline.lda, LdaModel)
        
def test_pipeline_infer(app):
    MODELS_DIR = app.config.get('MODELS_DIR')
    MODEL_TYPE = 'wikipedia'
    model_files = {
        'tf': os.path.join(MODELS_DIR, MODEL_TYPE, 'tf'),
        'lda': os.path.join(MODELS_DIR, MODEL_TYPE, 'lda')
    }

    pipeline = TopicModelPipeline(model_files['tf'], model_files['lda'])
    text = """USS Orizaba was a transport ship for the U.S. Navy in World War I and World War II, first commissioned on 27 May 1918. Orizaba made 15 transatlantic voyages for the Navy carrying troops to and from Europe in World War I with the second-shortest average in-port turnaround time of all Navy transports. The ship was turned over to the War Department in 1919 for use as Army transport USAT Orizaba. After the war, the troopship reverted to the Ward Line, her previous owners. In World War II the ship was requisitioned by the War Shipping Administration and again assigned to the War Department, but was soon transferred to the U.S. Navy as USS Orizaba (AP-24). The ship made several transatlantic runs, was damaged in an air attack in the Allied invasion of Sicily, made trips to South America, and served in the Pacific Theatre. In June 1945 the ship was transferred under Lend-Lease to the Brazilian Navy, where she served as Duque de Caxias (U-11). Permanently transferred to Brazil in 1953, the ship was decommissioned in 1959 and scrapped in 1963."""
    topics = pipeline.infer(text)
    for topic in topics:
        assert isinstance(topic, (tuple))