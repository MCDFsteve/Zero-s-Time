transform help_:
     xcenter 1.5
     alpha 0.0
     linear 0.2 xcenter 0.5 alpha 1.0
screen help():
    modal True
    tag menu
    add "gui/main_menu.webp"
    add "gui/nvl.webp"
    add "help/keyboard_ui.webp":
       at help_
    vbox:
        xpos 0
        ypos 0.219
        spacing 15
        text "[key_mousel][key_text1]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_mouser][key_text2]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_mousec][key_text4]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_mousec_w][key_text5]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_mousec_s][key_text6]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_f1][key_text3]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        if main_menu:
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action ShowMenu("menu")
          key "game_menu" action ShowMenu("menu")
          key "pad_b_press" action ShowMenu("menu")
        if not main_menu:
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action Return()
          key "game_menu" action Return()
          key "pad_b_press" action Return()
          key "help" action Return()
    default device = "keyboard"
    vbox:
        spacing 0
        xpos 0
        ypos 0
        imagebutton idle "ui_keyboard_on" hover "ui_keyboard_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action NullAction()
        imagebutton idle "ui_gamepad" hover "ui_gamepad_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help2")
    add "gui/ui_white.webp":
        ycenter 0.97
        xpos 0.01
        xzoom 1.2
    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        add "ui_page"
    hbox:
        xpos 0.18
        ypos 0.93
        spacing 15
        imagebutton idle "ui_page1_on" hover "ui_page1_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help")
        imagebutton idle "ui_page2" hover "ui_page2_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("helpb")
        imagebutton idle "ui_page3" hover "ui_page3_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("helpc")
        imagebutton idle "ui_page4" hover "ui_page4_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("helpd")
    add "help/help_ui.webp"
screen helpb():
    modal True
    tag menu
    add "gui/main_menu.webp"
    add "gui/nvl.webp"
    add "help/keyboard_ui.webp":
       at help_
    vbox:
        xpos 0
        ypos 0.219
        spacing 15
        text "[key_q][key_text7]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_h][key_text4]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_w][key_text8]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_f][key_text16]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_up][key_text9]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_down][key_text10]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        if main_menu:
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action ShowMenu("menu")
          key "game_menu" action ShowMenu("menu")
          key "pad_b_press" action ShowMenu("menu")
        if not main_menu:
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action Return()
          key "game_menu" action Return()
          key "pad_b_press" action Return()
          key "help" action Return()
    default device = "keyboard"
    vbox:
        spacing 0
        xpos 0
        ypos 0
        imagebutton idle "ui_keyboard_on" hover "ui_keyboard_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action NullAction()
        imagebutton idle "ui_gamepad" hover "ui_gamepad_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help2")
    add "gui/ui_white.webp":
        ycenter 0.97
        xpos 0.01
        xzoom 1.2
    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        add "ui_page"
    hbox:
        xpos 0.18
        ypos 0.93
        spacing 15
        imagebutton idle "ui_page1" hover "ui_page1_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help")
        imagebutton idle "ui_page2_on" hover "ui_page2_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("helpb")
        imagebutton idle "ui_page3" hover "ui_page3_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("helpc")
        imagebutton idle "ui_page4" hover "ui_page4_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("helpd")
    add "help/help_ui.webp"
screen helpc():
    modal True
    tag menu
    add "gui/main_menu.webp"
    add "gui/nvl.webp"
    add "help/keyboard_ui.webp":
       at help_
    vbox:
        xpos 0
        ypos 0.219
        spacing 15
        text "[key_left][key_text11]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_right][key_text12]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_ctrl][key_text14]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_tab][key_text14_2]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_esc][key_text2]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_enter][key_text1]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        if main_menu:
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action ShowMenu("menu")
          key "game_menu" action ShowMenu("menu")
          key "pad_b_press" action ShowMenu("menu")
        if not main_menu:
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action Return()
          key "game_menu" action Return()
          key "pad_b_press" action Return()
          key "help" action Return()
    default device = "keyboard"
    vbox:
        spacing 0
        xpos 0
        ypos 0
        imagebutton idle "ui_keyboard_on" hover "ui_keyboard_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action NullAction()
        imagebutton idle "ui_gamepad" hover "ui_gamepad_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help2")
    add "gui/ui_white.webp":
        ycenter 0.97
        xpos 0.01
        xzoom 1.2
    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        add "ui_page"
    hbox:
        xpos 0.18
        ypos 0.93
        spacing 15
        imagebutton idle "ui_page1" hover "ui_page1_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help")
        imagebutton idle "ui_page2" hover "ui_page2_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("helpb")
        imagebutton idle "ui_page3_on" hover "ui_page3_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("helpc")
        imagebutton idle "ui_page4" hover "ui_page4_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("helpd")
    add "help/help_ui.webp"
screen helpd():
    modal True
    tag menu
    add "gui/main_menu.webp"
    add "gui/nvl.webp"
    add "help/keyboard_ui.webp":
       at help_
    vbox:
        xpos 0
        ypos 0.219
        spacing 15
        text "[key_][key_text1_1]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        if main_menu:
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action ShowMenu("menu")
          key "game_menu" action ShowMenu("menu")
          key "pad_b_press" action ShowMenu("menu")
        if not main_menu:
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action Return()
          key "game_menu" action Return()
          key "pad_b_press" action Return()
          key "help" action Return()
    default device = "keyboard"
    vbox:
        spacing 0
        xpos 0
        ypos 0
        imagebutton idle "ui_keyboard_on" hover "ui_keyboard_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action NullAction()
        imagebutton idle "ui_gamepad" hover "ui_gamepad_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help2")
    add "gui/ui_white.webp":
        ycenter 0.97
        xpos 0.01
        xzoom 1.2
    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        add "ui_page"
    hbox:
        xpos 0.18
        ypos 0.93
        spacing 15
        imagebutton idle "ui_page1" hover "ui_page1_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help")
        imagebutton idle "ui_page2" hover "ui_page2_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("helpb")
        imagebutton idle "ui_page3" hover "ui_page3_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("helpc")
        imagebutton idle "ui_page4_on" hover "ui_page4_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("helpd")
    add "help/help_ui.webp"
screen help2():
    modal True
    tag menu
    add "gui/main_menu.webp"
    add "gui/nvl.webp"
    add "help/gamepad_ui.webp":
       at help_
    vbox:
        xpos 0
        ypos 0.219
        spacing 15
        text "[key_A][key_text1]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_B][key_text2_1]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_Y][key_text4]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_LB][key_text5]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_RB][key_text6]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_RE][key_text4]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        if main_menu:
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action ShowMenu("menu")
          key "game_menu" action ShowMenu("menu")
          key "pad_b_press" action ShowMenu("menu")
        if not main_menu:
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action Return()
          key "game_menu" action Return()
          key "pad_b_press" action Return()
          key "help" action Return()
    default device = "gamepad"
    vbox:
        spacing 0
        xpos 0
        ypos 0
        imagebutton idle "ui_keyboard" hover "ui_keyboard_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help")
        imagebutton idle "ui_gamepad_on" hover "ui_gamepad_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action NullAction()
    add "gui/ui_white.webp":
        ycenter 0.97
        xpos 0.01
        xzoom 1.2
    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        add "ui_page"
    hbox:
        xpos 0.18
        ypos 0.93
        spacing 15
        imagebutton idle "ui_page1_on" hover "ui_page1_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help2")
        imagebutton idle "ui_page2" hover "ui_page2_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help2b")
        imagebutton idle "ui_page3" hover "ui_page3_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help2c")
        imagebutton idle "ui_page4" hover "ui_page4_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help2d")
    add "help/help_ui.webp"
screen help2b():
    modal True
    tag menu
    add "gui/main_menu.webp"
    add "gui/nvl.webp"
    add "help/gamepad_ui.webp":
       at help_
    vbox:
        xpos 0
        ypos 0.219
        spacing 15
        text "[key_ST][key_text2]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_LT][key_text5_1]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_RT][key_text1]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_UP][key_text9]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_DOWN][key_text10]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_LEFT][key_text11]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        if main_menu:
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action ShowMenu("menu")
          key "game_menu" action ShowMenu("menu")
          key "pad_b_press" action ShowMenu("menu")
        if not main_menu:
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action Return()
          key "game_menu" action Return()
          key "pad_b_press" action Return()
          key "help" action Return()
    default device = "gamepad"
    vbox:
        spacing 0
        xpos 0
        ypos 0
        imagebutton idle "ui_keyboard" hover "ui_keyboard_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help")
        imagebutton idle "ui_gamepad_on" hover "ui_gamepad_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action NullAction()
    add "gui/ui_white.webp":
        ycenter 0.97
        xpos 0.01
        xzoom 1.2
    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        add "ui_page"
    hbox:
        xpos 0.18
        ypos 0.93
        spacing 15
        imagebutton idle "ui_page1" hover "ui_page1_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help2")
        imagebutton idle "ui_page2_on" hover "ui_page2_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help2b")
        imagebutton idle "ui_page3" hover "ui_page3_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help2c")
        imagebutton idle "ui_page4" hover "ui_page4_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help2d")
    add "help/help_ui.webp"
screen help2c():
    modal True
    tag menu
    add "gui/main_menu.webp"
    add "gui/nvl.webp"
    add "help/gamepad_ui.webp":
       at help_
    vbox:
        xpos 0
        ypos 0.219
        spacing 15
        text "[key_RIGHT][key_text12]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_LP][key_text13]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_RP][key_text13]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_RT_2][key_text14]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_LT_2][key_text15]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
        text "[key_RB_2][key_text14_1]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        if main_menu:
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action ShowMenu("menu")
          key "game_menu" action ShowMenu("menu")
          key "pad_b_press" action ShowMenu("menu")
        if not main_menu:
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action Return()
          key "game_menu" action Return()
          key "pad_b_press" action Return()
          key "help" action Return()
    default device = "gamepad"
    vbox:
        spacing 0
        xpos 0
        ypos 0
        imagebutton idle "ui_keyboard" hover "ui_keyboard_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help")
        imagebutton idle "ui_gamepad_on" hover "ui_gamepad_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action NullAction()
    add "gui/ui_white.webp":
        ycenter 0.97
        xpos 0.01
        xzoom 1.2
    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        add "ui_page"
    hbox:
        xpos 0.18
        ypos 0.93
        spacing 15
        imagebutton idle "ui_page1" hover "ui_page1_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help2")
        imagebutton idle "ui_page2" hover "ui_page2_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help2b")
        imagebutton idle "ui_page3_on" hover "ui_page3_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help2c")
        imagebutton idle "ui_page4" hover "ui_page4_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help2d")
    add "help/help_ui.webp"
screen help2d():
    modal True
    tag menu
    add "gui/main_menu.webp"
    add "gui/nvl.webp"
    add "help/gamepad_ui.webp":
       at help_
    vbox:
        xpos 0
        ypos 0.219
        spacing 15
        text "[key_LB_2][key_text15]" size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        if main_menu:
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action ShowMenu("menu")
          key "game_menu" action ShowMenu("menu")
          key "pad_b_press" action ShowMenu("menu")
        if not main_menu:
          imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action Return()
          key "game_menu" action Return()
          key "pad_b_press" action Return()
          key "help" action Return()
    default device = "gamepad"
    vbox:
        spacing 0
        xpos 0
        ypos 0
        imagebutton idle "ui_keyboard" hover "ui_keyboard_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help")
        imagebutton idle "ui_gamepad_on" hover "ui_gamepad_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action NullAction()
    add "gui/ui_white.webp":
        ycenter 0.97
        xpos 0.01
        xzoom 1.2
    hbox:
        
        xpos 0.0
        ypos 0.9
        spacing 15
        
        add "ui_page"
    hbox:
        xpos 0.18
        ypos 0.93
        spacing 15
        imagebutton idle "ui_page1" hover "ui_page1_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help2")
        imagebutton idle "ui_page2" hover "ui_page2_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help2b")
        imagebutton idle "ui_page3" hover "ui_page3_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help2c")
        imagebutton idle "ui_page4_on" hover "ui_page4_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("help2d")
    add "help/help_ui.webp"