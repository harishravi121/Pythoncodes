import random
a='https://harishravi121.wixsite.com/hhwebpage/blog-1/categories/cube-chess'

b='https://harishravi121.wixsite.com/hhwebpage/festival-wishes'
c='https://harishravi121.wixsite.com/hhwebpage/product-page/name-magic-card'
c='https://extremeadventureinc.business.site/posts/8401265236096691147?hl=en'


d='https://www.facebook.com/harish.ravishankar/videos_by'

print('Hi all here are a few links to wix site #webpages')
links=[a,b,c,d]
words=links
sent=''
for i in range(random.randint(2,5)):

    sent=sent+' '+random.choice(words)+'  '

print(sent)

'''
Thinking a lot and using a lot of equations and making peaceful games and solving things are amazing. Sports is cool and the simulation in that is also cool. 
Best wishes :)

'''
