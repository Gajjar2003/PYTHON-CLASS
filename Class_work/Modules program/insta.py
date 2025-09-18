import instaloader

loader = instaloader.Instaloader()

name = input("Enter Instagram username: ")

loader.download_profile(name, profile_pic_only=True)
