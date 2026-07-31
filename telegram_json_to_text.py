# Telegram JSON to Text
# Copyright (c) 2026 Uladzislau Aniskavets
# Project: https://github.com/u-aniskavets/telegram-json-to-text
# License: MIT

import json
import os

with open("result.json", "r", encoding="utf-8-sig") as file:
    data = json.load(file)

written = 0
service_skipped = 0
empty_skipped = 0

with open("messages.txt", "w", encoding="utf-8") as file:
    for message in data["messages"]:
        if message.get("type") != "message":
            service_skipped += 1
            continue

        text = message.get("text", "")

        if isinstance(text, list):
            text = "".join(
                part if isinstance(part, str) else part.get("text", "")
                for part in text
            )

        text = " ".join(text.split())

        if not text:
            empty_skipped += 1
            continue

        file.write(text + "\n")
        written += 1

input_size = os.path.getsize("result.json")
output_size = os.path.getsize("messages.txt")
reduction = input_size / output_size if output_size else 0

print(f"Messages written: {written}")
print(f"Service entries skipped: {service_skipped}")
print(f"Messages without text skipped: {empty_skipped}")
print(f"Input size: {input_size / 1024:.1f} KB")
print(f"Output size: {output_size / 1024:.1f} KB")
print(f"Reduced by: {reduction:.1f}x")
