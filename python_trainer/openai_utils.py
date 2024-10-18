import os
import json
import openai
from dotenv import load_dotenv
from pathlib import Path
from python_trainer.schemas import TrainingPlan

# Get the root directory of the project
root_dir = Path(__file__).resolve().parent.parent

# Load environment variables from .env file in the root directory
dotenv_path = root_dir / '.env'
load_dotenv(dotenv_path=dotenv_path)

# Set up OpenAI client
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL"),
)

model_name = os.getenv("MODEL_NAME")

def get_training_plan(prompt: str) -> TrainingPlan:
    """
    Send a prompt to OpenAI GPT and get a training plan response.

    Args:
        prompt (str): The generated prompt for OpenAI GPT.

    Returns:
        TrainingPlan: The generated training plan from OpenAI GPT, parsed into a TrainingPlan object.
    """
    response = send_openai_request(prompt)
    plan_dict = parse_openai_response(response)
    return TrainingPlan(**plan_dict)

def get_practice_task(prompt: str) -> str:
    """
    Send a prompt to OpenAI GPT and get a practice task response with concept explanations.

    Args:
        prompt (str): The generated prompt for OpenAI GPT.

    Returns:
        str: The generated concept explanations and practice task from OpenAI GPT.
    """
    response = send_openai_request(prompt)
    # Ensure the response is properly formatted as Markdown
    formatted_response = f"# Concept Explanations and Practice Task\n\n{response.strip()}"
    return formatted_response

def send_openai_request(prompt: str) -> str:
    """
    Send a request to OpenAI GPT and get a response.

    Args:
        prompt (str): The generated prompt for OpenAI GPT.

    Returns:
        str: The response from OpenAI GPT.
    """
    try:
        if model_name is None:
            raise ValueError("Model name is not set. Please check your environment variables.")

        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant that creates Python training plans, explains programming concepts, and designs practice tasks."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,  # Slightly increase temperature for more creative explanations
            max_tokens=3000,  # Increase max tokens to allow for longer responses including concept explanations
        )

        if response.choices and response.choices[0].message and response.choices[0].message.content:
            return response.choices[0].message.content.strip()
        else:
            raise ValueError("Unexpected response format from OpenAI API")
    except Exception as e:
        raise Exception(f"Error: Unable to generate response from OpenAI. {str(e)}")

def parse_openai_response(response: str) -> dict:
    """
    Parse the OpenAI response into a dictionary.

    Args:
        response (str): The response from OpenAI GPT.

    Returns:
        dict: The parsed response as a dictionary.
    """
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        # If it's not valid JSON, try to extract JSON from the string
        import re
        json_match = re.search(r'\{.*\}', response, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        else:
            raise ValueError("Could not extract valid JSON from the response")
