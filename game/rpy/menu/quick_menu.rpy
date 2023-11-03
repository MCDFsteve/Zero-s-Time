## 快捷菜单界面 ######################################################################
##
## 快捷菜单显示于游戏内，以便于访问游戏外的菜单。
transform quick:
         rotate 0
         zoom 0.5
         linear 1.5 rotate 360
         repeat
screen quick_menu():
    zorder 101
    if quick_menu:
        if persistent.quickswitch:
            imagebutton idle "gui/quickmenu.webp" hover "gui/quickmenu_on.webp" xpos 0.0 ypos 0  at quick hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
              action ToggleScreen("quick_menu_full")
        else:
            imagebutton idle "gui/quickmenu.webp" hover "gui/quickmenu_on.webp" xpos 0.0 ypos 0  at quick hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
              action ShowTransient("quick_menu_full")
    else:
      imagebutton idle "gui/none.webp" hover "gui/none.webp":
        action NullAction()
screen quick_menu_full():
    ## 确保该菜单出现在其他界面之上，
    key "pad_b_press" action Return()
    key "game_menu" action Hide("quick_menu_full",transition=dissolve)
    if quick_menu_full_:
        vbox:
            xpos 0.007
            ypos 0.12
            spacing 5
            imagebutton idle "ui_quickmenu_roll" hover "ui_quickmenu_roll_on"  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" at main_menu_show_btn() action Rollback()
            imagebutton idle "ui_quickmenu_history" hover "ui_quickmenu_history_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" at main_menu_show_btn(0.03) action ShowMenu('history')
            imagebutton idle "ui_quickmenu_tips" hover "ui_quickmenu_tips_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" at main_menu_show_btn(0.06) action ShowMenu('Tips')
            imagebutton idle "ui_quickmenu_quick" hover "ui_quickmenu_quick_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" at main_menu_show_btn(0.09) action Skip() alternate Skip(fast=True, confirm=True)
            imagebutton idle "ui_quickmenu_auto" hover "ui_quickmenu_auto_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" at main_menu_show_btn(0.12) action Preference("auto-forward", "toggle")
            imagebutton idle "ui_quickmenu_save" hover "ui_quickmenu_save_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" at main_menu_show_btn(0.15) action ShowMenu('save')
            imagebutton idle "ui_quickmenu_load" hover "ui_quickmenu_load_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" at main_menu_show_btn(0.21) action ShowMenu('load')
            imagebutton idle "ui_quickmenu_quicksave" hover "ui_quickmenu_quicksave_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" at main_menu_show_btn(0.18) action QuickSave()
            imagebutton idle "ui_quickmenu_quickload" hover "ui_quickmenu_quickload_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" at main_menu_show_btn(0.21) action QuickLoad()
            imagebutton idle "ui_quickmenu_menu" hover "ui_quickmenu_menu_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" at main_menu_show_btn(0.24) action ShowMenu('game_menu')
    else:
        vbox:
            xpos 0.005
            ypos 0.1
    zorder 100
    tag menu
    use say_option_hide

## 此代码确保只要用户没有主动隐藏界面，就会在游戏中显示 quick_menu 界面。
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True
default quick_menu_full_ = True
style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")