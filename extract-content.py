#!/usr/bin/env python3

import os
import sys
import subprocess
from bs4 import BeautifulSoup
from progress.bar import Bar

pages = []

# Create a list of all pages to convert
for path, subdirs, files in os.walk("wiki"):
	for name in files:
		if not "?" in name and not ".." in name and ".html" in name:
			pages.append(os.path.join(path, name))

# Also convert the toplevel index.html
pages.append("index.html")

# Progress bar
numPages = len(pages)
bar = Bar('Converting pages', max=numPages)

# Actual extraction
for count, page in enumerate(pages):
	pageFile = open(page, "r")
	pageSoup = BeautifulSoup(pageFile, 'html.parser')
	pageFile.close()

	content = pageSoup.find(id="content")
	#print(content)

	contentPage = open(page + ".content", "w")
	if not type(content) is None:
		contentPage.write(str(content))

	contentPage.close()

	subprocess.call(["pandoc", "-f", "html", "-t", "markdown-header_attributes-link_attributes-native_divs-native_spans", page + ".content", "-o", page.replace(".html", ".md")])

	os.remove(page + ".content")
	bar.next()

bar.finish()
