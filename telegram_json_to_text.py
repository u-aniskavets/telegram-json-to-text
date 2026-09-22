# Telegram JSON to Text
# Copyright (c) 2026 Uladzislau Aniskavets
# Project: https://github.com/u-aniskavets/telegram-json-to-text
# License: MIT

import json
import os

# Read the JSON file exported from Telegram.
with open("result.json", "r", encoding="utf-8-sig") as file:
    data = json.load(file)

written = 0
service_skipped = 0
empty_skipped = 0
last_date = None

# Create a compact text file with messages grouped by day.
with open("messages.txt", "w", encoding="utf-8") as file:
    for message in data["messages"]:
        # Skip Telegram events such as joins, leaves and pinned messages.
        if message.get("type") != "message":
            service_skipped += 1
            continue

        text = message.get("text", "")

        # Telegram may store one message as several formatted text parts.
        if isinstance(text, list):
            text = "".join(
                part if isinstance(part, str) else part.get("text", "")
                for part in text
            )

        text = " ".join(text.split())

        # Skip photos, files, stickers, etc. if they contain no text.
        if not text:
            empty_skipped += 1
            continue

        # Telegram date looks like: 2025-07-24T11:20:02
        date = message.get("date", "")[:10]

        # Write the date only once, when a new day begins.
        if date and date != last_date:
            day = f"{date[8:10]}.{date[5:7]}.{date[:4]}"
            file.write(f"\n=== {day} ===\n")
            last_date = date

        file.write(text + "\n")
        written += 1

input_size = os.path.getsize("result.json")
output_size = os.path.getsize("messages.txt")
reduction = input_size / output_size if output_size else 0

# Explain what the conversion produced and what was skipped.
print(f"{written} - text messages saved to messages.txt")
print(f"{service_skipped} - Telegram service events skipped (joins, pins, etc.)")
print(f"{empty_skipped} - messages with no text skipped (photos, files, stickers, etc.)")
print(f"{input_size / 1024:.1f} KB - original result.json size")
print(f"{output_size / 1024:.1f} KB - final messages.txt size")
print(f"{reduction:.1f}x - smaller than the original JSON")
