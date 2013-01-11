#! /usr/bin/env python
'''
Python command line YouTube ViewCount script

Usage:
	python youtube_count.py
'''


import gdata.youtube.service

target_video = '87SnJ7-9jT0'
yt_service = gdata.youtube.service.YouTubeService()
yt_service.ssl = True
yt_service.developer_key = 'AI39si6rrh_W0KC3Pl9RPEij-S11vBt-GRFBCBRN25kZ_DHCTNlZnHhWAn4_CUT3JA1RYyHhWB31IXBwzkqYgBd0tYahhYqs1g'
yt_service.client_id = 'botviewers'

entry = yt_service.GetYouTubeVideoEntry(video_id=target_video)
print 'View Count: %s' % entry.statistics.view_count

