
urls = {}

def check_url(url):
    if urls.get(url):
        return f"{urls[url]} - cached"
    else:
        data = f"some data obtained from url {url}"
        urls[url] = data
        return data


def main():
    pages = ["www.google.com", "www.elsitio.com", "www.twitter.com", "www.google.com", "www.elsitio.com"]
    for page in pages:
        data = check_url(page)
        print(data)


if __name__ == "__main__":
    main()