import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ITech.settings')

import django

django.setup()

import datetime
from django.utils import timezone
from bookwormsunite.models import *


def populate():
    reader1 = add_reader("sashaalsberg", 'https://d.gr-assets.com/users/1444743640p6/10915830.jpg')
    reader2 = add_reader("tammy", 'https://d.gr-assets.com/users/1394292082p6/28395194.jpg')
    reader3 = add_reader("emily-may", 'https://d.gr-assets.com/users/1402215455p6/4622890.jpg')
    reader4 = add_reader("beckfoster", 'https://d.gr-assets.com/users/1383924009p6/5875398.jpg')
    reader5 = add_reader("maliemania", 'https://d.gr-assets.com/users/1415192892p6/1334245.jpg')
    reader6 = add_reader("pimjunha", 'https://d.gr-assets.com/users/1376729372p6/15480984.jpg', is_superuser=True)

    r1 = add_readathon("Winter Biannual Bibliothon",
                       "A week of reading and booktubing hosted by MissSassyKassie, emmmabooks, Kellys BookSpill, Little Red Reader, sierrareads, OHxXxSNAP13 and Brittni's Book Find!",
                       datetime.datetime(2016, 1, 3, 0, 0, 0, tzinfo=timezone.get_current_timezone()),
                       datetime.datetime(2016, 1, 9, 23, 59, 59, tzinfo=timezone.get_current_timezone()))

    r2 = add_readathon("Bout of Books 15.0",
                       "The Bout of Books Read-a-Thon was created by Amanda @ On a Book Bender on a complete whim in August 2011*. It took on a life of its own and was such a hit that Amanda decided to do it again and turn it into a somewhat regular occurrence. \n" +
                       "It is low pressure, meaning participants are only asked to push themselves to read more than they normally would during any given week. There is no competition between readers.",
                       datetime.datetime(2016, 1, 4, 0, 0, 0, tzinfo=timezone.get_current_timezone()),
                       datetime.datetime(2016, 1, 10, 23, 59, 59, tzinfo=timezone.get_current_timezone()))

    r3 = add_readathon("TopicAThon",
                       "",
                       datetime.datetime(2016, 2, 10, 0, 0, 0, tzinfo=timezone.get_current_timezone()),
                       datetime.datetime(2016, 2, 14, 23, 59, 59, tzinfo=timezone.get_current_timezone()))

    r4 = add_readathon("AYearAThon (Horror/Suspense)",
                       "This group is for yearly read-a-thons.We'll do one read-a-thon a month, the first full week of every month. We also occasionally vote on one group read a month.",
                       datetime.datetime(2016, 3, 7, 0, 0, 0, tzinfo=timezone.get_current_timezone()),
                       datetime.datetime(2016, 3, 13, 23, 59, 59, tzinfo=timezone.get_current_timezone()))

    r5 = add_readathon("AYearAThon (Re-reads)",
                       "This group is for yearly read-a-thons.We'll do one read-a-thon a month, the first full week of every month. We also occasionally vote on one group read a month.",
                       datetime.datetime(2016, 4, 4, 0, 0, 0, tzinfo=timezone.get_current_timezone()),
                       datetime.datetime(2016, 4, 10, 23, 59, 59, tzinfo=timezone.get_current_timezone()))

    r6 = add_readathon("Bout of Books 16.0",
                       "The Bout of Books Read-a-Thon was created by Amanda @ On a Book Bender on a complete whim in August 2011*. It took on a life of its own and was such a hit that Amanda decided to do it again and turn it into a somewhat regular occurrence. \n" +
                       "It is low pressure, meaning participants are only asked to push themselves to read more than they normally would during any given week. There is no competition between readers.",
                       datetime.datetime(2016, 5, 9, 0, 0, 0, tzinfo=timezone.get_current_timezone()),
                       datetime.datetime(2016, 5, 15, 23, 59, 59, tzinfo=timezone.get_current_timezone()))

    r7 = add_readathon("Summer Biannual Bibliothon",
                       "A week of reading and booktubing hosted by MissSassyKassie, emmmabooks, Kellys BookSpill, Little Red Reader, sierrareads, OHxXxSNAP13 and Brittni's Book Find!",
                       datetime.datetime(2016, 6, 3, 0, 0, 0, tzinfo=timezone.get_current_timezone()),
                       datetime.datetime(2016, 6, 9, 23, 59, 59, tzinfo=timezone.get_current_timezone()))

    r8 = add_readathon("MS Readathon",
                       "The MS Readathon run by MS Australia started in 1979 and is Australia's premier reading-based fundraiser. The MS Readathon encourages Australians to read books, learn about multiple sclerosis (MS) and raise funds to help people living with Multiple Sclerosis.",
                       datetime.datetime(2016, 8, 1, 0, 0, 0, tzinfo=timezone.get_current_timezone()),
                       datetime.datetime(2016, 8, 31, 23, 59, 59, tzinfo=timezone.get_current_timezone()))

    r9 = add_readathon("Harry Xmas To You",
                       "A Read-a-Watch-a-Long-a-Thon of Harry Potter in the month of December!",
                       datetime.datetime(2016, 12, 1, 0, 0, 0, tzinfo=timezone.get_current_timezone()),
                       datetime.datetime(2016, 12, 31, 23, 59, 59, tzinfo=timezone.get_current_timezone()))

    r10 = add_readathon("CramAThon",
                        "",
                        datetime.datetime(2016, 12, 17, 0, 0, 0, tzinfo=timezone.get_current_timezone()),
                        datetime.datetime(2016, 12, 20, 23, 59, 59, tzinfo=timezone.get_current_timezone()))

    r1c1 = add_challenge(r1, "Read a book that has been sitting on your shelf for over a year")
    r1c2 = add_challenge(r1, "Read a book that you haven't read the synopsis of/can't remember the synopsis of")
    r1c3 = add_challenge(r1, "Read a book from your favourite genre")
    r1c4 = add_challenge(r1, "Read a book that is over 300 pages")
    r1c5 = add_challenge(r1, "Reread your favourite book in a series")
    r1c6 = add_challenge(r1, "read a book that has been recommended to you more than once")

    r10c1 = add_challenge(r10, "Read a children's book")
    r10c2 = add_challenge(r10, "Read a hardback")
    r10c3 = add_challenge(r10, "Read 2 books in 24 hours")
    r10c4 = add_challenge(r10, "Read a graphic novel")
    r10c5 = add_challenge(r10, "Read a book written in verse")
    r10c6 = add_challenge(r10, "Read a novella")
    r10c7 = add_challenge(r10, "Read 5 books total")

    b1 = add_book("Glass Sword", "9780062310668", "https://d.gr-assets.com/books/1436460934l/23174274.jpg",
                  "Victoria Aveyard")
    b2 = add_book("Morning Star", "9780345539847", "https://d.gr-assets.com/books/1426928658l/18966806.jpg",
                  "Pierce Brown")
    b3 = add_book("Starflight", "9781484723241", "https://d.gr-assets.com/books/1454218105l/21793182.jpg",
                  "Melissa Landers")
    b4 = add_book("Salt to the Sea", "9780399160301", "https://d.gr-assets.com/books/1437084512l/25614492.jpg",
                  "Ruta Sepetys")
    b5 = add_book("A Gathering of Shadows", "9780765376473", "https://d.gr-assets.com/books/1429627728l/20764879.jpg",
                  "V.E. Schwab")
    b6 = add_book("Symptoms of Being Human", "9780062382863", "https://d.gr-assets.com/books/1434997054l/22692740.jpg",
                  "Jeff Garvin")

    add_accomplishment(reader1, r1c1, [b1,b6])
    add_accomplishment(reader2, r1c1, [b2])
    add_accomplishment(reader3, r1c1, [b3])
    add_accomplishment(reader4, r1c1, [b4])
    add_accomplishment(reader5, r1c1, [b5])
    add_accomplishment(reader6, r1c1, [b6])

    add_accomplishment(reader1, r1c3,[b1,b6])
    add_accomplishment(reader2, r1c3, [b5])
    add_accomplishment(reader3, r1c1, [b4])
    add_accomplishment(reader4, r1c1, [b2,b3])
    add_accomplishment(reader5, r1c1, [b2])
    add_accomplishment(reader6, r1c1, [b1])


def add_reader(username, img, is_superuser=False):
    r = Reader.objects.get_or_create(username=username, img=img, is_superuser=is_superuser)[0]
    r.set_password('1234')
    r.save()
    return r


def add_readathon(name, desc, stDate, edDate):
    r = Readathon.objects.get_or_create(name=name, description=desc, start_date=stDate, end_date=edDate)[0]
    r.save()
    return r


def add_challenge(readathon, name):
    c = Challenge.objects.get_or_create(readathon_id=readathon, name=name)[0]
    c.save()
    return c


def add_accomplishment(user, challenge, books):
    a = Accomplishment.objects.get_or_create(user=user, challenge=challenge)[0]
    a.save()
    for book in books:
        a.books.add(book)
    return a


def add_book(name, isbn, cover, author):
    b = Book.objects.get_or_create(book_name=name, isbn=isbn, cover=cover, author=author)[0]
    b.save()
    return b


def add_activity(user, msg):
    a = Activity.objects.get_or_create(user=user, message=msg)[0]
    a.save()
    return a


# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    populate()
