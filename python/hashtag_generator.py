string = '', 'Hello World', ' Hello world ', 'h w '


def generate_hashtag(s):
    if len(s) >= 140 or not s: return False
    res = "#{}".format(s.title())
    return ''.join(res.split())

res = generate_hashtag()
print(res)