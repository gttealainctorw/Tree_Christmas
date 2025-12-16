import time
import os
import random

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_tree(lights, lyric_line=""):
    tree = [
        "       *       ",
        "      ***      ",
        "     *****     ",
        "    *******    ",
        "   *********   ",
        "  ***********  ",
        " ************* ",
        "***************",
        "      |||      ",
        "      |||      "
    ]

    colors = {
        'R': "\033[31m",  # Rojo
        'G': "\033[32m",  # Verde
        'Y': "\033[33m",  # Amarillo
        'B': "\033[34m",  # Azul
        'M': "\033[35m",  # Púrpura
        'C': "\033[36m",  # Cyan
        'W': "\033[37m"   # Blanco
    }
    RESET = "\033[0m"

    for i, row in enumerate(tree):
        line = ""
        for j, char in enumerate(row):
            if char == '*':
                if lights[i][j]:
                    light_color = random.choice(list(colors.keys()))
                    line += colors[light_color] + "*" + RESET
                else:
                    line += "*"
            else:
                line += char
        
        if i == 4:
            line += "   " + lyric_line
        
        print(line)

def main():
    try:
        lights = [[False for _ in range(15)] for _ in range(8)]
        

        lyrics = [
            "Last Christmas, I gave you my heart",
            "But the very next day, you gave it away",
            "This year, to save me from tears",
            "I'll give it to someone special",
            "",
            "Last Christmas, I gave you my heart",
            "But the very next day, you gave it away",
            "(you gave it away)",
            "This year, to save me from tears",
            "I'll give it to someone special",
            "(special)"
        ]
        
        lyric_index = 0
        char_index = 0
        current_line = lyrics[lyric_index]
        display_text = ""
        
        while True:
            clear_console()
            
            for i in range(8):
                for j in range(15):
                    if random.random() < 0.3:
                        lights[i][j] = random.choice([True, False])
            

            if char_index < len(current_line):
                display_text = current_line[:char_index + 1]
                char_index += 1
            else:
                time.sleep(0.1)
                char_index = 0
                lyric_index = (lyric_index + 1) % len(lyrics)
                current_line = lyrics[lyric_index]
                display_text = ""
            
            print_tree(lights, display_text)
            time.sleep(0.10)  

    except KeyboardInterrupt:
        print("\nAnimación terminada.")

if __name__ == "__main__":
    if os.name == 'nt':
        os.system('color')
    main()