# Sierokarte-Bot
Discord Bot geared toward Granblue Fantasy

Currently set up to run locally, meaning that on person needs to execute the program via `python3 main.py` in order to actually interact with the bot.\

How we will run it 24/7 is a challenge for later.\

Set up a `main.py`. This will be where all the top level stuff will be (All the chat commands). Any other code we add, we will simply `import (other module)`. `main.py` currently has 2 commands `$hello` and `$wiki`. They are there for testing purposes. `$hello` will have the bot respond with hello, and `$wiki` will link the Grandblue Fantasy wiki. DO NOT CHANGE OR TOUCH THE LINE THAT SAYS `client.run()`\
