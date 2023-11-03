#CG鉴赏
#请根据你的需求改掉坐标及图片，直接放到专案目录下运行会报错（大概）
## Extra screen ###############################################################
transform extra(wait=0):
    xoffset 50
    alpha 0.0
    pause(wait)
    easein 0.5 xoffset 0 alpha 1
transform extra_zoom:
   zoom 0.35
   linear 1.0 zoom 0.35
   repeat
transform end_zoom:
   zoom 0.3
screen Extra():
    tag menu
    modal True
    key "pad_b_press" action ShowMenu("menu")
    key "game_menu" action ShowMenu("menu")
    add "gui/extra.webp"
    add "gui/nvl.webp"
    hbox:
        xpos 0.638
        ypos 0.9
        spacing 15
        
        imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("menu")
    vbox:
        spacing 30
        xpos 0
        ycenter 0.4
        imagebutton idle "ui_cg" hover "ui_cg_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("CG")
        imagebutton idle "ui_music" hover "ui_music_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("music_room")
        imagebutton idle "ui_end" hover "ui_end_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("endextra")
        imagebutton idle "ui_chapter" hover "ui_chapter_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("chapterextra")
        #imagebutton idle "ui_mail" hover "ui_mail_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          #action ShowMenu("mailextra")
    add "extra/extra_ui.webp"
screen mailextra():
    tag menu
    modal True
    key "pad_b_press" action ShowMenu("menu")
    key "game_menu" action ShowMenu("menu")
    add "gui/extra.webp"
    add "gui/nvl.webp"
    text _("[mail]") xcenter 0.5 ypos 0.05 xsize 2000 size 50 color "#FFFFFF" outlines [(2,"#000000",1,1)]
    hbox:
        xpos 0.638
        ypos 0.9
        spacing 15
        
        imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("menu")
screen endextra():
    tag menu
    modal True
    key "pad_b_press" action ShowMenu("Extra")
    add "gui/extra.webp"
    add "gui/nvl.webp"
    add "gui/ui_end.webp"
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        
        imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Extra")
    key "game_menu" action ShowMenu("Extra")
    hbox:
        xcenter 0.5
        ypos 0.06
        spacing 30
        if persistent.end1:
            imagebutton hover "extraend1_on" idle "extraend1"  at end_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        else:
            imagebutton hover "end_locked" idle "end_locked_on"  at end_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.end2:
            imagebutton hover "extraend2_on" idle "extraend2" at end_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        else:
            imagebutton hover "end_locked" idle "end_locked_on" at end_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.end3:
            imagebutton hover "extraend3_on" idle "extraend3" at end_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        else:
            imagebutton hover "end_locked" idle "end_locked_on" at end_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    hbox:
        xcenter 0.5
        ypos 0.46
        spacing 30
        if persistent.end4:
            imagebutton hover "extraend4_on" idle "extraend4"  at end_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        else:
            imagebutton hover "end_locked" idle "end_locked_on"  at end_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.end5:
            imagebutton hover "extraend5_on" idle "extraend5" at end_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        else:
            imagebutton hover "end_locked" idle "end_locked_on" at end_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.end6:
            imagebutton hover "extraend6_on" idle "extraend6" at end_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        else:
            imagebutton hover "end_locked" idle "end_locked_on" at end_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
screen chapterextra():
    tag menu
    modal True
    key "pad_b_press" action ShowMenu("Extra")
    add "gui/extra.webp"
    add "gui/nvl.webp"
    add "gui/ui_end.webp"
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        
        imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Extra")
    key "game_menu" action ShowMenu("Extra")
    hbox:
        xcenter 0.5
        ypos 0.06
        spacing 30
        if persistent.extra_chapter1:
            imagebutton hover "extrachapter1_on" idle "extrachapter1"  at end_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        else:
            imagebutton hover "end_locked" idle "end_locked_on"  at end_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.extra_chapter2:
            imagebutton hover "extrachapter2_on" idle "extrachapter2" at end_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        else:
            imagebutton hover "end_locked" idle "end_locked_on" at end_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.extra_chapter3:
            imagebutton hover "extrachapter3_on" idle "extrachapter3" at end_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        else:
            imagebutton hover "end_locked" idle "end_locked_on" at end_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    hbox:
        xcenter 0.5
        ypos 0.46
        spacing 30
        if persistent.extra_chapter4:
            imagebutton hover "extrachapter4_on" idle "extrachapter4"  at end_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        else:
            imagebutton hover "end_locked" idle "end_locked_on"  at end_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.extra_chapter5:
            imagebutton hover "extrachapter5_on" idle "extrachapter5" at end_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        else:
            imagebutton hover "end_locked" idle "end_locked_on" at end_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.extra_chapter6:
            imagebutton hover "extrachapter6_on" idle "extrachapter6" at end_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        else:
            imagebutton hover "end_locked" idle "end_locked_on" at end_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
screen CG():
    tag menu
    modal True
    key "pad_b_press" action ShowMenu("Extra")
    add "gui/extra.webp"
    add "gui/nvl.webp"
    add "gui/cg_menu.webp"
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
        
        imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Extra")
    key "game_menu" action ShowMenu("Extra")
    hbox:
        xpos 0.18
        ypos 0.93
        spacing 15
        imagebutton idle "ui_page1_on" hover "ui_page1_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("CG")
        imagebutton idle "ui_page2" hover "ui_page2_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("CG2")
        imagebutton idle "ui_page3" hover "ui_page3_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("CG3")
        imagebutton idle "ui_page4" hover "ui_page4_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("CG4")
    hbox:
        xpos 0.05
        ypos 0.05
        spacing 30
        if persistent.cg01_unlocked:
            imagebutton hover "cg_1_on" idle "cg_1"  at extra_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
              action ShowMenu('cg01')
        else:
            imagebutton hover "unlocked_on" idle "unlocked"  at extra_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
              action NullAction()

        if persistent.cg02_unlocked:
            imagebutton hover "cg_2_on" idle "cg_2" at extra_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
              action ShowMenu('cg02')
        else:
            imagebutton hover "unlocked_on" idle "unlocked" at extra_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
              action NullAction()
    hbox:
        xpos 0.05
        ypos 0.43
        spacing 30
        if persistent.cg03_unlocked:
            imagebutton hover "cg_3_on" idle "cg_3" at extra_zoom  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg03')
        else:
            imagebutton hover "unlocked_on" idle "unlocked" at extra_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.cg04_unlocked:
            imagebutton hover "cg_4_on" idle "cg_4" at extra_zoom  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg04')
        else:
            imagebutton hover "unlocked_on" idle "unlocked" at extra_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
screen CG2():
    tag menu
    modal True
    key "pad_b_press" action ShowMenu("Extra")
    add "gui/extra.webp"
    add "gui/nvl.webp"
    add "gui/cg_menu.webp"
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
        
        imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Extra")
    key "game_menu" action ShowMenu("Extra")
    hbox:
        xpos 0.18
        ypos 0.93
        spacing 15
        imagebutton idle "ui_page1" hover "ui_page1_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("CG")
        imagebutton idle "ui_page2_on" hover "ui_page2_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("CG2")
        imagebutton idle "ui_page3" hover "ui_page3_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("CG3")
        imagebutton idle "ui_page4" hover "ui_page4_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("CG4")
    hbox:
        xpos 0.05
        ypos 0.05
        spacing 30
        if persistent.cg05_unlocked:
            imagebutton hover "cg_5_on" idle "cg_5"  at extra_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg05')
        else:
            imagebutton hover "unlocked_on" idle "unlocked"  at extra_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()

        if persistent.cg06_unlocked:
            imagebutton hover "cg_6_on" idle "cg_6" at extra_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg06')
        else:
            imagebutton hover "unlocked_on" idle "unlocked" at extra_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    hbox:
        xpos 0.05
        ypos 0.43
        spacing 30
        if persistent.cg07_unlocked:
            imagebutton hover "cg_7_on" idle "cg_7" at extra_zoom  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg07')
        else:
            imagebutton hover "unlocked_on" idle "unlocked" at extra_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.cg08_unlocked:
            imagebutton hover "cg_8_on" idle "cg_8" at extra_zoom  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg08')
        else:
            imagebutton hover "unlocked_on" idle "unlocked" at extra_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()

screen CG3():

    tag menu
    modal True
    key "pad_b_press" action ShowMenu("Extra")
    add "gui/extra.webp"
    add "gui/nvl.webp"
    add "gui/cg_menu.webp"
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
        
        imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Extra")
    hbox:
        xpos 0.18
        ypos 0.93
        spacing 15
        imagebutton idle "ui_page1" hover "ui_page1_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("CG")
        imagebutton idle "ui_page2" hover "ui_page2_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("CG2")
        imagebutton idle "ui_page3_on" hover "ui_page3_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("CG3")
        imagebutton idle "ui_page4" hover "ui_page4_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("CG4")
        
    key "game_menu" action ShowMenu("Extra")#设置右键返回，方便使用
    hbox:
        xpos 0.05
        ypos 0.05
        spacing 30
        if persistent.cg09_unlocked:
            imagebutton hover "cg_9_on" idle "cg_9"  at extra_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg09')
        else:
            imagebutton hover "unlocked_on" idle "unlocked"  at extra_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()

        if persistent.cg10_unlocked:
            imagebutton hover "cg_10_on" idle "cg_10" at extra_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg10')
        else:
            imagebutton hover "unlocked_on" idle "unlocked" at extra_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    hbox:
        xpos 0.05
        ypos 0.43
        spacing 30
        if persistent.cg11_unlocked:
            imagebutton hover "cg_11_on" idle "cg_11" at extra_zoom  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg11')
        else:
            imagebutton hover "unlocked_on" idle "unlocked" at extra_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.cg12_unlocked:
            imagebutton hover "cg_12_on" idle "cg_12" at extra_zoom  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg12')
        else:
            imagebutton hover "unlocked_on" idle "unlocked" at extra_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
screen CG4():

    tag menu
    modal True
    key "pad_b_press" action ShowMenu("Extra")
    add "gui/extra.webp"
    add "gui/nvl.webp"
    add "gui/cg_menu.webp"
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
        
        imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("Extra")
    hbox:
        xpos 0.18
        ypos 0.93
        spacing 15
        imagebutton idle "ui_page1" hover "ui_page1_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("CG")
        imagebutton idle "ui_page2" hover "ui_page2_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("CG2")
        imagebutton idle "ui_page3" hover "ui_page3_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("CG3")
        imagebutton idle "ui_page4_on" hover "ui_page4_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
          action ShowMenu("CG4")
        
    key "game_menu" action ShowMenu("Extra") #设置右键返回，方便使用
    hbox:
        xpos 0.05
        ypos 0.05
        spacing 30
        if persistent.cg13_unlocked:
            imagebutton hover "cg_13_on" idle "cg_13"  at extra_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg13')
        else:
            imagebutton hover "unlocked_on" idle "unlocked"  at extra_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()

        if persistent.cg14_unlocked:
            imagebutton hover "cg_14_on" idle "cg_14" at extra_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg14')
        else:
            imagebutton hover "unlocked_on" idle "unlocked" at extra_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    hbox:
        xpos 0.05
        ypos 0.43
        spacing 30
        if persistent.cg15_unlocked:
            imagebutton hover "cg_15_on" idle "cg_15" at extra_zoom  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg15')
        else:
            imagebutton hover "unlocked_on" idle "unlocked" at extra_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.cg16_unlocked:
            imagebutton hover "cg_16_on" idle "cg_16" at extra_zoom  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action ShowMenu('cg16')
        else:
            imagebutton hover "unlocked_on" idle "unlocked" at extra_zoom hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()

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
        key "game_menu" action ShowMenu('CG')
        key "pad_b_press" action ShowMenu("CG")
        hotspot (0, 0, 1920, 1080) action ShowMenu("CG")
        #hotspot那里，因为我这是1920x1080分辨率就写这个数，其他分辨率自行改正

#每一个按钮都写一个screen，有多少CG就复制粘贴多少次（扶额
#如果CG有差分怎么办？很简单……

screen cg02:
    tag menu
    imagemap:
        ground 'bg_kexi_momo'
        key "game_menu" action ShowMenu('CG')
        key "pad_b_press" action ShowMenu("CG")
        if persistent.cg02_1_unlocked:
            hotspot (0, 0, 1920, 1080) action ShowMenu("cg02_1")
        if not persistent.cg02_1_unlocked:
            hotspot (0, 0, 1920, 1080) action ShowMenu("CG")

screen cg02_1:
    tag menu
    imagemap:
        ground '你的CG图差分'
        key "game_menu" action ShowMenu('CG')
        key "pad_b_press" action ShowMenu("CG")
        hotspot (0, 0, 1920, 1080) action ShowMenu("CG")

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
        key "game_menu" action ShowMenu('CG')
        key "pad_b_press" action ShowMenu("CG")
        hotspot (0, 0, 1920, 1080) action ShowMenu("CG")
screen cg04:
    tag menu
    imagemap:
        ground 'bg_sorawomiru'
        key "game_menu" action ShowMenu('CG')
        key "pad_b_press" action ShowMenu("CG")
        hotspot (0, 0, 1920, 1080) action ShowMenu("CG")
screen cg05:
    tag menu
    imagemap:
        ground 'bg_sorawomiru2'
        key "game_menu" action ShowMenu('CG2')
        key "pad_b_press" action ShowMenu("CG2")
        hotspot (0, 0, 1920, 1080) action ShowMenu("CG2")
screen cg06:
    tag menu
    imagemap:
        ground 'bg_neko'
        key "game_menu" action ShowMenu('CG2')
        key "pad_b_press" action ShowMenu("CG2")
        hotspot (0, 0, 1920, 1080) action ShowMenu("CG2")
screen cg07:
    tag menu
    imagemap:
        ground 'bg_mizu'
        key "game_menu" action ShowMenu('CG2')
        key "pad_b_press" action ShowMenu("CG2")
        hotspot (0, 0, 1920, 1080) action ShowMenu("CG2")
screen cg08:
    tag menu
    imagemap:
        ground 'bg_kawa'
        key "game_menu" action ShowMenu('CG2')
        key "pad_b_press" action ShowMenu("CG2")
        hotspot (0, 0, 1920, 1080) action ShowMenu("CG2")
screen cg09:
    tag menu
    imagemap:
        ground 'bg_kabann'
        key "game_menu" action ShowMenu('CG3')
        key "pad_b_press" action ShowMenu("CG3")
        hotspot (0, 0, 1920, 1080) action ShowMenu("CG3")
screen cg10:
    tag menu
    imagemap:
        ground 'bg_kexi_miru'
        key "game_menu" action ShowMenu('CG3')
        key "pad_b_press" action ShowMenu("CG3")
        hotspot (0, 0, 1920, 1080) action ShowMenu("CG3")
screen cg11:
    tag menu
    imagemap:
        ground 'bg_school_hiroba'
        key "game_menu" action ShowMenu('CG3')
        key "pad_b_press" action ShowMenu("CG3")
        hotspot (0, 0, 1920, 1080) action ShowMenu("CG3")
screen cg12:
    tag menu
    imagemap:
        ground 'bg_school_hiroba2'
        key "game_menu" action ShowMenu('CG3')
        key "pad_b_press" action ShowMenu("CG3")
        hotspot (0, 0, 1920, 1080) action ShowMenu("CG3")
screen cg13:
    tag menu
    imagemap:
        ground 'bg_kexi_shiru'
        key "game_menu" action ShowMenu('CG4')
        key "pad_b_press" action ShowMenu("CG4")
        hotspot (0, 0, 1920, 1080) action ShowMenu("CG4")
screen cg14:
    tag menu
    imagemap:
        ground 'bg_zicheng_te'
        key "game_menu" action ShowMenu('CG4')
        key "pad_b_press" action ShowMenu("CG4")
        hotspot (0, 0, 1920, 1080) action ShowMenu("CG4")
screen cg15:
    tag menu
    imagemap:
        ground 'bg_kexi_syashin'
        key "game_menu" action ShowMenu('CG4')
        key "pad_b_press" action ShowMenu("CG4")
        hotspot (0, 0, 1920, 1080) action ShowMenu("CG4")
screen cg16:
    tag menu
    imagemap:
        ground 'bg_zicheng_te2'
        key "game_menu" action ShowMenu('CG4')
        key "pad_b_press" action ShowMenu("CG4")
        hotspot (0, 0, 1920, 1080) action ShowMenu("CG4")
#CG鉴赏