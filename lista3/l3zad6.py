from bs4 import BeautifulSoup
import requests
import webbrowser
import re

def find_wiki_article(loops:int=5) -> None:
    """
    Finds and opens a random article from Wikipedia

    ...

    Input
    ----------
    loops (int): The number of attempts to find a random article (5 by deafult)

    Raises
    ----------
    TypeError: If 'loops' is not an integer
    ValueError: If 'loops' is less than 1
    """

    if type(loops) != int:
        raise TypeError("Loops type has to integer")
    
    if loops < 1:
        raise ValueError("Loops has to be equal or greater than 1")

    url = "https://en.wikipedia.org/wiki/Special:Random"

    for _ in range(loops):
        print("Looking for a random article from wikipedia...")
        
        page = requests.get(url).text

        doc = BeautifulSoup(page, "html.parser")

        art_title = doc.title.text[:-12]    #removing " - Wikipedia" from title

        href = doc.find(rel="canonical")
        art_url = re.search('https://[^\s"]+', str(href)).group()

        response = input(f"Got '{art_title}'. Do u want to proceed? (y/n)")

        if response == "y":
            webbrowser.open(art_url)
            response = input("Do you want to terminate the programm? (y/n)")
            if response == "y":
                break
            else:
                continue


if __name__ == "__main__":
    find_wiki_article()
