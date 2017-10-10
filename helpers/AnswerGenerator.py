# -*- coding: utf-8 -*-
ANSWER_TYPES = {
    "answer_with_probability": "This news is from {0} category (with probability of classification {1}",
    "answer_pass_to_consultant": "Pass to consultant (probability={1} is below threshold for category {0})",
    "answer_specify_additional_info": "Please specify {2}"

}


def generate_answer(answer_type, answers_formatting_list):
    return ANSWER_TYPES[answer_type].format(*answers_formatting_list)

if __name__ == "__main__":
    print generate_answer("answer_pass_to_consultant", ["e", "0.4"])