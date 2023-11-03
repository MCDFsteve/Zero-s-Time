screen tips_option:
    if main_menu:
        key "pad_b_press" action ShowMenu("menu")
    if not main_menu:
        key "pad_b_press" action Return()
screen Tips():

    tag menu
    modal True
    add "gui/tips.webp"
    add "gui/nvl.webp"
    use tips_option
    add "gui/ui_white.webp":
        ycenter 0.97
        xpos 0.01
        xzoom 1.21
    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        add "ui_page"
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
    hbox:
        xpos 0.18
        ypos 0.93
        spacing 15
        imagebutton idle "ui_page1_on" hover "ui_page1_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips")
        imagebutton idle "ui_page2" hover "ui_page2_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips2")
        imagebutton idle "ui_page3" hover "ui_page3_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips3")
        imagebutton idle "ui_page4" hover "ui_page4_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips4")
        imagebutton idle "ui_page5" hover "ui_page5_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips5")
        imagebutton idle "ui_page6" hover "ui_page6_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips6")
        imagebutton idle "ui_page7" hover "ui_page7_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips7")
        imagebutton idle "ui_page8" hover "ui_page8_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips8")
        imagebutton idle "ui_page9" hover "ui_page9_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips9")
        imagebutton idle "ui_page10" hover "ui_page10_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips10")
    if main_menu:
          
          key "game_menu" action ShowMenu("menu")
          key "pad_b_press" action ShowMenu("menu")
    if not main_menu:
          
          key "game_menu" action Return()
          key "pad_b_press" action Return() #设置右键返回，方便使用
    vbox:
        xpos 0.05
        ypos 0.04
        spacing 0
        if persistent.tips01:
          textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}pbb{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips01")
        else:
          textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips02:
          textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}本子{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips02")
        else:
          textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips03:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}d站{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips03")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips04:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}鬼畜{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips04")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips05:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}cq{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips05")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips06:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}番剧{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips06")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips07:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}NPC{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips07")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips08:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}地球online{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips08")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips09:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}家里蹲{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips09")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips10:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}油陷{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips10")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips11:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}希望之草{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips11")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips12:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}现充{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips12")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips13:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}战场原白仪{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips13")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    add "gui/tips_menu.webp"
        
screen Tips2():

    tag menu
    modal True
    add "gui/tips.webp"
    add "gui/nvl.webp"
    use tips_option

    add "gui/ui_white.webp":
        ycenter 0.97
        xpos 0.01
        xzoom 1.21
    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        add "ui_page"
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
    hbox:
        xpos 0.18
        ypos 0.93
        spacing 15
        imagebutton idle "ui_page1" hover "ui_page1_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips")
        imagebutton idle "ui_page2_on" hover "ui_page2_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips2")
        imagebutton idle "ui_page3" hover "ui_page3_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips3")
        imagebutton idle "ui_page4" hover "ui_page4_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips4")
        imagebutton idle "ui_page5" hover "ui_page5_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips5")
        imagebutton idle "ui_page6" hover "ui_page6_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips6")
        imagebutton idle "ui_page7" hover "ui_page7_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips7")
        imagebutton idle "ui_page8" hover "ui_page8_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips8")
        imagebutton idle "ui_page9" hover "ui_page9_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips9")
        imagebutton idle "ui_page10" hover "ui_page10_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips10")
    if main_menu:
          
          key "game_menu" action ShowMenu("menu")
          key "pad_b_press" action ShowMenu("menu")
    if not main_menu:
          
          key "game_menu" action Return()
          key "pad_b_press" action Return() #设置右键返回，方便使用
    vbox:
        xpos 0.05
        ypos 0.04
        spacing 0
        if persistent.tips14:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}斧乃木正弦{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips14")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips15:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}故事系列{/font}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips15")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips16:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}厨{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips16")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips17:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}这是禁止事项{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips17")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips18:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}•福杰{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips18")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips19:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}社牛{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips19")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips20:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}再上映{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips20")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips21:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}二次元{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips21")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips22:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}中二{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips22")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips23:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}也儿夕传说{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips23")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips24:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}也儿夕传说:旷野之炊{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips24")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips25:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}林库{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips25")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips26:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}抖乐{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips26")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    add "gui/tips_menu.webp"
screen Tips3():

    tag menu
    modal True
    add "gui/tips.webp"
    add "gui/nvl.webp"
    use tips_option

    add "gui/ui_white.webp":
        ycenter 0.97
        xpos 0.01
        xzoom 1.21
    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        add "ui_page"
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
    hbox:
        xpos 0.18
        ypos 0.93
        spacing 15
        imagebutton idle "ui_page1" hover "ui_page1_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips")
        imagebutton idle "ui_page2" hover "ui_page2_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips2")
        imagebutton idle "ui_page3_on" hover "ui_page3_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips3")
        imagebutton idle "ui_page4" hover "ui_page4_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips4")
        imagebutton idle "ui_page5" hover "ui_page5_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips5")
        imagebutton idle "ui_page6" hover "ui_page6_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips6")
        imagebutton idle "ui_page7" hover "ui_page7_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips7")
        imagebutton idle "ui_page8" hover "ui_page8_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips8")
        imagebutton idle "ui_page9" hover "ui_page9_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips9")
        imagebutton idle "ui_page10" hover "ui_page10_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips10")
    if main_menu:
          
          key "game_menu" action ShowMenu("menu")
          key "pad_b_press" action ShowMenu("menu")
    if not main_menu:
          
          key "game_menu" action Return()
          key "pad_b_press" action Return() #设置右键返回，方便使用
    vbox:
        xpos 0.05
        ypos 0.04
        spacing 0
        if persistent.tips27:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}腹黑{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips27")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips28:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}宝可魔{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips28")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips29:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}任地堂{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips29")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips30:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}witch{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips30")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips31:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}泥可泥丝{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips31")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips32:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}蒸汽朋克：边缘行者{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips32")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips33:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}AADR{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips33")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips34:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}ChieAnime{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips34")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips35:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}漫展{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips35")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips36:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}cosplay{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips36")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips37:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}coser{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips37")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips38:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}低德地图{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips38")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips39:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}高塔{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips39")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    add "gui/tips_menu.webp"
screen Tips4():

    tag menu
    modal True
    add "gui/tips.webp"
    add "gui/nvl.webp"
    use tips_option

    add "gui/ui_white.webp":
        ycenter 0.97
        xpos 0.01
        xzoom 1.21
    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        add "ui_page"
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
    hbox:
        xpos 0.18
        ypos 0.93
        spacing 15
        imagebutton idle "ui_page1" hover "ui_page1_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips")
        imagebutton idle "ui_page2" hover "ui_page2_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips2")
        imagebutton idle "ui_page3" hover "ui_page3_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips3")
        imagebutton idle "ui_page4_on" hover "ui_page4_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips4")
        imagebutton idle "ui_page5" hover "ui_page5_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips5")
        imagebutton idle "ui_page6" hover "ui_page6_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips6")
        imagebutton idle "ui_page7" hover "ui_page7_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips7")
        imagebutton idle "ui_page8" hover "ui_page8_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips8")
        imagebutton idle "ui_page9" hover "ui_page9_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips9")
        imagebutton idle "ui_page10" hover "ui_page10_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips10")
    if main_menu:
          
          key "game_menu" action ShowMenu("menu")
          key "pad_b_press" action ShowMenu("menu")
    if not main_menu:
          
          key "game_menu" action Return()
          key "pad_b_press" action Return() #设置右键返回，方便使用
    vbox:
        xpos 0.05
        ypos 0.04
        spacing 0
        if persistent.tips40:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}颜文字{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips40")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips41:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}神庙{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips41")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips42:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}撒旦的结合{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips42")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips43:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}堂屋{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips43")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips44:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}橘外人{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips44")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips45:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}零子{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips45")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips46:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}皮带炖肉{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips46")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips47:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}海马体{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips47")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips48:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}时间悖论{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips48")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips49:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}时间刻校正仪{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips49")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips51:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}影子{/font}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips51")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips52:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}端锅{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips52")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips50:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}死亡回归{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips50")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    add "gui/tips_menu.webp"
screen Tips5():

    tag menu
    modal True
    add "gui/tips.webp"
    add "gui/nvl.webp"
    use tips_option

    add "gui/ui_white.webp":
        ycenter 0.97
        xpos 0.01
        xzoom 1.21
    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        add "ui_page"
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
    hbox:
        xpos 0.18
        ypos 0.93
        spacing 15
        imagebutton idle "ui_page1" hover "ui_page1_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips")
        imagebutton idle "ui_page2" hover "ui_page2_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips2")
        imagebutton idle "ui_page3" hover "ui_page3_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips3")
        imagebutton idle "ui_page4" hover "ui_page4_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips4")
        imagebutton idle "ui_page5_on" hover "ui_page5_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips5")
        imagebutton idle "ui_page6" hover "ui_page6_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips6")
        imagebutton idle "ui_page7" hover "ui_page7_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips7")
        imagebutton idle "ui_page8" hover "ui_page8_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips8")
        imagebutton idle "ui_page9" hover "ui_page9_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips9")
        imagebutton idle "ui_page10" hover "ui_page10_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips10")
    if main_menu:
          
          key "game_menu" action ShowMenu("menu")
          key "pad_b_press" action ShowMenu("menu")
    if not main_menu:
          
          key "game_menu" action Return()
          key "pad_b_press" action Return() #设置右键返回，方便使用
    vbox:
        xpos 0.05
        ypos 0.04
        spacing 0
        if persistent.tips53:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}原子匹配分布表{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips53")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips54:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}蓝图{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips54")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips55:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}黑化{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips55")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips56:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}沙皇{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips56")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips57:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}原地tp{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips57")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips58:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}时间刻{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips58")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips59:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}鸡嘴火龙{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips59")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips60:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}鸡嘴火兽{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips60")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips61:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}抖M{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips61")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips62:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}平行宇宙{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips62")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips63:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}电话电磁炉{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips63")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips64:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}斯坦因之窗{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips64")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips65:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}蝴蝶效应{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips65")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    add "gui/tips_menu.webp"
screen Tips6():

    tag menu
    modal True
    add "gui/tips.webp"
    add "gui/nvl.webp"
    use tips_option

    add "gui/ui_white.webp":
        ycenter 0.97
        xpos 0.01
        xzoom 1.21
    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        add "ui_page"
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
    hbox:
        xpos 0.18
        ypos 0.93
        spacing 15
        imagebutton idle "ui_page1" hover "ui_page1_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips")
        imagebutton idle "ui_page2" hover "ui_page2_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips2")
        imagebutton idle "ui_page3" hover "ui_page3_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips3")
        imagebutton idle "ui_page4" hover "ui_page4_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips4")
        imagebutton idle "ui_page5" hover "ui_page5_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips5")
        imagebutton idle "ui_page6_on" hover "ui_page6_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips6")
        imagebutton idle "ui_page7" hover "ui_page7_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips7")
        imagebutton idle "ui_page8" hover "ui_page8_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips8")
        imagebutton idle "ui_page9" hover "ui_page9_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips9")
        imagebutton idle "ui_page10" hover "ui_page10_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips10")
    if main_menu:
          
          key "game_menu" action ShowMenu("menu")
          key "pad_b_press" action ShowMenu("menu")
    if not main_menu:
          
          key "game_menu" action Return()
          key "pad_b_press" action Return() #设置右键返回，方便使用
    vbox:
        xpos 0.05
        ypos 0.04
        spacing 0
        if persistent.tips66:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}宕机{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips66")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips67:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}零之石{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips67")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips68:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}NC{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips68")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips69:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}上界传送门{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips69")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips70:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}未地传送门{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips70")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips71:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}传送门方块{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips71")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips72:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}排异反应{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips72")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips73:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}共鸣{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips73")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips74:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}计划C{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips74")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips75:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}哈希值{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips75")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips76:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}忒修斯之船{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips76")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips77:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}肌肉记忆{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips77")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips78:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}正转裁判{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips78")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    add "gui/tips_menu.webp"
screen Tips7():

    tag menu
    modal True
    add "gui/tips.webp"
    add "gui/nvl.webp"
    use tips_option

    add "gui/ui_white.webp":
        ycenter 0.97
        xpos 0.01
        xzoom 1.21
    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        add "ui_page"
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
    hbox:
        xpos 0.18
        ypos 0.93
        spacing 15
        imagebutton idle "ui_page1" hover "ui_page1_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips")
        imagebutton idle "ui_page2" hover "ui_page2_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips2")
        imagebutton idle "ui_page3" hover "ui_page3_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips3")
        imagebutton idle "ui_page4" hover "ui_page4_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips4")
        imagebutton idle "ui_page5" hover "ui_page5_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips5")
        imagebutton idle "ui_page6" hover "ui_page6_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips6")
        imagebutton idle "ui_page7_on" hover "ui_page7_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips7")
        imagebutton idle "ui_page8" hover "ui_page8_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips8")
        imagebutton idle "ui_page9" hover "ui_page9_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips9")
        imagebutton idle "ui_page10" hover "ui_page10_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips10")
    if main_menu:
          
          key "game_menu" action ShowMenu("menu")
          key "pad_b_press" action ShowMenu("menu")
    if not main_menu:
          
          key "game_menu" action Return()
          key "pad_b_press" action Return() #设置右键返回，方便使用
    vbox:
        xpos 0.05
        ypos 0.04
        spacing 0
        if persistent.tips79:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}炮丸论破{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips79")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips80:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}名侦探柯北{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips80")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips81:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}复活笔记{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips81")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips82:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}火菓{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips82")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips83:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}人材{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips83")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips84:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}生理测量者{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips84")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips85:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}犯罪参数{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips85")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips86:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}百脑汇{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips86")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips87:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}麻将{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips87")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips88:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}苏打水{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips88")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips89:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}经典地图{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips89")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips90:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}西卡之石{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips90")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips91:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}世界线收束{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips91")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    add "gui/tips_menu.webp"
screen Tips8():

    tag menu
    modal True
    add "gui/tips.webp"
    add "gui/nvl.webp"
    use tips_option

    add "gui/ui_white.webp":
        ycenter 0.97
        xpos 0.01
        xzoom 1.21
    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        add "ui_page"
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
    hbox:
        xpos 0.18
        ypos 0.93
        spacing 15
        imagebutton idle "ui_page1" hover "ui_page1_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips")
        imagebutton idle "ui_page2" hover "ui_page2_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips2")
        imagebutton idle "ui_page3" hover "ui_page3_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips3")
        imagebutton idle "ui_page4" hover "ui_page4_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips4")
        imagebutton idle "ui_page5" hover "ui_page5_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips5")
        imagebutton idle "ui_page6" hover "ui_page6_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips6")
        imagebutton idle "ui_page7" hover "ui_page7_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips7")
        imagebutton idle "ui_page8_on" hover "ui_page8_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips8")
        imagebutton idle "ui_page9" hover "ui_page9_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips9")
        imagebutton idle "ui_page10" hover "ui_page10_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips10")
    if main_menu:
          
          key "game_menu" action ShowMenu("menu")
          key "pad_b_press" action ShowMenu("menu")
    if not main_menu:
          
          key "game_menu" action Return()
          key "pad_b_press" action Return() #设置右键返回，方便使用
    vbox:
        xpos 0.05
        ypos 0.04
        spacing 0
        if persistent.tips92:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}京西{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips92")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips93:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}球棍{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips93")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips94:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}蟋蟀鸣泣之时{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips94")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips95:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}橘子{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips95")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips96:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}驳倒{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips96")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips97:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}苗花诚{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips97")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips98:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}学级裁判{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips98")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips99:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}四大天王{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips99")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips100:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}二周目{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips100")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips101:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}联盟冠军{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips101")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips102:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}压岁钱{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips102")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips103:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}处理器{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips103")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips104:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}お可愛い子供{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips104")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    add "gui/tips_menu.webp"
screen Tips9():

    tag menu
    modal True
    add "gui/tips.webp"
    add "gui/nvl.webp"
    use tips_option

    add "gui/ui_white.webp":
        ycenter 0.97
        xpos 0.01
        xzoom 1.21
    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        add "ui_page"
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
    hbox:
        xpos 0.18
        ypos 0.93
        spacing 15
        imagebutton idle "ui_page1" hover "ui_page1_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips")
        imagebutton idle "ui_page2" hover "ui_page2_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips2")
        imagebutton idle "ui_page3" hover "ui_page3_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips3")
        imagebutton idle "ui_page4" hover "ui_page4_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips4")
        imagebutton idle "ui_page5" hover "ui_page5_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips5")
        imagebutton idle "ui_page6" hover "ui_page6_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips6")
        imagebutton idle "ui_page7" hover "ui_page7_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips7")
        imagebutton idle "ui_page8" hover "ui_page8_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips8")
        imagebutton idle "ui_page9_on" hover "ui_page9_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips9")
        imagebutton idle "ui_page10" hover "ui_page10_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips10")
    if main_menu:
          
          key "game_menu" action ShowMenu("menu")
          key "pad_b_press" action ShowMenu("menu")
    if not main_menu:
          
          key "game_menu" action Return()
          key "pad_b_press" action Return() #设置右键返回，方便使用
    vbox:
        xpos 0.05
        ypos 0.04
        spacing 0
        if persistent.tips105:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}服务器{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips105")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips106:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}恨蜜莉雅{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips106")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips107:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}二雷娜{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips107")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips108:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}倒霉星{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips108")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips109:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}amido{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips109")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips110:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}AI{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips110")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips111:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}出芽{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips111")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips112:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}衰变{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips112")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips113:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}客户端{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips113")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips114:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}原初时间刻{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips114")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips115:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}五分钟创世说{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips115")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips116:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}十四机兵防卫圈{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips116")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips117:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}DNA序列{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips117")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    add "gui/tips_menu.webp"
screen Tips10():

    tag menu
    modal True
    add "gui/tips.webp"
    add "gui/nvl.webp"
    use tips_option

    add "gui/ui_white.webp":
        ycenter 0.97
        xpos 0.01
        xzoom 1.21
    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        add "ui_page"
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
    hbox:
        xpos 0.18
        ypos 0.93
        spacing 15
        imagebutton idle "ui_page1" hover "ui_page1_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips")
        imagebutton idle "ui_page2" hover "ui_page2_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips2")
        imagebutton idle "ui_page3" hover "ui_page3_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips3")
        imagebutton idle "ui_page4" hover "ui_page4_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips4")
        imagebutton idle "ui_page5" hover "ui_page5_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips5")
        imagebutton idle "ui_page6" hover "ui_page6_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips6")
        imagebutton idle "ui_page7" hover "ui_page7_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips7")
        imagebutton idle "ui_page8" hover "ui_page8_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips8")
        imagebutton idle "ui_page9" hover "ui_page9_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips9")
        imagebutton idle "ui_page10_on" hover "ui_page10_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Tips10")
    if main_menu:
          
          key "game_menu" action ShowMenu("menu")
          key "pad_b_press" action ShowMenu("menu")
    if not main_menu:
          
          key "game_menu" action Return()
          key "pad_b_press" action Return() #设置右键返回，方便使用
    vbox:
        xpos 0.05
        ypos 0.04
        spacing 0
        if persistent.tips118:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}2012世界末日{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips118")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips119:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}沼泽人{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips119")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips120:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}数字生命{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips120")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips121:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}数字灵魂{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips121")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips122:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}蒸汽朋克1877{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips122")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips123:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}黄斑三郎{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips123")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips124:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}出芽{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips124")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips125:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}衰变{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips125")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips126:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}客户端{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips126")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips127:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}原初时间刻{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips127")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips128:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}五分钟创世说{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips128")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips129:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}十四机兵防卫圈{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips129")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips130:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}DNA序列{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips130")
        else:
            textbutton _("{size=50}{font=Huayuan.Gothic.Bold.ttf}？？？{/font}{/size}")   hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    add "gui/tips_menu.webp"
screen tips01:
    use Tips
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips')
    text _("{size=50}（架空）即拼波波，一款网上购物软件。因为往往能以便宜的价格买到商品，所以近些年逐渐流行起来。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips02:
    use Tips
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips')
    text _("{size=50}流行意思指同人漫画。也有课本或笔记本的简称叫这个。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips03:
    use Tips
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips')
    text _("{size=50}（架空）即Dilidili,一个弹幕视频网站。在青少年中很是流行，不仅可以用来看动漫，还能学习知识和技术。具有弹幕发送功能相较于其他流媒体网站相当于是特色了。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips04:
    use Tips
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips')
    text _("{size=50}主要是指将特定素材进行拼接，调音，p图等形式制作的无厘头搞笑视频。题材可以分为纯搞笑类，以及调音唱歌类。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips05:
    use Tips
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips')
    text _("{size=50}（架空）逊公司推出的一款基于互联网的即时通讯软件。支持一对一对话，以及添加群聊对话。其发布几十年内积累了数以亿计的用户，但是近些年活跃量却逐渐减少。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips06:
    use Tips
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips')
    text _("{size=50}主要是对日本动画的一种称谓。细分则可以分为表番和里番，表番又能细分出肉番。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips07:
    use Tips
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips')
    text _("{size=50}指非玩家控制的游戏角色。多在RPG游戏内起着引导玩家，或者给玩家布置任务的职责。或者扮演玩家的队友，陪玩家一起游玩游戏。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips08:
    use Tips
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips')
    text _("{size=50}虚构的游戏，其实是现实生活比喻成游戏的称呼。是一种网络调侃用语。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips09:
    use Tips
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips')
    text _("{size=50}即整天呆在家里的阿宅。不擅长出门和社交，却擅长各类高难度电子游戏，动画角色和剧情则娓娓道来是这类群体的主要特征之一。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips10:
    use Tips
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips')
    text _("{size=50}（架空）沁野市的特色美食之一。由面粉裹上土豆丝和葱油炸而成。吃起来先脆后软，很是享受。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips11:
    use Tips
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips')
    text _("{size=50}（架空）电视动画《机动战士矮达：铁血的奥利给》第二季的片尾曲的第一句歌词。因为该集过于生草而变成网络热梗。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips12:
    use Tips
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips')
    text _("{size=50}一般指那种，不接触ACG，在现实世界生活的很好的人，一般这种人都有对象，并且经常参加社交活动。他们很少看动画和玩二次元游戏，社交圈子很广大。基本可以算是二次元/阿宅的反义词了。多含贬义（从阿宅的口中说出时）。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips13:
    use Tips
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips')
    text _("{size=50}（架空）电视动画《故事系列》的登场角色。擅长挥舞各种文具，是典型的女强人形象。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips14:
    use Tips2
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips2')
    text _("{size=50}（架空）电视动画《故事系列》的登场角色。是尸体经过变化得到的，称为付丧神。不擅长表达自己的表情。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips15:
    use Tips2
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips2')
    text _("{size=50}（架空）STAEE制作的电视动画。讲述了平凡高中生捡到吸血鬼以后发生的故事。具有很浓厚的艺术风格，而且出了很多神曲。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips16:
    use Tips2
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips2')
    text _("{size=50}指对XX作品很热爱的人的一种称呼。互联网发展到现在，厨已经是粉丝的代名词了，但是厨仅能替代某作品的粉丝来使用，所谓作品多是游戏或者动画。某人或者某个公司则不能替代粉丝这个称呼。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips17:
    use Tips2
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips2')
    text _("{size=50}（架空）网络用语，出自电视动画《热宫春日的忧郁》中朝比奈十一九六的台词。想回避一些不想谈论或者是触碰到秘密的话题时可以使用。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips18:
    use Tips2
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips2')
    text _("{size=50}（架空）是电视动画《刺客过家家》中主角的姓氏。其中女主角的设定是拥有读心术超能力的小孩子。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips19:
    use Tips2
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips2')
    text _("{size=50}网络用语，全称为“社交牛逼症，这个称呼则又是由“社交恐惧症”衍生而来，用来形容那些很擅长与陌生人交流的人。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips20:
    use Tips2
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips2')
    text _("{size=50}（架空）电视动画《只有你不存在的街道》中男主角的能力，可以让时间逆转。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips21:
    use Tips2
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips2')
    text _("{size=50}原意是指只有两个维的次元，即只有平面，后延伸词义，变成了ACG宅文化的代名词。能玩到这个游戏的人应该很清楚这个词是什么意思吧。（笑）{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips22:
    use Tips2
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips2')
    text _("{size=50}形容经常幻想自己是什么大人物，或者具有某种超能力，未成年人动画看多了可能会这样。但是成年人中的动画受众群体也有存在。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips23:
    use Tips2
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips2')
    text _("{size=50}（架空）任地堂所开发的游戏系列，游戏的主要玩法是解密，剧情主要是救公主，启蒙了很多后来者游戏。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips24:
    use Tips2
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips2')
    text _("{size=50}（架空）也儿夕传说系列的第一部真正的开放世界游戏，玩家可以随心所欲地做自己想做的事情，该游戏获得了PNG2017年度游戏大奖。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips25:
    use Tips2
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips2')
    text _("{size=50}（架空）《也儿夕传说：旷野之炊》的玩家操控的角色的名字。林库可以直接传送到任意一个已解锁的神庙或者高塔上面。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips26:
    use Tips2
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips2')
    text _("{size=50}（架空）字节跑动公司推出的一款短视频软件。在全世界受到欢迎。很大程度上让中年老年人享受到了智能电子设备带来的便利。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips27:
    use Tips3
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips3')
    text _("{size=50}ACG萌属性之一，当然现实世界也广泛存在。多用来形容那些表面上讨好他人，彬彬有礼，实际上深谋远虑，打算利用他人对自己的好感，将他人作为自己想要实现的计划的一部分的一种性格。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips28:
    use Tips3
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips3')
    text _("{size=50}（架空）GameFurry开发的掌机游戏系列。主要玩法是抓怪和对战，在全世界有着极高的人气。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips29:
    use Tips3
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips3')
    text _("{size=50}（架空）世界知名的游戏开发公司，旗下代表作有《也儿夕传说》，《超级羊里奥》等。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips30:
    use Tips3
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips3')
    text _("{size=50}（架空）任地堂旗下与QS4,Xdox one同世代的游戏主机，具有掌机和主机两种形态。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips31:
    use Tips3
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips3')
    text _("{size=50}（架空）2022年七月原创新番。讲的是现代女忍者披着jk的外皮执行任务。结局令很多观众不满。但是人设和音乐都很棒，只能说是不过不失。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips32:
    use Tips3
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips3')
    text _("{size=50}（架空）改编自游戏《蒸汽朋克1877》的原创动画。出色的剧情和人物表现力收获了一片好评。甚至带动了原本一蹶不振的原作游戏销量大幅增加。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips33:
    use Tips3
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips3')
    text _("{size=50}（架空）全称America Atom's Digitization Research organization。美国原子数据化研究组织。主要研究方向是原子的数据化转换，传输和还原。在全球多个国家设有分部。有超过两千多位登记在册的科学家。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips34:
    use Tips3
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips3')
    text _("{size=50}（架空）沁野市最大的动漫展出，活动主要包括cosplay，网络游戏对战以及售卖动漫周边和同人志等。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips35:
    use Tips3
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips3')
    text _("{size=50}指ACG文化相关的展会，按照内容不同，漫展也可以被分为不同的种类，比如同人展、博览会等。对于部分御宅族，尤其是较缺乏实体ACG资源的地区来说是重要的ACG活动。漫展的举办地点一般是当地的会展中心、宾馆或大学校园，取决于会展的性质、规模及主办方。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips36:
    use Tips3
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips3')
    text _("{size=50}一种扮演虚构角色的表演艺术，是ACG领域的一种重要文化活动。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips37:
    use Tips3
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips3')
    text _("{size=50}对进行cosplay的人的称呼。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips38:
    use Tips3
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips3')
    text _("{size=50}（架空）一款国产地图导航软件。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips39:
    use Tips3
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips3')
    text _("{size=50}（架空）《也儿夕传说：旷野之炊》中的一种建筑，玩家需要爬上该建筑并与之互动才能解锁所在地区的地图信息，相关的术语有“爬塔开图”。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips40:
    use Tips4
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips4')
    text _("{size=50}指网络上用标点符号组成的表示自己喜怒哀乐的抽象表情。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips41:
    use Tips4
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips4')
    text _("{size=50}（架空）《也儿夕传说：旷野之炊》里遍布全地图的一类建筑，内部往往是各种解密，到达终点以后可以获得用于提高血量和体力上限的奖励。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips42:
    use Tips4
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips4')
    text _("{size=50}（架空）一款肉鸽（高难度，低画面表现的一类游戏的称呼，主要特色有难度很高，随机的地图和道具，死后重新开始等）游戏。玩家需要扮演“撒旦”在各个房间探索和打怪。高度的随机性和丰富的道具种类使得其非常耐玩。被玩家奉为“肉鸽之神”。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips43:
    use Tips4
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips4')
    text _("{size=50}（架空）“客厅”在沁野市方言中的称呼。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips44:
    use Tips4
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips4')
    text _("{size=50}（架空）“橘”出自知名百合番《柑橘味香水》。用来调侃ACG女角色之间的亲密关系已经接近恋爱的程度了，可谓“大橘已定”，冒出个男的来则称为“橘外人”。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips45:
    use Tips4
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips4')
    text _("{size=50}（架空）一种未被以前的科学家发现的，一种新的物质形态。物理性质介于有质量的由原子构成的物体和电子之间，由原子转换而来，也能转换回原子，可以像电子一样被光速传输和被电子设备接收。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips46:
    use Tips4
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips4')
    text _("{size=50}即被打，用皮带抽那种。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips47:
    use Tips4
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips4')
    text _("{size=50}大脑中负责存储记忆的一块区域，因其结构长得像海马而得名。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips48:
    use Tips4
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips4')
    text _("{size=50}最早在科幻小说中出现，指时间穿越者回到过去以后对未来造成的种种悖论。例如典型的祖父悖论：我回到过去杀死我的祖父，因为我的祖父死了，那就不会有我，那我就不可能回到过去杀死我的祖父。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips49:
    use Tips4
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips4')
    if persistent.time == 0:
        text _("{size=50}（架空）由叶梓澄之父开发出的跟零子有关的科学仪器。{/size}") xpos 0.35 ypos 0.05 xsize 1160
    elif persistent.time == 1:
        text _("{size=50}（架空）由叶梓澄之父开发出的跟零子有关的科学仪器。具有危险性，可以向+1维度注入零子。{/size}") xpos 0.35 ypos 0.05 xsize 1160
    elif persistent.time == 2:
        text _("{size=50}（架空）由叶梓澄之父开发出的跟零子有关的科学仪器。可以将零子注入更高维度。{/size}") xpos 0.35 ypos 0.05 xsize 1160
    elif persistent.time == 3:
        text _("{size=50}（架空）由叶梓澄之父开发出的跟零子有关的科学仪器。具有危险性，可以向+1维度注入零子以及从+1维度抽出零子到人类所处的0维度，是+1维度和0维度之间进行数据交换的桥梁。{/size}") xpos 0.35 ypos 0.05 xsize 1160
    elif persistent.time == 4:
        text _("{size=50}（架空）由叶梓澄之父开发出的跟零子有关的科学仪器。具有危险性，可以向+1维度注入零子以及从+1维度抽出零子到人类所处的0维度，是+1维度和0维度之间进行数据交换的桥梁。抽出和注入均会导致+1时间刻维度对0时间刻维度产生干涉。抽出之前注入的零子可终止干涉。{/size}") xpos 0.35 ypos 0.05 xsize 1160
    elif persistent.time == 5:
        text _("{size=50}（架空）由叶梓澄之父开发出的跟零子有关的科学仪器。具有危险性，可以向+1维度注入零子以及从+1维度抽出零子到人类所处的0维度，是+1维度和0维度之间进行数据交换的桥梁。抽出和注入均会导致+1时间刻维度对0时间刻维度产生干涉。抽出之前注入的零子可终止干涉。本体是一个电路板上带着零之石以及负责注入和抽出的通道，和一个观测注入抽出值的显示数字的表盘。{/size}") xpos 0.35 ypos 0.05 xsize 1160
    else:
        text _("{size=50}（架空）由叶梓澄之父开发出的跟零子有关的科学仪器。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips50:
    use Tips4
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips4')
    text _("{size=50}（架空）电视动画《Re:从一开始的异世界生活》中男主角的能力，死亡以后会回到死之前的一段时间。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips51:
    use Tips4
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips4')
    text _("{size=50}（架空）电视动画《秋日重现》中的反派，男主角由于无意识之中获得了影子中蛭子神的右眼，获得了死后回到过去的能力。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips52:
    use Tips4
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips4')
    text _("{size=50}（架空）电视剧《端锅》中一个反派，企图在锅里装上炸弹拉整公交车人陪葬。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips53:
    use Tips5
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips5')
    text _("{size=50}（架空）通过仪器将物质再构成为零子的时候用于记录再构成前物质的原子排布信息的，不属于物质本身所再构成的，外来的一部分零子，在零子还原为物质的过程中起着关键作用。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips54:
    use Tips5
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips5')
    text _("{size=50}原指建筑或工程项目的设计图纸，用于指导建设和执行。后延伸含义为一项计划或行动的详细方案和策略。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips55:
    use Tips5
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips5')
    text _("{size=50}网络用语，形容自己（或他人）的内心已经堕落或者性格已经发生坏方向的转变，十分中二的词汇。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips56:
    use Tips5
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips5')
    text _("{size=50}（架空）《蟋蟀鸣泣之时》中的角色“南条沙都子”的网络绰号。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips57:
    use Tips5
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips5')
    text _("{size=50}网络用语，源自电子游戏中的传送（TP）功能，原地TP即从原地传送到原地，可以形容做无用功以及说废话。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips58:
    use Tips5
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips5')
    text _("{size=50}（架空）给各个维度以编号命名进行区分的量词。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips59:
    use Tips5
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips5')
    text _("{size=50}（架空）《宝可魔》中的一只精灵，属性是火，需要通过携带熔炉，通讯交换的方式由鸡嘴火兽进化而来。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips60:
    use Tips5
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips5')
    text _("{size=50}（架空）《宝可魔》中的一只精灵，属性是火，可以通过携带熔炉，通讯交换的方式进化为鸡嘴火龙。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips61:
    use Tips5
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips5')
    text _("{size=50}即受虐狂，越是被虐就越兴奋，似乎是精神疾病的一种，也似乎是萌点的一种。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips62:
    use Tips5
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips5')
    text _("{size=50}学术上的概念，认为在除了我们所处的宇宙之外，存在许多相似但不一样的其他宇宙。此概念经常用于文学创作中。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips63:
    use Tips5
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips5')
    text _("{size=50}（架空）《斯坦因之窗（Steins;Window)》中的虚构道具，机能是将短信发送到过去。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips64:
    use Tips5
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips5')
    text _("{size=50}（架空）一款视觉小说游戏，并有同名改编动画。讲述了天才疯狂科学家发明时间机器之后的一系列事件。该作凭借其出色的剧情和设定，在各大评分网站都是排行靠前的常客。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips65:
    use Tips5
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips5')
    text _("{size=50}指一个小小的事件可能会在远处引发一连串的连锁反应，导致一个巨大的影响。这就是著名的“蝴蝶扇动翅膀在巴西，引起美国的龙卷风”的现象，意思是微小的变化可以在复杂系统中引起巨大的影响。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips66:
    use Tips6
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips6')
    text _("{size=50}指的是计算机或其他电子设备因故障或其他原因无法正常运行或访问的状态。它意味着设备无法正常工作或提供服务，通常需要修复或恢复才能重新运行。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips67:
    use Tips6
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips6')
    text _("{size=50}（架空）是制造时间机器和时间刻校正仪的核心部件,来源和形成原因是个谜。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips68:
    use Tips6
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips6')
    text _("{size=50}（架空）即《NINECRAFT》，中文名字叫《九的世界》，是由端点的OJANG工作室开发的一款沙盒游戏，凭借着其超高的自由度在全世界很受欢迎，甚至能够被用来从事教育。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips69:
    use Tips6
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips6')
    text _("{size=50}（架空）《NINECRAFT》中存在的一种结构，用于将玩家传送到游戏中的“上界”维度。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips70:
    use Tips6
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips6')
    text _("{size=50}（架空）《NINECRAFT》中存在的一种结构，用于将玩家传送到游戏中的“未地”维度。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips71:
    use Tips6
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips6')
    text _("{size=50}（架空）《NINECRAFT》中激活上界传送门或者未地传送门以后框架中出现的方块，是传送门的核心，起着传送玩家的作用。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips72:
    use Tips6
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips6')
    text _("{size=50}指身体对于外来物质（如异体组织、器官、细胞、药物等）产生的不适应或抗拒反应。这种反应通常由免疫系统引起，导致身体对外来物质进行攻击和破坏。排异反应可能会导致各种不同的症状和疾病，包括过敏反应、器官移植失败等。。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips73:
    use Tips6
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips6')
    text _("{size=50}指的是物理学中的一类现象，即当一个物体受到另一个振动体的激励时，如果其固有频率与振动体相同或者相近，那么它会以比外力更大的振幅进行振动。这种现象也被称为共振。共振在物理、工程、音乐等领域都有广泛的应用。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips74:
    use Tips6
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips6')
    text _("{size=50}指迫不得已的最终手段，往往带有对自身的反噬的负面影响。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips75:
    use Tips6
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips6')
    text _("{size=50}是指将任意长度的数据通过哈希函数（也称摘要算法）变换成固定长度的唯一值（通常是一个字符串），用于数据的唯一标识和加密。哈希值在密码学、数据存储等领域都有广泛的应用。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips76:
    use Tips6
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips6')
    text _("{size=50}是一个哲学上著名的悖论，指的是一艘船，它的所有部件都被逐一更换，直至没有一件部件是最初的那艘船的部件，那么这艘船是否还是原来的那艘船，这个问题引出了“同一性问题”的思考。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips77:
    use Tips6
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips6')
    text _("{size=50}是一种非言语的学习和记忆过程，指的是通过长时间的练习和重复，让身体的肌肉习惯于执行特定的动作或技能。当一个人多次练习某个动作时，他们的肌肉会逐渐适应这个动作，从而使动作变得更加自然和准确。这种现象在学习各种技能，如打字、骑自行车、弹钢琴等方面都有体现。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips78:
    use Tips6
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips6')
    text _("{size=50}（架空）是一款经典的视觉小说类冒险推理游戏。游戏以法庭为背景，玩家扮演一名年轻律师成步堂龙二，需要在法庭上为被告辩护，揭示真相。游戏分为两个部分：调查和庭审。在调查阶段，玩家搜集证据和线索；在庭审阶段，玩家通过驳斥对方证词、展示证据等方式击败对手，成功为自己的客户辩护。整个游戏充满悬念，剧情紧凑，玩家需要运用智慧和观察力来解决各种案件，为正义而战。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips79:
    use Tips7
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips7')
    text _("{size=50}（架空）是一款经典的视觉小说类冒险推理游戏。游戏故事发生在被称为希望之花学园的精英高中，玩家扮演一名被选中的学生。在学园中，一位名为黑白猫的神秘人物设置了一个残酷的游戏：学生们必须互相杀戮，只有成功杀人并在学园审判中逃过一劫的人才能离开学园。玩家需要与其他学生互动、收集线索，然后在审判中揭示凶手，才能让自己和其他无辜的学生活下来。游戏结合了侦探推理、互动剧情和法庭辩论等元素，以独特的画风、悬疑的剧情和丰富的角色塑造吸引了大量玩家。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips80:
    use Tips7
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips7')
    text _("{size=50}（架空）是一部著名的漫画作品。有动画、电影等多种改编。故事讲述了一个天才高中侦探工藤新二，在调查一个神秘组织时被追踪并被迫服下毒药，结果变成了小学生的身体。为了找寻解药，新二化名为江户川柯北，暂住在青梅竹马的女友甩利兰家中，并协助兰的父亲——著名侦探甩利小五郎破解各种棘手的案件。在解决案件的过程中，柯北不仅要揭示真相，还要小心隐藏自己的身份，同时继续追查那个神秘组织。该作以其独特的侦探推理、精彩的剧情和丰富的角色塑造受到了广泛喜爱，不仅吸引了许多漫画迷，也成为了推理类作品的经典之一。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips81:
    use Tips7
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips7')
    text _("{size=50}（架空）是一部著名的漫画作品。这部作品凭借其独特的故事背景和精彩的剧情，成为了现象级的漫画，还被改编成了动画、电影、电视剧等多种形式。故事讲述了一名高中生夜神日无意中捡到了一个名为“复活笔记”的神秘本子。这个本子上写着一个规则：写上某人的名字，那个人就会复活。出于对现实世界犯罪的不满，夜神日决定利用复活笔记来惩罚罪犯，建立一个没有犯罪的乌托邦。然而，他的行为引起了警方的注意，天才侦探M开始追踪夜神日，展开了一场智力角逐。该作以其独特的悬疑剧情、复杂的角色关系和紧张的心理战受到了广泛喜爱，成为了悬疑推理漫画的经典之作。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips82:
    use Tips7
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips7')
    text _("{size=50}（架空）是一部轻小说系列的首卷标题，同时也是其改编动画的标题。故事主要围绕着文学部的四名高中生展开，其中包括天才但懒散的折棍奉太郎，好奇心旺盛的万反田爱瑠，以及他们的朋友伊原摩耶草和福部外志。在万反田爱瑠的怂恿下，折棍奉太郎和其他成员一起解决了许多学校和日常生活中的小谜团和悬疑事件。改作以其轻松的推理故事、生动的角色描绘和优美的画风受到了许多读者和观众的喜爱，成为了轻小说和青春推理作品的佳作。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips83:
    use Tips7
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips7')
    text _("{size=50}（架空）回合制游戏《少娜少娜！一起来干好事吧！》中的词汇。对主角所在单位从业人员的叫法。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips84:
    use Tips7
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips7')
    text _("{size=50}（架空）是一部原创TV科幻悬疑动画作品，这部作品以其独特的故事背景、深刻的主题和紧张的剧情受到了广泛关注和喜爱。故事发生在一个未来的日本，社会治安维持在一个名为“生理测量系统”的系统下。这个系统通过分析人们的生理状态，预测他们可能犯下的罪行，并进行干预。主角常守紫是一名刚刚加入公安局刑事课的新警察，她和其他执行官、侦查官一起维护社会秩序，解决各种罪案。在这个过程中，她不仅要面对复杂的案件，还要深入思考这个系统的合理性和人性的本质。该作以其独特的设定、引人深思的主题和精彩的剧情成为了科幻悬疑动画的经典之作。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips85:
    use Tips7
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips7')
    text _("{size=50}（架空）《生理测量者》中的一个指数，是对人们生理状态的测量以预估其是否会发生犯罪的指数。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips86:
    use Tips7
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips7')
    text _("{size=50}（架空）《生理测量者》中测量犯罪参数的核心系统是由几百个人脑组成。被戏称为“百脑汇”。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips87:
    use Tips7
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips7')
    text _("{size=50}是一种源自中国的策略性棋牌游戏，通常需要四个玩家参与。游戏由144块或更多的瓷片或卡片（即麻将牌）组成，这些牌上印有不同的符号和图案,如“圈子”（饼）、“索子”（条）、“万子”、东南西北风、中发白等。游戏的目标是通过抓牌、出牌、吃、碰、杠等操作，最终获得特定组合（通常是4个组合和1对，也就是所谓的“胡牌”）的牌型。每种特定的牌型都有相应的分数，不同的地方和文化可能有不同的规则和得分系统。麻将不仅需要运气，也需要策略和技巧，包括记忆、预测和风险管理等能力。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips88:
    use Tips7
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips7')
    text _("{size=50}是一种无色、无味的碳酸气泡饮料。它由水和二氧化碳（CO2）混合而成，通常不含糖、香料或其他添加剂。苏打水口感清爽，具有微弱的酸味，常作为解渴饮料或混合饮料的基底。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips89:
    use Tips7
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips7')
    text _("{size=50}指在竞技类网游里，出的最早的或者使用次数最多的游戏地图。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips90:
    use Tips7
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips7')
    text _("{size=50}（架空）《也儿夕传说：旷野之炊》中的重要道具，给玩家提供拍照，技能，地图和任务指引等诸多功能，其外形酷似任地堂的主机MiiU。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips91:
    use Tips7
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips7')
    text _("{size=50}一个常在科幻作品中出现的概念，原则上，它涉及到平行宇宙或多元宇宙的理论。这个概念通常用于描述在无数可能的时间线或“世界线”中，无论我们做出什么选择或进行何种干预，最终的结果总是会收束回到某一特定的状态或事件。换句话说，它是一种无论你如何尝试改变历史，最终的结果总是无法避免的设定。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips92:
    use Tips8
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips8')
    text _("{size=50}（架空）一款网上购物软件。商品价格相对而言一般都更贵，但是自营类商品往往送的很快。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips93:
    use Tips8
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips8')
    text _("{size=50}（架空）《蟋蟀鸣泣之时》中男主角所使用的武器。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips94:
    use Tips8
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips8')
    text _("{size=50}（架空）由蛇骑士08所创作的视觉小说游戏，带有恐怖和悬疑色彩。已被改编成漫画，动画，手游等多种载体。和《西方》，《日姬》并称为同人三大奇迹。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips95:
    use Tips8
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips8')
    text _("{size=50}即“局子”，对警察局的称谓。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips96:
    use Tips8
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips8')
    text _("{size=50}（架空）《炮丸论破》系列游戏中，玩家在法庭上所使用的技能之一，作用是用证据反驳对方的证词。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips97:
    use Tips8
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips8')
    text _("{size=50}（架空）《炮丸论破》系列首作中男主角，即玩家扮演角色的名字。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips98:
    use Tips8
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips8')
    text _("{size=50}（架空）《炮丸论破》系列中出现被害者以后进行的类似法庭一样的玩法，玩家需要用获得的证据驳倒其他人的证言，同时在其他人和自己的思考下推断出真正的凶手。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips99:
    use Tips8
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips8')
    text _("{size=50}（架空）《宝可魔》系列正作中，大多数情况下剧情后期玩家需要挑战宝可魔联盟，四大天王就是宝可魔联盟的主要组成部分，由四个不同属性的顶级训练家组成。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips100:
    use Tips8
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips8')
    text _("{size=50}（架空）在不同游戏中的意思不太一样。对《宝可魔》来说，二周目往往是指打败联盟冠军，看完制作人员名单以后的新剧情和玩法。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips101:
    use Tips8
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips8')
    text _("{size=50}（架空）《宝可魔》系列中玩家一周目的最终目标，成为联盟冠军意味着成为了所在地区受宝可魔联盟认证的最强宝可魔训练师。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips102:
    use Tips8
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips8')
    text _("{size=50}是中国传统习俗中的一种礼金。它通常在农历新年期间给予未婚的子女或年幼的亲戚朋友。压岁钱的目的是祝福和鼓励接受礼物的人，在新的一年里平安、幸福和顺利。压岁钱通常以红包的形式给出，里面装有一定金额的钱。这被认为是对新年的祝福和好运的象征，同时也是传统习俗中尊重长辈、传递爱心的方式之一。接受压岁钱的人会感到开心和受到关爱，而赠送压岁钱的人则表达了对亲人、朋友和年轻一代的关心和祝福。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips103:
    use Tips8
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips8')
    text _("{size=50}是计算机中的核心组件之一，也被称为中央处理器（CPU）。它是一种电子芯片，负责执行计算机程序中的指令和处理数据。处理器可以看作是计算机的大脑，它控制和协调计算机的各个部件的工作。处理器通过时钟信号按照指令的顺序逐步执行，并执行诸如算术运算、逻辑操作、数据传输等操作。处理器的性能通常由其时钟频率、核心数、缓存等指标来衡量，较高的性能意味着它能够更快地执行任务。处理器的种类很多，如x86架构、ARM架构等，不同的处理器适用于不同类型的计算机和设备。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips104:
    use Tips8
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips8')
    text _("{size=50}（架空）即“可爱的孩子/真是可爱呢”。TV动画《辉日大小姐想让我告白~天才们的恋爱头脑战》中女主角五宫辉日的名台词。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips105:
    use Tips9
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips9')
    text _("{size=50}是一种专门用来存储、处理和提供数据和服务的高性能计算机。它在网络中扮演着重要的角色，用于承载网站、应用程序、文件和其他网络资源。服务器能够接收来自客户端的请求，并根据请求提供相应的数据或服务。它通常具有强大的处理能力、大容量的存储空间和稳定的网络连接，以满足大量用户的需求。服务器可以是物理设备，也可以是虚拟化的实体，常见的类型包括Web服务器、文件服务器、数据库服务器等。它们提供了互联网上各种各样的服务和资源。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips106:
    use Tips9
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips9')
    text _("{size=50}（架空）电视动画《Re:从一开始的异世界生活》中的女主角。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips107:
    use Tips9
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips9')
    text _("{size=50}（架空）电视动画《魔男之旅》中的女主角。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips108:
    use Tips9
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips9')
    text _("{size=50}（架空）一部经典的四格漫画，讲述了少女们的日常，被改编有TV动画载体。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips109:
    use Tips9
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips9')
    text _("{size=50}（架空）任地堂推出的一种互动玩具和游戏配件。以小型塑料人物或卡片的形式出现，每个代表了不同的角色或游戏。它们具有内置的射频识别芯片，可以通过与兼容的游戏主机或设备（Witch、Mii U和3BS）进行交互，以获得游戏内的道具。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips110:
    use Tips9
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips9')
    text _("{size=50}即人工智能，是一种计算机科学领域的技术。它使计算机系统能够模拟人类的智能行为和决策过程。AI通过学习、理解和执行任务，可以自动化任务、处理复杂的数据，并做出决策。它的应用范围广泛，包括语音识别、图像处理、自然语言处理等。AI是目前科技领域的重要发展方向之一。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips111:
    use Tips9
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips9')
    text _("{size=50}是指在水晶的表面或内部形成新的小水晶。当水晶处于适当的环境条件下，溶解的矿物质会重新结晶并沉积在现有的水晶上，形成一个小的、与原水晶相连的新晶体。这个过程类似于植物的出芽，因此被称为水晶的出芽。出芽使水晶的结构逐渐扩展，并形成更复杂的形态和纹理。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips112:
    use Tips9
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips9')
    text _("{size=50}是指原子核或粒子发生变化，转变为不同的原子核或粒子的过程。这种转变可以是自发的，也可以是受到外界的刺激而发生。衰变可能导致原子核的放射性衰变，释放出射线或粒子，同时伴随着能量的释放。这个过程会改变原子核的质量数和原子序数，从而使物质的性质和组成发生变化。物质的衰变是自然界中普遍存在的现象，也是核能和放射治疗等领域的重要基础。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips113:
    use Tips9
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips9')
    text _("{size=50}是指与服务器或主机进行通信的计算机或设备。它通常是指用户使用的设备，如个人电脑、手机、平板电脑等。在客户端-服务器模型中，客户端发送请求给服务器，并接收服务器返回的响应。客户端负责向用户提供界面和功能，使用户能够与服务器进行交互和访问网络服务。客户端通过网络连接到服务器，发送请求并接收数据，完成特定的任务或获取所需的信息。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips114:
    use Tips9
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips9')
    text _("{size=50}（架空）即在时间刻校正仪进行抽出零子操作导致世界发生改变之前的世界。标志性的事件有覃可汐在小学溺亡，以及不存在名为AADR的组织。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips115:
    use Tips9
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips9')
    text _("{size=50}是一个哲学假设，用来讨论时间和现实的概念。它认为我们所经历的一切，包括记忆和感知，都是在过去的五分钟内被创造出来的，而对于更长时间段的记忆只是虚假的。它挑战我们对时间和现实本质的理解，引发思考：我们如何知道过去的经历是真实的，而不是刚刚被创造出来的虚幻体验？它没有科学依据，更像是哲学思考，用来探索我们对世界的理解方式和意识、记忆如何构建现实体验。无论是否成立，它提醒我们审视现实和时间，并怀疑我们对世界的认知方式。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips116:
    use Tips9
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips9')
    text _("{size=50}（架空）是一款由Btlus开发的动作角色扮演游戏。游戏的故事发生在一个被机械生命体侵略的未来世界，玩家将扮演十四名驾驶着巨型机甲的少年少女，与敌人展开激烈的战斗。游戏的特色是可以随时切换不同的机甲和角色，以及拥有多种结局的分支剧情。游戏的剧情内容十分丰富，玩家赞不绝口，很多人直呼“希望失忆以后再玩一遍”。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips117:
    use Tips9
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips9')
    text _("{size=50}是指DNA分子中的一系列核苷酸的排列顺序。DNA（脱氧核糖核酸）是生物体内存储遗传信息的分子，它由四种不同的核苷酸单元组成，分别是腺嘌呤（A）、胞嘧啶（C）、鸟嘌呤（G）和胸腺嘧啶（T）。DNA序列描述了基因组中的基因和其他非编码区域的具体排列。基因是DNA序列的一部分，它们携带了生物体遗传信息的编码，决定了生物体的形态、功能和特征。通过分析DNA序列，科学家可以研究基因的功能、进化关系以及与疾病相关的变异。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips118:
    use Tips10
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips10')
    text _("{size=50}即“2012末日预言”或“2012末日事件”，是指一些人相信在2012年12月21日，根据古代玛雅文明的预测，世界将面临灾难性的事件，甚至可能是世界末日的到来。这个预言源自玛雅文明的长周期历法，即玛雅历的长计数周期。根据一种解释，该日历在2012年12月21日结束，导致一些人将其解释为世界将在那一天毁灭。然而，科学界对于这种预言的真实性持怀疑态度。许多科学家和学者认为，这只是对玛雅历法的误解和误解解读，而非真正意味着世界末日的发生。2012年12月21日来临后，并没有发生全球性的灾难或世界末日事件。这一预言被广泛视为一个谣言或误解，并在科学界和大众之间引发了许多讨论和争议。尽管2012年世界末日预言没有实现，但它提醒了人们对于预言和未来事件的怀疑态度，以及对科学证据和合理推理的重要性。同时，它也显示了人类对于末日和未知的永恒关注和好奇心。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips119:
    use Tips10
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips10')
    text _("{size=50}是一个哲学上的思想实验，用来探讨身份和意识的本质。它的基本情景是这样的：假设有一个人在沼泽里被闪电击中，同时沼泽里的分子组成了一个和他完全一样的复制品。这个复制品有着和原来的人一样的记忆、性格和行为，但是他不知道自己是一个复制品。那么，这个复制品是否就是原来的人？他是否有着和原来的人一样的意识和权利？这个问题涉及到了人类的本质、自我认同和道德责任等复杂的主题，也引发了不同的哲学观点和争论。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips120:
    use Tips10
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips10')
    text _("{size=50}是指将人的意识和思维过程转化为数字化的形式，然后将其上传到计算机或其他数字化系统中的过程。这意味着个体的思维、记忆和个性等信息被转换为计算机可处理的数据，并在计算机内部模拟和存储。将人的意识上传到计算机内，可以理解为将大脑中的信息通过技术手段转移到计算机中，使得个体的意识能够在计算机系统中继续存在和运行。这可能涉及扫描和复制大脑的结构和功能，并将其转化为算法和数据的形式。数字生命的概念涉及到深入理解和模拟人脑的复杂性和神经科学的原理，以及开发出高度先进的计算机系统和算法来处理和模拟这些信息。尽管这个领域仍然在发展中，并面临众多科学和伦理挑战，但数字生命的概念激发了人们对意识和人类认知的深刻思考。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips121:
    use Tips10
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips10')
    text _("{size=50}是一个涉及人类精神和技术交叉领域的概念。它描述了将人的内在意识和非物质性特质转化为数字化的形式或表达方式的想法。数字灵魂的概念基于假设，即人类的意识、思维、情感等非物质性属性可以被转化为数字化的信息和数据，并在计算机系统中模拟或复制。这意味着个体的思维过程、记忆、个性等可以被编码成算法和数据的形式，然后在数字系统中进行处理、存储和传输。然而，值得注意的是，数字灵魂是一个有争议的概念，缺乏确切的定义和科学共识。它在哲学、人工智能和认知科学等领域引发了广泛的讨论和思考。目前，实现数字灵魂的概念仍然面临许多科学、技术和伦理挑战，且距离实际可行性还存在很大的差距。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips122:
    use Tips10
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips10')
    text _("{size=50}（架空）是一款由CPDD开发的科幻冒险游戏。后被改编成动画。游戏背景设定在1877年的都市夜市——日之城，一个高度技术化的城市。在游戏中，玩家扮演一位名叫“W”的角色，一个雇佣冷血杀手。玩家将探索这个庞大的开放世界，与各种角色互动，并根据自己的选择和决策塑造游戏故事的走向。游戏的世界充满了科技与黑暗的冲突。人类改造自己的身体，融入了各种机械和生物改良，从而获得超能力和增强的能力。然而，科技的进步也带来了贫富分化和社会问题，政府和巨头公司之间的斗争不断升级。在游戏中，玩家可以选择各种任务和剧情线索，参与枪战、潜行、驾驶等各种动作和战斗。玩家还可以通过升级技能和收集装备来提升角色能力，并与其他角色建立关系。该游戏以其独特的世界观、深入的故事情节和惊人的视觉效果而闻名。游戏融合了科幻元素、黑暗主题和道德抉择，让玩家沉浸在一个充满犯罪乌托邦的世界中。{/size}") xpos 0.35 ypos 0.05 xsize 1160
screen tips123:
    use Tips10
    modal True
    zorder 100
    tag menu
    key "game_menu" action ShowMenu('Tips10')
    text _("{size=50}（架空）游戏《蒸汽朋克1877》中的角色，黄斑集团的创始人。游戏中被自己的儿子杀死，后通过死前的备份“复活”，成了数字人类。{/size}") xpos 0.35 ypos 0.05 xsize 1160