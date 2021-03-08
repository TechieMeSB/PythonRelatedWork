import requests
from bs4 import BeautifulSoup
import csv
from fpdf import FPDF
import csv
import json

#webscraping to csv

def open_url():
                                                                    #Inspirational Quotes Scraping
    URL = 'http://www.values.com/inspirational-quotes'
    r = requests.get(URL)
    try:
        r.raise_for_status()                                        #Raises Exception when Bad download
    except Exception as exc:
        print('There was a problem: %s' % (exc))
    soup = BeautifulSoup(r.content, 'html5lib')

    quotes=[]  # a list to store quotes

    table = soup.find('div', attrs = {'id':'all_quotes'})

    for row in table.findAll('div',
                            attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
        quote = {}
        quote['theme'] = row.h5.text
        quote['url'] = row.a['href']
        quote['img'] = row.img['src']
        quotes.append(quote)

    filename = 'inspirational_quote.csv'
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f,['theme','url','img'])
        w.writeheader()
        for quote in quotes:
            w.writerow(quote)


#csv to json

#import csv
#import json
def csv_to_json():
    csvfile = open('inspirational_quote.csv', 'r')
    jsonfile = open('file.json', 'w')

    fieldnames = ('theme','url','img')
    reader = csv.DictReader( csvfile, fieldnames)
    for row in reader:
        json.dump(row, jsonfile)
        jsonfile.write('\n')


#json to pdf



def json_to_pdf():

#from fpdf import FPDF

    # save FPDF() class into
    # a variable pdf
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size = 5.3)

    # open the text file in read mode
    f = open("file.json", "r")

    # insert the texts in pdf
    for x in f:
        pdf.cell(0, 10, txt= x, ln = 2, align='A')
        #print(x)

    # save the pdf with name .pdf
    pdf.output("inspirational_quote.pdf")
if __name__=="__main__":
    open_url()
    csv_to_json()
    json_to_pdf()
