import praw

def post_to_reddit(title, body, link, image_path, creds):
    reddit = praw.Reddit(
        client_id=creds["uZF-msBMxFsm8JoRdKX9UQ"],
        client_secret=creds["9DR9y9nseRKksyyFublFnX3piA6uhQ"],
        username=creds["LargePick7036"],
        password=creds["Rehana.978"],
        user_agent=creds["reddit_post.py"]
    )

    try:
        # Post to user's profile (safer than subreddit)
        target = f'u_{creds["LargePick7036"]}'
        subreddit = reddit.subreddit(target)

        # Add a fallback selftext for link posts (Reddit spam filter workaround)
        if link:
            body = body if body else "Check this out 👇"
            post = subreddit.submit(title=title, url=link, send_replies=False)
        else:
            post = subreddit.submit(title=title, selftext=body or " ", send_replies=False)

        return f"✅ Reddit: {post.shortlink}"

    except Exception as e:
        return f"❌ Reddit Error: {str(e)}"

