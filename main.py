from bs4 import BeautifulSoup
import requests


def scrape_to_csv(response_text):
    """From the input pure html text it takes the value of the class 'text'.
    Separates them to Vietnamese and English words by slicing.
    Exports and appends them to a CSV file"""
    soup = BeautifulSoup(response_text, "html.parser")
    words = soup.find_all(class_="text")
    word_texts = []
    word_list = []
    for word in words:
        text = word.getText()
        word_texts.append(text)
        word_list = word_texts[::2]
    vietnamese = word_list[0::2]
    english = word_list[1::2]

    with open("vietnamese.csv", "a") as file:
        for row in range(len(vietnamese)):

            file.write(f"{vietnamese[row]},{english[row]}\n")


for level in range(1, 85):
    """Loops through all the 84 pages and parses them.
    By using the scrape_to_csv function it exports the Vietnamese and English word-pairs into a CSV file"""
    response = requests.get(f"https://app.memrise.com/course/1070394/duolingo-vietnamese-vocabulary/{level}/")
    response_text = response.text
    scrape_to_csv(response_text)



