#!/usr/bin/env python3
"""RSS Aggregator - fetch last N days of updates from OPML feed list"""
import feedparser
import html
from datetime import datetime, timedelta
import sys
import os
import re
from concurrent.futures import ThreadPoolExecutor
import signal

# Parse args
days = 1
if len(sys.argv) > 1 and sys.argv[1] == '--days':
    days = int(sys.argv[2]) if len(sys.argv) > 2 else 1

opml_path = '/Users/wanglingwei/.openclaw/skills/rss-aggregator/references/feeds.opml'
import xml.etree.ElementTree as ET
tree = ET.parse(opml_path)
feeds = []
for outline in tree.iter('outline'):
    xml_url = outline.get('xmlUrl', '')
    title = outline.get('title', '') or outline.get('text', '')
    if xml_url:
        feeds.append({'title': title, 'url': xml_url})

cutoff = datetime.now() - timedelta(days=days)

def fetch_feed(feed):
    articles = []
    try:
        parsed = feedparser.parse(feed['url'])
        for entry in parsed.entries:
            try:
                updated = None
                if hasattr(entry, 'published_parsed') and entry.published_parsed:
                    updated = datetime(*entry.published_parsed[:6])
                elif hasattr(entry, 'updated_parsed') and entry.updated_parsed:
                    updated = datetime(*entry.updated_parsed[:6])
                if updated and updated >= cutoff:
                    summary = ''
                    if hasattr(entry, 'summary'):
                        summary = entry.summary
                    elif hasattr(entry, 'content'):
                        summary = entry.content[0].value if entry.content else ''
                    summary = re.sub(r'<[^>]+>', '', summary)
                    summary = html.unescape(summary).strip()
                    link = entry.get('link', '')
                    articles.append({
                        'title': html.unescape(entry.get('title', '')),
                        'author': entry.get('author', feed['title']),
                        'summary': summary[:800],
                        'updated': updated.strftime('%Y-%m-%d %H:%M'),
                        'link': link,
                        'source': feed['title']
                    })
            except Exception:
                continue
    except Exception:
        pass
    return articles

all_articles = []
with ThreadPoolExecutor(max_workers=8) as executor:
    futures = {executor.submit(fetch_feed, f): f for f in feeds}
    for future in futures.values():
        try:
            result = future.result(timeout=6)
            all_articles.extend(result)
        except Exception:
            pass

all_articles.sort(key=lambda x: x['updated'], reverse=True)

for a in all_articles:
    print(f"## {a['title']}")
    print(f"**来源**: {a['source']} | **时间**: {a['updated']} | **作者**: {a['author']}")
    print(f"**链接**: {a['link']}")
    print()
    if a['summary']:
        print(a['summary'][:600])
    print()
    print("---")
    print()