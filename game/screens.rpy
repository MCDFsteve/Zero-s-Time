################################################################################
## 初始化
################################################################################

init offset = -1


################################################################################
## 样式
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.webp", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.webp", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.webp", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.webp", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.webp", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.webp"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.webp", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.webp"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.webp", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## 游戏内界面
################################################################################


## 对话界面 ########################################################################
##
## 对话界面用于向用户显示对话。它需要两个参数，who 和 what，分别是叙述角色的名字
## 和所叙述的文本。（如果没有名字，参数 who 可以是 None。）
##
## 此界面必须创建一个 id 为 what 的文本可视控件，因为 Ren'Py 使用它来管理文本显
## 示。它还可以创建 id 为 who 和 id 为 window 的可视控件来应用样式属性。
##
## https://www.renpy.cn/doc/screen_special.html#say
#手表
transform watch_center:
         xcenter 0.1
         ycenter 0.1
transform year:
         xcenter 0.1
         ycenter 0.05
transform _time:
         xcenter 0.1
         ycenter 0.1
         alpha 1.0
         linear 1.0 alpha 0.5
         linear 1.0 alpha 1.0
         repeat
transform week:
         xcenter 0.1
         ycenter 0.15
screen watch:
    add "gui/watch.webp":
       at watch_center
    text "[years]" size 30 font "Cubic-11-1.000-R-2.ttf" color "#ffffff":
       at year
    text "{b}[times]{/b}" size 65 font "Cubic-11-1.000-R-2.ttf" color "#ffffff":
       at _time
    text "{b}[weeks]{/b}" size 45 font "Cubic-11-1.000-R-2.ttf" color "#ffffff":
       at week
    add "gui/watch_light.webp":
       at watch_center
#音乐盒
init python:

    #  步骤1，创建一个MusicRoom实例。
    mr = MusicRoom(fadeout=1.0)

    # Step 2. 添加音乐文件。
    mr.add("music/title.ogg")
    mr.add("music/richang.ogg")
    mr.add("music/school.ogg")
    mr.add("music/lanzhu.ogg")
    #mr.add("track2.ogg")
    #mr.add("track3.ogg")
# Step 3. 创建音乐空间界面。
screen music_room:
    add  "extra/bg_musicroom.webp"
    tag menu

    #frame:
        #has vbox

        # 每条音轨的播放按钮。
        #textbutton "Track 1" action mr.Play("music/title.ogg")
        #textbutton "Track 2" action mr.Play("track2.ogg")
       # textbutton "Track 3" action mr.Play("track3.ogg")

        #null height 20

        # 切换音轨按钮。
        #textbutton "Next" action mr.Next()
        #textbutton "Previous" action mr.Previous()

        #null height 20

        # 用户退出音乐空间的按钮。
    vbox:
        xpos 0.07
        ypos 0.07
        spacing 39
        textbutton _("{size=80}主题曲-陈次犬{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action mr.Play("music/title.ogg")
        if persistent.music_richang:
          textbutton _("{size=80}日常-陈次犬{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action mr.Play("music/richang.ogg")
        else:
          textbutton _("{size=80}？？？{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.music_school:
          textbutton _("{size=80}校园-陈次犬{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action mr.Play("music/school.ogg")
        else:
          textbutton _("{size=80}？？？{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.music_lanzhu:
          textbutton _("{size=80}危机-陈次犬{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action mr.Play("music/lanzhu.ogg")
        else:
          textbutton _("{size=80}？？？{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        if main_menu:
          imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action ShowMenu("menu")
        if not main_menu:
          imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action Return()

    # 音乐空间的音乐播放入口。
    on "replace" action mr.Play()

    # 离开时恢复主菜单的音乐。
    on "replaced" action Play("music", "music/title.ogg")
#音乐盒
screen Tips():

    tag menu
    modal True
    add "gui/tips.webp"

    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        imagebutton idle "extra/page.webp" hover "extra/page_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips2")
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        if main_menu:
          imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action ShowMenu("menu")
        if not main_menu:
          imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action Return()
    hbox:
        xpos 0.2
        ypos 0.93
        spacing 15
        imagebutton idle "extra/page1_on.webp" hover "extra/page1_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips")
        imagebutton idle "extra/page2.webp" hover "extra/page2_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips2")
        imagebutton idle "extra/page3.webp" hover "extra/page3_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips3")
        imagebutton idle "extra/page4.webp" hover "extra/page4_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips4")
        imagebutton idle "extra/page5.webp" hover "extra/page5_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips5")
        
    key "game_menu" action Return() #设置右键返回，方便使用
    if persistent.tips01:
        textbutton _("{size=50}{b}pbb{/b}{/size}") xpos 0.05 ypos 0.05 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips01")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.05 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips02:
        textbutton _("{size=50}{b}工口同人本{/b}{/size}") xpos 0.05 ypos 0.1 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips02")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.1 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips03:
        textbutton _("{size=50}{b}d站{/b}{/size}") xpos 0.05 ypos 0.15 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips03")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.15 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips04:
        textbutton _("{size=50}{b}鬼畜{/b}{/size}") xpos 0.05 ypos 0.2 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips04")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.2 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips05:
        textbutton _("{size=50}{b}cq{/b}{/size}") xpos 0.05 ypos 0.25 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips05")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.25 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips06:
        textbutton _("{size=50}{b}番剧{/b}{/size}") xpos 0.05 ypos 0.3 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips06")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.3 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips07:
        textbutton _("{size=50}{b}npc{/b}{/size}") xpos 0.05 ypos 0.35 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips07")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.35 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips08:
        textbutton _("{size=50}{b}地球online{/b}{/size}") xpos 0.05 ypos 0.4 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips08")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.4 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips09:
        textbutton _("{size=50}{b}家里蹲{/b}{/size}") xpos 0.05 ypos 0.45 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips09")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.45 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips10:
        textbutton _("{size=50}{b}油陷{/b}{/size}") xpos 0.05 ypos 0.5 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips10")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.5 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips11:
        textbutton _("{size=50}{b}希望之花{/b}{/size}") xpos 0.05 ypos 0.55 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips11")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.55 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips12:
        textbutton _("{size=50}{b}现充{/b}{/size}") xpos 0.05 ypos 0.6 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips12")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.6 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips13:
        textbutton _("{size=50}{b}巴麻镁{/b}{/size}") xpos 0.05 ypos 0.65 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips13")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.65 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    
        
screen Tips2():

    tag menu
    modal True
    add "gui/tips.webp"

    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        imagebutton idle "extra/page.webp" hover "extra/page_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips3")
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        if main_menu:
          imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action ShowMenu("menu")
        if not main_menu:
          imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action Return()
    hbox:
        xpos 0.2
        ypos 0.93
        spacing 15
        imagebutton idle "extra/page1.webp" hover "extra/page1_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips")
        imagebutton idle "extra/page2_on.webp" hover "extra/page2_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips2")
        imagebutton idle "extra/page3.webp" hover "extra/page3_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips3")
        imagebutton idle "extra/page4.webp" hover "extra/page4_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips4")
        imagebutton idle "extra/page5.webp" hover "extra/page5_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips5")
        
        
    key "game_menu" action Return() #设置右键返回，方便使用
    if persistent.tips14:
        textbutton _("{size=50}{b}晓美岩{/b}{/size}") xpos 0.05 ypos 0.05 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips14")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.05 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips15:
        textbutton _("{size=50}{b}《魔法少女小方》{/b}{/size}") xpos 0.05 ypos 0.1 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips15")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.1 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips16:
        textbutton _("{size=50}{b}厨{/b}{/size}") xpos 0.05 ypos 0.15 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips16")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.15 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips17:
        textbutton _("{size=50}{b}这是禁止事项{/b}{/size}") xpos 0.05 ypos 0.2 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips17")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.2 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips18:
        textbutton _("{size=50}{b}at立场{/b}{/size}") xpos 0.05 ypos 0.25 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips18")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.25 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips19:
        textbutton _("{size=40}{b}已经没有什么好怕的了{/b}{/size}") xpos 0.05 ypos 0.3 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips19")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.3 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips20:
        textbutton _("{size=50}{b}再上映{/b}{/size}") xpos 0.05 ypos 0.35 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips20")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.35 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips21:
        textbutton _("{size=50}{b}和我签订契约吧！{/b}{/size}") xpos 0.05 ypos 0.4 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips21")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.4 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips22:
        textbutton _("{size=50}{b}中二{/b}{/size}") xpos 0.05 ypos 0.45 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips22")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.45 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips23:
        textbutton _("{size=50}{b}灵魂宝石{/b}{/size}") xpos 0.05 ypos 0.5 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips23")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.5 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips24:
        textbutton _("{size=50}{b}时间系能力{/b}{/size}") xpos 0.05 ypos 0.55 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips24")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.55 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips25:
        textbutton _("{size=50}{b}女装{/b}{/size}") xpos 0.05 ypos 0.6 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips25")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.6 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips26:
        textbutton _("{size=50}{b}抖乐{/b}{/size}") xpos 0.05 ypos 0.65 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips26")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.65 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    
screen Tips3():

    tag menu
    modal True
    add "gui/tips.webp"

    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        imagebutton idle "extra/page.webp" hover "extra/page_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips4")
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        if main_menu:
          imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action ShowMenu("menu")
        if not main_menu:
          imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action Return()
    hbox:
        xpos 0.2
        ypos 0.93
        spacing 15
        imagebutton idle "extra/page1.webp" hover "extra/page1_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips")
        imagebutton idle "extra/page2.webp" hover "extra/page2_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips2")
        imagebutton idle "extra/page3_on.webp" hover "extra/page3_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips3")
        imagebutton idle "extra/page4.webp" hover "extra/page4_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips4")
        imagebutton idle "extra/page5.webp" hover "extra/page5_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips5")
        
    key "game_menu" action Return() #设置右键返回，方便使用
    if persistent.tips27:
        textbutton _("{size=50}{b}PUA{/b}{/size}") xpos 0.05 ypos 0.05 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips27")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.05 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips28:
        textbutton _("{size=50}{b}宝可魔{/b}{/size}") xpos 0.05 ypos 0.1 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips28")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.1 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips29:
        textbutton _("{size=50}{b}任地堂{/b}{/size}") xpos 0.05 ypos 0.15 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips29")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.15 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips30:
        textbutton _("{size=50}{b}witch{/b}{/size}") xpos 0.05 ypos 0.2 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips30")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.2 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips31:
        textbutton _("{size=50}{b}泥可泥丝{/b}{/size}") xpos 0.05 ypos 0.25 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips31")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.25 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips32:
        textbutton _("{size=40}{b}蒸汽朋克：边缘行者{/b}{/size}") xpos 0.05 ypos 0.3 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips32")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.3 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips33:
        textbutton _("{size=50}{b}AADR{/b}{/size}") xpos 0.05 ypos 0.35 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips33")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.35 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips34:
        textbutton _("{size=50}{b}ChieAnime{/b}{/size}") xpos 0.05 ypos 0.4 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips34")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.4 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips35:
        textbutton _("{size=50}{b}漫展{/b}{/size}") xpos 0.05 ypos 0.45 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips35")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.45 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips36:
        textbutton _("{size=50}{b}cosplay{/b}{/size}") xpos 0.05 ypos 0.5 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips36")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.5 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips37:
        textbutton _("{size=50}{b}coser{/b}{/size}") xpos 0.05 ypos 0.55 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips37")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.55 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips38:
        textbutton _("{size=50}{b}低德地图{/b}{/size}") xpos 0.05 ypos 0.6 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips38")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.6 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips39:
        textbutton _("{size=50}{b}pb{/b}{/size}") xpos 0.05 ypos 0.65 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips39")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.65 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
screen Tips4():

    tag menu
    modal True
    add "gui/tips.webp"

    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        imagebutton idle "extra/page.webp" hover "extra/page_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips5")
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        if main_menu:
          imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action ShowMenu("menu")
        if not main_menu:
          imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action Return()
    hbox:
        xpos 0.2
        ypos 0.93
        spacing 15
        imagebutton idle "extra/page1.webp" hover "extra/page1_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips")
        imagebutton idle "extra/page2.webp" hover "extra/page2_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips2")
        imagebutton idle "extra/page3.webp" hover "extra/page3_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips3")
        imagebutton idle "extra/page4_on.webp" hover "extra/page4_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips4")
        imagebutton idle "extra/page5.webp" hover "extra/page5_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips5")
        
    key "game_menu" action Return() #设置右键返回，方便使用
    if persistent.tips40:
        textbutton _("{size=50}{b}颜文字{/b}{/size}") xpos 0.05 ypos 0.05 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips40")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.05 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips41:
        textbutton _("{size=50}{b}鹿目方{/b}{/size}") xpos 0.05 ypos 0.1 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips41")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.1 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips42:
        textbutton _("{size=50}{b}撒旦的结合{/b}{/size}") xpos 0.05 ypos 0.15 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips42")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.15 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips43:
        textbutton _("{size=50}{b}堂屋{/b}{/size}") xpos 0.05 ypos 0.2 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips43")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.2 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips44:
        textbutton _("{size=50}{b}橘外人{/b}{/size}") xpos 0.05 ypos 0.25 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips44")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.25 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips45:
        textbutton _("{size=50}{b}零子{/b}{/size}") xpos 0.05 ypos 0.3 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips45")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.3 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips46:
        textbutton _("{size=50}{b}电子{/b}{/size}") xpos 0.05 ypos 0.35 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips46")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.35 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips47:
        textbutton _("{size=50}{b}海马体{/b}{/size}") xpos 0.05 ypos 0.4 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips47")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.4 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips48:
        textbutton _("{size=50}{b}时间悖论{/b}{/size}") xpos 0.05 ypos 0.45 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips48")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.45 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips49:
        textbutton _("{size=50}{b}宇宙质量守恒{/b}{/size}") xpos 0.05 ypos 0.5 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips49")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.5 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips51:
        textbutton _("{size=50}{b}影子{/b}{/size}") xpos 0.05 ypos 0.55 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips51")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.55 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips52:
        textbutton _("{size=50}{b}端锅{/b}{/size}") xpos 0.05 ypos 0.6 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips52")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.6 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.tips50:
        textbutton _("{size=50}{b}死亡回归{/b}{/size}") xpos 0.05 ypos 0.65 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips50")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.65 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
screen Tips5():

    tag menu
    modal True
    add "gui/tips.webp"

    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        imagebutton idle "extra/page.webp" hover "extra/page_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips")
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        if main_menu:
          imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action ShowMenu("menu")
        if not main_menu:
          imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action Return()
    hbox:
        xpos 0.2
        ypos 0.93
        spacing 15
        imagebutton idle "extra/page1.webp" hover "extra/page1_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips")
        imagebutton idle "extra/page2.webp" hover "extra/page2_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips2")
        imagebutton idle "extra/page3.webp" hover "extra/page3_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips3")
        imagebutton idle "extra/page4.webp" hover "extra/page4_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips4")
        imagebutton idle "extra/page5_on.webp" hover "extra/page5_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips5")
        
    key "game_menu" action Return() #设置右键返回，方便使用
    if persistent.tips53:
        textbutton _("{size=50}{b}原子核{/b}{/size}") xpos 0.05 ypos 0.05 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips53")
    else:
        textbutton _("{size=50}{b}？？？{/b}{/size}") xpos 0.05 ypos 0.05 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
screen tips01:
    use Tips
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips')
    textbutton _("{size=50}（架空）即拼波波，一款网购软件。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips")
screen tips02:
    use Tips
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips')
    textbutton _("{size=50}即R18同人志。好孩子不要看这个！{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips")
screen tips03:
    use Tips
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips')
    textbutton _("{size=50}（架空）即Dilidili,一个弹幕视频网站。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips")
screen tips04:
    use Tips
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips')
    textbutton _("{size=50}主要是指将特定素材进行拼接，调音，p图等形式制作的\n无厘头搞笑视频。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips")
screen tips05:
    use Tips
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips')
    textbutton _("{size=50}（架空）逊公司推出的一款基于互联网的即时通讯软件。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips")
screen tips06:
    use Tips
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips')
    textbutton _("{size=50}主要是对日本动画的一种称谓。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips")
screen tips07:
    use Tips
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips')
    textbutton _("{size=50}指非玩家控制的游戏角色。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips")
screen tips08:
    use Tips
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips')
    textbutton _("{size=50}虚构的游戏，其实是现实生活比喻成游戏的称呼。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips")
screen tips09:
    use Tips
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips')
    textbutton _("{size=50}即整天呆在家里的阿宅。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips")
screen tips10:
    use Tips
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips')
    textbutton _("{size=50}（架空）沁野市的特色美食之一。由面粉裹上土豆丝和葱\n油炸而成。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips")
screen tips11:
    use Tips
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips')
    textbutton _("{size=50}（架空）电视动画《机动战士矮达：铁血的奥利给》第二\n季的片尾曲的第一句歌词。因为该集过于生草而变成网络\n热梗。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips")
screen tips12:
    use Tips
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips')
    textbutton _("{size=50}一般指那种，不接触ACG，在现实世界生活的很好的人，\n一般这种人都有对象，并且经常参加社交活动。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips")
screen tips13:
    use Tips
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips')
    textbutton _("{size=50}（架空）电视动画《魔法少女小方》的登场角色。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips")
screen tips14:
    use Tips2
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips2')
    textbutton _("{size=50}（架空）电视动画《魔法少女小方》的登场角色。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips2")
screen tips15:
    use Tips2
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips2')
    textbutton _("{size=50}（架空）STAEE制作的电视动画。获奖无数。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips2")
screen tips16:
    use Tips2
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips2')
    textbutton _("{size=50}指对XX作品很热爱的人的一种称呼。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips2")
screen tips17:
    use Tips2
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips2')
    textbutton _("{size=50}（架空）网络用语，出自电视动画《热宫春日的忧郁》中\n朝比奈十一九六的台词。想回避一些不想谈论或者是触碰\n到秘密的话题时可以使用。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips2")
screen tips18:
    use Tips2
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips2')
    textbutton _("{size=50}（架空）是电视动画《旧世纪福音战士》系列中的一种虚\n构力场。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips2")
screen tips19:
    use Tips2
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips2')
    textbutton _("{size=50}（架空）标准flag之一。出自电视动画《魔法少女小方》\n的巴麻镁。其在说完这句台词后没多久就被咬断了头。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips2")
screen tips20:
    use Tips2
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips2')
    textbutton _("{size=50}（架空）电视动画《只有你不存在的街道》中男主角的能\n力，可以让时间逆转。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips2")
screen tips21:
    use Tips2
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips2')
    textbutton _("{size=50}（架空）电视动画《魔法少女小方》中pb的名台词。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips2")
screen tips22:
    use Tips2
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips2')
    textbutton _("{size=50}形容经常幻想自己是什么大人物，或者具有某种超能力，\n未成年人动画看多了可能会这样。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips2")
screen tips23:
    use Tips2
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips2')
    textbutton _("{size=50}（架空）电视动画《魔法少女小方》中的物品，魔法少女\n存储灵魂的容器。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips2")
screen tips24:
    use Tips2
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips2')
    textbutton _("{size=50}涉及时间的超能力，例如时间停止，时间加速，时间倒流\n等。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips2")
screen tips25:
    use Tips2
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips2')
    textbutton _("{size=50}ACG萌属性，指男人穿上女人的服饰。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips2")
screen tips26:
    use Tips2
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips2')
    textbutton _("{size=50}（架空）字节跑动公司推出的一款短视频软件。在全世界\n受到欢迎。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips2")
screen tips27:
    use Tips3
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips3')
    textbutton _("{size=50}全称“Pick-up Artist”，原意是指“搭讪艺术家”，其原本是\n指男性接受过系统化学习、实践并不断更新提升、自我完\n善情商的行为，后来泛指很会吸引异性、让异性着迷的人\n和其相关行为{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips3")
screen tips28:
    use Tips3
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips3')
    textbutton _("{size=50}（架空）GameFurry开发的掌机游戏系列。主要玩法是抓\n怪和对战，在全世界有着极高的人气。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips3")
screen tips29:
    use Tips3
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips3')
    textbutton _("{size=50}（架空）世界知名的游戏开发与硬件开发公司，旗下代表\n作有也儿夕传说，超级羊里奥等。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips3")
screen tips30:
    use Tips3
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips3')
    textbutton _("{size=50}（架空）任地堂旗下最新世代掌机。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips3")
screen tips31:
    use Tips3
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips3')
    textbutton _("{size=50}（架空）2022年七月新番。讲的是现代女忍者披着jk的外\n皮执行任务。结局令很多观众不满。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips3")
screen tips32:
    use Tips3
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips3')
    textbutton _("{size=50}（架空）改编自游戏《蒸汽朋克1877》的原创动画。出色\n的剧情和人物表现力收获了一片好评。甚至带动了游戏销\n量大幅增加。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips3")
screen tips33:
    use Tips3
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips3')
    textbutton _("{size=50}（架空）全称America Atom's Digitization Research orga\nnization。美国原子数据化研究组织。主要研究方向是原子\n的数据化转换，传输和还原。在全球多个国家设有分部。\n有超过两千多位登记在册的科学家。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips3")
screen tips34:
    use Tips3
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips3')
    textbutton _("{size=50}（架空）沁野市最大的动漫展出，活动主要包括cosplay，\n网络游戏对战以及售卖动漫周边和同人志。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips3")
screen tips35:
    use Tips3
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips3')
    textbutton _("{size=50}指ACG文化相关的展会，按照内容不同，漫展也可以被分\n为不同的种类，比如同人展、博览会等。对于部分御宅族，\n尤其是较缺乏实体ACG资源的地区来说是重要的ACG活动。\n漫展的举办地点一般以当地的会展中心、宾馆或大学校园\n为举办地，取决于会展的性质、规模及主办方。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips3")
screen tips36:
    use Tips3
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips3')
    textbutton _("{size=50}一种扮演虚构角色的表演艺术，是ACG领域的一种重要文\n化活动。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips3")
screen tips37:
    use Tips3
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips3')
    textbutton _("{size=50}对进行cosplay的人的称呼。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips3")
screen tips38:
    use Tips3
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips3')
    textbutton _("{size=50}（架空）一款国产地图导航软件。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips3")
screen tips39:
    use Tips3
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips3')
    textbutton _("{size=50}（架空）电视动画《魔法少女小方》登场角色。外表长得\n像一只兔子，不会说谎，拥有把女孩子变成魔法少女的能\n力。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips3")
screen tips40:
    use Tips4
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips4')
    textbutton _("{size=50}指网络上用标点符号组成的表示自己喜怒哀乐的抽象表情。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips4")
screen tips41:
    use Tips4
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips4')
    textbutton _("{size=50}（架空）电视动画《魔法少女小方》登场角色。主角。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips4")
screen tips42:
    use Tips4
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips4')
    textbutton _("{size=50}（架空）一款肉鸽游戏。玩家需要扮演“撒旦”在各个房间\n探索和打怪。高度的随机性和丰富的道具种类使得其非常\n耐玩。被玩家奉为“肉鸽之神”。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips4")
screen tips43:
    use Tips4
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips4')
    textbutton _("{size=50}（架空）“客厅”在沁野市方言中的称呼。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips4")
screen tips44:
    use Tips4
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips4')
    textbutton _("{size=50}（架空）“橘”出自知名百合番《柑橘色味道》。在妹子和\n妹子透漏出百合气息时，可道“大橘已定”，冒出个男的来\n则称为“橘外人”。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips4")
screen tips45:
    use Tips4
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips4')
    textbutton _("{size=50}（架空）一种未被以前的科学家发现的，一种新的物质形\n态。物理性质介于有质量的由原子构成的物体和电子之间\n，由原子转换而来，也能转换回原子，可以像电子一样被\n光速传输和被电子设备接收。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips4")
screen tips46:
    use Tips4
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips4')
    textbutton _("{size=50}是一种可以在电场中运动的粒子，可以通过载体材料进行\n传导。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips4")
screen tips47:
    use Tips4
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips4')
    textbutton _("{size=50}大脑中负责存储记忆的一块区域，因其结构长得像海马而\n得名。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips4")
screen tips48:
    use Tips4
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips4')
    textbutton _("{size=50}最早在科幻小说中出现，指时间穿越者回到过去以后对未\n来造成的种种悖论。例如典型的祖父悖论：我回到过去杀\n死我的祖父，因为我的祖父死了，那就不会有我，那我就\n不可能回到过去杀死我的祖父。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips4")
screen tips49:
    use Tips4
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips4')
    textbutton _("{size=50}指宇宙不管怎么运动，宇宙的总质量都是不变的。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips4")
screen tips50:
    use Tips4
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips4')
    textbutton _("{size=50}（架空）电视动画《Re:从一开始的异世界生活》中男主角\n的能力，死亡以后会回到死之前的一段时间。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips4")
screen tips51:
    use Tips4
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips4')
    textbutton _("{size=50}（架空）电视动画《秋日重现》中的反派，男主角由于无\n意识之中获得了影子中蛭子神的右眼，获得了死后回到过\n去的能力。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips4")
screen tips52:
    use Tips4
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips4')
    textbutton _("{size=50}（架空）电视剧《端锅》中一个反派，企图在锅里装上炸\n弹拉整公交车人陪葬。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips4")
screen tips53:
    use Tips5
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips5')
    textbutton _("{size=50}原子的最重要部分。由质子和中子组成。是粒子但是不具\n有电荷，所以无法进行电子传导。{/size}") xpos 0.3 ypos 0.05 action ShowMenu("Tips5")
#CG鉴赏
#请根据你的需求改掉坐标及图片，直接放到专案目录下运行会报错（大概）
## Extra screen ###############################################################
transform extra(wait=0):
    xoffset 50
    alpha 0.0
    pause(wait)
    easein 0.5 xoffset 0 alpha 1
screen Extra():

    tag menu
    modal True
    add "gui/extra.webp"
    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        imagebutton idle "extra/page.webp" hover "extra/page_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Extra2")
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        
        imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("menu")
    hbox:
        
        xpos 0.792
        ypos 0.1
        spacing 15
        
        imagebutton idle "extra/musicroom.webp" hover "extra/musicroom_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("music_room")
    hbox:
        xpos 0.2
        ypos 0.93
        spacing 15
        imagebutton idle "extra/page1_on.webp" hover "extra/page1_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Extra")
        imagebutton idle "extra/page2.webp" hover "extra/page2_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Extra2")
        imagebutton idle "extra/page3.webp" hover "extra/page3_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Extra3")
        imagebutton idle "extra/page4.webp" hover "extra/page4_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Extra4")
    key "game_menu" action Return() #设置右键返回，方便使用

#--------------------------------------------------------------------
    if persistent.cg01_unlocked:
        imagebutton hover "cg_gohan_tukue2" idle "cg_gohan_tukue2_on" xpos 0.05 ypos 0.05  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg01')
    else:
        imagebutton hover "no_cg" idle "no_cg_on" xpos 0.05 ypos 0.05 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()

    if persistent.cg02_unlocked:
        imagebutton hover "cg_kexi_momo" idle "cg_kexi_momo_on" xpos 0.43 ypos 0.05  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg02')
    else:
        imagebutton hover "no_cg" idle "no_cg_on" xpos 0.43 ypos 0.05 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()

    if persistent.cg03_unlocked:
        imagebutton hover "cg_kexi_egao" idle "cg_kexi_egao_on" xpos 0.05 ypos 0.43  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg03')
    else:
        imagebutton hover "no_cg" idle "no_cg_on" xpos 0.05 ypos 0.43 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.cg04_unlocked:
        imagebutton hover "cg_sorawomiru" idle "cg_sorawomiru_on" xpos 0.43 ypos 0.43  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg04')
    else:
        imagebutton hover "no_cg" idle "no_cg_on" xpos 0.43 ypos 0.43 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    #我个人用的，加上声效以及没解锁时也有按钮（免除P背景图的麻烦
    #一页有多少个CG就弄多少个按钮，记得每个复制粘贴后都要改
screen Extra2():

    tag menu
    modal True
    add "gui/extra.webp"

    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        imagebutton idle "extra/page.webp" hover "extra/page_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Extra3")
    hbox:
        
        xpos 0.792
        ypos 0.1
        spacing 15
        
        imagebutton idle "extra/musicroom.webp" hover "extra/musicroom_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("music_room")
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        
        imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("menu")
    hbox:
        xpos 0.2
        ypos 0.93
        spacing 15
        imagebutton idle "extra/page1.webp" hover "extra/page1_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Extra")
        imagebutton idle "extra/page2_on.webp" hover "extra/page2_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Extra2")
        imagebutton idle "extra/page3.webp" hover "extra/page3_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Extra3")
        imagebutton idle "extra/page4.webp" hover "extra/page4_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Extra4")
        
    key "game_menu" action Return() #设置右键返回，方便使用
    if persistent.cg05_unlocked:
        imagebutton hover "cg_sorawomiru2" idle "cg_sorawomiru2_on" xpos 0.05 ypos 0.05  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg05')
    else:
        imagebutton hover "no_cg" idle "no_cg_on" xpos 0.05 ypos 0.05 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.cg06_unlocked:
        imagebutton hover "cg_neko" idle "cg_neko_on" xpos 0.43 ypos 0.05  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg06')
    else:
        imagebutton hover "no_cg" idle "no_cg_on" xpos 0.43 ypos 0.05 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.cg07_unlocked:
        imagebutton hover "cg_mizu" idle "cg_mizu_on" xpos 0.05 ypos 0.43  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg07')
    else:
        imagebutton hover "no_cg" idle "no_cg_on" xpos 0.05 ypos 0.43 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.cg08_unlocked:
        imagebutton hover "cg_kawa" idle "cg_kawa_on" xpos 0.43 ypos 0.43  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg08')
    else:
        imagebutton hover "no_cg" idle "no_cg_on" xpos 0.43 ypos 0.43 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()

screen Extra3():

    tag menu
    modal True
    add "gui/extra.webp"
    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        imagebutton idle "extra/page.webp" hover "extra/page_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Extra4")
    hbox:
        
        xpos 0.792
        ypos 0.1
        spacing 15
        
        imagebutton idle "extra/musicroom.webp" hover "extra/musicroom_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("music_room")
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        
        imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("menu")
    hbox:
        xpos 0.2
        ypos 0.93
        spacing 15
        imagebutton idle "extra/page1.webp" hover "extra/page1_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Extra")
        imagebutton idle "extra/page2.webp" hover "extra/page2_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Extra2")
        imagebutton idle "extra/page3_on.webp" hover "extra/page3_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Extra3")
        imagebutton idle "extra/page4.webp" hover "extra/page4_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Extra4")
        
    key "game_menu" action Return() #设置右键返回，方便使用
    if persistent.cg09_unlocked:
        imagebutton hover "cg_kabann" idle "cg_kabann_on" xpos 0.05 ypos 0.05  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg09')
    else:
        imagebutton hover "no_cg" idle "no_cg_on" xpos 0.05 ypos 0.05 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.cg10_unlocked:
        imagebutton hover "cg_kexi_miru" idle "cg_kexi_miru_on" xpos 0.43 ypos 0.05  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg10')
    else:
        imagebutton hover "no_cg" idle "no_cg_on" xpos 0.43 ypos 0.05 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.cg11_unlocked:
        imagebutton hover "cg_school_hiroba" idle "cg_school_hiroba_on" xpos 0.05 ypos 0.43  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg11')
    else:
        imagebutton hover "no_cg" idle "no_cg_on" xpos 0.05 ypos 0.43 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.cg12_unlocked:
        imagebutton hover "cg_school_hiroba2" idle "cg_school_hiroba2_on" xpos 0.43 ypos 0.43  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg12')
    else:
        imagebutton hover "no_cg" idle "no_cg_on" xpos 0.43 ypos 0.43 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
screen Extra4():

    tag menu
    modal True
    add "gui/extra.webp"
    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        imagebutton idle "extra/page.webp" hover "extra/page_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Extra")
    hbox:
        
        xpos 0.792
        ypos 0.1
        spacing 15
        
        imagebutton idle "extra/musicroom.webp" hover "extra/musicroom_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("music_room")
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        
        imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("menu")
    hbox:
        xpos 0.2
        ypos 0.93
        spacing 15
        imagebutton idle "extra/page1.webp" hover "extra/page1_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Extra")
        imagebutton idle "extra/page2.webp" hover "extra/page2_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Extra2")
        imagebutton idle "extra/page3.webp" hover "extra/page3_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Extra3")
        imagebutton idle "extra/page4_on.webp" hover "extra/page4_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Extra4")
        
    key "game_menu" action Return() #设置右键返回，方便使用
    if persistent.cg13_unlocked:
        imagebutton hover "cg_kexi_shiru" idle "cg_kexi_shiru_on" xpos 0.05 ypos 0.05  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg13')
    else:
        imagebutton hover "no_cg" idle "no_cg_on" xpos 0.05 ypos 0.05 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.cg14_unlocked:
        imagebutton hover "cg_zicheng_te" idle "cg_zicheng_te_on" xpos 0.43 ypos 0.05  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg14')
    else:
        imagebutton hover "no_cg" idle "no_cg_on" xpos 0.43 ypos 0.05 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.cg15_unlocked:
        imagebutton hover "cg_kexi_syashin" idle "cg_kexi_syashin_on" xpos 0.05 ypos 0.43  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg15')
    else:
        imagebutton hover "no_cg" idle "no_cg_on" xpos 0.05 ypos 0.43 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    if persistent.cg16_unlocked:
        imagebutton hover "cg_zicheng_te2" idle "cg_zicheng_te2_on" xpos 0.43 ypos 0.43  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg16')
    else:
        imagebutton hover "no_cg" idle "no_cg_on" xpos 0.43 ypos 0.43 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
#--------------------------------------------------------------------

    
    #我个人用的，加上声效以及没解锁时也有按钮（免除P背景图的麻烦
    #一页有多少个CG就弄多少个按钮，记得每个复制粘贴后都要改
#--------------------------------------------------------------------
#现在第一页算是写完了，不过怎样让CG显示？
#因为是傻瓜式写法，所以……
    
screen cg01:
    tag menu
    imagemap:
        ground 'bg_gohan_tukue2'
        key "game_menu" action ShowMenu('Extra')
        hotspot (0, 0, 1920, 1080) action ShowMenu("Extra")
        #hotspot那里，因为我这是1920x1080分辨率就写这个数，其他分辨率自行改正

#每一个按钮都写一个screen，有多少CG就复制粘贴多少次（扶额
#如果CG有差分怎么办？很简单……

screen cg02:
    tag menu
    imagemap:
        ground 'bg_kexi_momo'
        key "game_menu" action ShowMenu('Extra')
        if persistent.cg02_1_unlocked:
            hotspot (0, 0, 1920, 1080) action ShowMenu("cg02_1")
        if not persistent.cg02_1_unlocked:
            hotspot (0, 0, 1920, 1080) action ShowMenu("Extra")

screen cg02_1:
    tag menu
    imagemap:
        ground '你的CG图差分'
        key "game_menu" action ShowMenu('Extra')
        hotspot (0, 0, 1920, 1080) action ShowMenu("Extra")

#再写一个界面就行了……记得给差分也设个变数
#这里的变数很容易弄错，记得仔细测试，不要弄错CG的编号

#那么第二页怎么写呢？其实就是把第一页复制一遍，将
#screen Extra():
#这一行改成
#screen Extra2():
#然后将CG也改成第二页的就可以了。要注意的是，给第二页的CG写screen的时候

screen cg03:
    tag menu
    imagemap:
        ground 'bg_kexi_egao'
        key "game_menu" action ShowMenu('Extra')
        hotspot (0, 0, 1920, 1080) action ShowMenu("Extra")
screen cg04:
    tag menu
    imagemap:
        ground 'bg_sorawomiru'
        key "game_menu" action ShowMenu('Extra')
        hotspot (0, 0, 1920, 1080) action ShowMenu("Extra")
screen cg05:
    tag menu
    imagemap:
        ground 'bg_sorawomiru2'
        key "game_menu" action ShowMenu('Extra2')
        hotspot (0, 0, 1920, 1080) action ShowMenu("Extra2")
screen cg06:
    tag menu
    imagemap:
        ground 'bg_neko'
        key "game_menu" action ShowMenu('Extra2')
        hotspot (0, 0, 1920, 1080) action ShowMenu("Extra2")
screen cg07:
    tag menu
    imagemap:
        ground 'bg_mizu'
        key "game_menu" action ShowMenu('Extra2')
        hotspot (0, 0, 1920, 1080) action ShowMenu("Extra2")
screen cg08:
    tag menu
    imagemap:
        ground 'bg_kawa'
        key "game_menu" action ShowMenu('Extra2')
        hotspot (0, 0, 1920, 1080) action ShowMenu("Extra2")
screen cg09:
    tag menu
    imagemap:
        ground 'bg_kabann'
        key "game_menu" action ShowMenu('Extra3')
        hotspot (0, 0, 1920, 1080) action ShowMenu("Extra3")
screen cg10:
    tag menu
    imagemap:
        ground 'bg_kexi_miru'
        key "game_menu" action ShowMenu('Extra3')
        hotspot (0, 0, 1920, 1080) action ShowMenu("Extra3")
screen cg11:
    tag menu
    imagemap:
        ground 'bg_school_hiroba'
        key "game_menu" action ShowMenu('Extra3')
        hotspot (0, 0, 1920, 1080) action ShowMenu("Extra3")
screen cg12:
    tag menu
    imagemap:
        ground 'bg_school_hiroba2'
        key "game_menu" action ShowMenu('Extra3')
        hotspot (0, 0, 1920, 1080) action ShowMenu("Extra3")
screen cg13:
    tag menu
    imagemap:
        ground 'bg_kexi_shiru'
        key "game_menu" action ShowMenu('Extra4')
        hotspot (0, 0, 1920, 1080) action ShowMenu("Extra4")
screen cg14:
    tag menu
    imagemap:
        ground 'bg_zicheng_te'
        key "game_menu" action ShowMenu('Extra4')
        hotspot (0, 0, 1920, 1080) action ShowMenu("Extra4")
screen cg15:
    tag menu
    imagemap:
        ground 'bg_kexi_syashin'
        key "game_menu" action ShowMenu('Extra4')
        hotspot (0, 0, 1920, 1080) action ShowMenu("Extra4")
screen cg16:
    tag menu
    imagemap:
        ground 'bg_zicheng_te2'
        key "game_menu" action ShowMenu('Extra4')
        hotspot (0, 0, 1920, 1080) action ShowMenu("Extra4")
#CG鉴赏

screen say(who, what):
    key "game_menu" action ShowMenu("game_menu")
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## 如果有对话框头像，会将其显示在文本之上。请不要在手机界面下显示这个，因为
    ## 没有空间。
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## 通过 Character 对象使名称框可用于样式化。
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.webp", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.webp", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## 输入界面 ########################################################################
##
## 此界面用于显示 renpy.input。prompt 参数用于传递文本提示。
##
## 此界面必须创建一个 id 为 input 的输入可视控件来接受各种输入参数。
##
## https://www.renpy.cn/doc/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## 选择界面 ########################################################################
##
## 此界面用于显示由 menu 语句生成的游戏内选项。参数 items 是一个对象列表，每个对
## 象都有字幕和动作字段。
##
## https://www.renpy.cn/doc/screen_special.html#choice

screen choice(items):
    style_prefix "choice"
    key "game_menu" action ShowMenu("game_menu")
    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")

## 快捷菜单界面 ######################################################################
##
## 快捷菜单显示于游戏内，以便于访问游戏外的菜单。

screen quick_menu():

    ## 确保该菜单出现在其他界面之上，
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("回退")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action Rollback()
            textbutton _("历史") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('history')
            textbutton _("提示") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('Tips')
            textbutton _("快进") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动播放") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action Preference("auto-forward", "toggle")
            textbutton _("保存") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('save')
            textbutton _("快存") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action QuickSave()
            textbutton _("快读") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action QuickLoad()
            textbutton _("菜单") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('game_menu')


## 此代码确保只要用户没有主动隐藏界面，就会在游戏中显示 quick_menu 界面。
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## 标题和游戏菜单界面
################################################################################

## 导航界面 ########################################################################
##
## 该界面包含在标题菜单和游戏菜单中，并提供导航到其他菜单，以及启动游戏。

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("开始游戏") action Start()
            textbutton _("读取游戏") action ShowMenu("load")
            textbutton _("快速读取") action QuickLoad()
            textbutton _("CG鉴赏") action ShowMenu("Extra")
            textbutton _("词典") action ShowMenu("Tips")
            textbutton _("设置") action ShowMenu("preferences")
            textbutton _("帮助") action ShowMenu("help")
            textbutton _("关于") action ShowMenu("about")
            textbutton _("退出") action Quit(confirm=True)
        if not main_menu:

            textbutton _("历史") action ShowMenu("history")

            textbutton _("保存") action ShowMenu("save")
            textbutton _("快速保存") action QuickSave()
            
            textbutton _("读取游戏") action ShowMenu("load")
            textbutton _("快速读取") action QuickLoad()
            textbutton _("提示") action ShowMenu("Tips")
            textbutton _("设置") action ShowMenu("preferences")
            textbutton _("帮助") action ShowMenu("help")
            textbutton _("关于") action ShowMenu("about")
            textbutton _("标题界面") action MainMenu()
            textbutton _("退出") action Quit(confirm=True)
            key "game_menu" action Return()
        
        if _in_replay:

            textbutton _("结束回放") action EndReplay(confirm=True)



            

        

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## 标题菜单界面 ######################################################################
##
## 用于在 Ren'Py 启动时显示标题菜单。
##
## https://www.renpy.cn/doc/screen_special.html#main-menu
transform gear:
     rotate 0
     rotate_pad False
     transform_anchor True
     around (0.5,0.5)
     xanchor 0.5
     yanchor 0.5
     xpos 0.68
     ypos 0.1
     linear 1.5 rotate 360
     repeat
transform main_menu_show_btn(wait=0):
    xoffset 100
    alpha 0.0
    pause(wait)
    easein 0.5 xoffset 0 alpha 1
screen title1:
    add "title/title1.webp" xpos 0.19 ypos 0.03
screen title2:
    add "title/title2.webp" xpos 0.19 ypos 0.03
screen title3:
    add "title/title3.webp" xpos 0.19 ypos 0.03
screen title4:
    add "title/title4.webp" xpos 0.19 ypos 0.03
screen menu:
    use title_main
    modal True
    add "block"
    add "block2"
    add "block3"
    add "copyright"
#换标题
    if persistent.chapter2:
       use title2
    if not persistent.chapter2:
       use title1
    if persistent.chapter2 and persistent.chapter3:
       use title3
    if not persistent.chapter2 and persistent.chapter3:
       use title1
    if persistent.chapter2 and persistent.chapter3 and persistent.chapter4:
       use title4
    if not persistent.chapter2 and persistent.chapter3 and persistent.chapter4:
       use title1
#换标题
    vbox:
        spacing 0
        xpos 0
        ypos 0.1
        style_prefix "radio"
        imagebutton idle "title/start.webp" hover "title/start_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn()
          action Start()
        imagebutton idle "title/load.webp" hover "title/load_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn(0.1)
          action ShowMenu("load")
        imagebutton idle "title/quick.webp" hover "title/quick_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn(0.2)
          action QuickLoad()
        imagebutton idle "title/extra.webp" hover "title/extra_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn(0.3)
          action ShowMenu("Extra")
        imagebutton idle "title/tips.webp" hover "title/tips_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn(0.4)
          action ShowMenu("Tips")
        imagebutton idle "title/help.webp" hover "title/help_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn(0.5)
          action ShowMenu("help")
        imagebutton idle "title/about.webp" hover "title/about_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn(0.6)
          action ShowMenu("about")
    imagebutton idle "title/options.webp" hover "title/options_on.webp" xpos 0.599 ypos 0.01 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("preferences")
    add "title/gear.webp":
       at gear
    imagebutton idle "title/exit.webp" hover "title/exit_on.webp" xpos 0.64 ypos 0.9 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action Quit(confirm=True)
    #key "game_menu" action Return()
image block =SnowBlossom("title/block.webp",count=45,border=10,xspeed=(-2,50),yspeed=(20,30),start=0,fast=True,horizontal=False)
image block3 =SnowBlossom("title/block3.webp",count=40,border=10,xspeed=(-2,50),yspeed=(20,30),start=0,fast=True,horizontal=False)
image block2 =SnowBlossom("title/block2.webp",count=20,border=10,xspeed=(-2,50),yspeed=(20,30),start=0,fast=False,horizontal=True)
image copyright= Text("{b}Copyright © 2023 DFsteve{/b}",xpos=0,ypos=0.93,font="CangErYuMoW01-2.ttf",size=40,color="#000000")
transform black:
     alpha 1.0
     linear 3.0 alpha 0.4
     linear 3.0 alpha 1.0
     repeat
transform title_black:
     alpha 0.0
     linear 30.0 alpha 0.4
     linear 30.0 alpha 0.0
     repeat
transform gear2:
     rotate 0
     rotate_pad False
     transform_anchor True
     around (0.5,0.5)
     xanchor 0.5
     yanchor 0.5
     xpos 0.85
     ypos 0.6
     linear 2.0 rotate -360
     repeat
transform gear3:
     rotate 0
     rotate_pad False
     transform_anchor True
     around (0.5,0.5)
     xanchor 0.5
     yanchor 0.5
     xpos 0.55
     ypos 0.8
     linear 5.0 rotate 360
     repeat
screen title_main():
    ## 此语句可确保替换掉任何其他菜单界面。
    tag menu
    add "gui/black.webp"
#换背景
    if persistent.chapter2:
       add "gui/main_menu.webp":
        at black
    if not persistent.chapter2:
       add "gui/main_menu_3.webp":
        at black
    if persistent.chapter2 and persistent.chapter3:
       add "gui/main_menu_2.webp":
        at black
    if not persistent.chapter2 and persistent.chapter3:
       add "gui/main_menu_3.webp":
        at black
    if persistent.chapter2 and persistent.chapter3 and persistent.chapter4:
       add "gui/main_menu_4.webp":
        at black
    if not persistent.chapter2 and persistent.chapter3 and persistent.chapter4:
       add "gui/main_menu_3.webp":
        at black
    add "gui/title_black.webp":
        at title_black
    add "title/gear2.webp":
        at gear2
    add "title/gear3.webp":
        at gear3
    key "game_menu" action Return()
    ## 此空框可使标题菜单变暗。
    #frame:
        #style "main_menu_frame"


    ## use 语句将其他的界面包含进此界面。标题界面的实际内容在导航界面中。
    #use navigation

    #if gui.show_name:
        
       # vbox:
          #  style "main_menu_vbox"

           # text "[config.name!t]":
             #   style "main_menu_title"

           # text "[config.version]":
             #   style "main_menu_version"
 
transform start:
   alpha 1.0
   linear 0.5 alpha 0.2
   linear 1.0 alpha 1.0
   repeat
screen main_menu():
    use title_main
#换标题
    if persistent.chapter2:
       use title2
    if not persistent.chapter2:
       use title1
    if persistent.chapter2 and persistent.chapter3:
       use title3
    if not persistent.chapter2 and persistent.chapter3:
       use title1
    if persistent.chapter2 and persistent.chapter3 and persistent.chapter4:
       use title4
    if not persistent.chapter2 and persistent.chapter3 and persistent.chapter4:
       use title1
#换标题
    hbox: 
      xalign 0.0 
      yalign 0.0
      imagebutton idle "gui/none.webp" hover "gui/none.webp" activate_sound "audio/button.ogg":
         action ShowMenu('menu')
    key "game_menu" action ShowMenu('menu')
    key "dismiss" action ShowMenu('menu')
    add "gui/title_start.webp":
        at start
style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.webp"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")
##游戏菜单
screen game_menu():
    add "game_menu/bg.webp"
    key "game_menu" action Return()
    imagebutton idle "title/options.webp" hover "title/options_on.webp" xpos 0.599 ypos 0.01 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("preferences")
    add "title/gear.webp":
       at gear
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        
        imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action Return()
    vbox:
        spacing 0
        xpos 0
        ypos 0.05
        imagebutton idle "game_menu/quicksave.webp" hover "game_menu/quicksave_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn()
          action QuickSave()
        imagebutton idle "game_menu/quickload.webp" hover "game_menu/quickload_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn(0.1)
          action QuickLoad()
        imagebutton idle "game_menu/save.webp" hover "game_menu/save_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn(0.2)
          action ShowMenu("save")
        imagebutton idle "game_menu/load.webp" hover "game_menu/load_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn(0.3)
          action ShowMenu("load")
        imagebutton idle "game_menu/history.webp" hover "game_menu/history_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn(0.4)
          action ShowMenu("history")
        imagebutton idle "game_menu/tips.webp" hover "game_menu/tips_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn(0.5)
          action ShowMenu("Tips")
        imagebutton idle "game_menu/help.webp" hover "game_menu/help_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn(0.6)
          action ShowMenu("help")
        imagebutton idle "game_menu/about.webp" hover "game_menu/about_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn(0.7)
          action ShowMenu("about")
        imagebutton idle "game_menu/title.webp" hover "game_menu/title_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn(0.8)
          action MainMenu()
        imagebutton idle "game_menu/exit.webp" hover "game_menu/exit_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn(0.9)
          action Quit(confirm=True)
## 游戏菜单界面 ######################################################################
##
## 此界面列出了游戏菜单的基本共同结构。可使用界面标题调用，并显示背景、标题和导
## 航菜单。
##
## scroll 参数可以是 None，也可以是 viewport 或 vpgrid。当此界面与一个或多个子界
## 面同时使用时，这些子界面将被嵌入（放置）在其中。

#screen game_menu(title, scroll=None, yinitial=0.0):

    #style_prefix "game_menu"

    #if main_menu:
       # add gui.main_menu_background
   # else:
       # add gui.game_menu_background

   # frame:
       # style "game_menu_outer_frame"

        #hbox:

            ## 导航部分的预留空间。
           # frame:
               # style "game_menu_navigation_frame"

           # frame:
               # style "game_menu_content_frame"

               # if scroll == "viewport":

                   # viewport:
                     #   yinitial yinitial
                       # scrollbars "vertical"
                      #  mousewheel True
                       # draggable True
                       # pagekeys True

                       # side_yfill True

                       # vbox:
                       #     transclude

               # elif scroll == "vpgrid":

                   # vpgrid:
                       # cols 1
                      #  yinitial yinitial

                       # scrollbars "vertical"
                       # mousewheel True
                      #  draggable True
                      #  pagekeys True

                       # side_yfill True

                       # transclude

                #else:

                    #transclude

    #use navigation

    #textbutton _("返回"):
        #style "return_button"

        #action Return()

    #label title

    #if main_menu:
        #key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 45

    background "gui/overlay/game_menu.webp"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 55
    top_margin 30
    ysize 900

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## 关于界面 ########################################################################
##
## 此界面提供有关游戏和 Ren'Py 的制作人员和版权信息。
##
## 此界面没有什么特别之处，因此它也可以作为一个例子来说明如何制作一个自定义界
## 面。

screen about():

    tag menu
    modal True
    add "gui/main_menu_4.webp"
    style_prefix "about"
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        if main_menu:
          imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action ShowMenu("menu")
        if not main_menu:
          imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action Return()
    vbox:
        spacing -4
        xpos 0.2
        ypos 0.1
        label "[config.name!t]"
        text _("版本 [config.version!t]\n")

            ## gui.about 通常在 options.rpy 中设置。
        if gui.about:
            text "[gui.about!t]\n"

        text _("引擎：{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]\n\n[renpy.license!t]")
        key "game_menu" action Return()
            
style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size
## 读取和保存界面 #####################################################################
##
## 这些界面负责让用户保存游戏并能够再次读取。由于它们几乎完全一样，因此这两个界
## 面都是以第三个界面 file_slots 来实现的。
##
## https://www.renpy.cn/doc/screen_special.html#save https://www.renpy.cn/doc/
## screen_special.html#load
screen save():
    use save_menu
    modal True
    tag menu
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        if main_menu:
          imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action ShowMenu("menu")
        if not main_menu:
          imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action Return()
screen save_menu():
    add "game_menu/save_bg.webp"
    tag menu
    key "game_menu" action FileDelete(None, confirm=True, page=None)
    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动存档"), quick=_("快速存档"))
    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        imagebutton idle "extra/page.webp" hover "extra/page_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action FilePageNext()
    button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value
    hbox:
        xpos 0.2
        ypos 0.93
        spacing 15
        imagebutton idle "extra/page1.webp" hover "extra/page1_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action FilePage(1)
        imagebutton idle "extra/page2.webp" hover "extra/page2_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action FilePage(2)
        imagebutton idle "extra/page3.webp" hover "extra/page3_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action FilePage(3)
        imagebutton idle "extra/page4.webp" hover "extra/page4_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action FilePage(4)
        imagebutton idle "extra/page5.webp" hover "extra/page5_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action FilePage(5)
        imagebutton idle "extra/page6.webp" hover "extra/page6_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action FilePage(6)
        imagebutton idle "extra/page7.webp" hover "extra/page7_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action FilePage(7)
        imagebutton idle "extra/page8.webp" hover "extra/page8_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action FilePage(8)
        imagebutton idle "extra/page9.webp" hover "extra/page9_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action FilePage(9)
    

    

    fixed:

            ## 此代码确保输入控件在任意按钮执行前可以获取 enter 事件。
        ##order_reverse True

            ## 页面名称，可以通过单击按钮进行编辑。
        ##button:
            ##style "page_label"

            ##key_events True
           ## xalign 0.5
            ##action page_name_value.Toggle()

            ##input:
                ##style "page_label_text"
                ##value page_name_value

            ## 存档位网格。
        grid gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"

            xalign 0.85
            yalign 0.3

            spacing gui.slot_spacing

            for i in range(gui.file_slot_cols * gui.file_slot_rows):

                $ slot = i + 1

                button:
                    action FileAction(slot)

                    has vbox

                    add FileScreenshot(slot) xalign 0.5

                    text FileTime(slot, format=_("{font=Cubic-11-1.000-R-2.ttf}{#file_time}%Y-%m-%d %H:%M{/font}"), empty=_("空白存档")):
                        style "slot_time_text"

                    text FileSaveName(slot):
                        style "slot_name_text"

                    key "save_delete" action FileDelete(slot)


screen load():
    use save_menu
    modal True
    tag menu
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        if main_menu:
          imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action ShowMenu("menu")
        if not main_menu:
          imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action Return()
screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动存档"), quick=_("快速存档"))

    use game_menu(title):

        fixed:

            ## 此代码确保输入控件在任意按钮执行前可以获取 enter 事件。
            order_reverse True

            ## 页面名称，可以通过单击按钮进行编辑。
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## 存档位网格。
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("空存档位")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## 用于访问其他页面的按钮。
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}自动\n存档") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}快速\n存档") action FilePage("quick")

                ## range(1, 10) 给出 1 到 9 之间的数字。
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is choice_button_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## 设置界面 ########################################################################
##
## 设置界面允许用户配置游戏，使其更适合自己。
##
## https://www.renpy.cn/doc/screen_special.html#preferences

screen preferences():

    tag menu
    modal True
    add "gui/option.webp"
    key "game_menu" action Return()
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        if main_menu:
          imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action ShowMenu("menu")
        if not main_menu:
          imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action Return()
        
    vbox:
        xpos 0
        ypos 0
        spacing 15
        style_prefix "radio"
        imagebutton idle "options/display.webp" hover "options/display_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            at main_menu_show_btn()
            action NullAction()
        textbutton _("{size=45}窗口化{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action Preference("display", "window")
        textbutton _("{size=45}全屏{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action Preference("display", "fullscreen")
    vbox:
        xpos 0
        ypos 0.26
        spacing 15
        style_prefix "check"
        imagebutton idle "options/skip.webp" hover "options/skip_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            at main_menu_show_btn()
            action NullAction()
        textbutton _("{size=45}未读文本{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action Preference("skip", "toggle")
        textbutton _("{size=45}选项后继续{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action Preference("after choices", "toggle")
        textbutton _("{size=45}忽略转场{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action InvertSelected(Preference("transitions", "toggle"))

                ## 可在此处添加 radio_pref 或 check_pref 类型的额外 vbox，以添加
                ## 额外的创建者定义的偏好设置。
    hbox:
        
        xpos 0.635
        ypos 0
        spacing 15
        imagebutton idle "options/other.webp" hover "options/other_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action NullAction()
    vbox:
        xpos 0.45
        ypos 0.15
        spacing 15
        style_prefix "slider"
        box_wrap True
        label _("{size=45}文字速度{/size}")
        bar value Preference("text speed") released Play("sound","audio/bar.ogg") 
        label _("{size=45}自动前进时间{/size}")
        bar value Preference("auto-forward time") released Play("sound","audio/bar.ogg") 
        if config.has_music:
            label _("{size=45}音乐音量{/size}")

            hbox:
                bar value Preference("music volume") released Play("sound","audio/bar.ogg") 
        if config.has_sound:
            label _("{size=45}音效音量{/size}")
            hbox:
                bar  value Preference("sound volume") released Play("sound","audio/bar.ogg") 
    vbox:
        xpos 0.445
        ypos 0.63
        spacing 15
        if config.has_music or config.has_sound or config.has_voice:
            null height gui.pref_spacing

            textbutton _("{size=50}全部静音{/size}"):
             action Preference("all mute", "toggle")
            style "mute_all_button"
        #if config.sample_sound:
            #textbutton _("测试") action Play("sound", config.sample_sound)


        #if config.has_voice:
            #label _("语音音量")

            #hbox:
                #bar value Preference("voice volume")

        #if config.sample_voice:
            #textbutton _("测试") action Play("voice", config.sample_voice)

        

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 1000

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675

## 历史界面 ########################################################################
##
## 这是一个向用户显示对话历史的界面。虽然此界面没有什么特别之处，但它必须访问储
## 存在 _history_list 中的对话历史记录。
##
## https://www.renpy.cn/doc/history.html
screen old_menu(title, scroll=None, yinitial=0.0):
    frame:
        style "game_menu_outer_frame"

        hbox:

            ## 导航部分的预留空间。
            #frame:
                #style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True 
                        xpos 0.2
                        #vbox:
                            #transclude
                            

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude
screen history():
    modal True
    tag menu
    add "game_menu/history_bg.webp"
    ## 避免预缓存此界面，因为它可能非常大。
    predict False
    hbox:
        xpos 0.638
        ypos 0.9
        spacing 0
        imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
           action Return()

    use old_menu(_("历史"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## 此代码可确保如果 history_height 为 None 时仍可正常显示条目。
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## 从 Character 对象中获取叙述角色的文字颜色，如果设置了
                        ## 的话。
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("尚无对话历史记录。")


## 此代码决定了允许在历史记录界面上显示哪些标签。

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## 帮助界面 ########################################################################
##
## 提供有关键盘和鼠标映射信息的界面。它使用其它界面（keyboard_help、mouse_help
## 和 gamepad_help）来显示实际的帮助内容。
screen help_keyboard():
    add "gui/main_menu.webp"
    hbox:
        
        xpos 0.05
        ypos 0.175
        spacing 15
        
        imagebutton idle "help/keyboard_help.webp" hover "help/keyboard_help_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action NullAction()
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        if main_menu:
          imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action ShowMenu("menu")
        if not main_menu:
          imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action Return()
    default device = "keyboard"
    vbox:
        spacing 0
        xpos 0
        ypos 0
        imagebutton idle "help/keyboard.webp" hover "help/keyboard_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn()
          action ShowMenu("help")
        imagebutton idle "help/gamepad.webp" hover "help/gamepad_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn()
          action ShowMenu("help2")
screen help_gamepad():
    add "gui/main_menu.webp"
    hbox:
        
        xpos 0.05
        ypos 0.175
        spacing 15
        
        imagebutton idle "help/gamepad_help.webp" hover "help/gamepad_help_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action NullAction()
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        if main_menu:
          imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action ShowMenu("menu")
        if not main_menu:
          imagebutton idle "title/return.webp" hover "title/return_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action Return()
    default device = "gamepad"
    vbox:
        spacing 0
        xpos 0
        ypos 0
        imagebutton idle "help/keyboard.webp" hover "help/keyboard_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn()
          action ShowMenu("help")
        imagebutton idle "help/gamepad.webp" hover "help/gamepad_on.webp" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn()
          action ShowMenu("help2")
screen help():
    key "game_menu" action Return()
    modal True
    tag menu
    use help_keyboard
screen help2():
    key "game_menu" action Return()
    modal True
    tag menu
    use help_gamepad

################################################################################
## 其他界面
################################################################################


## 确认界面 ########################################################################
##
## 当 Ren'Py 需要询问用户有关确定或取消的问题时，会调用确认界面。
##
## https://www.renpy.cn/doc/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## 显示此界面时，确保其他界面无法输入。
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.webp"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("确定") action yes_action
                textbutton _("取消") action no_action

    ## 右键点击退出并答复 no（取消）。
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is quick_button_text
style confirm_button is gui_medium_button
style confirm_button_text is choice_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.webp", "gui/frame.webp"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## 快进指示界面 ######################################################################
##
## skip_indicator 界面用于指示快进正在进行中。
##
## https://www.renpy.cn/doc/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("正在快进")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## 此变换用于一个接一个地闪烁箭头。
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.webp", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## 我们必须使用包含“▸”（黑色右旋小三角）字形的字体。
    font "DejaVuSans.ttf"


## 通知界面 ########################################################################
##
## 通知界面用于向用户显示消息。（例如，当游戏快速保存或进行截屏时。）
##
## https://www.renpy.cn/doc/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.webp", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL 模式界面 ####################################################################
##
## 此界面用于 NVL 模式的对话和菜单。
##
## https://www.renpy.cn/doc/screen_special.html#nvl


screen nvl(dialogue, items=None):
    key "game_menu" action ShowMenu("game_menu")
    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## 在 vpgrid 或 vbox 中显示对话框。
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## 此语句控制一次可以显示的 NVL 模式条目的最大数量。
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.webp"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## 移动设备界面
################################################################################

#style pref_vbox:
    #variant "medium"
    #xsize 675

## 由于可能没有鼠标，我们将快捷菜单替换为一个使用更少、更大按钮的版本，这样更容
## 易触摸。
#screen quick_menu():
    #variant "touch"

    #zorder 100

    #if quick_menu:

        #hbox:
            #style_prefix "quick"

            #xalign 0.5
           #yalign 1.0

            #textbutton _("回退") action Rollback()
            #textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            #textbutton _("自动播放") action Preference("auto-forward", "toggle")
            #textbutton _("菜单") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.webp"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.webp"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.webp"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.webp"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.webp"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.webp"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.webp", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.webp", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.webp", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.webp", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.webp", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.webp"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.webp", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.webp"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
