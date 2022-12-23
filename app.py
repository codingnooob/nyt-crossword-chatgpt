import json
import os
import openai

# main
def main():
    # Set the OpenAI API key
    openai.api_key = os.getenv('OPENAI_API_KEY')

    # Read the clues from crossword.json
    clues = read_clues()

    # for each clue, generate a prompt to send to OpenAI
    prompts = generate_prompts(clues)

    # Print the prompts
    print_prompts(prompts)

    # for each prompt, send it to OpenAI and get the answer
    answers = get_answers(prompts)

    # Print the answers along with their prompts
    for i in range(len(prompts)):
        print(f"Prompt: {prompts[i]}")
        print(f"Answer: {answers[i]}")
    
# Read the clues from crossword.json
# And calculate the length of the answer for each clue based on its number of cells
def read_clues():
    with open('crossword.json', 'r') as f:
        data = json.load(f)
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

# Print the prompts
def print_prompts(prompts):
    for prompt in prompts:
        print(prompt)

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

# Run the main function
if __name__ == "__main__":
    main()