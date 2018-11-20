import sys
import os
import smtplib
from email.mime.text import MIMEText
#####################################################
svnlook_bin_path =r'C:\VisualSVN Server\bin\svnlook.exe'
#####################################################
mail_user = '***@qq.com'
mail_password = '***'
mail_sender = '***@qq.com'
#####################################################
mail_receiver = ['***@qq.com','***@qq.com','***@qq.com']
#####################################################
# content = html_template % (repo_name, rev, author, date, log, file_list)
html_template = """
<html>
        <h2 style="color:#FFFFFF; background: #4682B4;">基本信息</h2>
            <div> <b>版本库：</b>%s
            </div>
            <div> <b>版本号：</b>%s
            </div>
            <div> <b>提交者：</b>%s
            </div>
            <div> <b>提交时间：</b>%s
            </div>
        <h2 style="color:#FFFFFF; background: #4682B4;">提交说明</h2>
            <xmp>%s</xmp>
        <h2 style="color:#FFFFFF; background: #4682B4;">文件清单</h2>
            <xmp>%s</xmp>
        <hr>
        <center>
                ☆ Powered by QMC ☆
        </center>
</html>
"""
#####################################################


def get_author(repo, rev):
    global svnlook_bin_path
    cmd = '"%s" author -r %s %s' % (svnlook_bin_path, rev, repo)
    output = os.popen(cmd).read()
    return output


def get_date(repo, rev):
    global svnlook_bin_path
    cmd = '"%s" date -r %s %s' % (svnlook_bin_path, rev, repo)
    output = os.popen(cmd).read()
    return output


def get_log(repo, rev):
    global svnlook_bin_path
    cmd = '"%s" log -r %s %s' % (svnlook_bin_path, rev, repo)
    output = os.popen(cmd).read()
    return output


def get_file_list(repo, rev):
    global svnlook_bin_path
    cmd = '"%s" changed -r %s %s' % (svnlook_bin_path, rev, repo)
    output = os.popen(cmd).read()
    return output


def write_mail(sender, receiver, sub, cnt):
    msg = MIMEText(cnt, _subtype='html', _charset='gb2312')
    msg['From'] = sender
    msg['To'] = ';'.join(receiver)
    msg['Subject'] = sub
    return msg


def write_mail_content(repo, rev):
    repo_name = os.path.basename(repo)
    author = get_author(repo, rev)
    date = get_date(repo, rev)
    log = get_log(repo, rev)
    file_list = get_file_list(repo, rev)
    content = html_template % (repo_name, rev, author, date, log, file_list)
    return content


def send_mail(msg, sender, to_list):
    try:
        s = smtplib.SMTP_SSL('smtp.qq.com', 465)
        s.login(mail_user, mail_password)
        s.sendmail(sender, to_list, msg.as_string())
        s.close()
        return True
    except Exception as e:
        print(str(e))
        return False

if __name__ == '__main__':
    mail_subject = 'SVN变更通知'
    mail_content = write_mail_content(sys.argv[1], sys.argv[2])
    msg = write_mail(mail_sender, mail_receiver, mail_subject, mail_content)
    send_mail(msg, mail_sender, mail_receiver)
