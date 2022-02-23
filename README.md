# 自动填写 PAFD

⚠️⚠️：本项目填写地址的原理是自动延续上一次手动填写的；所以如果您中长期切换了居住地，如寒暑假/交流等，**请务必在地址稳定后手动填写一次**让之后的地址自动填写正确，**否则可能会被学校锁门禁权限**。

update: 如果你是 PAFD 的用户，对技术感兴趣，欢迎加入我们的 slack 组织，用 fudan.edu.cn 或者 m.fudan.edu.cn 的学号邮箱[点击这里注册加入 slack](https://join.slack.com/t/fducslg/signup) （可能需要科学上网工具）

[技术原理解读文章](https://github.com/FDUCSLG/fducslg/blob/master/content/blog/2020-11-23-PAFD-EXPLAINED.md)

update: 如果你收到了填报失败的通知，可以考虑更新一下你的 fork，在你原来 fork 的仓库页面，点击 fetch upstream 即可

![image](https://user-images.githubusercontent.com/29735669/139017607-a7888bfa-75d6-4949-b498-3a7982158a0b.png)


credit: 这份代码受 [daily_fudan](https://github.com/k652/daily_fudan) 启发，并参考了其实现方式，在此表示感谢。

首先请注册一个 GitHub 帐号，然后点击右上角的 fork 创建一个副本。

![fork](https://github.com/fducslg/pafd-automated/blob/master/docs/fork.png?raw=true)

然后在你 fork 的副本中，点击 Settings, Secrets 和 New secret

![create-secrets](https://github.com/fducslg/pafd-automated/blob/master/docs/create-secrets.png?raw=true)

然后创建两个值，Name 为 STD_ID 的在 Value 里填入学号

![id](https://github.com/fducslg/pafd-automated/blob/master/docs/id.png?raw=true)

![password](https://github.com/fducslg/pafd-automated/blob/master/docs/password.png?raw=true)

Name 为 PASSWORD 的在 Value 里填入 UIS 密码。这里可以不用担心安全性问题，这些 scecrets 的值只有你能看见，此外因为背后是 GitHub 为你保障安全——GitHub 的安全性应该比复旦的 UIS 要高。

通过 GitHub Action，每天十点会自动运行脚本帮你填写 PAFD，填写的地址是上一次的位置，从而你再也不用担心被辅导员催啦~
