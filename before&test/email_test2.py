import yagmail, datetime

sender = 'taltalmailing@gmail.com'
password = 'mlhwdtmjcvzmugof'
receiver = 'jjj1305@hanmail.net'
subject = '네이버매물-{}'.format(datetime.date.today())
body = '{} 네이버 매물 정리'.format(datetime.date.today())
filename1 = '구의빌라-{}.xlsx'.format(datetime.date.today())
filename2 = '구의원룸-{}.xlsx'.format(datetime.date.today())
filename3 = '자양빌라-{}.xlsx'.format(datetime.date.today())
filename4 = '자양원룸-{}.xlsx'.format(datetime.date.today())
filelist = [filename1, filename2, filename3, filename4]


yag = yagmail.SMTP(sender, password)
yag.send(
    to=receiver,
    subject=subject,
    contents=body, 
    attachments=filelist
)