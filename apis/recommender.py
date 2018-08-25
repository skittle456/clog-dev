from apis.models import *
from datetime import datetime, timedelta

class Recommender:
    
    def __init__(self):
        pass
    
    ## Get most view blog in the last 2 days to 30 days 
    ## size of return blog =  number_of_content (default = 7)
    def getTrendingPost(self,number_of_content = 7):
        time_zone_info = Blog.objects.order_by('-total_views')[0].created_on.tzinfo
        now = datetime.now(time_zone_info)
        dateEnd = now.isoformat()
        trending_list = []
        days = 2
        while (len(trending_list) < number_of_content):
            dateStart = (now - timedelta(days=days)).isoformat()
            trending_list = Blog.objects.filter(created_on__range=[dateStart, dateEnd]) \
                                        .order_by('-total_views')[:number_of_content]
            days += 1
            if days > 30:
                break
        return trending_list

    