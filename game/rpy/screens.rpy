################################################################################
## 初始化
################################################################################

init offset = -1
################################################################################
## 样式
################################################################################
transform main_menu_show_btn(wait=0):
    xoffset 100
    alpha 0.0
    pause(wait)
    easein 0.5 xoffset 0 alpha 1
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
    thumb_offset 15
style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    right_bar Frame("gui/slider/horizontal_[prefix_]bar.webp", gui.slider_borders, tile=gui.slider_tile)
    left_bar Frame("gui/slider/horizontal_hover_bar.webp", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.webp"
    thumb_offset 20
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
transform watch_center2:
         xcenter 0.1+0.82
         ycenter 0.1
         linear 1.0 alpha 0.5
         linear 1.0 alpha 0.0
         repeat
transform watch_center:
         xcenter 0.1+0.82
         ycenter 0.1
transform year:
         xcenter 0.1+0.82
         ycenter 0.05
transform _time:
         xcenter 0.1+0.82
         ycenter 0.1
         alpha 1.0
         linear 1.0 alpha 0.5
         linear 1.0 alpha 1.0
         repeat
transform week:
         xcenter 0.1+0.82
         ycenter 0.15
transform year2:
         xcenter 0.28
         ycenter 0.23
transform _time2:
         xcenter 0.28
         ycenter 0.5
         alpha 1.0
         linear 1.0 alpha 0.5
         linear 1.0 alpha 1.0
         repeat
transform week2:
         xcenter 0.282
         ycenter 0.77
screen watch:
    imagebutton idle "gui/watch.webp" hover "gui/watch_on.webp" at watch_center hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
      action ShowMenu("watch_ui")
    text "[years]" size 30 font "Cubic-11-1.000-R-2.ttf" color "#ffffff":
       at year
    text "{b}[times]{/b}" size 65 font "Cubic-11-1.000-R-2.ttf" color "#ffffff":
       at _time
    text "{b}[weeks]{/b}" size 45 font "Cubic-11-1.000-R-2.ttf" color "#ffffff":
       at week
    add "gui/watch_light.webp":
       at watch_center
    use watch_option
screen watch_loop1:
    imagebutton idle "gui/watch.webp" hover "gui/watch_on.webp" at watch_center hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
      action Jump("loop1_true")
    add "gui/watch_kira.webp":
        at watch_center2
    text "[years]" size 30 font "Cubic-11-1.000-R-2.ttf" color "#ffffff":
       at year
    text "{b}[times]{/b}" size 65 font "Cubic-11-1.000-R-2.ttf" color "#ffffff":
       at _time
    text "{b}[weeks]{/b}" size 45 font "Cubic-11-1.000-R-2.ttf" color "#ffffff":
       at week
    add "gui/watch_light.webp":
       at watch_center
    use watch_option1
screen watch_loop2:
    imagebutton idle "gui/watch.webp" hover "gui/watch_on.webp" at watch_center hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
      action Jump("loop2_true")
    add "gui/watch_kira.webp":
        at watch_center2
    text "[years]" size 30 font "Cubic-11-1.000-R-2.ttf" color "#ffffff":
       at year
    text "{b}[times]{/b}" size 65 font "Cubic-11-1.000-R-2.ttf" color "#ffffff":
       at _time
    text "{b}[weeks]{/b}" size 45 font "Cubic-11-1.000-R-2.ttf" color "#ffffff":
       at week
    add "gui/watch_light.webp":
       at watch_center
    use watch_option2
screen watch_ui:
    add "gui/background.webp"
    add "gui/watch_bg2.webp"
    add "gui/watch_bg.webp"
    text "[years]" size 160 font "Cubic-11-1.000-R-2.ttf" color "#ffffff":
       at year2
    text "{b}[times]{/b}" size 340 font "Cubic-11-1.000-R-2.ttf" color "#ffffff":
       at _time2
    text "{b}[weeks]{/b}" size 240 font "Cubic-11-1.000-R-2.ttf" color "#ffffff":
       at week2
    key "pad_b_press" action Return()
    key "game_menu" action Return()
    hbox:
        xpos 0.638
        ypos 0.9
        spacing 15
        imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action Return()
    use watch_option_hide
screen loop1_screen:
    add "gui/loop_bg.webp" at shake
    add "gui/nvl.webp"
    add "gui/watch_bg2.webp"
    add "gui/watch_bg.webp"
    add "loop_d":
       at year2
    add "loop_t":
       at _time2
    add "loop_w":
       at week2
screen loop2_screen:
    add "gui/loop_bg.webp" at shake
    add "gui/nvl.webp"
    add "gui/watch_bg2.webp"
    add "gui/watch_bg.webp"
    add "loop2_d":
       at year2
    add "loop2_t":
       at _time2
    add "loop2_w":
       at week2
screen loop3_screen:
    add "gui/loop_bg.webp" at shake
    add "gui/nvl.webp"
    add "gui/watch_bg2.webp"
    add "gui/watch_bg.webp"
    add "loop3_d":
       at year2
    add "loop3_t":
       at _time2
    add "loop3_w":
       at week2
screen say_option:
    key ["q", "pad_back_press"] action ToggleScreen("quick_menu_full")
screen say_option_hide:
    key ["q", "pad_back_press"] action Hide("quick_menu_full")
screen watch_option:
    key ["w", "pad_b_press"] action ShowMenu("watch_ui")
screen watch_option_hide:
    key ["w", "pad_b_press"] action Return()
screen watch_option1:
    key ["w", "pad_b_press"] action Jump("loop1_true")
screen watch_option2:
    key ["w", "pad_b_press"] action Jump("loop2_true")
screen say(who, what):
    key "game_menu" action ShowMenu("game_menu")
    style_prefix "say"
    use say_option
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
    add "gui/nvl.webp"
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
transform titlepos:
     xpos 0.3
     ypos 0.0-0.01
screen title1():
    add "title/title1.webp" at titlepos
screen title2():
    add "title/title2.webp" at titlepos
screen title3():
    add "title/title3.webp" at titlepos
screen title4():
    add "title/title4.webp" at titlepos
image copyright= Text("Copyright © 2022-2023 DFsteve",font="Aldrich-Regular.ttf", size=40,color="#000000",outlines = [(3,"#FFFFFF",1,2)])
screen menu:
    use title_main
    modal True
    add "gui/background2.webp":
       at back_1
    hbox:
        spacing 15
        xpos 0.0
        ypos 0.93
        add "copyright"
        text "|[config.version]" size 40 font "Aldrich-Regular.ttf" color "#000000" outlines [(3,"#FFFFFF",1,2)]
    add "title/gear2.webp":
        at gear2
    key "game_menu" action [Hide("menu"), ShowMenu("main_menu")]
    key "pad_b_press" action [Hide("menu"), ShowMenu("main_menu")]

#换标题
    if persistent.chapter==1:
       use title1
    elif persistent.chapter==2:
       use title2
    elif persistent.chapter==5:
       use title3
    elif persistent.chapter==6:
       use title4
    else:
       use title1
#换标题
    vbox:
        spacing 15
        xpos 0
        ypos 0.01
        imagebutton idle "ui_start" hover "ui_start_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn()
          action Start()
        imagebutton idle "ui_load" hover "ui_load_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn(0.1)
          action ShowMenu("load")
        imagebutton idle "ui_quick" hover "ui_quick_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn(0.2)
          action QuickLoad()
        imagebutton idle "ui_tips" hover "ui_tips_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn(0.3)
          action ShowMenu("Tips")
        imagebutton idle "ui_help" hover "ui_help_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn(0.4)
          action ShowMenu("help")
        imagebutton idle "ui_about" hover "ui_about_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn(0.5)
          action ShowMenu("about")
        imagebutton idle "ui_exit" hover "ui_exit_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn(0.6)
          action Quit(confirm=True)
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        
        imagebutton idle "ui_extra" hover "ui_extra_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Extra")
    imagebutton idle "ui_option" hover "ui_option_on" xpos 0.615 ypos 0.01 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("preferences")
transform gear2:
     rotate 0
     rotate_pad False
     transform_anchor True
     around (0.5,0.5)
     xanchor 0.5
     yanchor 0.5
     xpos 0.9155
     ypos 0.4
     linear 2.5 rotate -360
     repeat
transform alpha_anime:
     alpha 1.0
     linear 10 alpha 0.9
     linear 3 alpha 0.4
     linear 3 alpha 1.0
     repeat
screen title_main():
    ## 此语句可确保替换掉任何其他菜单界面。
    tag menu
#换背景
    if persistent.chapter==1:
       add "gui/main_menu_3.webp"
    elif persistent.chapter==2:
       add "gui/main_menu.webp"
    elif persistent.chapter==5:
       add "gui/main_menu_2.webp"
    elif persistent.chapter==6:
       add "gui/main_menu_4.webp"
    else:
       add "gui/main_menu_3.webp"
    add "gui/alpha.webp" at alpha_anime
    add "gui/background.webp"
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

             #   style "main_menu_version"
 
transform start:
   alpha 1.0
   linear 0.5 alpha 0.2
   linear 1.0 alpha 1.0
   repeat
screen main_menu():
    use title_main
#换标题
    if persistent.chapter==1:
       use title1
    elif persistent.chapter==2:
       use title2
    elif persistent.chapter==5:
       use title3
    elif persistent.chapter==6:
       use title4
    else:
        use title1
#换标题
    hbox: 
      xalign 0.0 
      yalign 0.0
      imagebutton idle "gui/none.webp" hover "gui/none.webp" activate_sound "audio/button.ogg":
         action ShowMenu('menu')
    key "game_menu" action ShowMenu('menu')
    key "dismiss" action ShowMenu('menu')
    add "press_start":
        xcenter 0.5
        ycenter 0.8
        at start
image press_start= Text("PRESS ANY KEY TO START",font="Aldrich-Regular.ttf", size=50,color="#ffffff",outlines = [(3,"#000000",2,2)])
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
transform back_1:
     alpha 0.0
     ycenter -0.5
     linear 0.3 alpha 1.0 ycenter 0.5
screen game_menu():
    add "gui/background.webp"
    add "gui/background2.webp":
       at back_1
    key "game_menu" action Return()
    key "pad_b_press" action Return()
    imagebutton idle "ui_option" hover "ui_option_on" xpos 0.615 ypos 0.01 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("preferences")
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        
        imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action Return()
    vbox:
        spacing 15
        xpos 0
        ycenter 0.5
        imagebutton idle "ui_save" hover "ui_save_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn()
          action ShowMenu("save")
        imagebutton idle "ui_load" hover "ui_load_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn(0.1)
          action ShowMenu("load")
        imagebutton idle "ui_help" hover "ui_help_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn(0.2)
          action ShowMenu("help")
        imagebutton idle "ui_about" hover "ui_about_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn(0.3)
          action ShowMenu("about")
        imagebutton idle "ui_title" hover "ui_title_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn(0.4)
          action MainMenu()
        imagebutton idle "ui_exit" hover "ui_exit_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          at main_menu_show_btn(0.5)
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
    add "gui/nvl.webp"
    style_prefix "about"
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        if main_menu:
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action ShowMenu("menu")
        if not main_menu:
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action Return()
    vbox:
        spacing -4
        xpos 0.2
        ypos 0.0
        if persistent.chapter==1:
          add "title/title1.webp":
            zoom 0.5
            xpos 0.0
        elif persistent.chapter==2:
          add "title/title2.webp":
            zoom 0.5
            xpos 0.0
        elif persistent.chapter==5:
          add "title/title3.webp":
            zoom 0.5
            xpos 0.0
        elif persistent.chapter==6:
          add "title/title4.webp":
            zoom 0.5
            xpos 0.0
        else:
          add "title/title1.webp":
            zoom 0.5
            xpos 0.0
        text _("版本 [config.version]\n")

            ## gui.about 通常在 options.rpy 中设置。
        if gui.about:
            text "[gui.about!t]\n"

        text _("引擎：{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]\n\n[renpy.license!t]")
        text "    "
        add "gui/logo2.webp":
            zoom 0.5
        key "game_menu" action Return()
        key "pad_b_press" action Return()
            
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
    use tips_option
    modal True
    tag menu
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        if main_menu:
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action ShowMenu("menu")
        if not main_menu:
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action Return()
screen save_menu():
    add "game_menu/save_bg.webp"
    add "gui/nvl.webp"
    add "gui/save_menu.webp"
    tag menu
    key "game_menu" action FileDelete(None, confirm=True, page=None)
    key "pad_b_press" action Return()
    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动存档"), quick=_("快速存档"))
    add "gui/ui_white.webp":
        ycenter 0.97
        xpos 0.01
        xzoom 1.1
    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        add "ui_page"
    button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value
    hbox:
        xpos 0.18
        ypos 0.93
        spacing 15
        imagebutton idle "ui_page1" hover "ui_page1_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action FilePage(1)
        imagebutton idle "ui_page2" hover "ui_page2_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action FilePage(2)
        imagebutton idle "ui_page3" hover "ui_page3_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action FilePage(3)
        imagebutton idle "ui_page4" hover "ui_page4_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action FilePage(4)
        imagebutton idle "ui_page5" hover "ui_page5_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action FilePage(5)
        imagebutton idle "ui_page6" hover "ui_page6_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action FilePage(6)
        imagebutton idle "ui_page7" hover "ui_page7_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action FilePage(7)
        imagebutton idle "ui_page8" hover "ui_page8_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action FilePage(8)
        imagebutton idle "ui_page9" hover "ui_page9_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
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
    use tips_option
    modal True
    tag menu
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        if main_menu:
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action ShowMenu("menu")
        if not main_menu:
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
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
    add "gui/nvl.webp"
    use tips_option
    on "hide" action Hide("quick_menu_full")
    key "game_menu" action Return()
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        if main_menu:
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action ShowMenu("menu")
        if not main_menu:
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action Return()
        
    vbox:
        xpos 0
        ypos 0
        spacing 15
        style_prefix "check"
        add "ui_display"
        textbutton _("{size=45}窗口化{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action Preference("display", "window")
        textbutton _("{size=45}全屏{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action Preference("display", "fullscreen")
    vbox:
        xpos 0
        ypos 0.3
        spacing 15
        style_prefix "check"
        add "ui_skip"
        textbutton _("{size=45}未读文本{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action Preference("skip", "toggle")
        textbutton _("{size=45}选项后继续{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action Preference("after choices", "toggle")
        textbutton _("{size=45}忽略转场{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action InvertSelected(Preference("transitions", "toggle"))

                ## 可在此处添加 radio_pref 或 check_pref 类型的额外 vbox，以添加
                ## 额外的创建者定义的偏好设置。
    vbox:
        xpos 0.45
        ypos 0.0
        spacing 15
        style_prefix "slider"
        box_wrap True
        add "ui_other"
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
        if config.has_music or config.has_sound or config.has_voice:

            textbutton _("{size=50}全部静音{/size}") xpos -0.03 ypos 0.6 hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
             action Preference("all mute", "toggle")
        label _("{size=45}快捷菜单样式{/size}")
        vbox:
          xpos -0.02
          ypos 0.0
          spacing 0
          style_prefix "check"
          textbutton _("{size=45}自动折叠{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action SetVariable("persistent.quickswitch",False)
          textbutton _("{size=45}保持挂起{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action SetVariable("persistent.quickswitch",True)
    add "gui/option_menu.webp"
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
    add "gui/nvl.webp"
    ## 避免预缓存此界面，因为它可能非常大。
    predict False
    hbox:
        xpos 0.638
        ypos 0.9
        spacing 0
        imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
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
                    kerning 10
                    line_spacing 5

        if not _history_list:
            label _("尚无对话历史记录。")
        key "pad_b_press" action Return()
        key "game_menu" action Return()


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
    add "gui/nvl.webp"
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
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action ShowMenu("menu")
        if not main_menu:
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
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
    add "gui/nvl.webp"
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
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action ShowMenu("menu")
        if not main_menu:
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
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
    key "pad_b_press" action Return()
    modal True
    tag menu
    use help_keyboard
screen help2():
    key "game_menu" action Return()
    key "pad_b_press" action Return()
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
    zorder 98
    add "gui/say.webp":
       ycenter 0.068
    hbox:
        spacing 1
        ycenter 0.068
        xpos 0.07
        text _("{b}正在快进{/b}") size 35 font "Huayuan.Gothic.Regular.ttf" color "#ffffff"
        text "■" at delayed_blink(0.0, 1.0) size 35 font "Cubic-11-1.000-R-2.ttf" color "#ffffff"
        text "■" at delayed_blink(0.2, 1.0) size 35 font "Cubic-11-1.000-R-2.ttf" color "#ffffff"
        text "■" at delayed_blink(0.4, 1.0)  size 35 font "Cubic-11-1.000-R-2.ttf" color "#ffffff"
screen tips_say():
    zorder 99
    add "gui/say.webp":
       ycenter 0.068
    hbox:
        spacing 1
        ycenter 0.068
        xpos 0.07
        text _("{b}新的提示已记录{/b}") size 35 font "Huayuan.Gothic.Regular.ttf" color "#ffffff"
        text "{b}~{/b}" at delayed_blink(0.0, 1.0) size 35 font "Cubic-11-1.000-R-2.ttf" color "#ffffff"
screen tips_say2():
    zorder 99
    add "gui/say2.webp":
       ycenter 0.068
    hbox:
        spacing 1
        ycenter 0.068
        xpos 0.07
        text _("{b}提示“{color=#BFBFFF}时间刻校正仪{/color}”已更新{/b}") size 35 font "Huayuan.Gothic.Regular.ttf" color "#ffffff"
        text "{b}~{/b}" at delayed_blink(0.0, 1.0) size 35 font "Cubic-11-1.000-R-2.ttf" color "#ffffff"
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


## 通知界面 ########################################################################
##
## 通知界面用于向用户显示消息。（例如，当游戏快速保存或进行截屏时。）
##
## https://www.renpy.cn/doc/screen_special.html#notify-screen
screen notify(message):

    zorder 99
    add "gui/say.webp":
       ycenter 0.068
    hbox:
        spacing 1
        ycenter 0.068
        xpos 0.07
        text "{b}[message!tq]{/b}" size 35 font "Huayuan.Gothic.Regular.ttf" color "#ffffff"
    timer 2.5 action Hide('notify',transition=dissolve)


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
    use say_option
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


