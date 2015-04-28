import csv
import re
import time
from urllib import request


def read_data():
    datafile = '/tmp/' + 'data_' + time.strftime("%Y-%m-%d") + ".tsv"
    pattern_url = re.compile(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    with open(datafile) as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
        for row in csvreader:
            if pattern_url.search(row[4]):
                print('\t'.join(pattern_url.findall(row[4])))


def get_urls(text):
    '''
    this function returns a list of all urls present in the given text
    '''
    return None


def get_url_details(url):
    '''
    this function returns details of an url
    url_subject: a subject for the url
    url_type: image, video
    '''
    try:
        fp = request.urlopen(url)
        print(fp.geturl())
    except URLError as error:
        print("Error occurred: {0}".format(error))
    except exception:
        raise exception
    return None


def main():
    # read_data()
    get_url_details('http://t.co/vYnYlsFU6U')


if __name__ == '__main__':
    main()
