import json
import requests
import re
import os


# Define your function to process JSON data
def process_json(json_data):
    print("helloooooooooooooooooo")
    description = json_data.get("description")
    print("Description: ", description)
    if description:
        data_input = description
        data = {
            "user": "user",
            "query": data_input
            + ",the command should be the last word(s) of the sentence",
        }
        post_response = requests.post("http://localhost:8080/", json=data)
        post_response_json = post_response.json()
        print(post_response_json)

        text = post_response_json

        pattern1 = '^(.*) "(.*)" command.'
        pattern2 = '^(.*) "(.*)"'
        pattern3 = '^(.*) "(.*)".'

        m1 = re.search(pattern1, text)
        m2 = re.search(pattern2, text)
        m3 = re.search(pattern3, text)

        if m3:
            found = m3.group(2)
            print("Pattern 3 match: ", found)

        elif m2:
            found = m2.group(2)
            print("Pattern 2 match: ", found)

        elif m1:
            found = m1.group(2)
            print("Pattern 1 match: ", found)

        else:
            with open("required.txt", "a") as file:
                file.write(text)


# Open the JSONL file
def main():
    with open(
        "/home/arush/altf5/llm-app/examples/data/pathway-docs/LinuxCommands.jsonl", "r"
    ) as file:
        # Read each line and parse it as JSON
        for line in file:
            try:
                # Parse JSON string to a dictionary
                json_data = json.loads(line)
                # Call the function on the "description" value
                process_json(json_data)
            except json.JSONDecodeError as e:
                # Handle JSON decoding errors (if any)
                print(f"Error decoding JSON: {e}")


# Run the main function sequentially
if __name__ == "__main__":
    main()
