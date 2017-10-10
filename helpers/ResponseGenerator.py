from helpers.Scorer import Scorer
import pandas as pd
from config import Config
from helpers import AnswerGenerator


CATEGORY_MAPPING = {
    "b": "business",
    "e": "entertainment",
    "m": "health",
    "t": "science and technology"
}


def generate_response(req):
    query = req["result"]["resolvedQuery"]

    sc = Scorer("model/best-model.pkl")

    short_category, probability = sc.score_all(pd.Series([query]))

    category = CATEGORY_MAPPING.get(str(short_category))
    probability_formated = "{:0.2f}".format(probability)

    if probability >= Config.SCORING_THRESHOLD:
        answer_type = 'answer_with_probability'
    else:
        answer_type = 'answer_pass_to_consultant'

    return AnswerGenerator.generate_answer(answer_type, [category, probability_formated])
