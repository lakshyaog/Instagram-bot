from instabot import Bot

# Create an instance of the Bot
bot = Bot()

# Login to your Instagram account
username = "your_username"
password = "your_password"
bot.login(username=username, password=password)

# Like posts based on a hashtag
hashtag = "your_hashtag"
number_of_posts = 5

# Get posts by hashtag
posts = bot.get_hashtag_medias(hashtag)

# Like specified number of posts
for post in posts[:number_of_posts]:
    bot.like(post)

print(f"Liked {number_of_posts} posts with hashtag #{hashtag}.")
