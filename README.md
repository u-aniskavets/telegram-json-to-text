# Telegram JSON to Text

A small, dependency-free Python script that converts a Telegram Desktop JSON export into a compact plain-text file.

It keeps the written content of messages and removes metadata such as sender names, dates, message IDs, reactions, reply references, service events, and media information.

The resulting file is easier to read, search, archive, process, or use with AI tools while consuming less context.

## Features

* One message per line
* Supports Telegram rich-text message structures
* Normalizes spaces and line breaks
* Skips service events and media-only messages
* Works fully offline
* Requires no Telegram login, API credentials, or external Python packages
* Recreates the output file on every run
* Reports message counts and file size reduction

## Use Case

Imagine that you vaguely remember discussing a philosophical topic months or years ago, but you no longer remember when it happened or which exact words were used. In that situation, Telegram search may not help because you do not have a reliable keyword or date.

You can export the chat history, convert it with this script, and get a compact plain-text version that contains only the written message content.

This smaller file can then be reviewed with an AI assistant using a natural-language description of what you remember.

For example:

> Find the conversation where we discussed whether people can truly change their personality.

Removing JSON structure, reactions, IDs, timestamps, sender metadata, and media information reduces the amount of unnecessary text that the AI has to process. More of its context window can then be used for the actual conversation, which makes long chat histories easier to analyze.

After the relevant passage is found, you can use its exact phrases to search for the original message in Telegram.

## Exporting JSON from Telegram Desktop

To export a chat as JSON:

1. Open the chat menu in Telegram Desktop.
2. Select **Export chat history**.
3. In the export window, find the line showing **Format: HTML** and the export path.
4. Click the word **HTML**.
5. Change it to **Machine-readable JSON**.
6. Configure the remaining export options.
7. Click **Export**.

Telegram will create a single `result.json` file. An HTML export may instead contain multiple HTML files and supporting folders.

## Requirements

* Python 3.8 or newer
* A Telegram Desktop export named `result.json`

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

If `messages.txt` already exists, it is overwritten.

## Example Output

```text
I sent the documents this morning.
They confirmed that the application was received.
I will share the result when I receive an answer.
```

## Console Report

```text
Messages written: 10695
Service entries skipped: 2
Messages without text skipped: 98
Input size: 8915.0 KB
Output size: 2184.7 KB
Reduced by: 4.1x
```

* **Service entries skipped:** events such as members joining, messages being pinned, or topics being created.
* **Messages without text skipped:** photos, videos, voice messages, stickers, or files without captions.
* **Reduced by:** the size ratio between the original JSON file and the generated text file.

## Privacy

All processing happens locally.

The script does not connect to Telegram, access your account, use the internet, or upload any files.

Do not commit private `result.json` or `messages.txt` files to a public repository. They are excluded by the included `.gitignore`.

## License

MIT
