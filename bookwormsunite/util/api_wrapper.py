import xml.etree.ElementTree as ET
import urllib2
import urllib
import logging

class APIWrapper(object):

    BASE_URL = "http://www.goodreads.com/"
    KEY = "MDJqEMH3YFyMuHGWqYCnHg"

    MAX_SEARCH_RESULTS = 10

    def http_request(self, url):
        request = urllib2.Request(url)
        logging.info("Making request to %s" % url)
        return urllib2.urlopen(request)

    # get the details of a book from its ISBN (Can be both ISBN10 and ISBN13)
    def get_book_info_by_isbn(self, isbn):

        # make HTTP request
        url = "%s/book/isbn?key=%s&isbn=%s" % (self.BASE_URL, self.KEY, isbn)
        response = self.http_request(url)

        # parse the response
        resp_parsed = ET.parse(response)
        root = resp_parsed.getroot()
        book = root.find("book")

        # get the name of the book
        title = book.find("title").text

        # get the authors of the book
        authors = ""
        num_authors = len(book.find("authors"))
        for i in range (num_authors):
            authors = authors + book.find("authors")[i].find("name").text
            if( i < num_authors - 1 ):
                authors = authors + ", "

        # get the cover of the book
        cover_url = book.find("image_url").text

        return (title, authors, cover_url)

    def search_book(self, keywords):

        url = "%s/search/index.html?key=%s&q=%s" % (self.BASE_URL, self.KEY, urllib.quote(keywords, safe=''))
        print url
        response = self.http_request(url)

        # parse the response
        resp_parsed = ET.parse(response)
        root = resp_parsed.getroot()
        search = root.find("search")

        num_results = 0
        results = []
        for result in search.find("results"):
            book = result.find("best_book")
            title = book.find("title").text
            author = book.find("author").find("name").text
            cover_url = book.find("image_url").text
            results.append((title, author, cover_url))

            num_results = num_results + 1
            if num_results == self.MAX_SEARCH_RESULTS:
                break

        return results


# x = APIWrapper()
# title, authors, img = x.get_book_info_by_isbn('9780679783268')
# print title
# print authors
#
# results = x.search_book("hunger's games")
# print results