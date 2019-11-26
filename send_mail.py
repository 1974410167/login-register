import os
from django.core.mail import send_mail,EmailMultiAlternatives
os.environ['DJANGO_SETTINGS_MODULE']='mysite.settings'


if __name__=="__main__":

    subject,from_email,to='我是H。Y','ghao.yuan@qq.com','1909874106@qq.com'
    text_content='欢迎访问https://www.alididi.club,这是G。Y的博客'
    html_content='<p>欢迎访问<a href="https://www.alididi.club" target=blank>www.alididi.club</a>,这里是G。Y的博客</p>'
    msg=EmailMultiAlternatives(subject,text_content,from_email,[to])
    msg.attach_alternative(html_content,"text/html")
    msg.send()



'''
if __name__=="__main__":

    send_mail(
        '来自H。Y的测试邮件',
        '欢迎来到LOL',
        'ghao.yuan@qq.com',
        ['1909874106@qq.com']
    )
'''
