import openai

import os
import openai

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.environ['OPENAI_API_KEY']

# Configure the model ID. Change this to your model ID.
model = "ft:gpt-3.5-turbo-0125:personal:drug-malady-data:ATORblu6"

# Let's use a drug from each class
drugs = [
    "A CN Gel(Topical) 20gmA CN Soap 75gm",  # Class 0
    "Attentin 10mg Capsule 10'S",                    # Class 1
    "ABICET M Tablet 10's",                  # Class 2
]

# Returns a drug class for each drug
for drug_name in drugs:
    prompt = [{"role": "system", "content": ""},
    {"role": "user", "content": "Drug: {}\nMalady:".format(drug_name)}]

    response = openai.ChatCompletion.create(
        model=model,
        messages=prompt
    )

    # Print the generated text
    drug_class = response.choices[0].message.content
    # The result should be 0, 1, and 2
    print(drug_class)

print()

# Let's use a drug from each class
drugs = [
    "What is 'A CN Gel(Topical) 20gmA CN Soap 75gm' used for?",  # Class 0
    "What is 'Attentin 10mg Capsule 10'S' used for?",  # Class 1
    "What is 'ABICET M Tablet 10's' used for?",  # Class 2
]

class_map = {
    0: "Acne",
    1: "ADHD",
    2: "Allergies",
    # ...
}

# Returns a drug class for each drug
for drug_name in drugs:
    prompt = [{"role": "system", "content": ""},
    {"role": "user", "content": "Drug: {}\nMalady:".format(drug_name)}]

    response = openai.ChatCompletion.create(
        model=model,
        messages=prompt,
        temperature=1
    )

    response = response.choices[0].message.content
    try:
        print(drug_name + " is used for " + class_map[int(response)])
    except:
        print("I don't know what " + drug_name + " is used for.")
    print()
