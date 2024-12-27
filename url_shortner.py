import pyshorteners

shortner = pyshorteners.Shortener()
link = input("Enter a link >>  ")
x = shortner.tinyurl.short(link)
print(f"your new short link is >> ",{x})