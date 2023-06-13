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
