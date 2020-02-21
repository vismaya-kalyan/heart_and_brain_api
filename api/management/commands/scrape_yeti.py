import requests
from datetime import datetime
from bs4 import BeautifulSoup
from api.models import Characters
from api.models import Comics
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Scrape the awkward yeti website for heart and brain comics and store it in the DB'

    def handle(self, *args, **options):

        for i in range(1,34):
            URL = 'http://theawkwardyeti.com/chapter/heart-and-brain-2/page/'+str(i)+'/'
            page = requests.get(URL)

            soup = BeautifulSoup(page.content, 'html.parser')
            results = soup.find(id='content-column')
            elems = results.find_all('div', class_='comic')

            for comic in elems:
                post_title = comic.find('h2', class_='post-title')
                post_date =  comic.find('span', class_='post-date')
                comic_chapter = comic.find('div', class_='comic-chapter')
                comic_characters = comic.find('div', class_='comic-characters')
                comic_img = comic.find('img')['src']
                if None in (post_title,post_date,comic_chapter,comic_characters,comic_img):
                    continue
                title = post_title.text.strip()
                date = datetime.strptime(post_date.text.strip(), "%B %d, %Y").date()
                chapter = comic_chapter.text.strip()
                related = [x.strip().replace(" ", "").lower() for x in comic_characters.text.strip().split("Characters: ",1)[-1].split(',')]
    
                try:
                    comic, created = Comics.objects.get_or_create(title = title,date = date, chapter = chapter, image = comic_img)
                except:
                    print(title)
                    print(comic_img)
                    print(Comics.objects.get(title = title).image)
                if not created:
                    continue

                print("related",related)
                for i in related:
                    char, _ = Characters.objects.get_or_create(name = i)
                    comic.characters.add(char)