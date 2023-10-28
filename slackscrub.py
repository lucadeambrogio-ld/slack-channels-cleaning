import time
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Define your Slack token
slack_token = 'xoxp-your-slack-token'
client = WebClient(token=slack_token)

# Define the list of channel IDs
channels = [
    "channel-id-1",
    "channel-id-2",
    "channel-id-3"
    ]

# Initialize counters
total_deleted = 0
total_failed = 0

# Iterate over each channel
for channel in channels:
    # Fetch conversation history for the channel
    # conversations.history returns the first 100 messages by default
    try:
        result = client.conversations_history(channel=channel)
        conversation_history = result
    except SlackApiError as e:
        print(f"Error fetching messages: {e}")     
        
    # Loop through the messages in the conversation history
    for message in conversation_history['messages']:
        # Delete each message using its timestamp
        ts = message['ts']
        try:
            # Call the chat.chatDelete method using the built-in WebClient
            result = client.chat_delete(
                channel=channel,
                ts=ts
            )
            total_deleted += 1
        except SlackApiError as e:
            print(f"Error deleting message: {e}")
            total_failed += 1

        time.sleep(0.5)


# Print the summary
print(f"Total messages deleted: {total_deleted}")
print(f"Total deletion failures: {total_failed}")
