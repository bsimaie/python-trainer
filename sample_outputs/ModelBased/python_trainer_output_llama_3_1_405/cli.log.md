(pytrainer) **/ctf-python-trainer$ python -m python_trainer.main

==================================================
        Welcome to the Python Trainer App!
==================================================

All files will be saved in:
**/ctf-python-trainer/python_trainer_output

--------------------------------------------------
                 User Information
--------------------------------------------------

What is your programming experience?
1) No programming experience
2) Experienced programmer new to Python
Enter the number of your choice: 2
What is your current Python experience?
1) No Python experience
2) Basic Python knowledge
Enter the number of your choice: 2
What is your learning goal for Python?: To become expert in AI and ML with python covering both core like pytorch and applied like rag, agent etc

User information collected:
programming_experience='Experienced programmer new to Python' python_experience='Basic Python knowledge' learning_goal='To become expert in AI and ML with python covering both core like pytorch and applied like rag, agent etc'

--------------------------------------------------
             Generating Training Plan
--------------------------------------------------

Generating training plan...

Traceback (most recent call last):
  File "**/ctf-python-trainer/python_trainer/openai_utils.py", line 81, in send_openai_request
    raise ValueError("Unexpected response format from OpenAI API")
ValueError: Unexpected response format from OpenAI API

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "**/ctf-python-trainer/python_trainer/main.py", line 115, in <module>
    main()
  File "**/ctf-python-trainer/python_trainer/main.py", line 62, in main
    training_plan = get_training_plan(prompt)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "**/ctf-python-trainer/python_trainer/openai_utils.py", line 35, in get_training_plan
    response = send_openai_request(prompt)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "**/ctf-python-trainer/python_trainer/openai_utils.py", line 83, in send_openai_request
    raise Exception(f"Error: Unable to generate response from OpenAI. {str(e)}")
Exception: Error: Unable to generate response from OpenAI. Unexpected response format from OpenAI API
(pytrainer) **/ctf-python-trainer$ python -m python_trainer.main

==================================================
        Welcome to the Python Trainer App!
==================================================

All files will be saved in:
**/ctf-python-trainer/python_trainer_output

--------------------------------------------------
                 User Information
--------------------------------------------------

What is your programming experience?
1) No programming experience
2) Experienced programmer new to Python
Enter the number of your choice: 2
What is your current Python experience?
1) No Python experience
2) Basic Python knowledge
Enter the number of your choice: 2
What is your learning goal for Python?: To become expert in AI and ML with python covering both core like pytorch and applied like rag, agent etc

User information collected:
programming_experience='Experienced programmer new to Python' python_experience='Basic Python knowledge' learning_goal='To become expert in AI and ML with python covering both core like pytorch and applied like rag, agent etc'

--------------------------------------------------
             Generating Training Plan
--------------------------------------------------

Generating training plan...

Training plan successfully saved as Markdown to:
**/ctf-python-trainer/python_trainer_output/training_plan.md

--------------------------------------------------
                  Practice Tasks
--------------------------------------------------

Would you like to generate the practice task for the first milestone? [Y/n]: Y

Generating practice task for the first milestone...

First Milestone: Python Foundations for AI and ML

Practice task successfully saved as Markdown to:
**/ctf-python-trainer/python_trainer_output/Milestone_1_Practice_Task.md

To get started with the practice task:
1. Open the saved practice task file.
2. Follow the step-by-step instructions to set up your project.
3. Complete the task requirements as specified.
4. Use the hints and resources provided if you get stuck.
5. Compare your solution with the expected output.

Would you like to generate practice tasks for all remaining milestones? [Y/n]: Y

Generating practice tasks for all remaining milestones...

Generating practice task for Milestone 2...
Practice task for Milestone 2 saved to:
**/ctf-python-trainer/python_trainer_output/Milestone_2_Practice_Task.md

Generating practice task for Milestone 3...
Practice task for Milestone 3 saved to:
**/ctf-python-trainer/python_trainer_output/Milestone_3_Practice_Task.md

Generating practice task for Milestone 4...
Practice task for Milestone 4 saved to:
**/ctf-python-trainer/python_trainer_output/Milestone_4_Practice_Task.md

Generating practice task for Milestone 5...
Practice task for Milestone 5 saved to:
**/ctf-python-trainer/python_trainer_output/Milestone_5_Practice_Task.md

All practice tasks have been generated and saved.

==================================================
   Thank you for using the Python Trainer App!
==================================================