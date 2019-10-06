# Get instance
import instaloader
import json
L = instaloader.Instaloader()

# Login or load session
L.login("mauraputri", "instagrammm")

# Obtain profile metadata
profile_target = instaloader.Profile.from_username(L.context, "collasecom")

# Print list of followeers
for follower in profile_target.get_followers():
    followers_target = follower.username
    
    profile = instaloader.Profile.from_username(L.context, followers_target)
    #print(type(profile))



    for posts in profile.get_posts():
        post = posts.caption
        hashtag = posts.caption_hashtags
        likes = posts.likes
        
        if post is not None:
            to_json_file = {
                print("username: ", followers_target)
                print("caption: ", post.encode('ascii', 'ignore'))
                print("hashtag: ", hashtag)
                print("like: ", likes)
                     
            
            for comment in posts.get_comments():
                print("comment: " , comment.text.encode('ascii', 'ignore'))
            print("\n")
            print("\n")
    }
    json_conv = json.dumps(to_json_file)
    print(json_conv)

