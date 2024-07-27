import os
from docx import Document
import pandas as pd


def extract_questions_and_choices(directory_path, output_path):
    questions = []
    choices = []

    for filename in os.listdir(directory_path):
        if filename.endswith(".docx"):
            # Load the DOCX file
            doc_path = os.path.join(directory_path, filename)
            doc = Document(doc_path)

            # Extract text from each paragraph
            lines = [para.text.strip() for para in doc.paragraphs if para.text.strip()]

            # Iterate over the lines and separate questions and choices based on the index
            for i, line in enumerate(lines):
                if i % 2 == 0:
                    questions.append(line)
                else:
                    choices.append(line)

    results = {'questions': questions, 'choices': choices}

    df = pd.DataFrame(results)
    print(df.head())
    df.to_csv(output_path, index=False)
    print(output_path)
