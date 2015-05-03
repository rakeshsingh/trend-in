import csv
import re
import time
from urllib import request
from urllib.error import URLError
import utils


def analyze_data():
    urls = {}
    entries = []
    # datafile = '/tmp/' + 'data_' + time.strftime("%Y-%m-%d") + ".tsv"
    datafile = 'data.tsv'
    url_pattern = re.compile(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    with open(datafile) as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
        for row in csvreader:
            if url_pattern.search(row[4]):
                # print('\t'.join(pattern_url.findall(row[4])))
                for url in url_pattern.findall(row[4]):
                    if url in urls:
                        urls[url]['rank'] = urls[url]['rank'] + 1
                    else:
                        urls[url] = {}
                        urls[url]['rank'] = 1
                        urls[url]['details'] = get_url_details(url)
    # print all the urls
    conn = utils.get_connection()
    curr = conn.cursor()
    for url in urls:
        details = urls[url]['details']
        if details:
            entries.append((time.strftime("%Y-%m-%d"), details['base'], details[
                           'type'], details['title'], details['description'], urls[url]['rank']))
            print(details['base'] + "\t" + details['type'] + "\t" +
                  details['title'] + "\t" + details['description'])
    # bulk insert
    curr.executemany(
        "insert into entries(date, url, type, title, description, rank) values(?, ?,?,?,?,?)", entries)
    conn.commit()


def get_url_details(url):
    '''
    this function returns details of an url
    url
    url_subject: a subject for the url
    url_type: image, video, tweet
    url_description: Few texts from the url page
    url_category: just a place holder( in future, it can be news, sports, business and so on)
    '''
    url_detail = {}
    try:
        fp = request.urlopen(url)
        url_detail['base'] = fp.geturl()
        url_detail['type'] = 'html'
        url_detail['title'] = "__yet__to__find__"
        url_detail['description'] = "description__yet__to__find__"
        url_detail['category'] = 'news'
        print(fp.geturl())
    except URLError as error:
        print("Error occurred: {0}".format(error))
    except exception:
        raise exception
    return url_detail


def main():
    analyze_data()
    # get_url_details('http://t.co/vYnYlsFU6U')


if __name__ == '__main__':
    main()
