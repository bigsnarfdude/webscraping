import gdata.youtube.service
data = !cat cov_youtube_stats | grep 'href="/watch?v='
my_list=[]
for line in data:
    first = line.split()[1]
    second = first.split('=')[-1]
    third = second.split('"')[0]
    my_list.append(third)
    
for item in my_list:
    target_video = item
    yt_service = gdata.youtube.service.YouTubeService()
    yt_service.ssl = True
    yt_service.developer_key = 'AI39si6rrh_W0KC3Pl9RPEij-S11vBt-GRFBCBRN25kZ_DHCTNlZnHhWAn4_CUT3JA1RYyHhWB31IXBwzkqYgBd0tYahhYqs1g'
    yt_service.client_id = 'botviewers'

    entry = yt_service.GetYouTubeVideoEntry(video_id=target_video)
    print 'Video title: %s' % entry.media.title.text
    print 'View Count: %s' % entry.statistics.view_count
    print
