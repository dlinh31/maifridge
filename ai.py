import openai
import json


openai.api_key = "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"
message_history = []

def chat(inp, role="user"):
    message_history.append({"role": role, "content": f"{inp}"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history
    )
    reply_content = completion.choices[0].message.content
    message_history.append({"role": "assistant", "content": f"{reply_content}"})
    return reply_content


for i in range(2):
    user_input = input("> ")
    print("User's input was: ", user_input)
    print(chat(user_input))
    print()

# user_input = "what is 5 times 8?"


# message_history.append({'role': 'user', 'content': user_input})

# completion = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages = message_history
# )


# reply_content = completion['choices'][0]['message']['content']
# message_history.append({'role': 'assistant', 'content': reply_content})


# user_input = "Take the result you just get, and divide by 2, what do you get?"
# message_history.append({'role': 'user', 'content': user_input})


# completion = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages = message_history
# )

# reply_content = completion['choices'][0]['message']['content']
# message_history.append({'role': 'assistant', 'content': reply_content})
# print(message_history)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(message_history, f, ensure_ascii=False, indent=4)