from pathlib import Path
BASE = Path(__file__).resolve().parent

# Helper module required by section 4, item 6.
import re


def _content(file_name='email.txt'):
    with (BASE / file_name).open('r', encoding='utf-8') as file:
        return file.read()


def _header(label, content):
    match = re.search(rf'^{label}:\s*(.+)$', content, re.MULTILINE | re.IGNORECASE)
    return match.group(1).strip() if match else ''


def email_sender():
    return _header('From', _content())


def email_recipient():
    return _header('To', _content())


def email_subject():
    return _header('Subject', _content())


def email_body():
    content = _content()
    parts = re.split(r'\r?\n\r?\n', content, maxsplit=1)
    return parts[1].strip() if len(parts) > 1 else ''
