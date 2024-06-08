import openai
from dotenv import dotenv_values
config = dotenv_values(".env")
openai.api_key = config["api"]
keep_writing = True
limit = 0

def generate_blog(paragraph_topic):
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "Napisz akapit na następujący temat. " + paragraph_topic},
        ],
        max_tokens = 400,
        temperature = 0.3
    )

    retrieve_blog = response.choices[0].message['content']

    return retrieve_blog

while keep_writing and limit <2:
    odp = input('Napisać akapit? Y for yes, anything else for no. ')
    if (odp == 'y'):
        paragraph_topic = input('O czym piszemy? ')
        print(generate_blog(paragraph_topic))
        limit +=1
    else:
        keep_writing = False

if limit >=2:
    print('Przekroczono limit zapytań!')

