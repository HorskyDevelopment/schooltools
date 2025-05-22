from pytube import YouTube

def download(url: str):
    YouTube.streams.first(url ).download()