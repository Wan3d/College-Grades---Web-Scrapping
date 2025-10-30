import requests
from credentials import tokenBot, chatID

def sendTelegramMessage(isUpdated):
    # Get chat ID
    '''urlTokenBot = f"https://api.telegram.org/bot<TOKEN>/getUpdates"
    print(requests.get(urlTokenBot).json())'''

    # Set message and URL where is headed the message
    message = f'{isUpdated}'
    urlSendMessage = f"https://api.telegram.org/bot{tokenBot}/sendMessage?chat_id={chatID}&text={message}"

    # Send it
    requests.get(urlSendMessage)





