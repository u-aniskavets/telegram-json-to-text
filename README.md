# Telegram JSON to Text

A chat exported from Telegram usually contains around 75% unnecessary technical data, which makes AI analysis more expensive and less efficient.

This script removes that extra data and converts the chat into a compact text file that keeps the useful message content and daily dates.

## Why

If you vaguely remember a conversation but do not know the exact date or keywords, you can convert the exported chat to `messages.txt` and give the smaller file to an AI assistant.

Example:

> Find the conversation where we discussed whether people can truly change their personality.

## Features

* Keeps message text in chronological order
* Writes each date once per day
* Supports Telegram rich-text messages
* Skips service events and messages without text
* Shows message counts and file size reduction

## Exporting JSON from Telegram Desktop

To export a chat as JSON:

1. Open the chat menu in Telegram Desktop.
2. Select **Export chat history**.
3. In the export window, find **Format: HTML**.
4. Click **HTML**.
5. Select **Machine-readable JSON**.
6. Choose the export options you need.
7. Click **Export**.

Telegram will create a `result.json` file.

## Usage

Place both files in the same directory:

```text
telegram_json_to_text.py
result.json
```

Run:

```bash
python telegram_json_to_text.py
```

The script creates:

```text
messages.txt
```

## Output

```text
===== 24.07.2025 =====
I sent the documents this morning.
They confirmed that the application was received.

===== 25.07.2025 =====
I received their reply today.
```

## Console Output

```text
40232 - text messages saved to messages.txt
834 - Telegram service events skipped (joins, pins, etc.)
436 - messages with no text skipped (photos, files, stickers, etc.)
29809.7 KB - original result.json size
6534.4 KB - final messages.txt size
4.6x - smaller than the original JSON
```

## License

MIT
