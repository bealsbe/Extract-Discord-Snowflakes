# Extract-Discord-Snowflakes
Simple script for Discord Moderators to quickly extract User Ids from a join log to mitigate bot raids

Current Flow:
- Copy contents of moderation bot logs into clipboard
- Autohotkey runs a python script when a keyboard shortcut is pressed
- The python script grabs all of the content from your and extracts the user Ids
- The user ids are written to a file
- The file is opened.
