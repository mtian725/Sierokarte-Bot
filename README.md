# Sierokarte-Bot
Discord Bot geared toward Granblue Fantasy

Currently set up to run locally, meaning that on person needs to execute the program via `python3 main.py` in order to actually interact with the bot.

How we will run it 24/7 is a challenge for later.

Set up a `main.py`. This will be where all the top level stuff will be (All the chat commands). Any other code we add, we will simply `import (other module)`. `main.py` currently has 2 commands `$hello` and `$wiki`. They are there for testing purposes. `$hello` will have the bot respond with hello, and `$wiki` will link the Grandblue Fantasy wiki. DO NOT CHANGE OR TOUCH THE LINE THAT SAYS `client.run()`

Added json module which access local json file that has the bot token

.commands() vs using on_message() to parse through commands.

Everything following the command is read as an input, which reduces the amount of work needed, but using on_massage() to read in inputs allows for more natural and intuitive inputs.

# main.py
Contains all the commands, and running it runs the Bot
## !calcarcarum
Can also be invoked with `!ca`. When the command is called, the user will be asked to answer 4 prompts. These prompts are:
* Which summon
* The start step
* The end step
* Whether to show individual steps.

Each prompt is a discord embed image. The command can be cancelled at each step by either waiting 30 seconds, calling another command (even if the command does not exist), or responding with `c`.

## !eternals
Can also be invoked with `!e`. When the command is called, the user will be asked a prompt. When the user responds to the prompt, a new prompt is opened. This prompt has several emoji reactions. The user can click/tap one of the reactions to change the prompt to that corresponding step number. The prompt will stop reacting once the user does not interact with it for 25 seconds. **Because all the reactions need to be added first, clicking/tapping before all the emojis are added will result in no reaction.**

## !wiki
Can also be invoked with `!w`. Syntax to use the command is:

`!wiki <thing you are looking up>` - Bot will respond with a url that is the closest match to your query.

**OR**

`!wiki` - Bot will respond with the main page's url

Uses `googlesearch` library to search.
