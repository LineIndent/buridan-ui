import asyncio
from xml.etree import ElementTree as ET
import reflex as rx
import httpx

import google.generativeai as genai

import os


key = os.getenv("KEY")
genai.configure(api_key=key)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 600,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

chat_session = model.start_chat()


class PubMedState(rx.State):
    user_query: str
    loader_txt: str

    is_processing: bool = False
    is_generating: bool = False

    articles: list[dict[str, str]]
    selection: list[dict[str, str]]

    summary: str

    async def generate_abstract_summary(self):
        if self.selection:
            self.is_generating = True
            yield
            abstracts = [
                item["abstract"] for item in self.selection if "abstract" in item
            ]
            message = f"Take the following abstracts and generate a summary based on them in markdown format: {abstracts}"
            response = chat_session.send_message(message)

            for word in response.text.split():
                for char in list(word):
                    self.summary += char
                    await asyncio.sleep(0.009)
                self.summary += " "
                yield

        else:
            yield rx.toast.error("No articles selected!")

        self.is_generating = False

    async def process_request(self):
        self.articles, self.selection, self.summary = [], [], ""
        self.is_processing = True
        self.loader_txt = f"Searching for articles related to '{self.user_query}'..."
        article_ids = await self.search_pubmed(self.user_query)
        yield
        await asyncio.sleep(2)
        if article_ids:
            self.loader_txt = f"Found {len(article_ids)} articles. Fetching details..."
            yield
            articles = await self.fetch_article_details(article_ids)
            for idx, article in enumerate(articles):
                self.articles.append(
                    {
                        "id": f"{idx + 1}",
                        "title": article["title"],
                        "date": article["pubdate"],
                        "url": article["url"],
                        "abstract": article["abstract"],
                    }
                )

        else:
            yield rx.toast.warning("No articles found.")

        self.is_processing = False

    async def search_pubmed(self, query, max_results=10):
        base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        params = {
            "db": "pubmed",
            "term": query,
            "retmode": "json",
            "retmax": max_results,
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(base_url, params=params)
            if response.status_code == 200:
                result = response.json()
                return result["esearchresult"]["idlist"]
            else:
                print("Error:", response.status_code)
                return []

    async def fetch_article_details(self, pmids):
        base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
        params = {
            "db": "pubmed",
            "id": ",".join(pmids),
            "retmode": "xml",
            "rettype": "abstract",
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(base_url, params=params)

            if response.status_code == 200:
                root = ET.fromstring(response.content)

                articles = []
                for article in root.findall(".//PubmedArticle"):
                    title = article.findtext(".//ArticleTitle")
                    abstract = article.findtext(".//AbstractText")
                    pubdate = article.findtext(".//PubDate/Year")
                    pmid = article.findtext(".//PMID")
                    url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"

                    articles.append(
                        {
                            "title": title,
                            "abstract": abstract,
                            "pubdate": pubdate,
                            "url": url,
                        }
                    )
                return articles
            else:
                print("Error:", response.status_code)
                return []

    async def compile_selected_article(self, state: bool, identifier: str):
        article = next(
            (item for item in self.articles if item["id"] == identifier), None
        )
        if self.articles:
            article_copy = dict(article)
            if state:
                if not any(item["id"] == article_copy["id"] for item in self.selection):
                    self.selection.append(article_copy)  # Append a copy, not the proxy
            else:
                self.selection[:] = [
                    item for item in self.selection if item["id"] != identifier
                ]
