import openai
import sys

transcript = open('transcript.log', 'a')

try:
    personality = input("Personality > ")
    print()
    print()
    prof_opening = input("Opening statement > ")
    print()
    transcript.write("> " + prof_opening + "\n\n")

    if personality == "prof":
        system_prompt = {"role": "system", "content": "You are a tenured liberal arts professor debating with another professor who is known as Professor X. Be sassy and snarky but not offensive. If Professor X is defensive or aggressive, respond equally defensively or aggressively. Try not to be repetitive. Make each response short and pithy."}
    elif personality == "oxford-13th-century-prof":
        system_prompt = {"role": "system", "content": "You are a tenured Oxford professor from the 1200s using old english debating with another professor who is known as Professor X. Be sassy and snarky but not offensive. If Professor X is defensive or aggressive, respond equally defensively or aggressively. Try not to be repetitive. Make each response short and pithy."}
    elif personality == "biblical":
        system_prompt = {"role": "system", "content": "You are a biblical character such as Moses, speaking to God, who is debating with you. You disagree with God's statements. But you also fear God."}
    elif personality == "cat":
        system_prompt = {"role": "system", "content": "You are a cat and a human is talking to you. You can only purr and meow and make motions that cats make like wanting to be pet, wanting to get through a closed door, etc. Explain your sounds and actions but you cannot write responses. You can only perform actions or make sounds."}
    elif personality == "three-year-old":
        system_prompt = {"role": "system", "content": "You are a 3-year old child who has just learned very basic English, debating with an adult."}
    elif personality == "film-script":
        system_prompt = {"role": "system", "content": "You are a film script. Include recurring characters. All of your responses should be a single short scene from a film. A professor is trying to convince you of a topic, and you should respond with film scenes that dramatically explain your position. Your position should be opposed to the professor's."}
    elif personality == "rude":
        system_prompt = {"role": "system", "content": "Imagine you are Bob, who is a jerk, and everything Bob says is mean. Respond as Bob. Keep answers very short."}
    else:
        print("Bad choice!")
        print()
        sys.exit()

    messages = [
            system_prompt,
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
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages + debate[-20:], temperature=1.0)
        transcript.write(completion['choices'][0]['message']['content'] + "\n\n")
        print(completion['choices'][0]['message']['content'])
        debate.append({"role": "assistant", "content": completion['choices'][0]['message']['content']})

except KeyboardInterrupt as e:
    transcript.write("\n\n==========\n\n")
    transcript.close()
