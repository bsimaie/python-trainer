from python_trainer.config import UserInfo

def generate_prompt(user_info: UserInfo) -> str:
    """
    Generate a prompt for OpenAI GPT based on user information.
    
    Args:
        user_info (UserInfo): User information collected from CLI.
    
    Returns:
        str: A formatted prompt for the OpenAI GPT model.
    """
    prompt = f"""Create a Python training plan for a user with the following profile:
Experience level: {user_info.programming_experience}
Python knowledge: {user_info.python_experience or 'Not specified'}
Learning goal: {user_info.learning_goal}
Preferred learning style: {user_info.learning_style}

The plan should include several milestones with milestone names, objectives, and topics to cover. 
Each milestone should be tailored to the user's experience level and learning style.
Provide a structured response with clear sections for each milestone."""

    return prompt