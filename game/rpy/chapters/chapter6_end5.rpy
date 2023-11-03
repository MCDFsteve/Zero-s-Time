label chapter6_end5:
    nvle "所以还是........算了吧......."
    $ config.allow_skipping = True
    nvle "让那个“我”安静地过完一生吧......."
    nvle "将我的记忆植入给他.....只会给他造成负担.........."
    nvl clear
    hide screen watch
    with dissolve
    scene bg_none
    with fade2
    nvle "..................."
    nvl clear
    stop music fadeout 1.0
    "我敬畏地将手表摘下，放进它原本在的地方。"
    hide screen watch
    with dissolve
    play music title fadein 1.0 fadeout 1.0
    "好了，接下来该去做什么呢？"
    play music home fadein 1.0 fadeout 1.0
    nvle "...................."
    nvl clear
    nvle "...................."
    nvl clear
    scene bg_kennkyuujya_naka2
    with fade2
    nvle "我尝试性地再次拜访了叶梓澄父亲的研究所。"
    nvl clear
    show zicheng_chichi
    with dissolve
    l "您..........需要实验助手吗？"
    scene bg_none
    with fade2
    nvle "............."
    nvl clear
    play music title fadein 1.0 fadeout 1.0
    nvle "就这样,我成为了给叶梓澄父亲的研究所打工的助手。"
    nvle "我失去了我原本的容身之所.......但是却获得了新的容身之所......"
    nvle "这样倒也........挺好的......."
    nvl clear
    nvle "......................"
    nvle "......................"
    nvle "......................"
    nvl clear
    nvle "......................"
    nvle "......................"
    nvle "一晃十年过去了。"
    nvl clear
    play music richang fadein 1.0 fadeout 1.0
    scene bg_schoolmae hare
    with fade2
    "顶着临近正午的太阳，我回到了我的母校。"
    "虽然不清楚没成功毕业的学校到底能不能叫母校。"
    "在校门口摆了个摊，象征性地卖一些文具和生活用品。"
    "但我的真实目的其实是："
    play music sora fadein 1.0 fadeout 1.0
    "想再看一眼那个我.......那个......无垢的我............"
    "这便是对我所做的一切的最好的奖励与报答了。"
    "证明我所做的一切并没有做错的......最好的报答........"
    play sound car_stop
    "随着命中注定的公交车的停下，命中注定的那个我.....缓缓走了出来。"
    play sound run
    "朝我所在的方向看了看，慢慢走了过来。"
    show linluo_pose at jin
    with dissolve
    "我那个时候真好啊~"
    "年轻中透着稚嫩。充满朝气和光明的未来。"
    nvle "........."
    nvl clear
    hide linluo_pose
    play sound run
    show linluo_pose at jin:
        zoom 1.2
    with dissolve
    "他停在我的摊位面前，慢慢端详着我的商品。"
    scene bg_schoolmae
    with dissolve
    show linluo_pose at jin
    with dissolve
    "挑了几根笔，结账了。"
    nvle ".........."
    nvl clear
    hide linluo_pose
    with dissolve
    "然后便准备离开了........."
    play sound odoro
    with vpunch
    l "等一下！！"
    show linluo_pose at jin
    with dissolve
    voice v1
    l "嗯？"
    "我还是忍不住.......叫住了他........"
    l "祝你.....学业有成..........."
    l "也希望你能找到新的朋友..............."
    l "................"
    voice v1
    l "谢谢！！"
    hide linluo_pose
    with dissolve
    "接着便头也不回的.......走进了校门............."
    nvle "..............."
    nvl clear
    "希望我给他创造的这一没有纷争的世界.........他能够好好珍惜吧......"
    "未来的..........."
    "没有未来，却重新获得了未来的........"
    $ config.allow_skipping = False
    "我................"
    $ nise_end = False
    $ end = 5
    $ persistent.end5 = True
    hide screen quick_menu_full
    $ quick_menu = False
    $ quick_menu_full_= False
    play music "music/end.ogg" fadeout 1.0 fadein 1.0
    call disable_shortcut from _call_disable_shortcut_13
    scene bg_none
    show end5
    with fade2
    show endtext:
       xpos 0.3
       ypos 0.7
    with dissolve
    $ renpy.pause(4, hard=False)
    show screen game_end
    with fade2
    $ renpy.pause(189, hard=False)
    $ quick_menu = True
    $ quick_menu_full_= True
    call enable_shortcut from _call_enable_shortcut_12
    $ config.allow_skipping = True
    if persistent.hajimari_end:
        return
    else:
        $ persistent.hajimari_end = True
        play sound tips
        show screen extraconfirm("[endsay]",MainMenu(confirm=False))
        pause
        return