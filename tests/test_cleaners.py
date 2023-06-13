from crawled_data_cleaning.cleaner import (
    remove_repeating_new_lines,
    remove_nav_texts,
    remove_text_gpt,
)

text: str = """【Innovation LAB】NTTPCのAIパートナープログラム


CONTACT


TOP
ABOUT
PARTNERS
CASE
INTERVIEW
JOIN US




CASE活動実績
BACK TO LIST



おおいたAIテクノロジーセンター・NTTPC
つくみんAIアイデアソン
NTTPCは、2/22（水）、23（木）に津久見市で開催された『つくみんAIアイデアソン』にAIファシリテーターとして参加。
22日は、マグロ加工工場、石灰鉱山・石灰製造現場、つくみイルカ島の飼育現場、みかん農家の生産・販売現場の4つの現場を視察するフィールドワークを実施。
各コースには、業種・立場を問わずさまざまな参加者が入り、さまざまな視点を持って、AI利活用の課題解決や価値創造の種を生み出す企画。23日は、22日のフィールドワークを参考にして、AIアイデアソンを取り組み、AIアイデアを各チームより発表。

開催日：2023年2月22日~23日"""


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
