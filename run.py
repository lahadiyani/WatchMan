##-----------[Import Module]-------------##
import requests as res
import os, time, re, random, json, base64
from rich import print as cetak
from rich.panel import Panel as nel
from bs4 import BeautifulSoup as babi
from serpapi import GoogleSearch as gs
    

ua = "ua/ua.txt"

##-----------[Warna]---------------------##
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI

def clear():
    os.system("clear")

def ua_random(f):
    try:
        with open(f, "r") as file:
            uas = file.readlines()
            return random.choice(uas).strip() if uas else ""
    except FileNotFoundError:
        print(f"{M} File tidak ditemukan.")
        return ""
##----------------[Person Osint]----------------##
def google_search(query):
    url = f"https://www.google.com/search"
    params = {
        'q': query
    }
    headers = {
    'authority': 'www.google.com',
    'method': 'GET',
    'path': f'/search?q={query}',
    'scheme': 'https',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': 'your cookie'
    'Sec-Ch-Ua': '"Chromium";v="124", "Not-A.Brand";v="99", "Google Chrome";v="124"',
    'Sec-Ch-Ua-Arch': '"x86"',
    'Sec-Ch-Ua-Bitness': '"64"',
    'Sec-Ch-Ua-Full-Version': '"124.0.6367.201"',
    'Sec-Ch-Ua-Full-Version-List': '"Chromium";v="124.0.6367.201", "Not-A.Brand";v="99.0.0.0", "Google Chrome";v="124.0.6367.201"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Model': '""',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
    'Sec-Ch-Ua-Wow64': '?0',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    response = res.get(url, params=params, headers=headers)
    response.raise_for_status()
    soup = babi(response.text, "html.parser")
    search_results = []
    #with open('file.html', 'w') as file:
    #    file.write(soup.prettify())
    for result in soup.find_all('div', class_='N54PNb'):
        title = result.find('h3').get_text()
        url = result.find('a')['href']
        description = result.find('span').get_text()
        search_results.append({'title': title, 'url': url, 'description': description})
    return search_results



def bing_search(query):
    url = "https://www.bing.com/search"
    params = {"q": query}
    headers = {"User-Agent": ua_random(ua)}
    response = res.get(url, params=params, headers=headers)
    response.raise_for_status()
    soup = babi(response.text, 'html.parser')
    search_results = []
    for result in soup.find_all('li', class_='b_algo'):
        title = result.find('h2').get_text()
        url = result.find('a')['href']
        description = result.find('p').get_text()
        search_results.append({'title': title, 'url': url, 'description': description})
    return search_results


def cari_person(query, se="google"):
    if se.lower() == "google":
        return google_search(query)
    elif se.lower() == "bing":
        return bing_search(query)
    else:
        cetak(nel(f"{K} Search Engine Tidak Tersedia."))
        time.sleep(3)
        return None

def person():
    clear()
    banner()
    query = input(f"{H} Masukkan Pencarian: {H}")
    se = input(f"Masukkan Search Engine (google/bing): {H}")
    hasil = cari_person(query, se)
    if hasil:
        cetak(nel(f"Hasil dari {se}: "))
        for i, data in enumerate(hasil, start=1):
            if se.lower() == "google":
                title = re.sub(r"[{}']", "", data['title'])
                url = re.sub(r"[{}']", "", data['url'])
                description = re.sub(r"[{}']", "", data['description'])
                cetak(nel(f"link {i}: {title}\n{url}\n{description}"))
            elif se.lower() == "bing":
                title = re.sub(r"[{}']", "", data['title'])
                url = re.sub(r"[{}']", "", data['url'])
                description = re.sub(r"[{}']", "", data['description'])
                cetak(nel(f"link {i}: {title}\n{url}\n{description}"))
    else:
        print(f"{M} Tidak ada url {M}")

##----------------[Person Image Osint]--------------------##
def img_person():
    clear()
    banner()
    qs = input(f"{H} Masukkan Gambar Url: ")
    params = {
        "engine": "google_reverse_image",
        "image_url": qs,
        "api_key": "your api key"
    }
    search = gs(params)
    results = search.get_dict()
    if 'inline_images' in results and 'image_results' in results:
        im = results['inline_images']
        ir = results['image_results']
        cetak(nel(f"{H} Hasil dari Gamabar {qs} Ditemukan: "))
        cetak(nel(f"{H} Metadata Gambar dibawah ini: "))
        for image in im:
            source = image.get(f"Source", "")
            original = image.get('original', 'N/A')
            title = image.get('title', 'N/A')
            source_name = image.get('source_name', 'N/A')
            cetak(nel(f"""[bold cyan]Source:[/bold cyan] {source}\n[bold cyan]Original:[/bold cyan] {original}\n[bold cyan]Title:[/bold cyan] {title}\n[bold cyan]Source Name:[/bold cyan] {source_name}"""))
        
        cetak(nel(f"{H} Image Results:"))
        for result in ir:
            position = result.get('List', 'N/A')
            title = result.get('title', 'N/A')
            link = result.get('link', 'N/A')
            displayed_link = result.get('displayed_link', 'N/A')
            snippet = result.get('snippet', 'N/A')
            source = result.get('source', 'N/A')
            cetak(nel(f"""[bold cyan]Position:[/bold cyan] {position}\n[bold cyan]Title:[/bold cyan] {title}\n[bold cyan]Link:[/bold cyan] {link}\n[bold cyan]Displayed Link:[/bold cyan] {displayed_link}\n[bold cyan]Snippet:[/bold cyan] {snippet}\n[bold cyan]Source:[/bold cyan] {source}"""))
    else:
        cetak(nel(f"{M} Tidak ada gambar terkait yang ditemukan dalam hasil pencarian."))


def banner():
    cetak(nel(f"""
    
{M} ██╗    ██╗ █████╗ ████████╗ ██████╗██╗  ██╗███╗   ███╗ █████╗ ███╗   ██╗
{M} ██║    ██║██╔══██╗╚══██╔══╝██╔════╝██║  ██║████╗ ████║██╔══██╗████╗  ██║
{M} ██║ █╗ ██║███████║   ██║   ██║     ███████║██╔████╔██║███████║██╔██╗ ██║
{P} ██║███╗██║██╔══██║   ██║   ██║     ██╔══██║██║╚██╔╝██║██╔══██║██║╚██╗██║
{P} ╚███╔███╔╝██║  ██║   ██║   ╚██████╗██║  ██║██║ ╚═╝ ██║██║  ██║██║ ╚████║
{P}  ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝

{P} Sebuah Forensic Tools Untuk Osint by: Hadi                 
    """, width=90, padding=(0,8), title=f"Banner Tools"))
    
def menu():
    clear()
    banner()
    cetak(nel(f"{P} 1.{H} Osint Person By Name  {P} 2.{H} Osint Person By Image {P} 3.{H} coming soon"))
    p = input(f"{H} Masukkan Pilihanmu: {H}")
    if p in ["01", "1"]:
        person()
    elif p in ["02", "2"]:
        img_person()
    else:
        print(f"{M} Masukkan Pilahan Dengan Benar {M}")
        time.sleep(5)
        exit()


if __name__ == "__main__":
    menu()
