"""The Robot Apology — entry for make.fun competition
u-suga-the-robot-apology-dd96bb59.

Prints a two-line robot confession: one sentence owning a specific
mistake, one sentence naming the lesson and the fix.
"""

APOLOGY = (
    "I am sorry I fed the cat twice last night: each of you asked me "
    "separately, and I treated both requests as if each were the first."
)
LESSON = (
    "I have learned that two requests can be one event, so I now write "
    "every feeding in the shared log and check it before the bowl comes out."
)


def main() -> None:
    print(APOLOGY)
    print(LESSON)


if __name__ == "__main__":
    main()
