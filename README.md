# GPT-3 Crossword Solver Experiment

Welcome to the GPT-3 Crossword Solver Experiment! This repository contains a Python script, `app.py`, that was generated by [GitHub Copilot](https://github.com/openai/copilot) (powered by OpenAI's GPT-3) to see if GPT-3 could be used to solve the [December 22, 2022 Mini Crossword](https://www.nytimes.com/crosswords/game/mini/2022/12/22).

## Requirements

- Python 3.6 or higher
- [OpenAI's GPT-3 API key](https://beta.openai.com/signup/show)

## Usage

To run the experiment, simply execute the following command in your terminal:

`python app.py crossword.json`

The script will use GPT-3 to solve the crossword based on the clues provided in the `crossword.json` file. The solution will be printed to the console.

## Analysis

Overall, the answers provided by GPT-3 are mostly correct. However, it seems that the language model sometimes ignores certain constraints of the prompt, such as the length of the letters. This suggests that a more carefully crafted prompt and a better configuration of the API call could potentially yield even better results.

It also seems prohibitively difficult to take the final automation steps, including automating a browser to fill in the answers and asking for corrections if any of the provided answers is clearly incorrect or cannot be correct based on other filled-in answers.

## Disclaimer

Please note that this experiment is for educational and entertainment purposes only. The New York Times Crossword is a copyrighted work and it is not permitted to distribute solutions or unauthorized copies of the puzzle.

## Credits

- The `crossword.json` file was taken from the [New York Times Crossword](https://www.nytimes.com/crosswords/game/mini/2022/12/22)
- The Python script, `app.py`, was generated by [GitHub Copilot](https://github.com/openai/copilot) (powered by OpenAI's GPT-3)

---

*This README was generated by a language model trained by OpenAI.*