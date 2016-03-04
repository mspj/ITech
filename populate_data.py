import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ITech.settings')

import django

django.setup()

import datetime
from django.utils import timezone
from bookwormsunite.models import *


def populate():
    b1 = add_book("Queen of Shadows (Throne of Glass #4)", "9781619636040",
                  "https://d.gr-assets.com/books/1441230104l/18006496.jpg",
                  "Sarah J. Maas")
    b2 = add_book("An Ember in the Ashes (An Ember in the Ashes #1)", "9781595148049",
                  "https://d.gr-assets.com/books/1449158871l/27774758.jpg",
                  "Sabaa Tahir")
    b3 = add_book("Red Queen (Red Queen #1)", "9780062310637", "https://d.gr-assets.com/books/1449778912l/22328546.jpg",
                  "Victoria Aveyard")
    b4 = add_book("The Wrath and the Dawn (The Wrath and the Dawn #1)", "9780399171611",
                  "https://d.gr-assets.com/books/1417956963l/18798983.jpg",
                  "Renee Ahdieh")
    b5 = add_book("All the Bright Places", "9780385755887", "https://d.gr-assets.com/books/1404331702l/18460392.jpg",
                  "Jennifer Niven")
    b6 = add_book("P.S. I Still Love You (To All the Boys I've Loved Before #2)", "9781442426733",
                  "https://d.gr-assets.com/books/1422881430l/20698530.jpg",
                  "Jenny Han")

    b7 = add_book("Miles from Ordinary", "9780312555122", "https://d.gr-assets.com/books/1317792370l/8814993.jpg",
                  "Carol Lynch Williams")
    b8 = add_book("Stolen Away", "9781408811320", "https://d.gr-assets.com/books/1316818473l/12006176.jpg",
                  "Alyxandra Harvey")
    b9 = add_book("Inexcusable", "9780689847899", "https://d.gr-assets.com/books/1348760865l/821146.jpg",
                  "Chris Lynch")
    b10 = add_book("Invisible", "9780689869037", "https://d.gr-assets.com/books/1344664320l/22399.jpg",
                   "Pete Hautman")
    b11 = add_book("Saree", "9781922052933", "https://d.gr-assets.com/books/1396932575l/21857952.jpg",
                   "Su Dharmapala")
    b12 = add_book("The Fishing Fleet: Husband Hunting in the Raj", "9780297868477",
                   "https://d.gr-assets.com/books/1343618302l/15747679.jpg",
                   "Anne de Courcy")

    b13 = add_book("Gone with the Wind", "9780446675536", "https://d.gr-assets.com/books/1328025229l/18405.jpg",
                   "Margaret Mitchell")
    b14 = add_book("The Count of Monte Cristo", "9780140449266", "https://d.gr-assets.com/books/1309203605l/7126.jpg",
                   "Alexandre Dumas, Robin Buss")
    b15 = add_book("A Game of Thrones (A Song of Ice and Fire #1)", "9780553588484",
                   "https://d.gr-assets.com/books/1436732693l/13496.jpg",
                   "George R.R. Martin")
    b16 = add_book("East of Eden", "9780142000656", "https://d.gr-assets.com/books/1441547516l/4406.jpg",
                   "John Steinbeck")
    b17 = add_book("Outlander (Outlander #1)", "9780440242949", "https://d.gr-assets.com/books/1402600310l/10964.jpg",
                   "Diana Gabaldon")
    b18 = add_book("The Wind-Up Bird Chronicle", "9780965341981", "https://d.gr-assets.com/books/1327872639l/11275.jpg",
                   "Haruki Murakami")

    b19 = add_book("A Really Awesome Mess", "9781606843642", "https://d.gr-assets.com/books/1376497534l/17288907.jpg",
                   "Brendan Halpin, Trish Cook")
    b20 = add_book("The Cavendish Home for Boys and Girls", "9781442442917",
                   "https://d.gr-assets.com/books/1336841328l/10893214.jpg",
                   "Claire Legrand, Sarah Watts")
    b21 = add_book("Free Men", "9780062407597", "https://d.gr-assets.com/books/1448216082l/25817488.jpg",
                   "Katy Simpson Smith")
    b22 = add_book("We've Already Gone This Far: Stories", "9781627794657",
                   "https://d.gr-assets.com/books/1440050594l/25666065.jpg",
                   "Patrick Dacey")
    b23 = add_book("Beneath the Bonfire: Stories", "9781250039835",
                   "https://d.gr-assets.com/books/1416846902l/23014607.jpg",
                   "Nickolas Butler")
    b24 = add_book("Sphinx", "9781941920091", "https://d.gr-assets.com/books/1424750560l/23129715.jpg",
                   "Anne Garreta, Emma Ramadan")
    b25 = add_book("Here", "9780241145968", "https://d.gr-assets.com/books/1395943544l/20587888.jpg", "Richard McGuire")
    b26 = add_book("The Danish Girl", "9781474601573", "https://d.gr-assets.com/books/1451790312l/27864391.jpg",
                   "David Ebershoff")

    b27 = add_book("Half of a Yellow Sun", "9781400044160", "https://d.gr-assets.com/books/1327934717l/18749.jpg",
                   "Chimamanda Ngozi Adichie")
    b28 = add_book("So Long a Letter", "9780435905552", "https://d.gr-assets.com/books/1394825021l/151374.jpg",
                   "Mariama Ba")
    b29 = add_book("The Beautyful Ones Are Not Yet Born", "9780435905408",
                   "https://d.gr-assets.com/books/1338642082l/264587.jpg", "Ayi Kwei Armah")
    b30 = add_book("The Famished Road (The Famished Road #1)", "9780385425131",
                   "https://d.gr-assets.com/books/1344396715l/101094.jpg",
                   "Ben Okri")
    b31 = add_book("Purple Hibiscus", "9780007189885", "https://d.gr-assets.com/books/1329431038l/126381.jpg",
                   "Chimamanda Ngozi Adichie")
    b32 = add_book("Mine Boy", "9780435905620", "https://d.gr-assets.com/books/1348375529l/712960.jpg",
                   "Peter Abrahams")

    b33 = add_book("The Kite Runner", "9781594480003", "https://d.gr-assets.com/books/1394898159l/77203.jpg",
                   "Khaled Hosseini")
    b34 = add_book("Norwegian Wood", "9780375704024)", "https://d.gr-assets.com/books/1386924361l/11297.jpg",
                   "Haruki Murakami")
    b35 = add_book("Kitchen", "9780802142443", "https://d.gr-assets.com/books/1327904393l/50144.jpg",
                   "Banana Yoshimoto")
    b36 = add_book("Sightseeing", "9780802142344", "https://d.gr-assets.com/books/1347713953l/212246.jpg",
                   "Rattawut Lapcharoensap")
    b37 = add_book("Life of Pi", "9780770430078", "https://d.gr-assets.com/books/1320562005l/4214.jpg",
                   "Yann Martel")

    b38 = add_book("It's Kind of a Funny Story", "9780786851973",
                   "https://d.gr-assets.com/books/1420629730l/248704.jpg", "Ned Vizzini")
    b39 = add_book("The Bell Jar", "9780061148514", "https://d.gr-assets.com/books/1379098702l/6514.jpg",
                   "Sylvia Plath")
    b40 = add_book("One Flew Over the Cuckoo's Nest", "9780451163967",
                   "https://d.gr-assets.com/books/1364084465l/332613.jpg", "Ken Kesey")
    b41 = add_book("Room", "9780316098328", "https://d.gr-assets.com/books/1344271307l/9691607.jpg", "Emma Donoghue")
    b42 = add_book("A Million Little Pieces", "9780307276902", "https://d.gr-assets.com/books/1401465768l/1241.jpg",
                   "James Frey")
    b43 = add_book("Requiem for a Dream", "9781560252481)", "https://d.gr-assets.com/books/1353949849l/46945.jpg",
                   "Hubert Selby Jr.")

    b44 = add_book("Giovanni's Room", "9780141186351", "https://d.gr-assets.com/books/1389658936l/38462.jpg",
                   "James Baldwin")
    b45 = add_book("At Swim, Two Boys", "9780743222952", "https://d.gr-assets.com/books/1439613291l/96200.jpg",
                   "Jamie O'Neill")
    b46 = add_book("Middlesex", "9780312422158", "https://d.gr-assets.com/books/1437029776l/2187.jpg",
                   "Jeffrey Eugenides")
    b47 = add_book("The Charioteer", "9780375714184", "https://d.gr-assets.com/books/1389484698l/67699.jpg",
                   "Mary Renault")
    b48 = add_book("Fried Green Tomatoes at the Whistle Stop Cafe", "9780375508417",
                   "https://d.gr-assets.com/books/1165961740l/9375.jpg", "Fannie Flagg")
    b49 = add_book("Annie on My Mind", "9780374404147", "https://d.gr-assets.com/books/1388360021l/595375.jpg",
                   "Nancy Garden")

    # -----------------------------------------------------------------------------------

    reader1 = add_reader("sashaalsberg", 'https://d.gr-assets.com/users/1444743640p6/10915830.jpg')
    reader2 = add_reader("tammy", 'https://d.gr-assets.com/users/1394292082p6/28395194.jpg')
    reader3 = add_reader("emily-may", 'https://d.gr-assets.com/users/1402215455p6/4622890.jpg')
    reader4 = add_reader("beckfoster", 'https://d.gr-assets.com/users/1383924009p6/5875398.jpg')
    reader5 = add_reader("maliemania", 'https://d.gr-assets.com/users/1415192892p6/1334245.jpg')
    reader6 = add_reader("pimjunha", 'https://d.gr-assets.com/users/1376729372p6/15480984.jpg', is_superuser=True)
    reader7 = add_reader("cmackie21", 'https://d.gr-assets.com/users/1376729372p6/15480984.jpg', is_superuser=True)
    reader8 = add_reader("mirela", "https://d.gr-assets.com/users/1446303911p6/27789079.jpg")
    reader9 = add_reader("trevor", "https://d.gr-assets.com/users/1408549382p6/9563899.jpg")
    reader10 = add_reader("wil-wheaton", "https://d.gr-assets.com/authors/1356706649p6/37075.jpg")
    reader11 = add_reader("ross", "https://d.gr-assets.com/users/1248841616p6/2570271.jpg")
    reader12 = add_reader("kobelka", "https://d.gr-assets.com/users/1451353645p6/35929276.jpg")
    reader13 = add_reader("freeman", "https://d.gr-assets.com/users/1390967548p6/28158368.jpg")
    reader14 = add_reader("sethmathern", "https://d.gr-assets.com/users/1447631611p6/49026710.jpg")
    reader15 = add_reader("kelly", "https://d.gr-assets.com/users/1342801966p6/8430852.jpg")
    reader16 = add_reader("jenna", "https://d.gr-assets.com/users/1425854502p6/7030875.jpg")
    reader17 = add_reader("lashaan", "https://d.gr-assets.com/users/1439883342p6/43439266.jpg")
    reader18 = add_reader("manna", "https://d.gr-assets.com/users/1426922465p6/19723258.jpg")
    reader19 = add_reader("phah", "https://d.gr-assets.com/users/1445248393p6/48061010.jpg")
    reader20 = add_reader("luan", "https://d.gr-assets.com/users/1361115028p6/17551516.jpg")

    # -----------------------------------------------------------------------------------

    r1 = add_readathon("Book Shimmy Awards Readathon",
                       "a readathon to celebrate all the winners of the 2014 BookShimmyAwards. "
                       "This readathon will take place January 1st-31st and you can read what ever books you want that were nominated. "
                       "They could be the winners, or the runner ups.",
                       datetime.datetime(2016, 1, 3, 0, 0, 0, tzinfo=timezone.get_current_timezone()),
                       datetime.datetime(2016, 1, 31, 23, 59, 59, tzinfo=timezone.get_current_timezone()),
                       [reader1, reader3, reader5, reader7, reader9, reader11, reader13, reader19])
    r1c1 = add_challenge(r1, "Read a book that was nominated in BookShimmyAwards2014")

    r2 = add_readathon("Winter Biannual Bibliothon 2016",
                       "The Biannual Bibliothon is a week-long read-a-thon hosted twice a year by "
                       "MissSassyKassie, emmmabooks, Little Red Reader, Kellys BookSpill, OHxXxSNAP13, "
                       "sierrareads, and Brittni's BookFind.",
                       datetime.datetime(2016, 1, 4, 0, 0, 0, tzinfo=timezone.get_current_timezone()),
                       datetime.datetime(2016, 1, 11, 23, 59, 59, tzinfo=timezone.get_current_timezone()),
                       [reader1, reader2, reader3, reader4, reader16, reader17, reader18, reader19])
    r2c1 = add_challenge(r2, "Read a book that's been sitting on your shelf for over a year.")
    r2c2 = add_challenge(r2, "Read a book over 300 pages.")
    r2c3 = add_challenge(r2, "Read a book from your favorite genre.")
    r2c4 = add_challenge(r2, "Reread your favorite book in a series.")
    r2c5 = add_challenge(r2, "Read a book based on it's cover.")
    r2c6 = add_challenge(r2, "Read a book that's been recommended to you more than once.")

    r3 = add_readathon("24 Hour Read-A-Thon",
                       "Hey fellow readers of the world. In January we will kick off our 2nd Annual Winter 24 Hour Read-A-Thon!!!! "
                       "Last year we only had a few people participate so I am hoping we can have at least twenty people participate this time around. "
                       "It would be great to have everyone participate but if you can't there is always next year. "
                       "Also feel free to invite other people to join our book club so they can participate in it as well! "
                       "It will start at midnight and it will end at midnight on the next day. "
                       "The goal is to read as many books as you can in 24 hours. "
                       "You may take breaks to rest your eyes, eat, drink, take a shower or go to the bathroom. "
                       "I hope you will grab some Hot Cocoa or Coffee and a blanket and cozy up on the couch with us for the Winter 24 Hour Read-A-Thon for 2015!!!!!",
                       datetime.datetime(2016, 1, 17, 0, 0, 0, tzinfo=timezone.get_current_timezone()),
                       datetime.datetime(2016, 1, 17, 23, 59, 59, tzinfo=timezone.get_current_timezone()),
                       [reader1, reader2, reader3, reader4, reader5, reader6, reader7, reader8, reader9, reader10,
                        reader11, reader12, reader13, reader14, reader15, reader16])
    r3c1 = add_challenge(r3, "Read as many as books as you can!")

    r4 = add_readathon("The Under-Hyped Readathon",
                       "Basically, there has been a lot of talk on Booktube, and the internet in general, "
                       "about the shifting community and the difference between hyping books and promoting literacy. "
                       "These are valid points but I'd rather do something positive about it."
                       "So this readathon is for anyone who wants to promote under-hyped books, "
                       "books you think are worth the buzz but just aren't getting the attention they deserve.",
                       datetime.datetime(2016, 2, 25, 0, 0, 0, tzinfo=timezone.get_current_timezone()),
                       datetime.datetime(2016, 3, 25, 23, 59, 59, tzinfo=timezone.get_current_timezone()),
                       [reader1, reader3, reader5, reader7, reader9, reader11, reader13, reader15, reader17, reader19])
    r4c1 = add_challenge(r4, "Read an underhyped book.")

    r5 = add_readathon("Continent Readathon",
                       "Let's read more books by authors from different continents.",
                       datetime.datetime(2016, 3, 1, 0, 0, 0, tzinfo=timezone.get_current_timezone()),
                       datetime.datetime(2016, 3, 31, 23, 59, 59, tzinfo=timezone.get_current_timezone()),
                       [reader1, reader2, reader4, reader6, reader8, reader10])
    r5c1 = add_challenge(r5, "Read a book written by African author.")
    r5c2 = add_challenge(r5, "Read a book written by Asian author.")
    r5c3 = add_challenge(r5, "Read a book written by North American author.")

    r6 = add_readathon("Bookentine Readathon",
                       "This is a readathon with the aim to read as many contemporaries as possible. "
                       "We have 5 challenges though you do not need to do all or any of them.",
                       datetime.datetime(2016, 2, 14, 0, 0, 0, tzinfo=timezone.get_current_timezone()),
                       datetime.datetime(2016, 2, 21, 23, 59, 59, tzinfo=timezone.get_current_timezone()),
                       [reader1, reader2, reader6, reader10, reader15, reader17, reader12])
    r6c1 = add_challenge(r6, "Read a book with a mental illness.")
    r6c2 = add_challenge(r6, "Read a book set in your home Country.")
    r6c3 = add_challenge(r6, "Read a book with a LGBT character.")
    r6c4 = add_challenge(r6, "Read a debut. (any year as long as it's an authors debut)")
    r6c5 = add_challenge(r6, "Book that's been on your tbr the longest.")

    r7 = add_readathon("Read-O-Rama Readathon",
                       "This readathon is hosted by the following Booktubers: Chloe (@brunettebiblio), "
                       "Elizabeth (@zizzybookbabble), Danne (@DanneLen),  Katie (@kitkatscanread), and Emily Jean (@emilyjeanlives).",
                       datetime.datetime(2016, 4, 8, 0, 0, 0, tzinfo=timezone.get_current_timezone()),
                       datetime.datetime(2016, 4, 14, 23, 59, 59, tzinfo=timezone.get_current_timezone()),
                       [])
    r7c1 = add_challenge(r7, "A book from your TBR jar or that someone else picks.")
    r7c2 = add_challenge(r7, "A book with green on the cover.")
    r7c3 = add_challenge(r7, "A diverse book.")
    r7c4 = add_challenge(r7, "A book with flowers on the cover.")

    r8 = add_readathon("SWinter",
                       "Remember that Phineas and Ferb episode where they built a ski hill in their backyard during the Summer and called it 'Swinter.'"
                       " Yeah, well, this read-a-thon was kind of inspired by that.",
                       datetime.datetime(2016, 4, 16, 0, 0, 0, tzinfo=timezone.get_current_timezone()),
                       datetime.datetime(2016, 4, 25, 23, 59, 59, tzinfo=timezone.get_current_timezone()),
                       [])
    r8c1 = add_challenge(r8, "Read a summertime book.")
    r8c2 = add_challenge(r8, "Read a wintertime book.")

    r9 = add_readathon("AYearAThon (Fantasy & Scifi)",
                       "In this readathon, we pick a genre of books a year. :)",
                       datetime.datetime(2016, 5, 6, 0, 0, 0, tzinfo=timezone.get_current_timezone()),
                       datetime.datetime(2016, 5, 12, 23, 59, 59, tzinfo=timezone.get_current_timezone()),
                       [])
    r9c1 = add_challenge(r9, "Read a high-fantasy book.")
    r9c2 = add_challenge(r9, "Read a scifi book.")

    r10 = add_readathon("The Spring Into Reading 48 Hour Readathon",
                        "Hey fellow readers! At the end of April we will be having a 48 hour read-a-thon. "
                        "The goal is to read as many books as you can in 48 hours. "
                        "It is impossible to be able to stay up for 48 hours straight, "
                        "so you can go to sleep in the middle of it.",
                        datetime.datetime(2016, 5, 17, 0, 0, 0, tzinfo=timezone.get_current_timezone()),
                        datetime.datetime(2016, 5, 19, 23, 59, 59, tzinfo=timezone.get_current_timezone()),
                        [])
    r10c1 = add_challenge(r10, "Read a graphic novel.")
    r10c2 = add_challenge(r10, "Read a chapter book that you missed out reading as a child.")
    r10c3 = add_challenge(r10, "Read a book about a real life event.")
    r10c4 = add_challenge(r10, "Read a book that will help spring you into summer.")
    r10c5 = add_challenge(r10, "Read a book recommended by a friend.")
    r10c6 = add_challenge(r10, "Read a book with one of the elements of nature on the cover.")

    r11 = add_readathon("BookTubeAthon",
                        "BookTubeAThon is a week-long reading challenge where participants are encouraged to read as much as they can. "
                        "In addition to reading at a ferocious pace and engaging the community on YouTube and Twitter, "
                        "there are seven specific book challenges each year.",
                        datetime.datetime(2016, 6, 3, 0, 0, 0, tzinfo=timezone.get_current_timezone()),
                        datetime.datetime(2016, 6, 9, 23, 59, 59, tzinfo=timezone.get_current_timezone()),
                        [])
    r11c1 = add_challenge(r11, "Read a book with blue on the cover.")
    r11c2 = add_challenge(r11, "Read a book by an author who shares the same first letter of your last name")
    r11c3 = add_challenge(r11, "Read someone else's favorite book.")
    r11c4 = add_challenge(r11, "Read the last book you acquired.")
    r11c5 = add_challenge(r11, "Finish a book without letting go of it.")

    r12 = add_readathon("Ramazanathon",
                        "Ramazan/Ramadan-a-Thon (n): A Turkish/English read-a-thon that takes place during (the month of) Ramadan.",
                        datetime.datetime(2016, 7, 18, 0, 0, 0, tzinfo=timezone.get_current_timezone()),
                        datetime.datetime(2016, 8, 16, 23, 59, 59, tzinfo=timezone.get_current_timezone()),
                        [])

    # --------------------------------------

    add_activity('heart', reader1, 'joined Bookwormsunite!')
    add_activity('heart', reader2, 'joined Bookwormsunite!')
    add_activity('heart', reader3, 'joined Bookwormsunite!')
    add_activity('heart', reader4, 'joined Bookwormsunite!')
    add_activity('heart', reader5, 'joined Bookwormsunite!')
    add_activity('heart', reader6, 'joined Bookwormsunite!')
    add_activity('heart', reader7, 'joined Bookwormsunite!')
    add_activity('heart', reader8, 'joined Bookwormsunite!')
    add_activity('heart', reader9, 'joined Bookwormsunite!')
    add_activity('heart', reader10, 'joined Bookwormsunite!')
    add_activity('heart', reader11, 'joined Bookwormsunite!')
    add_activity('heart', reader12, 'joined Bookwormsunite!')
    add_activity('heart', reader13, 'joined Bookwormsunite!')
    add_activity('heart', reader14, 'joined Bookwormsunite!')
    add_activity('heart', reader15, 'joined Bookwormsunite!')
    add_activity('heart', reader16, 'joined Bookwormsunite!')
    add_activity('heart', reader17, 'joined Bookwormsunite!')
    add_activity('heart', reader18, 'joined Bookwormsunite!')
    add_activity('heart', reader19, 'joined Bookwormsunite!')
    add_activity('heart', reader20, 'joined Bookwormsunite!')

    add_activity('asterisk', reader1, 'joined ' + r1.name)
    add_activity('asterisk', reader3, 'joined ' + r1.name)
    add_activity('asterisk', reader5, 'joined ' + r1.name)
    add_activity('asterisk', reader7, 'joined ' + r1.name)
    add_activity('asterisk', reader9, 'joined ' + r1.name)
    add_activity('asterisk', reader11, 'joined ' + r1.name)
    add_activity('asterisk', reader13, 'joined ' + r1.name)
    add_activity('asterisk', reader15, 'joined ' + r1.name)

    add_accomplishment(reader1, r1c1, [b1])
    add_activity('book', reader1,
                 "completed challenge '" + r1c1.name + "' in " + r1.name + " by reading '" + b1.book_name + "'")
    add_accomplishment(reader3, r1c1, [b2])
    add_activity('book', reader3,
                 "completed challenge '" + r1c1.name + "' in " + r1.name + " by reading '" + b2.book_name + "'")
    add_accomplishment(reader5, r2c1, [b1])
    add_activity('book', reader5,
                 "completed challenge '" + r1c1.name + "' in " + r1.name + " by reading '" + b1.book_name + "'")
    add_accomplishment(reader7, r1c1, [b2])
    add_activity('book', reader7,
                 "completed challenge '" + r1c1.name + "' in " + r1.name + " by reading '" + b2.book_name + "'")
    add_accomplishment(reader9, r1c1, [b3])
    add_activity('book', reader9,
                 "completed challenge '" + r1c1.name + "' in " + r1.name + " by reading '" + b3.book_name + "'")
    add_accomplishment(reader11, r1c1, [b4])
    add_activity('book', reader11,
                 "completed challenge '" + r1c1.name + "' in " + r1.name + " by reading '" + b4.book_name + "'")
    add_accomplishment(reader13, r1c1, [b5])
    add_activity('book', reader13,
                 "completed challenge '" + r1c1.name + "' in " + r1.name + " by reading '" + b5.book_name + "'")
    add_accomplishment(reader15, r1c1, [b6])
    add_activity('book', reader15,
                 "completed challenge '" + r1c1.name + "' in " + r1.name + " by reading '" + b6.book_name + "'")

    add_activity('asterisk', reader1, 'joined ' + r2.name)
    add_activity('asterisk', reader2, 'joined ' + r2.name)
    add_activity('asterisk', reader3, 'joined ' + r2.name)
    add_activity('asterisk', reader4, 'joined ' + r2.name)
    add_activity('asterisk', reader16, 'joined ' + r2.name)
    add_activity('asterisk', reader17, 'joined ' + r2.name)
    add_activity('asterisk', reader18, 'joined ' + r2.name)
    add_activity('asterisk', reader19, 'joined ' + r2.name)

    add_accomplishment(reader1, r2c1, [b7])
    add_activity('book', reader1,
                 "completed challenge '" + r2c1.name + "' in " + r2.name + " by reading '" + b7.book_name + "'")
    add_accomplishment(reader1, r2c2, [b13])
    add_activity('book', reader1,
                 "completed challenge '" + r2c2.name + "' in " + r2.name + " by reading '" + b13.book_name + "'")
    add_accomplishment(reader2, r2c1, [b8])
    add_activity('book', reader2,
                 "completed challenge '" + r2c1.name + "' in " + r2.name + " by reading '" + b8.book_name + "'")
    add_accomplishment(reader2, r2c2, [b15])
    add_activity('book', reader2,
                 "completed challenge '" + r2c2.name + "' in " + r2.name + " by reading '" + b15.book_name + "'")
    add_accomplishment(reader3, r2c1, [b9])
    add_activity('book', reader3,
                 "completed challenge '" + r2c1.name + "' in " + r2.name + " by reading '" + b9.book_name + "'")
    add_accomplishment(reader3, r2c2, [b2])
    add_activity('book', reader3,
                 "completed challenge '" + r2c2.name + "' in " + r2.name + " by reading '" + b2.book_name + "'")
    add_accomplishment(reader4, r2c1, [b10])
    add_activity('book', reader4,
                 "completed challenge '" + r2c1.name + "' in " + r2.name + " by reading '" + b10.book_name + "'")
    add_accomplishment(reader4, r2c2, [b16])
    add_activity('book', reader4,
                 "completed challenge '" + r2c2.name + "' in " + r2.name + " by reading '" + b16.book_name + "'")
    add_accomplishment(reader16, r2c1, [b11])
    add_activity('book', reader16,
                 "completed challenge '" + r2c1.name + "' in " + r2.name + " by reading '" + b11.book_name + "'")
    add_accomplishment(reader16, r2c2, [b17])
    add_activity('book', reader16,
                 "completed challenge '" + r2c2.name + "' in " + r2.name + " by reading '" + b17.book_name + "'")
    add_accomplishment(reader17, r2c1, [b12])
    add_activity('book', reader17,
                 "completed challenge '" + r2c1.name + "' in " + r2.name + " by reading '" + b12.book_name + "'")
    add_accomplishment(reader17, r2c2, [b18])
    add_activity('book', reader17,
                 "completed challenge '" + r2c2.name + "' in " + r2.name + " by reading '" + b18.book_name + "'")
    add_accomplishment(reader18, r2c1, [b7])
    add_activity('book', reader18,
                 "completed challenge '" + r2c1.name + "' in " + r2.name + " by reading '" + b7.book_name + "'")
    add_accomplishment(reader18, r2c2, [b13])
    add_activity('book', reader18,
                 "completed challenge '" + r2c2.name + "' in " + r2.name + " by reading '" + b13.book_name + "'")
    add_accomplishment(reader19, r2c1, [b7])
    add_activity('book', reader19,
                 "completed challenge '" + r2c1.name + "' in " + r2.name + " by reading '" + b7.book_name + "'")
    add_accomplishment(reader19, r2c2, [b13])
    add_activity('book', reader19,
                 " completed challenge '" + r2c1.name + "' in " + r2.name + " by reading '" + b13.book_name + "'")

    add_accomplishment(reader1, r3c1, [b2])
    add_accomplishment(reader2, r3c1, [b2])
    add_accomplishment(reader3, r3c1, [b2])
    add_accomplishment(reader4, r3c1, [b2])
    add_accomplishment(reader5, r3c1, [b15])
    add_accomplishment(reader6, r3c1, [b15])
    add_accomplishment(reader7, r3c1, [b15])
    add_accomplishment(reader8, r3c1, [b18])
    add_accomplishment(reader9, r3c1, [b18])
    add_accomplishment(reader10, r3c1, [b13])
    add_accomplishment(reader11, r3c1, [b1])
    add_accomplishment(reader12, r3c1, [b12])
    add_accomplishment(reader13, r3c1, [b14])
    add_accomplishment(reader14, r3c1, [b1])
    add_accomplishment(reader15, r3c1, [b12])
    add_accomplishment(reader16, r3c1, [b14])

    add_accomplishment(reader1, r4c1, [b19])
    add_accomplishment(reader3, r4c1, [b19])
    add_accomplishment(reader5, r4c1, [b20])
    add_accomplishment(reader7, r4c1, [b21])
    add_accomplishment(reader9, r4c1, [b21])
    add_accomplishment(reader11, r4c1, [b22])
    add_accomplishment(reader13, r4c1, [b23])
    add_accomplishment(reader15, r4c1, [b24])
    add_accomplishment(reader17, r4c1, [b25])
    add_accomplishment(reader19, r4c1, [b26])

    add_accomplishment(reader1, r5c1, [b27])
    add_accomplishment(reader1, r5c2, [b33])
    add_accomplishment(reader2, r5c1, [b28])
    add_accomplishment(reader2, r5c2, [b33])
    add_accomplishment(reader4, r5c1, [b29])
    add_accomplishment(reader4, r5c2, [b34])
    add_accomplishment(reader6, r5c1, [b30])
    add_accomplishment(reader6, r5c2, [b35])
    add_accomplishment(reader8, r5c1, [b31])
    add_accomplishment(reader8, r5c2, [b36])
    add_accomplishment(reader10, r5c1, [b32])
    add_accomplishment(reader10, r5c2, [b37])

    add_accomplishment(reader1, r6c1, [b38])
    add_accomplishment(reader1, r6c3, [b44])
    add_accomplishment(reader2, r6c1, [b38])
    add_accomplishment(reader2, r6c3, [b45])
    add_accomplishment(reader6, r6c1, [b39])
    add_accomplishment(reader6, r6c3, [b46])
    add_accomplishment(reader10, r6c1, [b40])
    add_accomplishment(reader10, r6c3, [b47])
    add_accomplishment(reader15, r6c1, [b41])
    add_accomplishment(reader15, r6c3, [b48])
    add_accomplishment(reader17, r6c1, [b42])
    add_accomplishment(reader17, r6c3, [b49])
    add_accomplishment(reader12, r6c1, [b43])
    add_accomplishment(reader12, r6c3, [b44])


def add_reader(username, img, is_superuser=False):
    r = Reader.objects.get_or_create(username=username, img=img, is_superuser=is_superuser)[0]
    r.set_password('1234')
    r.save()
    return r


def add_readathon(name, desc, stDate, edDate, users):
    r = Readathon.objects.get_or_create(name=name, description=desc, start_date=stDate, end_date=edDate)[0]
    r.save()
    for user in users:
        r.readers.add(user)
    r.save()
    return r


def add_challenge(readathon, name):
    c = Challenge.objects.get_or_create(readathon=readathon, name=name)[0]
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


def add_activity(icon, user, msg):
    a = Activity.objects.get_or_create(icon=icon, user=user, message=msg)[0]
    a.save()
    return a


# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    populate()
