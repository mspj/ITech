import httplib
import logging
import urllib
import urllib2
import xml.etree.ElementTree as ET


class APIWrapper(object):
    BASE_URL = "http://www.goodreads.com/"
    KEY = "MDJqEMH3YFyMuHGWqYCnHg"

    MAX_SEARCH_RESULTS = 15

    def http_request(self, url):

        response = None

        try:
            request = urllib2.Request(url)
            logging.info("Making request to %s" % url)
            response = urllib2.urlopen(request)
            logging.info("Returning response from %s" % url)
        except urllib2.HTTPError, e:
            response = False
            logging.error('HTTPError = ' + str(e.code))
        except urllib2.URLError, e:
            logging.error('URLError = ' + str(e.reason))
        except httplib.HTTPException, e:
            logging.error('HTTPException')
        except Exception:
            import traceback
            logging.error('generic exception: ' + traceback.format_exc())

        return response

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
        for i in range(num_authors):
            authors = authors + book.find("authors")[i].find("name").text
            if i < num_authors - 1:
                authors += ", "

        # get the cover of the book
        cover_url = book.find("image_url").text

        return title, authors, cover_url

    def search_book(self, keywords):

        url = "%s/search/index.html?key=%s&q=%s" % (self.BASE_URL, self.KEY, urllib.quote(keywords, safe=''))
        print url
        response = self.http_request(url)

        if response is None:
            return response

        # parse the response
        resp_parsed = ET.parse(response)
        root = resp_parsed.getroot()
        search = root.find("search")

        num_results = 0
        results = []
        for result in search.find("results"):
            book = result.find("best_book")
            book_id = book.find("id").text
            title = book.find("title").text
            author = book.find("author").find("name").text
            cover_url = book.find("image_url").text
            results.append({'id': book_id, 'title': title, 'author': author, 'cover_url': cover_url})
            # results.append((title, author, cover_url))

            num_results += 1
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
