#!/usr/bin/env python
import xml
from bs4 import BeautifulSoup
from xml.etree import ElementTree

def main():
    print('Processing XML...')

    source_filename = 'data/cf79.xml'
    authors_filename = 'output/autores.xml'
    title_filename = 'output/titulo.xml'

    # read authors with beatifulsoup
    with open(source_filename, 'r') as source_file:
        content = BeautifulSoup(source_file.read(), 'lxml')

    # transform list of authors to a set
    set_authors = {i.string for i in content.find_all('author')}

    # write authors to output file
    with open(authors_filename, 'w') as output_authors:
        output_authors.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        output_authors.write('<authors>\n')
        for author in set_authors:
            output_authors.write(f'<author>{author}</author>\n')
        output_authors.write('</authors>\n')
    
    # read titles with etree
    content = ElementTree.parse(source_filename)
    set_titles = {i.text for i in content.findall('RECORD/TITLE')}

    # write authors to output file
    with open(title_filename, 'w') as output_titles:
        output_titles.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        output_titles.write('<titles>\n')
        for title in set_titles:
            output_titles.write(f'<title>{title}</title>\n')
        output_titles.write('</titles>\n')

    print(f'The processed files are in {authors_filename} and {title_filename}.')

if __name__ == '__main__':
    main()
