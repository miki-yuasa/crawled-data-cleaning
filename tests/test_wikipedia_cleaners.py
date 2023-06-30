import re

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

    assert (
        re.search(
            "(コンテンツにスキップ|メインメニュー|サイドバーに移動|非表示(\n)+		案内|メインページコミュニティ・ポータル最近の出来事新しいページ最近の更新おまかせ表示練習用ページアップロード \(ウィキメディア・コモンズ\)(\n)+		ヘルプ|ヘルプ井戸端お知らせバグの報告寄付ウィキペディアに関するお問い合わせ|言語\n\nこのWikipediaでは言語間リンクがページの先頭にある記事タイトルの向かい側に設置されています。ページの先頭をご覧ください。|検索(\n)+検索|アカウント作成ログイン|個人用ツール(\n)+ アカウント作成 ログイン|ログアウトした編集者のページ|もっと詳しく|投稿記録トーク|閲覧\n\nソースを閲覧\n\n履歴表示)",
            cleaned_text,
        )
        is None
    )


def test_remove_index():
    log_path: str = "tmp/wiki_index.txt"
    cleaned_text = remove_index(text)

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    print(cleaned_text)

    assert re.search("目次[\s\S]*目次の表示・非表示を切り替え", cleaned_text) is None


def test_remove_language_links():
    log_path: str = "tmp/wiki_language_links.txt"
    cleaned_text = remove_language_links(text)

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    print(cleaned_text)

    assert re.search("[0-9]{1,}の言語版[\s\S]*日本語", cleaned_text) is None


def test_remove_tool_menu():
    log_path: str = "tmp/wiki_tool_menu.txt"
    cleaned_text = remove_tool_menu(text)

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    print(cleaned_text)

    assert re.search("ツール[\s\S]*出典: フリー百科事典『ウィキペディア（Wikipedia）』", cleaned_text) is None


def test_remove_footer():
    log_path: str = "tmp/wiki_footer.txt"
    cleaned_text = remove_footer(text)

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    print(cleaned_text)

    assert re.search("表話編歴[\s\S]*典拠管理 全般[\s\S]*本文の横幅制限を有効化／無効化", cleaned_text) is None


def test_clean_wikipedia_page():
    log_path: str = "tmp/wiki_cleaned.txt"
    cleaned_text = clean_wikipedia_page(text)

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    print(cleaned_text)

    assert (
        re.search(
            "(コンテンツにスキップ|メインメニュー|サイドバーに移動|非表示(\n)+		案内|メインページコミュニティ・ポータル最近の出来事新しいページ最近の更新おまかせ表示練習用ページアップロード \(ウィキメディア・コモンズ\)(\n)+		ヘルプ|ヘルプ井戸端お知らせバグの報告寄付ウィキペディアに関するお問い合わせ|言語\n\nこのWikipediaでは言語間リンクがページの先頭にある記事タイトルの向かい側に設置されています。ページの先頭をご覧ください。|検索(\n)+検索|アカウント作成ログイン|個人用ツール(\n)+ アカウント作成 ログイン|ログアウトした編集者のページ|もっと詳しく|投稿記録トーク|閲覧\n\nソースを閲覧\n\n履歴表示)|目次[\s\S]*目次の表示・非表示を切り替え|[0-9]{1,}の言語版[\s\S]*日本語|ツール[\s\S]*出典: フリー百科事典『ウィキペディア（Wikipedia）』|表話編歴[\s\S]*典拠管理 全般[\s\S]*本文の横幅制限を有効化／無効化",
            cleaned_text,
        )
        is None
    )
