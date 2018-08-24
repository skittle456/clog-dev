from apis.models import *
import datetime

class Recommender:
    
    def __init__(self):
        pass
    
    ## Get most view blog in the last 7 days
    ## size of return blog =  number_of_content (default = 7)
    ## TODO: Check if this actually work
    def getTrendingInTheLast7days(self,number_of_content = 7):
        now = datetime.datetime.now()
        blog_list = Blog.objects.order_by('-total_views')
        if len(blog_list) == 0:
            return []
        tz_info = blog_list[0].created_on.tzinfo
        now = datetime.datetime.now(tz_info)
        trending_list = []
        count = 0
        for blog in blog_list:
            if len(trending_list) == number_of_content:
                break
                
            time_difference = now - blog.created_on
            if abs(time_difference.days) < 7:
                trending_list.append(blog)

        return trending_list

    