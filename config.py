import random

CONTENT_MAP = {
    "toy_my": {
        "title": "titles/toy_my.txt",
        "tag": "tags/toy_my.txt"
    },
    "beauty_tiktok": {
        "title": "titles/beauty_tiktok.txt",
        "tag": "tags/beauty_tiktok.txt"
    }
}

TOY_DELAY = (60, 70)
BEAUTY_DELAY = (60, 70)

def random_delay(vtype):
    if vtype == "toy_my":
        return random.randint(*TOY_DELAY)
    return random.randint(*BEAUTY_DELAY)