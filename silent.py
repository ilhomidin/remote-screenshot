"""
Run remscreen without any output.
Write stdout to the `remscreen.log` file.
"""
import subprocess


with open("remscreen.log", "w") as file:
    subprocess.Popen("python remscreen.py", stdout=file)
