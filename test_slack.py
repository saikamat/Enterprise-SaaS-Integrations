from src.integrations.slack_client import SlackClient
from src.config import SLACK_BOT_TOKEN

def main():
    print("Testing Slack Integration...")

    # create client
    client = SlackClient(SLACK_BOT_TOKEN)

    # test getting the bot info
    bot_info = client.get_bot_info()
    print(f"Successfully connected to Slack")
    print(f"Username: {bot_info['username']}")
    print(f"Team Name: {bot_info['team_name']}")

    # test getting the channel's list
    channel_list = client.list_channels()
    print(f"\nAvailable channels:")
    for channel in channel_list:
        print(f"- {channel['name']}(ID: {channel['id']})")

    # test sending message
    message_text = "Hello from Slack Bot. this is a test message"
    channel_name = input("Choose a channel: ")
    channel_response = client.send_message(channel_name, message_text)
    if channel_response['success']:
        print(f"✓ Message sent successfully!")
    else: 
        print(f"Failed to send message: {channel_response['error']}")


if __name__ == "__main__":
    main()