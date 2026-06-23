# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
## 1.
  -The game looked like it was developed to the point that it was the most minimal bare implementation of an interface to test the game logic. We had a set of .py 
  files and a library called streamlit to install to get the game running. Once dependencies were taken care of, the program starts a webserver which hosts the .py 
  game logic and serves them to a user with a minimal interface. 
  - 1) The hints were backwards- when the guessed number is too high, the user is presented with a "Go Lower" message, and vice versa.
    2) The score makes no sense. It can jump around a lot. 
    3) There's something broken which makes it so that sometimes the # of attempts is not honored, even with valid remaining attempts
    4) The difficulty settings are weird. A normal game has a larger domain of inputs than the harder game. Easy is 20, Normal 100 and Hard 50. 
     The values for Normal and Hard are switched.
**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| secret:99 -> guess:100| "Go LOWER" hint | "Go Higher" hint shown| "none"|
| secret:99 -> guess:100, repeated input| "Go LOWER" hint, score reduction | "Go Higher" hint shown, score went positive after failed guess, score=5| "none"|
| secret:99 -> guess:  0| It should throw an error due to invalid input range | "Go LOWER" hint shown| "none"|
| secret:99 -> guess:  101| It should throw an error due to invalid input range | "Go HIGHER" hint shown| "none"|
| Difficulty:Normal| difficulty parameters (range, # of guesses) should be set to middle value between easy and hard| difficulty parameters for "Normal" are more difficult than those for "Hard" - e.g. line 9 in app.py| "none"|


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
## 2.
  -I used ChatGPT 5.5 "Thinking" for system tasks e.g. helping me remember git commands etc. My VSCode is integrated with Copilot, but I turned off most functions so that it only makes syntax suggestions. In terms of interrogating the codebase and finding out what's going on, I used Claude with the Haiku model set to High Efort, and with Thinking set to on. I'm playing around with Claude and seeing what the different models output. 
  -The AI suggested that the hint output messages were reversed:it outputs "Go HIGHER!" when the "Go LOWER!" message should be output. This was correct. I verified it by checking line 38 and line 40 of app.py.
  -One of the frustrating and incorrect things that the AI did was make incorrect suggestions for installing dependencies and getting the streamlit package running. I got all of the dependencies installed and working and put a few hours in to this project, and saved everything to Github. It was late at night and I was tired and I was just copying AI suggestions on how to add and commit and push. A few days later I came back and wanted to work on the project. I pulled my repo from Github and realized that I totally screwed up my .venv. I ended up having to spend hours trying to fix and undo the errors I made.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
## 3.
  -Claude made suggestions on bugfixing, so I saved my project to Git and then allowed Claude to make the changes. I then tested with the modified program. For some bugs I asked Claude for suggestions on how to test them: Claude suggested running the program and call the function from the Python shell. This was great because I could get Claude to programatically test the functions. Once Claude had programatically tested the functions (they looked OK using print statements) I switched to assertions. I then asked Claude to set up pytest tests for my project.
  -While I was working, I would ask the AI to help me "eyeball" the results. For example, I made edits to the check_guess() function, and Claude helped me test them by opening the Python shell and importing the function from app.py. I could then check repeated guesses with a for loop. 
    for i in range(5): 
      print(i, check_guess(42, 42))   # should always be ("Win", ...)
      print(i, check_guess(50, 42))   # should always be ("Too High", ...)
      print(i, check_guess(10, 42))   # should always be ("Too Low", ...)
    I also asked when I had fixed bugs and refactored code, for Claude to create a set of pytest tests, based on my fixes. It created them. I ran the tests and it worked perfectly. It saved me a ton of time!
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
## 4.
  -Streamlit rebuilds itsef every time it is loaded, the variables are all reset. The Streamlit "session state" lets you save it's state so that values can be persistent between "reruns". Sort of like "random.seed()" with the random library. FOr testing purposes we want to be able to have each variable be persistent. "st.session_state" is the way Streamlit saves all of the variables so that when it is reloaded, the program state is saved. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
## 5.
  -I have begun to value using git the way that it is demonstrated in Codepath. It is an incredible time saver and helps me maintain revisions to code like no other code management software. I've had problems with AI wiping out good code and having the discipline to use git after changes really helps. In my snippets manager I keep:
      git status
      git add .
      git commit -m "Describe changes"
      git push
  so that I can just copy and paste the line in to the terminal and hit enter.
  - Next time I use a coding agent, I will be more apt to use a stronger model. For most of the project I was using Claude and haiku. I switched over to Opus at the end. I was impressed with the results. Next time I might do something like work on my prompt with haiku and then once refined, send it over to Opus.
  - I had never fully integrated AI in to VS Code. I am truly impressed with how powerful it is, especially agent mode. I used to ask GPT for changes and I would have to hunt through files and insert them ... the agent mode is amazing! It just ... does it. 