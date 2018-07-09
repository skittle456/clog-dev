from django import template
from django.template.defaultfilters import stringfilter
import re
import html
register = template.Library()

@register.filter
@stringfilter
def upto(value, delimiter=None):
    return value.split(delimiter)[0]
upto.is_safe = True

def splitWithIndices(a, c=' '):
            matches = [(m.group(0), (m.start(), m.end()-1)) for m in re.finditer(r'\w+', a)]
            return matches

@register.filter
@stringfilter
def keep_blockquote(value):
    # string = value
    # lst = splitWithIndices(string)
    # #print(lst)
    # count = 0
    # pair = []
    # count_scp = 0
    # pair_scp = []
    # for i in lst:
    #     x = i[1][0]
    #     y = i[1][1]
    #     if 'blockquote' in string[x:y+1]:
    #         pair.append((x,y))
    #         count +=1
    #         if count % 2==0 and count!=0:
    #             x1,y1 = pair.pop(0)
    #             x2,y2 = pair.pop(0)
    #             x1-=4
    #             y2+=5
    #             str_lst = list(string)
    #             str_lst[x1:y2] = html.unescape(string[x1:y2])
    #             string = "".join(str_lst)
    value = html.unescape(value)
    return value
                    