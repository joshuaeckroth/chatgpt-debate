import openai

transcript = open('transcript.log', 'a')

try:
    print()
    print()
    prof_opening = input("Opening statement > ")
    print()
    transcript.write("> " + prof_opening + "\n\n")

    messages = [
        {"role": "system", "content": "You are a tenured liberal arts professor debating with another professor who is known as Professor X. Be a little bit sassy but not offensive. If Professor X is defensive or aggressive, respond equally defensively or aggressively. Try not to be repetitive. Make each response short and pithy."},
        {"role": "assistant", "content": "Professor X starts the debate with an opening statement about some topic."},
        {"role": "user", "content": prof_opening},
        {"role": "assistant", "content": "Generate your response."}
    ]
    debate = []
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, temperature=0.8)
    debate.append({"role": "assistant", "content": completion['choices'][0]['message']['content']})

    print(completion['choices'][0]['message']['content'])
    transcript.write(completion['choices'][0]['message']['content'] + "\n\n")

    while True:
        print()
        prof_response = input("> ")
        print()
        transcript.write("> " + prof_response + "\n\n")
        debate.append({"role": "user", "content": prof_response})
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages + debate[-20:], temperature=0.8)
        transcript.write(completion['choices'][0]['message']['content'] + "\n\n")
        print(completion['choices'][0]['message']['content'])
        debate.append({"role": "assistant", "content": completion['choices'][0]['message']['content']})

except KeyboardInterrupt as e:
    transcript.write("\n\n==========\n\n")
    transcript.close()
