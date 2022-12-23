import requests
import os
import openai

# main
def main():
    # Set the OpenAI API key
    openai.api_key = os.getenv('OPENAI_API_KEY')

    # Get the new crossword data
    data = get_crossword_data()

    # Read the cluses 
    clues = read_clues(data)

    # for each clue, generate a prompt to send to OpenAI
    prompts = generate_prompts(clues)

    # for each prompt, send it to OpenAI and get the answer
    answers = get_answers(prompts)

    # correlate the answers with the clues
    for i in range(len(clues)):
        clues[i]['answer'] = answers[i]
    # print the clues along with the answer, grouping by direction
    print_clues(clues)

# Get the JSON crossword data from the New York Times at https://www.nytimes.com/svc/crosswords/v6/puzzle/mini.json
def get_crossword_data():
    # Request the data at https://www.nytimes.com/svc/crosswords/v6/puzzle/mini.json
    response = requests.get("https://www.nytimes.com/svc/crosswords/v6/puzzle/mini.json")
    # Get the JSON data from the response
    data = response.json()
    # return the data
    return data

# Read the clues from the JSON data
# And calculate the length of the answer for each clue based on its number of cells
def read_clues(data):
    # for each clue in the data make an object with the clue text, the count of cells, the label, and the direction of the clue
    clues = []
    # get the clues from the data
    # where the json is structured like this:
    # data['body'][0]['clues'][0]['text'][0]['plain']
    for clue in data['body'][0]['clues']:
        # append the clue to the clues array
        # where the clue is an object with the clue text, the count of cells, the label, and the direction of the clue
        clues.append({
            'text': clue['text'][0]['plain'],
            'count': len(clue['cells']),
            'label': clue['label'],
            'direction': clue['direction']
        })
    return clues

# for each clue, generate a prompt to send to OpenAI
def generate_prompts(clues):
    prompts = []
    for clue in clues:
        # Set the prompt to "Give a crossword answer for This New York Times Crossword clue "{clue text}". The answer must be a word that is {clue count} letters long"
        prompt = f"Give a crossword answer for This New York Times Crossword clue \"{clue['text']}\". The answer must be a word that is {clue['count']} letters long"
        # add the prompt to the prompts array
        prompts.append(prompt)
    return prompts

# for each prompt, send it to OpenAI and get the answer
def get_answers(prompts):
    answers = []
    for prompt in prompts:
        # send the prompt to OpenAI
        response = openai.Completion.create(
            # engine="text-davinci-003"
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1024,
            temperature=0.5,
            frequency_penalty=0,
            presence_penalty=0
        )
        answers.append(response.choices[0].text)
        # remove whitespace from the answers
        answers = [answer.strip() for answer in answers]
    return answers

# print the clues along with the answer, grouping by direction
def print_clues(clues):
    # sort the clues by direction
    clues.sort(key=lambda clue: clue['direction'])
    # print each direction and the clues for that direction
    for direction in ['Across', 'Down']:
        print(direction)
        for clue in clues:
            if clue['direction'] == direction:
                # Print in this format: 1. Fast plane: JET
                print(f"{clue['label']}. {clue['text']}: {clue['answer']}")

# Run the main function
if __name__ == "__main__":
    main()