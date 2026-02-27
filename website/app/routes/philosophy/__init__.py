from flask import Blueprint

philosophy_bp = Blueprint('philosophy', __name__)

from . import (
    index,
    why_static,
    why_not_frameworks,
    why_i_build,
    manifesto,
)