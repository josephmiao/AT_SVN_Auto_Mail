一、使用方法

    1、将附件的三个文件放到SVN服务器端对应仓库的hooks文件夹下，其中【post-commit.tmpl】会覆盖源文件，但不要紧。
        （以Windows为例：F:\Repositories\local_svn\hooks）

    2、【post-commit.tmpl】文件不需要变动，保持原样即可；

    3、修改【post-commit.bat】文件，如下两行分别设置成对应实际目录：

            set HOOK_DIR=F:\Repositories\local_svn\hooks
            set PYTHON_BIN=C:\Python35\python.exe

    4、修改【mailer.py】文件，如下几个参数，分别设置成实际参数值：

            #####################################################
            svnlook_bin_path =r'C:\VisualSVN Server\bin\svnlook.exe'
            #####################################################
            mail_user = '***@qq.com'
            mail_password = '***'
            mail_sender = '***@qq.com'
            #####################################################
            mail_receiver = ['***@qq.com','***@qq.com','***@qq.com']
            #####################################################

二、注意事项

    1、操作系统不同，获取参数时的代码会有少许调整；

    2、邮箱代码源设定的是QQ邮箱，如果设置其他邮箱，请在【send_mail】方法中修改；

    3、记得抄送人要规划好，最好设置邮件组形式，这样有人员变动时就不需要改代码了。