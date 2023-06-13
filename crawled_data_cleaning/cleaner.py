import re


def remove_repeating_new_lines(text: str) -> str:
    """
    Removes repeating new lines from a string

    Parameters
    ----------
    text : str
        Text to remove repeating new lines from

    Returns
    -------
    cleaned_text : str
        Text with repeating new lines removed
    """

    cleaned_text = re.sub(r"\n+", "\n", text)

    return cleaned_text


def remove_nav_texts(text: str) -> str:
    """
    Removes navigation texts from a string such as "CONTACT", "TOP", "ABOUT", "JOIN US" and "BACK TO LIST".

    Parameters
    ----------
    text : str
        Text to remove menu texts from

    Returns
    -------
    cleaned_text : str
        Text with menu texts removed
    """

    cleaned_text = re.sub(
        r"(CONTACT|TOP|ABOUT|BACK TO LIST|JOIN US|Contact|Top|About)", "", text
    )

    return cleaned_text
