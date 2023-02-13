﻿## 此文件包含有可自定义您游戏的设置。
##
## 以“##”开头的语句是注释，您不应该对其取消注释。以“#”开头的语句是注释掉的代码，
## 在适用的时候您可能需要对其取消注释。
## 基础 ##########################################################################
define audio.v1 = "voice/v1.ogg"
define audio.v3 = "voice/v3.ogg"
define audio.v5 = "voice/v5.ogg"
define audio.v7 = "voice/v7.ogg"
define audio.v9 = "voice/v9.ogg"
define audio.v11 = "voice/v11.ogg"
image logo= At("title/logo.webp")
image warning= Text("{b}本故事纯属虚构。\n与现实生活中任何人\n和组织无关。请勿主观带入。{/b}",font="Cubic-11-1.000-R-2.ttf", size=45,color="#ffffff")
image play= Text("{b}本游戏推荐外设设备：鼠标。\n使用鼠标游玩以获得最佳效果。{/b}",font="Cubic-11-1.000-R-2.ttf", size=45,color="#ffffff")
image start= Text("{b}START{/b}", size=45,color="#000000")
label splashscreen:
    if persistent.chapter3:
       $ config.main_menu_music = "music/title2.ogg"
    if not persistent.chapter3:
       $ config.main_menu_music = "music/title.ogg"
    if persistent.chapter2 and persistent.chapter3 and persistent.chapter4:
       $ config.main_menu_music = "music/title.ogg"
    if not persistent.chapter2 and persistent.chapter3 and persistent.chapter4:
       $ config.main_menu_music = "music/title2.ogg"
    scene bg_none 
    with fade
    show logo:
      xcenter 0.5
      ycenter 0.5
    with dissolve
    $ renpy.pause(2, hard=False)
    hide logo with dissolve
    show warning:
      xcenter 0.5
      ycenter 0.5
    with dissolve
    $ renpy.pause(3, hard=False)
    hide warning with dissolve
    with fade
    return
## 用户可读的游戏名称。此命令用来设置默认窗口标题，并且会在界面和错误报告中出
## 现。
##
## 带有 _() 的字符串表示其可被翻译。
init python:
    define.move_transitions("move", 0.3)
define config.name = _("彼零之时")
define gui.interface_text_outlines = [(4,"#000000",0,0)]
define gui.input_text_outlines = [(4,"#000000",0,0)]
define gui.input_prompt_text_outlines = [(4,"#000000",0,0)]
define gui.label_text_outlines = [(4,"#000000",0,0)]
define gui.prompt_text_outlines = [(4,"#000000",0,0)]
define gui.dialogue_text_outlines = [(2,"#000000",1,1)]
define gui.notify_text_outlines = [(4,"#000000",0,0)]
##define gui.name_text_outlines = [(2,"#ffffff",0,0)]
define config.mouse = { }
define config.mouse['default'] = [ ( "gui/arrow.webp", 0, 0) ]
define config.nvl_adv_transition = Dissolve(1)
define config.adv_nvl_transition = Dissolve(1)
## 决定上面给出的标题是否显示在标题界面屏幕。设置为 False 来隐藏标题。

define gui.show_name = False

## 游戏版本号。

define config.version = "alpha.0.33"


## 放置在游戏内“关于”屏幕上的文本。将文本放在三个引号之间，并在段落之间留出空
## 行。

define gui.about = _p("""
作者：戴夫邻居史蒂夫DFsteve
\n个人博客：{a=https://www.dfsteve.top}www.dfsteve.top{/a}

""")


## 在构建的发布版中，可执行文件和目录所使用的短名称。此处仅限使用 ASCII 字符，并
## 且不能包含空格、冒号或分号。

define build.name = "Zero_no_toki"


## 音效和音乐 #######################################################################

## 这三个变量控制哪些内置的混音器会默认显示给用户。将其中一个设置为 False 将隐藏
## 对应的混音器。

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## 为了让用户在音效或语音轨道上播放测试音频，请取消对下面一行的注释并设置播放的
## 样本声音。

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## 将以下语句取消注释就可以设置标题界面播放的背景音乐文件。此文件将在整个游戏中
## 持续播放，直至音乐停止或其他文件开始播放。



## 转场 ##########################################################################
##
## 这些变量用来控制某些事件发生时的转场。每一个变量都应设置成一个转场，或者是
## None 来表示无转场。

## 进入或退出游戏菜单。

define config.enter_transition = Pixellate(.5,5)
define config.exit_transition = Pixellate(.5,5)


## 各个游戏菜单之间的转场。

define config.intra_transition = dissolve
define config.end_splash_transition = dissolve

## 载入游戏后使用的转场。

define config.after_load_transition = Pixellate(.5,5)


## 在游戏结束之后进入主菜单时使用的转场。

define config.end_game_transition = dissolve


## 用于控制在游戏开始标签不存在时转场的变量。作为替代，在显示初始化场景后使用
## with 语句。


## 窗口管理 ########################################################################
##
## 此命令控制对话框窗口何时显示。若为 show，对话框将总是显示。若为 hide，对话框
## 仅在对话出现时显示。若为 auto，对话框会在 scene 语句前隐藏，并在有新对话时重
## 新显示。
##
## 在游戏开始后，可以用 window show、window hide 和 window auto 语句来改变其状
## 态。

define config.window = "hide"


## 用于显示和隐藏对话框窗口的转场

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## 默认设置 ########################################################################

## 控制默认的文字显示速度。默认的 0 为瞬间，而其他数字则是每秒显示出的字符数。

default preferences.text_cps = 20


## 默认的自动前进延迟。数字越大，等待时间越长，有效范围为 0 - 30。

default preferences.afm_time = 8


## 存档目录 ########################################################################
##
## 控制 Ren'Py 放置游戏存档的特定操作系统目录。存档文件将放置在：
##
## Windows：%APPDATA\RenPy\<config.save_directory>
##
## Macintosh：$HOME/Library/RenPy/<config.save_directory>
##
## Linux：$HOME/.renpy/<config.save_directory>
##
## 该语句通常不应变更，若要变更，应为有效字符串而不是表达式。

define config.save_directory = "Zero_no_toki"


## 图标 ##########################################################################
##
## 在任务栏或 Dock 上显示的图标。

define config.window_icon = "gui/window_icon.png"


## 构建配置 ########################################################################
##
## 此部分控制 Ren'Py 如何将您的项目转变为发行版文件。

init python:

    ## 以下函数接受文件模式。文件模式不区分大小写，并与基础目录的相对路径相匹
    ## 配，包括或不包括 /。如果多个模式匹配，则使用第一个模式。
    ##
    ## 在一个模式中：
    ##
    ## / 是目录分隔符。
    ##
    ## * 匹配所有字符，目录分隔符除外。
    ##
    ## ** 匹配所有字符，包括目录分隔符。
    ##
    ## 例如，“*.txt”匹配基础目录中的 txt 文件，“game/**.ogg”匹配游戏目录或任何子
    ## 目录中的 ogg 文件，“**.psd”匹配项目中任何位置的 psd 文件。

    ## 将文件列为 None 来使其从构建的发行版中排除。

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## 若要封装文件，需将其列为“archive”。

    # build.classify('game/**.webp', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## 匹配为文档模式的文件会在 Mac 应用程序构建中被复制，因此它们同时出现在 APP
    ## 和 ZIP 文件中。

    build.documentation('*.html')
    build.documentation('*.txt')


## 下载扩展文件和执行应用内购需要一个 Google Play 许可密钥。许可密钥可以在
## Google Play 开发者控制台的“服务和 API”页面找到。

# define build.google_play_key = "..."


## 与 itch.io 项目相关的用户名和项目名，以 / 分隔。

# define build.itch_project = "renpytom/test-project"
