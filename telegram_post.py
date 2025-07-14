import requests

def post_to_telegram(title, body, link, image_path, creds):
    bot_token = creds["bot_token"]
    chat_id = creds["chat_id"]

    # Compose message text
    full_message = f"<b>{title}</b>\n"
    if body:
        full_message += f"{body}\n"
    if link:
        full_message += f"\n🔗 <a href=\"{link}\">{link}</a>"

    send_url = f"https://api.telegram.org/bot{bot_token}"

    # Send with photo or as plain text
    if image_path:
        with open(image_path, 'rb') as img:
            response = requests.post(
                f"{send_url}/sendPhoto",
                data={"chat_id": chat_id, "caption": full_message, "parse_mode": "HTML"},
                files={"photo": img}
            )
    else:
        response = requests.post(
            f"{send_url}/sendMessage",
            data={"chat_id": chat_id, "text": full_message, "parse_mode": "HTML"}
        )

    if response.status_code == 200:
        return "Posted to Telegram"
    else:
        raise Exception(f"Telegram error: {response.text}")
