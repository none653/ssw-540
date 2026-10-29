from html.parser import HTMLParser
from urllib.parse import urlparse, urljoin
from collections import defaultdict
from pathlib import Path
import argparse


class LinkExtractor(HTMLParser):


    def __init__(self, base_url=None):
        super().__init__()
        self.links = []
        self.base_url = base_url

    def handle_starttag(self, tag, attrs):
        if tag.lower() in ("a", "area"):
            for name, value in attrs:
                if name.lower() == "href" and value:
                    link = value.strip()

                    if link:

                        if self.base_url:
                            link = urljoin(self.base_url, link)

                        self.links.append(link)


def get_domain(link):
  
    parsed = urlparse(link)

    if parsed.hostname and parsed.scheme.lower() in ("http", "https"):
        return parsed.hostname.lower()


    if parsed.hostname and not parsed.scheme:
        return parsed.hostname.lower()

    return "(relative or non-web link)"


def main():
    arg_parser = argparse.ArgumentParser(
        description="Extract HTML hyperlinks and sort them by domain."
    )
    arg_parser.add_argument(
    "html_file",
    nargs="?",
    default=str(Path(__file__).resolve().parent / "sample.html"),
    help="Path to the HTML file"
    )
    arg_parser.add_argument(
        "--base-url",
        help="Optional page URL for resolving relative links"
    )
    args = arg_parser.parse_args()


    with open(args.html_file, "r", encoding="utf-8", errors="replace") as file:
        html_content = file.read()

    extractor = LinkExtractor(base_url=args.base_url)
    extractor.feed(html_content)

  
    grouped_links = defaultdict(list)

    for link in extractor.links:
        domain = get_domain(link)
        grouped_links[domain].append(link)


    for domain in sorted(grouped_links):
        print(f"\nDomain: {domain}")

        for link in sorted(grouped_links[domain], key=str.casefold):
            print(f"  {link}")


if __name__ == "__main__":
    main()
