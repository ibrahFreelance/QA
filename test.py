from openai import OpenAI
from dotenv import load_dotenv
from llama_index.core.tools import BaseTool, FunctionTool

load_dotenv()
client = OpenAI()


def synonyms_antonyms_determination(user_input):
    """ Used to determine synonyms  or antonyms in user input """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an AI assistant with expertise in linguistics and semantics"},
            {"role": "system",
             "content": "Your task is to analyze two given words and determine whether they are antonyms ("
                        "words with opposite meanings) or synonyms (words with similar meanings)"},
            {"role": "system", "content": "words could be in Arabic language so response with Arabic if so"},
            {"role": "system", "content": " 'antonyms' mean تضاد in Arabic and synonyms mean ترادف in arabic"},
            {"role": "system", "content": "Consider the context and common usage of the words to make an accurate "
                                          "determination. Please provide a brief explanation for your decision."},
            {"role": "system", "content": """Examples:
    
                Words: Happy, Joyful
                
                Relationship: Synonyms
                Explanation: Both words describe a state of being pleased or content.
                Words: Hot, Cold
                
                Relationship: Antonyms
                Explanation: 'Hot' refers to a high temperature, whereas 'Cold' refers to a low temperature."""},
            {"role": "user", "content": f"{user_input}"}
        ]
    )
    return response.choices[0].message.content


def synonyms_antonyms_generation(user_input):
    """ Used to generate synonyms  or antonyms words"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an AI assistant with expertise in linguistics and semantics"},
            {"role": "system",
             "content": "Your task is to randomly generate a word and then provide a list of either synonyms or "
                        "antonyms for that word  based on the user's request. Ensure the synonyms or antonyms are "
                        "relevant and commonly used."},
            {"role": "system", "content": "If user didn't specify Synonyms or antonyms generate at least 3 of each"},
            {"role": "system", "content": "if user input was in Arabic so generate Arabic words"},
            {"role": "system", "content": " 'antonyms' mean تضاد in Arabic and synonyms mean ترادف in arabic"},
            {"role": "system", "content": "Consider the context and common usage of the words to make an accurate "
                                          "determination. Please provide a brief explanation for your decision."},
            {"role": "system", "content": """Example:

                User Request: Generate a word and its synonyms.
                
                Generated Word: Happy
                
                Synonyms:
                
                Joyful
                Content
                Cheerful
                User Request: Generate a word and its antonyms.
                
                Generated Word: Hot
                
                Antonyms:
                
                Cold
                Cool
                Chilly"""},
            {"role": "user", "content": f"{user_input}"}
        ]
    )
    return response.choices[0].message.content


synonyms_antonyms_tool = FunctionTool.from_defaults(fn=synonyms_antonyms_determination,
                                                    name="synonyms_antonyms_determination")
synonyms_antonyms_generation_tool = FunctionTool.from_defaults(fn=synonyms_antonyms_generation,
                                                               name="synonyms_antonyms_generation")
