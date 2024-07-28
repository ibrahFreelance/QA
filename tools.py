from llama_index.core.tools import BaseTool, FunctionTool
from links import error_dir, com_dir
import pandas as pd
from random import randint


def error_tool(question_number=5):
    """This function used to retrieve Contextual error questions by taking an int values which is how many questions
    to retrieve and return a dict where keys is questions and values is choices """

    er_df = pd.read_csv(f"{com_dir}\result.csv", index_col=False)
    result = {}
    for i in range(question_number):
        v = randint(1, er_df.shape[0])
        result[er_df['questions'][v]] = er_df['choices'][v]

    return result


def complate_tool(question_number=5):
    """ This function used to retrieve Complete the sentence questions by taking an int values
     which is how many questions to retrieve and return a dict where keys is questions and values is choices """

    er_df = pd.read_csv(f"{error_dir}\error.csv", index_col=False)
    result = {}
    for i in range(question_number):
        v = randint(1, er_df.shape[0])
        #print(er_df['questions'][v], er_df['choices'][v])
        result[er_df['questions'][v]] = er_df['choices'][v]
    return result


error = FunctionTool.from_defaults(fn=error_tool, name="contextual_error")
complate = FunctionTool.from_defaults(fn=complate_tool, name="Complete_the_sentence")
