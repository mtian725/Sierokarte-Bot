# Sierokarte-Bot
Discord Bot geared toward Granblue Fantasy

**Progress on this project will no longer continue due to many of ideas/goals not being practical to put on discord bot**
Might return or restart the project on a later date

Runs on Heroku's free tier.

# main.py
Contains all the commands, and running it runs the Bot

## !help
Can also be invoked with `!h`. Will send a private message containing all the commands.

## !calcarcarum (will remove or edit)
Can also be invoked with `!ca`. When the command is called, the user will be asked to answer 4 prompts. These prompts are:
* Which summon
* The start step
* The end step
* Whether to show individual steps.

Each prompt is a discord embed image. The command can be cancelled at each step by either waiting 30 seconds, calling another command (even if the command does not exist), or responding with `c`.

## !eternals (will remove or edit)
Can also be invoked with `!e`. When the command is called, the user will be asked a prompt. When the user responds to the prompt, a new prompt is opened. This prompt has several emoji reactions. The user can click/tap one of the reactions to change the prompt to that corresponding step number. The prompt will stop reacting once the user does not interact with it for 25 seconds. **Because all the reactions need to be added first, clicking/tapping before all the emojis are added will result in no reaction.**

## !wiki
Can also be invoked with `!w`. Syntax to use the command is:

`!wiki <thing you are looking up>` - Bot will respond with an url that is the closest match to your query.

**OR**

`!wiki` - Bot will respond with the main page's url

Uses `googlesearch` library to search.

## !time
Can also be invoked with `!t`.
3 times will be typed out in this order:
* current time in JST 24 hour clock
* current time in JST 12 hour clock
* time until next daily reset

## !art
Can also be invoked with `!a`. Syntax to use the command is:

`!art <character name>` - Bot will respond with an embed that has all the character art that you are searching

## !find
Can also be invoked with `!f`. Syntax to use the command is :

`!find <trait1> <trait2> ...` - Include at least one trait and will list off all characters with that trait.

Currently registered traits:
* Rarity
* Element
* Race
* Weapon mastery
