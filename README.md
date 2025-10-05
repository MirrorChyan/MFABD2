<!-- markdownlint-disable MD033 MD041 -->
<div align="center">
  <img alt="LOGO" src="https://github.com/sunyink/MFABD2/blob/Fast/ReadMe/logo.png" width="180" height="180" />


# MaaBD2-棕色尘埃2自动化助手
[![License](https://img.shields.io/badge/License-MIT%2FApache--2.0-blue)](./LICENSE)
[![.NET Version](https://img.shields.io/badge/.NET-≥%208-512BD4?logo=csharp)](https://dotnet.microsoft.com/download/dotnet/8.0)
[![月提交](https://img.shields.io/github/commit-activity/m/sunyink/MFABD2?label=开发活跃度&color=blue)](https://github.com/sunyink/MFABD2/commits/main)
[![给项目点赞](https://img.shields.io/github/stars/sunyink/MFABD2?style=social&label=给项目点赞)](https://github.com/sunyink/MFABD2)
<br>
[![构建状态](https://img.shields.io/badge/构建状态-通过-success?logo=githubactions)](https://github.com/sunyink/MFABD2/actions)
[![最新版本](https://img.shields.io/github/v/release/sunyink/MFABD2?label=最新版本&logo=github&color=green)](https://github.com/sunyink/MFABD2/releases)
</div>

本项目基于 [MaaFramework](https://github.com/MaaXYZ/MaaFramework) 所提供的项目模板进行开发的棕色尘埃2自动化助手。

> **MaaFramework** 是基于图像识别技术、运用 [MAA] 开发经验去芜存菁、完全重写的新一代自动化黑盒测试框架。
> 低代码的同时仍拥有高扩展性，旨在打造一款丰富、领先、且实用的开源库，助力开发者轻松编写出更好的黑盒测试程序，并推广普及。

本项目继承 [JZPPP/MaaBD2](https://github.com/JZPPP/MaaBD2)衣钵 继续跟进游戏版本更新，主攻任务流程的优化强化。（任务流程基本重做，以前经验不再适用。）

> 向[JZPPP/MaaBD2]的开发和支持者致敬，在前人肩膀上起步事半功倍。

## 获取

### 版本区分

**目前决定分两个版本。**

+ **[MFABD2-Fast分支]** `快速版`: [github.com/sunyink/MFABD2-Fast](https://github.com/sunyink/MFABD2/tree/Fast)
  

  快速版，平时随用随开发随上传，**使用git更新**，可以选择比较稳定的提交来用。
  

+ **[MFABD2-Main分支]** 暂定位为`发布版`或`稳定版`: [github.com/sunyink/MFABD2-Main](https://github.com/sunyink/MFABD2/releases)

  “稳定版”，如果某个快速版表现较好，会考虑镜像过去做一个发布版。发布版参照正规MFA模板发布，**直接在releases下载包**，支持软件UI内资源版本升级，体验十分接近MAA。框架是新界面，UI与快速版不同。

<br>


<details>
  <summary> ⚠️【重要公告】 ：如果你正在使用1.*.*版本，请展开查看 </summary>

  
  __📌   以`快速版3c86ad0`、`发行版v1.2.2`为分界点，项目仓库进行重组。正在使用1.*.*用户应进行如下操作：__

  
  - `快速版`删除原文件夹，重新`git clone` `fast`分支。_（也可以自行命令行修改映射）_
  - `发行版`删除原文件夹，重新下载新的[`2.*.*`](https://github.com/sunyink/MFABD2/releases) 及更新发布包。

 📌 请放心，`1.*.*`本身没有问题，可以继续使用。但重组后远程路径已改变，一旦**更新**就会出现很大问题。
</details>

<br>


### ◆快速版部署
+ 部署：选择合适位置使用`Git` or `Powershell`，会自行创建子文件夹：

  1.`shift` + `右键` ,单击`在此处打开powershell窗口`。
  
  2.在弹出窗口中运行`git clone -c advice.detachedHead=false --depth 1 --branch Fast https://github.com/sunyink/MFABD2.git`

  - 版本切换：先完成`clone`，之后参照历史提交Hash标记切换，比如`git checkout 8002d62`
<details>
  <summary>版本切换进阶</summary>

  <p><strong>！！不要离开Fast分支确保你在<code>git switch Fast</code>！！</strong></p>

  <p>想自由切换先将浅层克隆恢复：<code>git fetch</code></p>

  <p>选取<code>Fast</code>分支的版本号来回溯，如：<code>git checkout 8002d62 -- .</code></p>

  <hr>
</details>

+ 更新：在根目录`pull`:

  1.在程序`根目录`中`shift` + `右键` ,单击`在此处打开powershell窗口`。
  
  2.在弹出窗口中运行`git pull`

**注意，快速版不要开启、使用GUI界面本身的更新功能，此版本应仅进行GitHub Code更新同步。** _重组改版后，逻辑上可以点Gui更新，但快速版一般都领先于发行版，所以行为没有意义。_

<br>

### ◆稳定版部署
+ 进入 **[MFABD2-Resource]发行版页** : [github.com/sunyink/MFABD2-Resource](https://github.com/sunyink/MFABD2-Resource/releases)，下载对应平台压缩包，解压即用。
  


## 使用方式 （仅支持模拟器使用）



 
>  功能、任务流程正在调试中，有问题可提交issues。能录or拍下视频最好，出问题前后几秒(步)带模拟器画面和MFA回显能，能帮助我快速排错。
  
  尽量在良好网络环境下运行。触发重连转圈可能吞掉那一瞬间操作导致错误，故失误概率可以是罕见、偶尔、泪目。

  1.推荐使用MuMu模拟器12运行游戏（可以直接使用国际版or自行配置Google环境），模拟器显示建议设置为`平板版 1920*1080 (DPI ≈ 270 or 280)`。
> - 多模拟器运作需要一定ADB知识。参考：adb.exe可视为windows服务，默认服务端口号`5037`，模拟器为其客户端，有各自的客户端口号。Mumu模拟器根据多开器编号决定`Adb端口号`，默认`0`号为`16384`、`1`号为`16416`。国际版与普通版可以共存。后启动的版本的端口号遵循前者规律+1，如`16385`。通常adb开启一个就可以控制多个模拟器，不建议多版本Adb并行启动，可能影响识别，可以自定义ADB路径与端口解决。
  

  2.游戏内设置均为默认，其中设置 `操作-选择操作方式-点击地面` `图像-分辨率-FHD` 。
 > 画面质量异常请进行检查，步骤2后仍异常可尝试切换渲染方法。_一般经验，新机器`Vulkan`、旧机器`DirectX`表现较好。_

 3.任务流程已基本实现箱庭地图状态识别、技能传送阵自行生成、几乎所有自行复位(餐馆卡带例外，请避免从餐馆下线)。推荐在`剧情主线地图`、`传送阵上`结束游戏。
 > 利用025.08新出的‘快速卡带’功能，已实现采集卡带自定义选择；需要在‘快速卡带’页面，将意向关卡标黄，如此标黄卡带就会移动到最前，操作顺序决定标黄卡带的排序；每日采集只能去3个卡带，利用下拉菜单分配剧情卡带/角色卡带。

 4.一些配置如下，配置一次就可以了

 > 装备请保留并锁定一件 SR +9的装备用来精炼
 >
>   PVP战斗和分解装备的设置如图，请手动设置一次即可（技能位置与装备强化等设置为模拟器本地保存，不会影响其他端游戏；强化设置老登可以自行适度上强度；PVP设置10倍也是可以的。）

>
> 可以关闭技能动画，加快速度
> 
- 人物技能请按图中设置

 > <img alt="LOGO" src="https://github.com/sunyink/MFABD2/blob/Fast/ReadMe/IT.png"  width="600px"/>
 > <img alt="LOGO" src="https://github.com/sunyink/MFABD2/blob/Fast/ReadMe/3.png"  width="400px"/>

## 功能一览

* [X] GUI界面 
  * [开发中] 增加一些自定义的功能、对已有功能完善。
  * [研究中] GUI界面交互

* [X] 启动游戏 
  * 能更新游戏程序
  * 能更新数据版本
  * （Google Play环境与网络环境需要自行解决）

* [X] 日常任务
  * [X] 扫荡
    * [X] 狩猎场关卡选择 
    * [X] 冒险航线策略、次数选择 （完善中）
    * [X] 圣石洞穴属性图选择 
  * [X] 采集派遣 
    * [X] 采集策略选择
      * [X] 自定义剧情卡带/角色卡带
  * [X] PVP
    * [X] PVP次数选择
  * [X] 白嫖抽卡 
  * [X] 装备制作强化分解 
  * [X] 领取日常任务奖励
    * [X] 公会签到
    * [X] 餐馆结算/常客圣石领取 
  * [X] 领取通行证奖励
  * [X] 肉鸽塔每日快速战斗 (子选项，默认关闭) 
  * [X] 领取邮件-普通与商品
* [X] 每周独立周常
    * [X] 末日之书一轮
    * [X] 小屋访问点赞
    * [X] 浏览街机界面
* [ ] 半自动操作：
  * [ ] 爬塔刷层数
  * [ ] 末日之书刷分数
  * [ ] （半自动指：手动调到页面后无限循环刷。**常闭，一次只能开一种**）

* [X] 活动图
  * [X] 关卡扫荡
    * [ ] 小游戏扫荡(平时应关闭)
    * [X] 难度选择（普通\挑战）

### 致谢

- [MaaFramework](https://github.com/MaaXYZ/MaaFramework) 自动化测试框架

- [MaaPracticeBoilerplate](https://github.com/MaaXYZ/MaaPracticeBoilerplate) MaaFramework项目模板

- [MFAWPF](https://github.com/SweetSmellFox/MFAWPF) Pipeline协议项目的通用GUI
- [MFAAvalonia](https://github.com/SweetSmellFox/MFAAvalonia) 基于Avalonia的MAAFramework通用GUI项目
- [MFATools](https://github.com/SweetSmellFox/MFATools) 开发工具
- [maa-support-extension](https://github.com/neko-para/maa-support-extension) VSCode扩展
### 规范
> 如果要参与开发，可以参考文档。必须先本地测试通过再合并。

- [Pipeline协议规范](https://github.com/MaaXYZ/MaaFramework/blob/main/docs/zh_cn/1.1-%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B.md)
- [帮助](/开发帮助.txt)

## 鸣谢

本项目继承 **[JZPPP/MaaBD2](https://github.com/JZPPP/MaaBD2)** 成果，感谢植树！
本项目由 **[MaaFramework](https://github.com/MaaXYZ/MaaFramework)** 强力驱动！

