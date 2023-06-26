import re


def remove_menu(text: str) -> str:
    """
    Removes menu texts from a Wikipedia page.

    Parameters
    ----------
    text : str
        Text to remove menu texts from

    Returns
    -------
    cleaned_text : str
        Text with menu texts removed
    """

    cleaned_text: str = re.sub(
        r"(コンテンツにスキップ|メインメニュー|サイドバーに移動|非表示(\n)+		案内|メインページコミュニティ・ポータル最近の出来事新しいページ最近の更新おまかせ表示練習用ページアップロード \(ウィキメディア・コモンズ\)(\n)+		ヘルプ|ヘルプ井戸端お知らせバグの報告寄付ウィキペディアに関するお問い合わせ|言語\n\nこのWikipediaでは言語間リンクがページの先頭にある記事タイトルの向かい側に設置されています。ページの先頭をご覧ください。|検索(\n)+検索|アカウント作成ログイン|個人用ツール(\n)+ アカウント作成 ログイン|ログアウトした編集者のページ|もっと詳しく|投稿記録トーク|閲覧\n\nソースを閲覧\n\n履歴表示)",
        "",
        text,
    )

    return cleaned_text


def remove_index(text: str) -> str:
    """
    Removes index texts from a Wikipedia page.

    Parameters
    ----------
    text : str
        Text to remove index texts from

    Returns
    -------
    cleaned_text : str
        Text with index texts removed
    """

    cleaned_text: str = re.sub(r"目次[\s\S]*目次の表示・非表示を切り替え", "", text)

    return cleaned_text


def remove_language_links(text: str) -> str:
    """
    Removes language links from a Wikipedia page.

    Parameters
    ----------
    text : str
        Text to remove language links from

    Returns
    -------
    cleaned_text : str
        Text with language links removed
    """

    cleaned_text = re.sub(
        r"[0-9]{1,}の言語版[\s\S]*日本語",
        "",
        text,
    )

    return cleaned_text


def remove_tool_menu(text: str) -> str:
    """
    Removes tool menu texts from a Wikipedia page.

    Parameters
    ----------
    text : str
        Text to remove tool menu texts from

    Returns
    -------
    cleaned_text : str
        Text with tool menu texts removed
    """

    cleaned_text: str = re.sub(r"ツール[\s\S]*出典: フリー百科事典『ウィキペディア（Wikipedia）』", "", text)

    return cleaned_text


def remove_footer(text: str) -> str:
    """
    Removes footer texts from a Wikipedia page.

    Parameters
    ----------
    text : str
        Text to remove footer texts from

    Returns
    -------
    cleaned_text : str
        Text with footer texts removed
    """

    cleaned_text: str = re.sub(r"典拠管理 全般[\s\S]*本文の横幅制限を有効化／無効化", "", text)

    return cleaned_text


def clean_wikipedia_page(text: str) -> str:
    """
    Cleans a Wikipedia page.

    Parameters
    ----------
    text : str
        Text to clean

    Returns
    -------
    cleaned_text : str
        Cleaned text
    """

    cleaned_text: str = remove_menu(text)
    cleaned_text: str = remove_index(cleaned_text)
    cleaned_text: str = remove_language_links(cleaned_text)
    cleaned_text: str = remove_tool_menu(cleaned_text)
    cleaned_text: str = remove_footer(cleaned_text)

    return cleaned_text
