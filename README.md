<p align="center">
  <pre>
██████╗  ██████╗  ██████╗ ██╗  ██╗    ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██████╔╝██║   ██║██║   ██║█████╔╝     ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
██╔══██╗██║   ██║██║   ██║██╔═██╗     ╚════██║██║     ██╔══██╗██╔══██║██╔══██╗██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝╚██████╔╝██║  ██╗    ███████║╚██████╗██║  ██║██║  ██║██║  ██║███████╗██║  ██║
╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
  </pre>
</p>

<h1 align="center">📚 THE BOOK SCRAPER<br>WITH INTERACTIVE SEARCH 🔍</h1>

<p align="center">
  <strong>Professional book crawling & search tool — v1.0.0</strong><br>
  <em>Scrapy CrawlSpider • JSON export • CLI filter engine • For educational use</em>
</p>

<p align="center">
  <a href="https://github.com/Ali-Haidar-Sy/scrap/stargazers"><img src="https://img.shields.io/github/stars/Ali-Haidar-Sy/scrap?style=for-the-badge&color=yellow"></a>
  <a href="https://github.com/Ali-Haidar-Sy/scrap/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Ali-Haidar-Sy/scrap?style=for-the-badge&color=blue"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white"></a>
  <a href="https://scrapy.org/"><img src="https://img.shields.io/badge/Scrapy-2.12+-green?style=for-the-badge&logo=scrapy&logoColor=white"></a>
  <a href="https://t.me/P33_9"><img src="https://img.shields.io/badge/Telegram-@P33_9-2CA5E0?style=for-the-badge&logo=telegram"></a>
  <a href="https://www.instagram.com/_ungn"><img src="https://img.shields.io/badge/Instagram-@_ungn-E4405F?style=for-the-badge&logo=instagram"></a>
  <a href="https://github.com/Ali-Haidar-Sy"><img src="https://img.shields.io/badge/GitHub-Ali--Haidar--Sy-181717?style=for-the-badge&logo=github"></a>
</p>

---

## 📖 FEATURES — SCRAPE & SEARCH LIKE A PRO

| Category           | Capabilities                                                                 |
|--------------------|------------------------------------------------------------------------------|
| **Scraping Engine** | CrawlSpider with smart link rules • parallel request handling • JSON output |
| **Data Fields**     | Title • Price (£) • Stock availability • Rating (One‑Five) • Category • URL |
| **CLI Search Tool** | Interactive menu • search by title • filter by max price • filter by rating  |
| **Export**          | Compact `books.json` ready for analysis or further filtering                 |
| **Code Quality**    | Clean Scrapy project structure • Scrapy Item definitions • custom pipeline   |

---

## 🚀 QUICK START

```bash
# 1. Clone the scraper's den
git clone https://github.com/Ali-Haidar-Sy/scrap.git
cd scrap

# 2. Install dependencies
pip install -r requirements.txt

# 3. Crawl the book store
cd lab2_scrapy
scrapy crawl books -o books.json

# 4. Launch the interactive search
cd ..
python search_books.py
Example session:

text
=== Book Search Interface ===
1. Search by title
2. Filter by maximum price
3. Filter by rating
4. Show all books
5. Exit
Enter choice (1-5): 1
Enter title (or part): sapiens
→ Sapiens: A Brief History of Humankind | Price: £54.23 | Rating: Five ...
⚠️ LEGAL NOTICE
This tool is designed for educational purposes and for scraping the openly available demo site books.toscrape.com.
Always respect robots.txt and the terms of service of any website you intend to scrape. Obtain permission when required.
The author is not responsible for misuse.

🤝 CONTRIBUTING
Found a bug or want to add a new search filter?
Open an Issue or submit a Pull Request. Contributions are always welcome!

📞 CONNECT WITH ME
Platform	Handle
Telegram	@P33_9
Instagram	@_ungn
GitHub	Ali-Haidar-Sy
<p align="center">
  <strong>📚 May your shelves be full and your data clean. 🔍</strong><br>
  ⭐ If this scraper saved you time, <strong>give it a star</strong> on GitHub! ⭐
</p>
