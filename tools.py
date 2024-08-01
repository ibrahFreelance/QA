from llama_index.core.tools import BaseTool, FunctionTool
from links import error_dir, com_dir
import pandas as pd
from random import randint
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()


def error_tool(user_input):
    """This function used to Generate Contextual error questions by taking user input
    to generate Contextual error questions based on user input """

    response = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {"role": "system", "content": "You are an AI assistant with expertise in linguistics"},
            {"role": "system", "content": "your goal is to Generate random multiple-choice questions containing "
                                          "statements with an incorrect word. The goal is to identify the incorrect "
                                          "word in the statement."},
            {"role": "system", "content": """Instructions:

                Create a statement with one incorrect word.
                Formulate a multiple-choice question asking to identify the incorrect word in the statement.
                Provide four answer choices:
                One correct answer that identifies the incorrect word.
                Three plausible but incorrect answers."""},
            {"role": "system", "content": """Example:

                Question:
                "Humanity must always seek war."
                
                Which word in the above statement is incorrect?
                
                Choices:
                A. Humanity
                B. Must
                C. Seek
                D. War"""},
            {"role": "system", "content": """Generate the following:

                Question:
                [Insert statement with an incorrect word]
                
                Which word in the above statement is incorrect?
                
                Choices:
                A. [Choice A]
                B. [Choice B]
                C. [Choice C]
                D. [Choice D]"""},
            {"role": "system", "content": "if user didn't specify how many question generate 3 at least"},
            {"role": "system", "content": "If user language was Arabic generate questions with Arabic"},
            {"role":"user","content":f"{user_input}"}
        ]
    )

    return response.choices[0].message.content


def complate_tool(user_input):
    """ This function used to generate Complete the sentence questions by taking  user input to generate Complete the
    sentence questions"""
    response = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {"role": "system", "content": "You are an AI assistant with expertise in linguistics"},
            {"role": "system", "content": "your goal is to Generate sentence completion questions with "
                                          "multiple-choice options. The goal is to provide a partially completed "
                                          "sentence with at least two placeholders and four choices for completing "
                                          "it, where only one choice correctly completes the sentence."},
            {"role": "system", "content": """Instructions:

                                            Create a partially completed sentence with at least two placeholders.
                                            Formulate a question asking to complete the sentence.
                                            Provide four answer choices:
                                            One correct answer that completes the sentence accurately.
                                            Three plausible but incorrect answers.."""},
            {"role": "system", "content": """Example:

                    Question:
                    "During the storm, the power went out, and we had to use ______ to see and ______ to stay warm."
                    
                    Choices:
                    A. flashlights; blankets
                    B. telephones; fans
                    C. computers; heaters
                    D. televisions; lights
                    
                    Correct Answer: A"""},
            {"role": "system", "content": """Generate the following:

                Question:
                [Insert partially completed sentence with at least two placeholders]

                Choices:
                A. [Choice A]
                B. [Choice B]
                C. [Choice C]
                D. [Choice D]"""},
            {"role": "system", "content": "if user didn't specify how many question generate 3 at least"},
            {"role": "system", "content": "If user language was Arabic generate questions with Arabic"},
            {"role":"system","content": "Don't include the correct answer as the user will try to solve it"},
            {"role": "user", "content": f"{user_input}"}
        ]
    )

    return response.choices[0].message.content


error = FunctionTool.from_defaults(fn=error_tool, name="contextual_error")
complate = FunctionTool.from_defaults(fn=complate_tool, name="Complete_the_sentence")



"""
    er_df = pd.read_csv(f"{com_dir}\\result.csv", index_col=False)
    result = {}
    for i in range(question_number):
        v = randint(1, er_df.shape[0])
        result[er_df['questions'][v]] = er_df['choices'][v]"""


"""er_df = pd.read_csv(f"{error_dir}\\error.csv", index_col=False)
    result = {}
    for i in range(question_number):
        v = randint(1, er_df.shape[0])
        #print(er_df['questions'][v], er_df['choices'][v])
        result[er_df['questions'][v]] = er_df['choices'][v]
    return result"""


