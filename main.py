#!/usr/bin/env python
import argparse
import os
from pyzotero import zotero
from collections import defaultdict

def get_longest_deepest_collection(collections, collections_dict):
    def get_collection_path(collection_key):
        path = []
        while collection_key in collections_dict:
            path.append(collections_dict[collection_key]['data']['name'])
            collection_key = collections_dict[collection_key]['data'].get('parentCollection')
        return path[::-1]

    collection_paths = [get_collection_path(c) for c in collections]
    longest_deepest_collection = max(collection_paths, key=lambda x: (len(x), len(''.join(x))))
    return os.path.join(*longest_deepest_collection)

def export_pdfs(zot, library_id, library_type, output_dir):
    collections_dict = {c['data']['key']: c for c in zot.collections()}
    items = zot.everything(zot.items())

    for item in items:
        if 'pdf' not in item['data']['title'].lower():
            continue

        collections = item['data'].get('collections', [])
        if not collections:
            continue

        target_dir = get_longest_deepest_collection(collections, collections_dict)
        target_dir = os.path.join(output_dir, target_dir)

        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        attachments = zot.children(item['key'], itemType='attachment')
        for attachment in attachments:
            if 'application/pdf' in attachment['data']['contentType']:
                pdf_url = attachment['data']['url']
                pdf_filename = os.path.join(target_dir, attachment['data']['filename'])

                with open(pdf_filename, 'wb') as pdf_file:
                    pdf_file.write(zot.file(pdf_url).content)

def main():
    parser = argparse.ArgumentParser(description='Export PDFs from Zotero organized by collections.')
    parser.add_argument('library_id', type=str, help='Your Zotero library ID')
    parser.add_argument('library_type', type=str, choices=['user', 'group'], help='Your Zotero library type')
    parser.add_argument('api_key', type=str, help='Your Zotero API key')
    parser.add_argument('output_dir', type=str, help='The directory where PDFs will be exported')

    args = parser.parse_args()

    zot = zotero.Zotero(args.library_id, args.library_type, args.api_key)
    export_pdfs(zot, args.library_id, args.library_type, args.output_dir)

if __name__ == '__main__':
    main()
