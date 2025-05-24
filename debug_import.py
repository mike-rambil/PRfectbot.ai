print("DEBUG SCRIPT STARTED")
import sys
import os
import prfectbot.gitutils

print("sys.path:", sys.path)
print("cwd:", os.getcwd())
print("prfectbot.gitutils path:", prfectbot.gitutils.__file__)
print("detect_code_changes signature:", prfectbot.gitutils.detect_code_changes)
print(
    "detect_code_changes args:",
    prfectbot.gitutils.detect_code_changes.__code__.co_varnames[
        : prfectbot.gitutils.detect_code_changes.__code__.co_argcount
    ],
)
