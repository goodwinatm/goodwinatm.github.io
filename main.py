import os
import openai
from git import Repo
from pathlib import Path
os.environ["GUY_OPENAI_KEYS"]='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'
openai.api_key=os.getenv("GUY_OPENAI_KEYS")
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
PATH_TO_BLOG_REPO=Path("C:\\Users\\guy52\\PycharmProjects\\goodwinatm.github.io\\.git")
PATH_TO_BLOG = PATH_TO_BLOG_REPO.parent
PATH_TO_CONTENT=PATH_TO_BLOG/"content"
# print(PATH_TO_CONTENT)
PATH_TO_CONTENT.mkdir(exist_ok=True,parents=True)
def update_blog(commit_message='Updates blog'):
    #GitPython -- Repo Location
    repo=Repo(PATH_TO_BLOG_REPO)
    #git add
    repo.git.add(all=True)
    #git commit -m "updates blog"
    repo.index.commit(commit_message)
    #git push
    origin = repo.remote(name='origin')
    origin.push()
random_text_string="Today interview Set <String> s= driver.getwindowshandles"
with open(PATH_TO_BLOG/"index.html", 'w') as f:
    f.write(random_text_string)
update_blog()