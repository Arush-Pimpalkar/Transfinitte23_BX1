# Transfinitte23_BX1

## Introduction

This project leverages the capabilities of OpenAI in conjunction with the Pathway framework to establish a secure, localized interface facilitating the execution of Linux commands through prompts in Simple English. The Pathway Framework constructs a dedicated dictionary containing command descriptions, ensuring data confidentiality by conducting searches locally without transmitting any information to OpenAI. This approach is particularly advantageous for developing a secure Command Line Interface (CLI) suitable for beginners and adept users, fostering efficient Linux system interaction.

<img width="1120" alt="Screenshot 2024-01-20 210350" src="https://github.com/Arush-Pimpalkar/Transfinitte23_BX1/assets/23013777/f9782387-08a0-441f-8f44-25dc325b65ea">

## Dictionary Creation Methodologies

### 1. '/usr/bin' and 'man' Algorithms

- Development of an algorithm that systematically generates a comprehensive and organized dictionary from locally available commands residing in '/usr/bin' directories and abstracting the description using ‘man’.

### 2. Linux Cheat Sheets

- Implementation of a simplified algorithm utilizing Linux Cheat Sheets accessible on the internet, offering a less intricate alternative.

The choice of prioritizing the first method is driven by its inherent capability to yield more precise and reliable responses for users and developers. This meticulous approach ensures the creation of a robust and user-friendly CLI, catering to both novice and experienced Linux users.

## Get Started:

Follow these steps to install and get started:

### Step 1: Clone the repository

This is done with the `git clone` command followed by the URL of the repository:

```bash
https://github.com/Arush-Pimpalkar/Transfinitte23_BX1
```

Next, navigate to the repository:

```bash
cd llm-app
```

### Step 2: Set environment variables

Create an .env file in the root directory and add the OpenAI api key. It may look like this 

```bash
APP_VARIANT=contextful
PATHWAY_REST_CONNECTOR_HOST=0.0.0.0
PATHWAY_REST_CONNECTOR_PORT=8080
OPENAI_API_TOKEN=<Your Token>
PATHWAY_CACHE_DIR=/tmp/cache
```

### Step 3: Build and run the app

Follow the steps to start the app 


* **Install poetry:**

    ```bash
    pip install poetry
    ```

* **Install llm_app and dependencies:**

    ```bash
    poetry install --with examples --extras local
    ```

    
* **Start the ** You can start the example with the command:

    ```bash
    poetry run ./run_examples.py contextful
    ```

### Step 4: Start interface

Start using the app from a different terminal:

     python3 pathway_client.py

### Created using pathway
Repository used : https://github.com/pathwaycom/llm-app/

Working Video:

![Jarvis Jr - Working Video](https://github.com/Arush-Pimpalkar/Transfinitte23_BX1/assets/23013777/66e34975-78db-4662-9e08-f859d4798708)
