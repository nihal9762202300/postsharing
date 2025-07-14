import requests
import os

def post_to_facebook(title, body, link, image_path, creds, to_page=True):
    token = creds["page_token"] if to_page else creds["group_token"]
    target_id = creds["page_id"] if to_page else creds["group_id"]

    message = f"{title}\n\n{body or ''}"
    post_url = f"https://graph.facebook.com/v18.0/{target_id}/"

    data = {
        "access_token": token,
        "message": message
    }

    # Attach link if available
    if link:
        data["link"] = link

    # Post photo if provided
    if image_path and os.path.isfile(image_path):
        files = {"source": open(image_path, 'rb')}
        url = f"{post_url}photos"
        response = requests.post(url, data=data, files=files)
    else:
        # Normal post
        url = f"{post_url}feed"
        response = requests.post(url, data=data)

    if response.status_code == 200:
        return "Posted to Facebook " + ("Page" if to_page else "Group")
    else:
        raise Exception(f"Facebook error: {response.text}")
