from crawled_data_cleaning.wikipedia import (
    remove_menu,
    remove_index,
    remove_language_links,
    remove_tool_menu,
    remove_footer,
    clean_wikipedia_page,
)

text_file_path: str = "assets/texts/hikakin.txt"

with open(text_file_path, "r", encoding="utf-8") as f:
    text: str = f.read()


def test_remove_menu():
    log_path: str = "tmp/wiki_menu.txt"
    cleaned_text = remove_menu(text)

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    print(cleaned_text)

    assert cleaned_text is not None


def test_remove_index():
    log_path: str = "tmp/wiki_index.txt"
    cleaned_text = remove_index(text)

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    print(cleaned_text)

    assert cleaned_text is not None


def test_remove_language_links():
    log_path: str = "tmp/wiki_language_links.txt"
    cleaned_text = remove_language_links(text)

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    print(cleaned_text)

    assert cleaned_text is not None


def text_remove_tool_menu():
    log_path: str = "tmp/wiki_tool_menu.txt"
    cleaned_text = remove_tool_menu(text)

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    print(cleaned_text)

    assert cleaned_text is not None


def text_remove_footer():
    log_path: str = "tmp/wiki_footer.txt"
    cleaned_text = remove_footer(text)

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    print(cleaned_text)

    assert cleaned_text is not None


def test_clean_wikipedia_page():
    log_path: str = "tmp/wiki_cleaned.txt"
    cleaned_text = clean_wikipedia_page(text)

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    print(cleaned_text)

    assert cleaned_text is not None
