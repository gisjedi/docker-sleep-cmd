FROM python:2-alpine

COPY sleep-cmd.py /

ENTRYPOINT ["/sleep-cmd.py"]
# First parameter is seconds to sleep between runs
CMD ["5", "echo", "Running..."]
