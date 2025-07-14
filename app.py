from flask import Flask, request, render_template
import os
import praw

app = Flask(__name__)

def load_config():
    return {
        "reddit": {
            "client_id": os.getenv("REDDIT_CLIENT_ID"),
            "client_secret": os.getenv("REDDIT_CLIENT_SECRET"),
            "username": os.getenv("REDDIT_USERNAME"),
            "password": os.getenv("REDDIT_PASSWORD"),
            "user_agent": os.getenv("REDDIT_USER_AGENT")
        }
    }

def post_to_reddit(title, body, link, creds):
    reddit = praw.Reddit(
        client_id=creds["client_id"],
        client_secret=creds["client_secret"],
        username=creds["username"],
        password=creds["password"],
        user_agent=creds["user_agent"]
    )
    try:
        subreddit = reddit.subreddit("test")  # Change to your subreddit or profile
        if link:
            submission = subreddit.submit(title, url=link)
        else:
            submission = subreddit.submit(title, selftext=body or " ")
        return f"✅ Posted: {submission.shortlink}"
    except Exception as e:
        return f"❌ Failed: {e}"

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")
        link = request.form.get("link")
        platform = request.form.getlist("platforms")
        creds = load_config()["reddit"]
        if "Reddit" in platform:
            message += post_to_reddit(title, body, link, creds) + "\n"
        if "Telegram" in platform:
            message += post_to_telegram(title, body, link) + "\n"
        if "Facebook" in platform:
            message += post_to_facebook(title, body, link) + "\n"
        if "Blogger" in platform:
            message += post_to_blogger(title, body, link) + "\n"
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)


def post_to_telegram(title, body, link):
    # Placeholder function for Telegram posting
    # Integrate Telegram Bot API here
    return "✅ (Simulated) Posted to Telegram"


def post_to_facebook(title, body, link):
    # Placeholder function for Facebook posting
    # Integrate Facebook Graph API here
    return "✅ (Simulated) Posted to Facebook"


def post_to_blogger(title, body, link):
    # Placeholder function for Blogger posting
    # Integrate Google Blogger API here
    return "✅ (Simulated) Posted to Blogger"
