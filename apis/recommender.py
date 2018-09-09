from apis.models import *
from datetime import datetime, timedelta

class Recommender:
    
    def __init__(self):
        pass
    
    ## Get most view blog in the last 2 days to 30 days 
    ## size of return blog =  number_of_content (default = 7)
    def get_trending_blog(self,number_of_content = 7):
        time_zone_info = Blog.objects.order_by('-total_views')[0].created_on.tzinfo
        now = datetime.now(time_zone_info)
        date_end = now.isoformat()
        trending_list = []
        days = 2
        while (len(trending_list) < number_of_content):
            date_start = (now - timedelta(days=days)).isoformat()
            trending_list = Blog.objects.filter(created_on__range=[date_start, date_end]) \
                                        .order_by('-total_views')[:number_of_content]
            days += 1
            if days > 30:
                break
        return trending_list
    ## Get 4 related posts with the same writer
    def get_related_post(self,blog):
        related_post = []
        try:
            same_writer = list(Blog.objects.filter(provider=blog.provider).order_by('-created_on')[:3])
            for post in same_writer:
                if post.blog_id == blog.blog_id:
                    same_writer.remove(post)
            related_post += same_writer[:2]

            tags = blog.tags.all()
            tag_index = 0
            tags_count = len(tags)
            while (len(related_post) < 4):
                temp_index = tag_index // tags_count
                temp = Blog.objects.filter(tags=tags[tag_index % tags_count]).order_by('-created_on')[temp_index:temp_index+1]
                if (temp[0].blog_id != blog.blog_id):
                    related_post.append(temp[0])
                tag_index += 1
            print("\t" , len(related_post))
            print(related_post)
            return related_post
        except:
            return self.get_trending_blog(4)


    