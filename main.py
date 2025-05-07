import os
import time
import requests
from colorama import Back, Fore, Style, init

token = "token"
channel_id = "channel id"
message = "text"
delay = 4

os.system("cls")
print(
    Fore.RED
    + """
███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
          made by  https://github.com/JinxedUp                               """
)


headers = {"Authorization": token, "Content-Type": "application/json"}

data = {"content": message}

while True:
    try:
        response = requests.post(
            f"https://discord.com/api/v10/channels/{channel_id}/messages",
            json=data,
            headers=headers,
        )

        if response.status_code == 200:
            print(Fore.GREEN + "message sent successfully")

        elif response.status_code == 429:
            print(Fore.RED + "ratelimited, retrying")
            retry_after = response.json().get("retry_after", 5)
            time.sleep(retry_after)

        else:
            print(
                Fore.RED
                + f"failed to send and was given this status: {response.status_code} "
            )

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Request error: {e}")
        time.sleep(delay)

    time.sleep(delay)
