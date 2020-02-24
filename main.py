import praw, sys, imgkit, regex, os

reddit = praw.Reddit('redditcrawler', user_agent='Python:RedditVideoCreator:v1.0.0 (by u/Brodude1337)')  # Create instance with details from praw.ini

url = str(sys.argv[1])

print("Generating video from: " + url)

post = reddit.submission(url=url)

punct_regex = regex.compile(r'(\p{Punctuation})')  # Regex example from https://codereview.stackexchange.com/questions/230126/string-operation-to-split-on-punctuation

post_forest = post.comments
post_forest.replace_more(0,0)

for comment in post_forest:
    comment_list = punct_regex.split(comment.body)
    comment_compiled = str()

    for index in range(0,len(comment_list)):
        try:
            print(comment.body)
        except:
            continue
        if index % 2 == 1:
            continue
        comment_compiled += comment_list[index]
        if index+1 < len(comment_list):
            comment_compiled += comment_list[index + 1]
        if os.path.exists("screenshot_source.html"):
            os.remove("screenshot_source.html")
        htmlfile = open("screenshot_source.html", "w")
        htmlfile.write("<!DOCTYPE html>\n")
        htmlfile.write("<html lang=\"en\">\n")
        htmlfile.write("<body>\n")
        htmlfile.write("<p style=\"font-family:Verdana;font-size:10px;color:#336699;font-weight:700;display:inline;\">[-] </p>\n")
        htmlfile.write("<p style=\"font-family:Verdana;font-size:10px;color:#336699;font-weight:700;display:inline;\">")
        try:
            htmlfile.write(comment.author.name)
        except:
            htmlfile.write("[deleted]")
        htmlfile.write("</p>\n")
        htmlfile.write("<p style=\"font-family:Verdana;font-size:10px;color:#888888;font-weight:400;display:inline;\">")
        htmlfile.write(str(comment.score))
        htmlfile.write(" points</p>\n")
        htmlfile.write("<br>\n")
        htmlfile.write("<p style=\"font-family:Verdana;font-size:14px;color:#222222;line-height:20px;font-weight:400;display:inline;\">")
        htmlfile.write(comment_compiled)
        htmlfile.write("</p>\n")
        htmlfile.write("</html>")
        htmlfile.close()

