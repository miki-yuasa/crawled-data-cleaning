import os
import re
from typing import Literal

from dotenv import load_dotenv
import openai


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


def remove_text_gpt(
    text: str,
    gpt_model: Literal["gpt-3.5-turbo", "gpt-4"] = "gpt-3.5-turbo",
    openai_api_key: str | None = None,
) -> str:
    """
    Removes unnecessary text from a string using OpenAI's GPT.

    Parameters
    ----------
    text : str
        Text to remove unnecessary text from
    gpt_model : Literal["gpt-3.5-turbo", "gpt-4"] = "gpt-3.5-turbo"
        GPT model to use
    openai_api_key : str | None = None
        OpenAI API key to use

    Returns
    -------
    cleaned_text : str
        Text with unnecessary text removed
    """

    if openai_api_key is None:
        load_dotenv()
        open_ai_api_key = os.getenv("OPENAI_API_KEY")
        if open_ai_api_key is None:
            raise ValueError(
                "OpenAI API key not found. Please set OPEN_AI_API_KEY environment variable."
            )
        else:
            print("Using OpenAI API key from environment variable.")
    else:
        print("Using OpenAI API key from function argument.")

    prompt: str = f"以下の文から不要な要素を取り出してください。\n\n{text}"

    response = openai.ChatCompletion.create(
        model=gpt_model,
        messages=[{"role": "user", "content": prompt}],
    )

    cleaned_text: str = response.choices[0].message.content

    return cleaned_text
