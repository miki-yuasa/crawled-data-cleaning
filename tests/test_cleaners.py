from crawled_data_cleaning.cleaner import (
    remove_repeating_new_lines,
    remove_nav_texts,
    remove_text_gpt,
)

text_file_path: str = "assets/texts/hikakin.txt"

with open(text_file_path, "r", encoding="utf-8") as f:
    text: str = f.read()


def test_remove_repeating_new_lines():
    log_path: str = "tmp/log_new_lines.txt"
    cleaned_text = remove_repeating_new_lines(text)

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    print(cleaned_text)

    assert cleaned_text is not None


def test_remove_nav_texts():
    log_path: str = "tmp/log_menu.txt"
    cleaned_text = remove_nav_texts(text)

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    print(cleaned_text)

    assert cleaned_text is not None


def test_remove_text_gpt():
    log_path: str = "tmp/log_gpt.txt"
    cleaned_text = remove_text_gpt(text)

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    print(cleaned_text)

    assert cleaned_text is not None
