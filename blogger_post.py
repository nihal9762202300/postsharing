from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os

def post_to_blogger(title, body, link, image_path, creds):
    creds_obj = Credentials(
        None,
        refresh_token=creds["refresh_token"],
        token_uri="https://oauth2.googleapis.com/token",
        client_id=creds["client_id"],
        client_secret=creds["client_secret"]
    )

    service = build("blogger", "v3", credentials=creds_obj)
    blog_id = creds["blog_id"]

    content = f"<h2>{title}</h2><p>{body or ''}</p>"
    if link:
        content += f'<p><a href="{link}">{link}</a></p>'
    if image_path and os.path.exists(image_path):
        img_url = upload_image_to_imgur(image_path)
        content += f'<img src="{img_url}" alt="Post Image"/>'

    post_body = {
        "title": title,
        "content": content
    }

    posts = service.posts()
    result = posts.insert(blogId=blog_id, body=post_body, isDraft=False).execute()

    return f"Posted to Blogger: {result['url']}"

# Optional: Upload to Imgur (or your preferred image host)
def upload_image_to_imgur(image_path):
    # You can replace this with your own image hosting
    return "https://via.placeholder.com/600x400.png?text=Image"
