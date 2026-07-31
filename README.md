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
Messages written: 4208
Service entries skipped: 523
Messages without text skipped: 40
Input size: 4200.5 KB
Output size: 310.2 KB
Reduced by: 13.5x
```

* **Service entries skipped** — events such as members joining, messages being pinned, or topics being created.
* **Messages without text skipped** — photos, videos, voice messages, stickers, or files without captions.
* **Reduced by** — the size ratio between the original JSON file and the generated text file.

## Privacy

All processing happens locally.

The script does not connect to Telegram, access your account, use the internet, or upload any files.

Do not commit private `result.json` or `messages.txt` files to a public repository. They are excluded by the included `.gitignore`.

## License

MIT
