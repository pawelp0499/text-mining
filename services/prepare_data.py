from services.clean_text import clean_text
from services.stem_text import *
from services.delete_stopwords import stopwords_del


def prepare_data(dataset):
    dataset = ''.join(dataset['full_tweet'])
    cleaned = clean_text(dataset)
    del_sw = stopwords_del(cleaned)
    result = stemming_list(del_sw)
    return result
