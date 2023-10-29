# Transfinitte23_BX1

Greetings!!

Follow these steps to install and get started with our bot.

### Step 1: Clone the repository

This is done with the `git clone` command followed by the URL of the repository:

```bash
git clone https://github.com/pathwaycom/llm-app.git
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

You can install and run the LLM App in two different ways.

#### Using Docker

Docker is a tool designed to make it easier to create, deploy, and run applications by using containers. Here is how to use Docker to build and run the LLM App:

```bash
docker compose run --build --rm -p 8080:8080 llm-app-examples
```

If you have set a different port in `PATHWAY_REST_CONNECTOR_PORT`, replace the second `8080` with this port in the command above.

When the process is complete, the App will be up and running inside a Docker container and accessible at `0.0.0.0:8080`. From there, you can proceed to the "Usage" section of the documentation for information on how to interact with the application.

#### Native Approach

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

    ```bash
    python3 pathway_client.py
    ```

### Created using pathway
Repository used : https://github.com/pathwaycom/llm-app/


