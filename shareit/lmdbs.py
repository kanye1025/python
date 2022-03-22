import lmdb



_short_cover_env = None
def get_short_cover_lmdb():
	global _short_cover_env
	if not _short_cover_env:
		_short_cover_env  = lmdb.open("/data/short_cover.lmdb",map_size=3*1024*1024*1024*1024)
	return _short_cover_env


_short_frames_env = None
def get_short_frames_env_lmdb():
	global _short_frames_env
	if not _short_frames_env:
		_short_frames_env  = lmdb.open("/data/short_frames.lmdb",map_size=3*1024*1024*1024*1024)
	return _short_frames_env



_logo_bg_env = None
def get_logo_bg_env_lmdb():
	global _logo_bg_env
	if not _logo_bg_env:
		_logo_bg_env  = lmdb.open("/data/logo_bg.lmdb",map_size=3*1024*1024*1024*1024)
	return _logo_bg_env