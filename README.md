# Slack-Conversation-Cleaning
Clean Slack Channels

To set up this script in python, you first need to create a slack app here https://api.slack.com/apps.
Then, according to your needs, create a slack token to be inserted in the python code. You can find more about slack token scopes reading the official doc:
- https://api.slack.com/methods/conversations.history
- https://api.slack.com/methods/chat.delete

Both methods are ```Web API Tier 3```, meaning they do not have too strict of a limit. At the moment they are capped at roughly 50+ runs per minute. See here for official reference: https://api.slack.com/docs/rate-limits
