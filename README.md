# Prompt-Analysis -Tool 


Introduction  to Prompt Analysis Tool is a web application that utilizes OpenAI's GPT-3.5 Turbo model to analyze chat prompts and provide a score based on specific parameters. This tool allows users to enter a chat prompt and receive a score on a scale of 1 to 100, indicating how well the prompt satisfies certain criteria set by the system. Additionally, the tool generates a new prompt that meets all the specified parameters.

## Objective

The main objective of this project is to provide a user-friendly web-based tool for analyzing chat prompts using OpenAI's powerful GPT-3.5 Turbo language model. The tool helps users ensure that their prompts are clear, and specific, and effectively communicate the desired context and instructions. By scoring and generating new prompts, users can improve the effectiveness of their interactions with the language model.

## Features

- Input OpenAI API Key: Users need to provide their OpenAI API key to access the language model's capabilities. The API key is hidden behind a password input field for added security.

- Analyze Chat Prompt: Users can input a chat prompt, which may include system and user instructions, explicit cues, and other context information.

- Prompt Scoring: The tool analyzes the given chat prompt and assigns a score from 1 to 100 based on specific parameters. The scoring criteria include clarity, specificity, context provision, and more.

- Generate New Prompt: If the initial prompt does not meet all the required parameters, the tool generates a new prompt that satisfies the criteria.

## Getting Started

1. Clone the repository: `git clone https://github.com/your_username/chat-prompt-analysis.git`
2. Install the required dependencies: `pip install Flask openai`
3. Set up your OpenAI API key: Create an account on the OpenAI website and obtain your API key.
4. Replace `"YOUR_OPENAI_API_KEY"` in `app.py` with your actual OpenAI API key.
5. Run the Flask app: `python app.py`

## How to Use

1. Access the application by visiting `http://127.0.0.1:5000/` in your web browser.
2. Enter your OpenAI API key in the provided input box. The API key will be hidden behind a password input field for security.
3. Enter your chat prompt in the designated text area. And See the magic 

## Credits

This Chat Prompt Analysis Tool was created by Vanamayaswanth and sethusai.

## Contributions

Contributions to the project are welcome. If you find any issues or have ideas for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Future Update :

1. Hugging face integration
2. Gradio APP
3. Docker
4. Advanced prompting Techniques

Note: Please note that this tool utilizes OpenAI's language model, and users are responsible for ensuring compliance with OpenAI's terms of service and any other relevant regulations. The tool is intended for educational and experimental purposes and should not be used for any malicious or harmful activities.

Enjoy using the Prompt Analysis Tool! If you have any questions or need assistance, feel free to reach out to the project maintainers. Happy prompting!
