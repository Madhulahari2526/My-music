import time
def type_lyric(line, char_delay=0.050):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(char_delay)
    print()

def print_lyrics():
    lyrics = [
        "I want you to know that I'm never leaving",
        "Cause I'm Mrs. Snow, til death we'll be freezing, yeah",
        "You are my home, my home for all seasons",
        "So come on, let's go",
        "Let's go below zero, and hide from the sun",
        "I'll love you forever, where we'll have some fun",
        "Yes, let's hit the North Pole and live happily",
        "Please don't cry no tears now, it's Christmas, baby",
        "My snowman and me, eh",
        "My snowman and me",
        "Baby",
    ]
    delays = [1.0, 0.9, 1.05, 1.2, 0.85, 1.0, 1.0, 0.85, 1.15, 0.95, 0.9, 0.75]
    print("\n🎵 Now Playing - Snowman❤\n")
    time.sleep(1.5)
    for  line,delay in zip(lyrics,delays):
        type_lyric(line)
        time.sleep(delay)

if __name__ == "__main__":
    print_lyrics()
    time.sleep(0.02)