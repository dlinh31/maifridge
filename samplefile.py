import ai

# load and set our key
ai.api_key = "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"

completion = ai.ChatCompletion.create(
  model="gpt-3.5-turbo", # this is "ChatGPT" $0.002 per 1k tokens
  messages=[{"role": "user", "content": "What is the circumference in km of the planet Earth?"}]
)

print(completion)

reply_content = completion.choices[0].message.content
print(reply_content)

message_history = []
# What is the moon's circumference in km?
user_input = input("> ")
print("User's input was: ", user_input)

message_history.append({"role": "user", "content": f"{user_input}"})

completion = ai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=message_history
)

# Now we can print the response:
reply_content = completion.choices[0].message.content
print(reply_content)

# note the use of the "assistant" role here. This is because we're feeding the model's response into context.
message_history.append({"role": "assistant", "content": f"{reply_content}"})

# which moon is that in reference to?
user_input = input("> ")
print("User's input was: ", user_input)
print()
message_history.append({"role": "user", "content": f"{user_input}"})

completion = ai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=message_history
)

reply_content = completion.choices[0].message.content
print(reply_content)