FROM python:2-alpine

RUN apk update && apk add libtorrent && pip install feedparser

COPY sleep-cmd.py /
COPY rss-torrent.py /

ENTRYPOINT ["/sleep-cmd.py"]
# First parameter is seconds to sleep between runs
CMD ["5", "echo", "Running..."]
