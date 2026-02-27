from datetime import datetime, timedelta

from flask import current_app, request

from app import db
from app.models.models import Visit


def _is_valid_request_for_visit_register() -> bool:
	if request.method != 'GET':
		return False

	if request.endpoint and request.endpoint == 'static':
		return False

	return True


def register_visit_middleware() -> None:
	if not _is_valid_request_for_visit_register():
		return

	ip_address = request.remote_addr
	if not ip_address:
		return

	user_agent = request.headers.get('User-Agent')

	last_visit = (
		Visit.query
		.filter_by(ip_address=ip_address)
		.order_by(Visit.visited_at.desc())
		.first()
	)

	if last_visit and last_visit.visited_at:
		elapsed = current_app.config.get('VISIT_REGISTER_INTERVAL_HOURS', 24)
		cutoff = datetime.utcnow() - timedelta(hours=elapsed)
		if last_visit.visited_at > cutoff:
			return

	try:
		visit = Visit(ip_address=ip_address, user_agent=user_agent)
		db.session.add(visit)
		db.session.commit()
	except Exception:
		db.session.rollback()


def init_visit_middleware(app) -> None:
	app.before_request(register_visit_middleware)
