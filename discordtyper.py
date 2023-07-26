import requests
import time

class Main:
    def run(self, repeat_times):
        messages = [
            {"content": "Crazy?", "cooldown": 0.1},
            {"content": "I was crazy once.", "cooldown": 0.5},
            {"content": "They locked me in a room", "cooldown": 1},
            {"content": "A rubber room.", "cooldown": 0.3},
            {"content": "A rubber room with rats", "cooldown": 0.4},
            {"content": "And rats make me crazy.", "cooldown": 0.7}
        ]
        channelId = '1133864754524463125'
        if repeat_times <= 0:
            while True:
                for message_data in messages:
                    message = message_data["content"]
                    cooldown = message_data["cooldown"]
                    self.send_message(channelId, message)
                    time.sleep(cooldown)
        else:
            for _ in range(repeat_times):
                for message_data in messages:
                    message = message_data["content"]
                    cooldown = message_data["cooldown"]
                    self.send_message(channelId, message)
                    time.sleep(cooldown)

    def send_message(self, channel_id, message):
        headers = {
            "Authorization": "NTYzODQ4OTg3NjM2MDA2OTM0.GCvQwN.t8iVHIQMPq4tVNFD2PjFc4NPt_Uydwp-b4uUxk",
            "Content-Type": "application/json"
        }
        data = {"content": message}
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            print(f"Message sent successfully: {message}")
        else:
            print(f"Failed to send message. Error code: {response.status_code}")


if __name__ == "__main__":
    typer = Main()
    try:
        repeat_times = 3  # 0 for infinite
        typer.run(repeat_times)
    except KeyboardInterrupt:
        print("Stopped.")
