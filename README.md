# Zotero PDF Collection Export

Python app to export a zotero database as pdfs arranged by collections

Currently just an idea, may never come to fruition as I am busy.

## The problem

It is very useful to have all of your PDFs arranged by collection and to be able
to browse those directly outside of Zotero. However, if you have one item in
multiple collections, you have to pick only one, which is annoying, and even
without that issue, you cannot use the standard Zotero sync if you do that and
it is very easy to end up with sync errors or path incompatibility.

## The solution (maybe)

A simple script to copy every pdf to a subdirectory tree that matches
collections and create links in all other subcollections the item is in. 

Plan is to try and keep this folder tree up to date, but not to sync changes
back to zotero, which would require fairly intelligent file comparison software
that I don't have the time to do well.
