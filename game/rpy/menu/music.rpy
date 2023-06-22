#音乐盒
init python:

    #  步骤1，创建一个MusicRoom实例。
    mr = MusicRoom(fadeout=1.0)

    # Step 2. 添加音乐文件。
    mr.add("music/title.ogg")
    mr.add("music/richang.ogg")
    mr.add("music/school.ogg")
    mr.add("music/lanzhu.ogg")
    mr.add("music/omou.ogg")
    mr.add("music/home.ogg")
    mr.add("music/sora.ogg")
    #mr.add("track2.ogg")
    #mr.add("track3.ogg")
# Step 3. 创建音乐空间界面。
screen music_room:
    add  "extra/bg_musicroom.webp"
    tag menu
    #on "replaced" action Play("music", "music/title.ogg")
    modal True
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
        if persistent.music_omou:
          textbutton _("{size=80}毁灭-陈次犬{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action mr.Play("music/omou.ogg")
        else:
          textbutton _("{size=80}？？？{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.music_home:
          textbutton _("{size=80}家-陈次犬{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action mr.Play("music/home.ogg")
        else:
          textbutton _("{size=80}？？？{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
        if persistent.music_sora:
          textbutton _("{size=80}天空-陈次犬{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action mr.Play("music/sora.ogg")
        else:
          textbutton _("{size=80}？？？{/size}")  hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg" action NullAction()
    hbox:
        
        xpos 0.638
        ypos 0.9
        spacing 15
        imagebutton idle "ui_return" hover "ui_return_on" hover_sound "audio/button_off.ogg" activate_sound "audio/button.ogg":
            action [Hide("music_room"), ShowMenu("Extra"),Play("music", "music/title.ogg")]

    # 音乐空间的音乐播放入口。
    on "replace" action mr.Play()
    key "game_menu" action ShowMenu("Extra")
    key "pad_b_press" action ShowMenu("Extra")
    # 离开时恢复主菜单的音乐。
#音乐盒