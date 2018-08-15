from apis.models import *
import datetime

class Recommender:
    
    def __init__():
        pass
    
    ## Get most view blog in the last 7 days
    ## size of return blog =  number_of_content (default = 7)
    ## TODO: Check if this actually work
    def getTrendingFromLast7Days(number_of_content = 7):
        now = datetime.datetime.now()
        blog_list = Blog.objects.order_by('-total_views')
        trending_list = []
        for blog in blog_list:
            if len(trending_list) == number_of_content:
                break
            time_difference = now - blog.created_on
            if abs(time_difference.day) < 7:
                trending_list.append(blog)
        return trending_list

    