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
        
    key "game_menu" action Return() #设置右键返回，方便使用
    vbox:
        xpos 0.05
        ypos 0.03
        spacing 0
        if persistent.tips01:
          textbutton _("{size=50}{b}pbb{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips01")
        else:
          textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips02:
          textbutton _("{size=50}{b}工口同人本{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips02")
        else:
          textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips03:
            textbutton _("{size=50}{b}d站{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips03")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips04:
            textbutton _("{size=50}{b}鬼畜{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips04")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips05:
            textbutton _("{size=50}{b}cq{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips05")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips06:
            textbutton _("{size=50}{b}番剧{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips06")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips07:
            textbutton _("{size=50}{b}NPC{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips07")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips08:
            textbutton _("{size=50}{b}地球online{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips08")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips09:
            textbutton _("{size=50}{b}家里蹲{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips09")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips10:
            textbutton _("{size=50}{b}油陷{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips10")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips11:
            textbutton _("{size=50}{b}希望之草{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips11")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips12:
            textbutton _("{size=50}{b}现充{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips12")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips13:
            textbutton _("{size=50}{b}战场原白仪{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips13")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    
        
screen Tips2():

    tag menu
    modal True
    add "gui/tips.webp"
    add "gui/nvl.webp"
    use tips_option

    add "gui/ui_white.webp":
        ycenter 0.97
        xpos 0.01
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
        
        
    key "game_menu" action Return() #设置右键返回，方便使用
    vbox:
        xpos 0.05
        ypos 0.03
        spacing 0
        if persistent.tips14:
            textbutton _("{size=50}{b}斧乃木正弦{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips14")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips15:
            textbutton _("{size=50}{b}故事系列{/b}{/size}")hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips15")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips16:
            textbutton _("{size=50}{b}厨{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips16")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips17:
            textbutton _("{size=50}{b}这是禁止事项{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips17")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips18:
            textbutton _("{size=50}{b}•福杰{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips18")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips19:
            textbutton _("{size=50}{b}社牛{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips19")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips20:
            textbutton _("{size=50}{b}再上映{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips20")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips21:
            textbutton _("{size=50}{b}二次元{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips21")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips22:
            textbutton _("{size=50}{b}中二{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips22")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips23:
            textbutton _("{size=50}{b}也儿夕传说{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips23")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips24:
            textbutton _("{size=50}{b}也儿夕传说：旷野之炊{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips24")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips25:
            textbutton _("{size=50}{b}林库{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips25")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips26:
            textbutton _("{size=50}{b}抖乐{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips26")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    
screen Tips3():

    tag menu
    modal True
    add "gui/tips.webp"
    add "gui/nvl.webp"
    use tips_option

    add "gui/ui_white.webp":
        ycenter 0.97
        xpos 0.01
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
        
    key "game_menu" action Return() #设置右键返回，方便使用
    vbox:
        xpos 0.05
        ypos 0.03
        spacing 0
        if persistent.tips27:
            textbutton _("{size=50}{b}腹黑{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips27")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips28:
            textbutton _("{size=50}{b}宝可魔{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips28")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips29:
            textbutton _("{size=50}{b}任地堂{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips29")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips30:
            textbutton _("{size=50}{b}witch{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips30")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips31:
            textbutton _("{size=50}{b}泥可泥丝{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips31")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips32:
            textbutton _("{size=50}{b}蒸汽朋克：边缘行者{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips32")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips33:
            textbutton _("{size=50}{b}AADR{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips33")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips34:
            textbutton _("{size=50}{b}ChieAnime{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips34")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips35:
            textbutton _("{size=50}{b}漫展{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips35")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips36:
            textbutton _("{size=50}{b}cosplay{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips36")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips37:
            textbutton _("{size=50}{b}coser{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips37")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips38:
            textbutton _("{size=50}{b}低德地图{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips38")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips39:
            textbutton _("{size=50}{b}高塔{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips39")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
screen Tips4():

    tag menu
    modal True
    add "gui/tips.webp"
    add "gui/nvl.webp"
    use tips_option

    add "gui/ui_white.webp":
        ycenter 0.97
        xpos 0.01
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
        
    key "game_menu" action Return() #设置右键返回，方便使用
    vbox:
        xpos 0.05
        ypos 0.03
        spacing 0
        if persistent.tips40:
            textbutton _("{size=50}{b}颜文字{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips40")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips41:
            textbutton _("{size=50}{b}神庙{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips41")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips42:
            textbutton _("{size=50}{b}撒旦的结合{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips42")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips43:
            textbutton _("{size=50}{b}堂屋{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips43")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips44:
            textbutton _("{size=50}{b}橘外人{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips44")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips45:
            textbutton _("{size=50}{b}零子{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips45")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips46:
            textbutton _("{size=50}{b}皮带炖肉{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips46")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips47:
            textbutton _("{size=50}{b}海马体{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips47")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips48:
            textbutton _("{size=50}{b}时间悖论{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips48")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips49:
            textbutton _("{size=50}{b}时间刻校正仪{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips49")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips51:
            textbutton _("{size=50}{b}影子{/b}{/size}") hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips51")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips52:
            textbutton _("{size=50}{b}端锅{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips52")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips50:
            textbutton _("{size=50}{b}死亡回归{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips50")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
screen Tips5():

    tag menu
    modal True
    add "gui/tips.webp"
    add "gui/nvl.webp"
    use tips_option

    add "gui/ui_white.webp":
        ycenter 0.97
        xpos 0.01
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
        
    key "game_menu" action Return() #设置右键返回，方便使用
    vbox:
        xpos 0.05
        ypos 0.03
        spacing 0
        if persistent.tips53:
            textbutton _("{size=50}{b}原子匹配分布表{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips53")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips54:
            textbutton _("{size=50}{b}蓝图{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips54")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips55:
            textbutton _("{size=50}{b}黑化{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips55")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips56:
            textbutton _("{size=50}{b}沙皇{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips56")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips57:
            textbutton _("{size=50}{b}原地tp{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips57")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips58:
            textbutton _("{size=50}{b}时间刻{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips58")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips59:
            textbutton _("{size=50}{b}鸡嘴火龙{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips59")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips60:
            textbutton _("{size=50}{b}鸡嘴火兽{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips60")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips61:
            textbutton _("{size=50}{b}抖M{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips61")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips62:
            textbutton _("{size=50}{b}平行宇宙{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips62")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips63:
            textbutton _("{size=50}{b}电话电磁炉{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips63")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips64:
            textbutton _("{size=50}{b}斯坦因之窗{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips64")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.tips65:
            textbutton _("{size=50}{b}蝴蝶效应{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu("tips65")
        else:
            textbutton _("{size=50}{b}？？？{/b}{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
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
    text _("{size=50}流行意思指18岁以上限制级漫画。也有课本或笔记本的简称叫这个。{/size}") xpos 0.35 ypos 0.05 xsize 1160
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
    text _("{size=50}（架空）《也儿夕传说：旷野之炊》中的一种建筑，玩家需要爬山该建筑并与之互动才能解锁所在地区的地图信息，相关的术语有“爬塔开图”。{/size}") xpos 0.35 ypos 0.05 xsize 1160
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
    text _("{size=50}“橘”出自知名百合番{a=http://citrus-anime.com}《柑橘味香气》{/a}。用来调侃ACG女角色之间的亲密关系已经接近恋爱的程度了，可谓“大橘已定”，冒出个男的来则称为“橘外人”。{/size}") xpos 0.35 ypos 0.05 xsize 1160
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
        textbutton _("{size=50}（架空）由叶梓澄之父开发出的跟零子有关的科学仪器。{/size}") xpos 0.35 ypos 0.05 xsize 1160
    elif persistent.time == 1:
        textbutton _("{size=50}（架空）由叶梓澄之父开发出的跟零子有关的科学仪器。具有危险性，可以向+1维度注入零子。{/size}") xpos 0.35 ypos 0.05 xsize 1160
    elif persistent.time == 2:
        textbutton _("{size=50}（架空）由叶梓澄之父开发出的跟零子有关的科学仪器。可以将零子注入更高维度。{/size}") xpos 0.35 ypos 0.05 xsize 1160
    elif persistent.time == 3:
        textbutton _("{size=50}（架空）由叶梓澄之父开发出的跟零子有关的科学仪器。具有危险性，可以向+1维度注入零子以及从+1维度抽出零子到人类所处的0维度，是+1维度和0维度之间进行数据交换的桥梁。{/size}") xpos 0.35 ypos 0.05 xsize 1160
    elif persistent.time == 4:
        textbutton _("{size=50}（架空）由叶梓澄之父开发出的跟零子有关的科学仪器。具有危险性，可以向+1维度注入零子以及从+1维度抽出零子到人类所处的0维度，是+1维度和0维度之间进行数据交换的桥梁。抽出和注入均会导致+1时间刻维度对0时间刻维度产生干涉。抽出之前注入的零子可终止干涉。{/size}") xpos 0.35 ypos 0.05 xsize 1160
    else:
        textbutton _("{size=50}（架空）由叶梓澄之父开发出的跟零子有关的科学仪器。{/size}") xpos 0.35 ypos 0.05 xsize 1160
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