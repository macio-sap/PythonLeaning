
- 下载git工具
- 启动工具 git-bash.exe
- 执行命令  ssh-keygen -t rsa -C "18248258@qq.com"

3.验证是否成功 
ssh -T git@github.com


set gitdir=D:\Program Files\PortableGit
set path=%gitdir%\cmd;%path%


cmd /k 'D:\\Program Files\\Python\\Python37\\python.exe' “$(FULL_CURRENT_PATH)” & ECHO. & PAUSE & EXIT

cmd /k cd "(CURRENT_DIRECTORY)" &  python "(FULL_CURRENT_PATH)" & ECHO. & PAUSE & EXIT