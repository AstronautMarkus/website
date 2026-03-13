from flask import render_template
from . import home_bp
import random
import os

from app.models.models import ExtraYoutubeSong, ExtraYoutubeVideo

_ascii_art_dir = os.path.join(os.path.dirname(__file__), 'ascii_art')

_ascii_art_files = [
    (f, open(os.path.join(_ascii_art_dir, f), encoding='utf-8').read())
    for f in sorted(os.listdir(_ascii_art_dir))
    if f.endswith('.txt')
]

def _shuffled_ascii_art():
    arts = list(_ascii_art_files)
    random.shuffle(arts)
    return arts

@home_bp.route('/extras')
def extras():
    youtube_songs = ExtraYoutubeSong.query.all()
    youtube_videos = ExtraYoutubeVideo.query.all()

    return render_template(
        '/home/extras.html',
        youtube_songs=youtube_songs,
        youtube_videos=youtube_videos,
        ascii_arts=_shuffled_ascii_art(),
    )

@home_bp.route('/es/extras')
def extras_es():

    youtube_songs = ExtraYoutubeSong.query.all()
    youtube_videos = ExtraYoutubeVideo.query.all()

    return render_template(
        '/home/es/extras.html',

        youtube_songs=youtube_songs,
        youtube_videos=youtube_videos,
        ascii_arts=_shuffled_ascii_art(),
    )