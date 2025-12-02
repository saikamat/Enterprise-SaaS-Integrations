"""
In src/integrations/slack_client.py, you'll create a class similar to the GitHub client structure. The basic skeleton should
   include:
  - Initialize the Slack WebClient
  - Methods to send messages to channels
  - Methods to list channels
  - Methods to get user information
"""
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackClient:
    def __init__(self, token):
        # initialise the slack webclient with the bot token
        self.client = WebClient(token)

    def get_bot_info(self):
        # get authentication bot's info-username & teamname
        user = self.client.auth_test()
        return{
            'username': user['user'],
            'team_name': user['team']
        }

    def list_channels(self):
        # list all public channels in the workspace
        response = self.client.conversations_list()
        channels = response['channels']

        # return a list
        return[
            {
                'id': channel['id'],
                'name': channel['name']
            }
            for channel in channels
        ]

    def send_message(self, channel, text):
        # send message to specific channel
        try:
            message = self.client.chat_postMessage(channel=channel, text=text)
            return{
                'success': True,
                'timestamp': message['ts'],
                'channel': message['channel'],
                'text': message['message']['text']
            }
        except SlackApiError as e:
            return{
                'success': False,
                'error': str(e),
                'channel': channel,
                'text': text
            }