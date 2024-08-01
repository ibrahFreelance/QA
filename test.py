from openai import OpenAI
from dotenv import load_dotenv
from llama_index.core.tools import BaseTool, FunctionTool

load_dotenv()
client = OpenAI()


def synonyms_antonyms_determination(user_input):
    """ Used to determine relations between two words"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an AI assistant with expertise in linguistics and semantics"},
            {"role": "system",
             "content": "Your task is to analyze two given words and determine the relationship between them"},
            {"role": "system", "content": "words could be in Arabic language so response with Arabic if so"},
            {"role": "system", "content": " Explain in details the relation between the given words"},
            {"role": "system", "content": "Consider the context and common usage of the words to make an accurate "
                                          "determination. Please provide a brief explanation for your decision."},
            {"role": "system", "content": """Examples:
    
                Words: Happy, Joyful
                
                Relationship: Synonyms
                Explanation: Both words describe a state of being pleased or content.
                Words: Hot, Cold
                
                Relationship: Antonyms
                Explanation: 'Hot' refers to a high temperature, whereas 'Cold' refers to a low temperature.
                Words: Eye:Glass
                
                Relationship: Corrective Explanation:  Glasses are designed to adjust the focus of light entering the 
                eyes, thereby improving vision clarity for individuals with refractive errors such as 
                nearsightedness, farsightedness, or astigmatism. Hence, the word "corrective" encapsulates the 
                purpose and function of glasses in relation to the eyes.        
                """},
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
             "content": "Your task is to randomly generate two words with any relation between them without providing "
                        "the relation to keep user guess"},
            {"role": "system", "content": "If user didn't specify the relation feel free to generate any"},
            {"role": "system", "content": "if user input was in Arabic so generate Arabic words"},
            {"role": "system", "content": "Consider the context and common usage of the words to make an accurate "
                                          "determination."},
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
                Chilly
                USer Request: Generate words with any relation between them.  
                Generated Word: Eye:Glass , Car:Gas, Light:Dark, Water:Human  
                """},
            {"role": "user", "content": f"{user_input}"}
        ]
    )
    return response.choices[0].message.content


synonyms_antonyms_tool = FunctionTool.from_defaults(fn=synonyms_antonyms_determination,
                                                    name="synonyms_antonyms_determination")
synonyms_antonyms_generation_tool = FunctionTool.from_defaults(fn=synonyms_antonyms_generation,
                                                               name="synonyms_antonyms_generation")
