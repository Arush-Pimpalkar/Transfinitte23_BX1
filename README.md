# Transfinitte23_BX1

Greetings!!

Follow these steps to install and get started with our bot.

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

Follow the steps to start the bot 


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

     python3 pathway_client.py


### Created using pathway
Repository used : https://github.com/pathwaycom/llm-app/


