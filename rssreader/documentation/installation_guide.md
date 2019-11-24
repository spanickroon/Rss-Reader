# RSS reader
RSS reader should be a command-line utility which receives RSS URL and prints results in human-readable format.

## Guide
1. Clone or Download [repository](https://github.com/Spanickroon/PythonHomework)
2. Go to folder /PythonHomework
3. **git branch**
4. There is no branch besides **master**? Then follow this tutorial.
    + **git branch -a**. Oh and here she is :D. Let's add it.
    + **git branch --track FinalTask remotes/origin/FinalTask**.
    + **git checkout FinalTask**.
    + **git branch**.
5. I recommend creating a virtual environment. **python3.8 -m venv env**, **source env/bin/activate**.
6. After this tutorial you will be in the branch **FinalTask**.
7. If you do not see the folder **dist**, this means that I did not compile the package, then collect it yourself. If there is a folder **dist**, then go to step **9**.
8. Let's collect our package **python3.8 setup.py sdist**.
9. Let's install our package **pip3.8 install dist/rss-reader-2.1.tar.gz**
10. All is ready. Read **manual**.