import httpx

from simple.card import HOST, PORT

URL = f"http://{HOST}:{PORT}"


def send_message(text: str):
    payload = {
        "jsonrpc": "2.0",
        "id": "1",
        "method": "SendMessage",
        "params": {
            "message": {
                "message_id": "msg-1",
                "role": "ROLE_USER",
                "parts": [{"text": text}],
            }
        },
    }
    headers = {"A2A-Version": "1.0"}
    response = httpx.post(URL, json=payload, headers=headers)
    print(response.json())


if __name__ == "__main__":
    send_message("Aditya")
