from flask import render_template
from . import home_bp
import random

music_playlists = [
    {
        "iframe": '<iframe width="420" height="236" src="https://www.youtube.com/embed/jcgDIUvLL6c" title="Di Gi Charat- Party Night" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
    },
    {
        "iframe": '<iframe width="420" height="236" src="https://www.youtube.com/embed/V_D2NSENY0g?si=QcELEtJg9Frvn-CX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
    },
    {
        "iframe": '<iframe width="420" height="236" src="https://www.youtube.com/embed/6RAehoXcOjI?si=d77dGB8MiuYnksK5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
    },
    {
        "iframe": '<iframe width="420" height="236" src="https://www.youtube.com/embed/tjlvmb8SGEs?si=eGcllafTKfx5kMif" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
    },
    {
        "iframe": '<iframe width="420" height="236" src="https://www.youtube.com/embed/UsXubuXq1lM?si=nREEgMWazXkGe52j" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
    },
    {
        "iframe": '<iframe width="420" height="236" src="https://www.youtube.com/embed/DwTinTO0o9I?si=3xVEGZZQ9jqoTXkI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
    },
    {
        "iframe": '<iframe width="420" height="236" src="https://www.youtube.com/embed/wbQEA_nxLaE?si=_iljl2KbGGs2NY3R" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
    },
    {
        "iframe": '<iframe width="420" height="236" src="https://www.youtube.com/embed/zTm666EKYRs?si=vyyBTpb23kw2Z637" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
    },
    {
        "iframe": '<iframe width="420" height="236" src="https://www.youtube.com/embed/Uoox9fpmDP0?si=75VuRgclHpBJOCAk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
    },
    {
        "iframe": '<iframe width="420" height="236" src="https://www.youtube.com/embed/hJBHMUGI7Nc?si=qnMIUev0L0ZhpYHN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
    },
    {
        "iframe": '<iframe width="420" height="236" src="https://www.youtube.com/embed/jmKRgqWGrWc?si=MkYBYf5-x1MtVmMn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
    },
    {
        "iframe": '<iframe width="420" height="236" src="https://www.youtube.com/embed/lCW6ueHZKe8?si=O2lSIDOxg_nrhO2P" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
    }
]

def _get_random_playlists():
    return random.sample(music_playlists, len(music_playlists))


underground_videos = [
    {
       "iframe": '<iframe width="560" height="315" src="https://www.youtube.com/embed/RQa-7Ql8vZM?si=Qznm0aIHptkJvNbd" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
    },
    {
        "iframe": '<iframe width="560" height="315" src="https://www.youtube.com/embed/2_jKiMUFUCk?si=58zseC861tYNcIES" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
    },
    {
        "iframe": '<iframe width="560" height="315" src="https://www.youtube.com/embed/5eSkvWswrL0?si=0ygUQkBBDwjxJb0S" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
    },
    {
        "iframe": '<iframe width="560" height="315" src="https://www.youtube.com/embed/OrOB9vLzksc?si=o5c09ECmDFqk8EtB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
    },
    {
        "iframe": '<iframe width="560" height="315" src="https://www.youtube.com/embed/EnJMohlO5BM?si=4lcjAqQup2N1gEfY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
    },
    {
        "iframe": '<iframe width="560" height="315" src="https://www.youtube.com/embed/6zF2_SALHHw?si=5vNKlPZg2VumzzC4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
    }
]

@home_bp.route('/extras')
def extras():
    return render_template('extras.html', playlists=_get_random_playlists(), underground_videos=underground_videos)

@home_bp.route('/es/extras')
def extras_es():
    return render_template('/es/extras.html', playlists=_get_random_playlists(), underground_videos=underground_videos)