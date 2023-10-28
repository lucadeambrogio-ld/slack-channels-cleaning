# slack-channels-cleaning

Clean Slack Channels

To set up this script in python, you first need to create a slack app here https://api.slack.com/apps.
Then, according to your needs, create a slack token to be inserted in the python code. You can find more about slack token scopes reading the official doc:
- https://api.slack.com/methods/conversations.history
- https://api.slack.com/methods/chat.delete

Both methods fall under ```Web API Tier 3```, which implies they have relatively lenient rate limits. Currently, they are restricted to approximately 50 or more runs per minute. For official rate limit details, please refer to this link: https://api.slack.com/docs/rate-limits.
