label chapter6_end6:
    nvle "所以我还是想.......再渡过一次正常人的人生............."
    $ config.allow_skipping = True
    nvle "再在高中校园里..........和同学.....有说有笑......一起讨论自己的爱好........一起参加漫展........"
    nvle "一起...............一起..................."
    nvl clear
    nvle "....................."
    hide screen watch
    with dissolve
    scene bg_none
    with fade2
    nvl clear
    nvle "..........................."
    stop music fadeout 2.0
    ai "记忆备份已完成。"
    nvle "......................"
    nvl clear
    nvle "......................"
    nvl clear
    nvle "......................"
    nvl clear
    nvle "......................"
    nvl clear
    nvle "......................"
    nvl clear
    play music richang fadein 1.0 fadeout 1.0
    scene bg_none
    with fade2
    "好晕好难受........"
    "快受不了了........."
    "不过我得稳住。我大口呼吸，调整着心态。"
    "用右手使劲按住小腹上侧食管的位置。"
    "胜利.....就在前方............"
    nvle "................"
    nvl clear
    play audio "audio/car_stop.ogg"
    car "{color=#C1394F}尊敬的旅客您好！沁野市高级中学站到了！请各位旅客有序下车！谢谢！{/color}"
    play sound odoro
    with vpunch
    "呼，终于到了。"
    "现在满脑子只想着赶快脱离汽车这个“恶魔”。"
    "明明是开学的日子却运气不佳，坐的这趟车，靠窗的座位全都被占了。"
    l "呃呜~"
    "喉咙里像卡住了塑料袋。受不了了！必须得下车！"
    scene bg_schoolmae
    with fade
    "我死命捶打着自己的胸口，希望能缓解一点症状。"
    "负责生产公交车的那些人难道都没有晕车的吗？为什么不在汽车上设立一个晕车专用座位。我如此抱怨着。"
    "好吧我并不傻，只要上了车，坐哪里都一样会晕。除非把头伸到天窗外面去。"
    stop sound
    stop audio
    "公交车渐渐走远了，我的眩晕感也慢慢的减弱。我背着包，站在校门附近，四处端详我即将入学的这个新学校。"
    "沁野市高级中学。"
    "由于沁野市地方比较小，人口也不多，所以貌似公立高中就只有这一所。"
    "虽然跟我之前读的那所学校比起来显得很小，但也还能接受。"
    "我是昨天才搬到这个城市来。实际上已经开学大概两个多星期了吧。"
    "校门口附近都没有什么人，两个保安也只是在门后的窗口那谈笑风生着。也对，这个点都要到正午了。"
    "门口附近的公路旁边摆的有地摊。但是这个点基本都收摊了，遮阳伞下面什么东西也没摆。"
    "{size=50}等等！{/size}似乎有一个摊位还在营业。"
    "摊上摆的是一些文具和生活用品。"
    "这些我还没怎么准备。现在采购也不迟吧！"
    play sound run
    "我这样想着，走到了摊位面前。"
    show linluo_mirai
    with dissolve
    "摊主穿着一身白大褂，端坐在那。"
    "见我过来了，摊主慢慢抬起头。左手朝我这边伸了过来。"
    play music lanzhu fadeout 1.0 fadein 1.0
    with vpunch
    l "{size=50}呃！~~{/size}"
    "感觉自己的手臂被抓住了。那瞬间施加的力量，让我的手臂不自觉的颤抖起来。我惊恐地叫出了声。"
    "是这个摊主。不清楚他想干什么。"
    l "{size=50}呃啊~~{/size}"
    l "你想干什么？"
    "我略带质问着说道。"
    "店主不吭声，另一只手伸出来，想递给我一个东西。"
    show hold_watch:
      xcenter 0.2
      ycenter 0.3
    with dissolve
    "是一块黑色的手表。应该是手表吧。"
    voice v3
    t "这块手表送你了。戴上吧。"
    "摊主开口了。很硬朗的中年男性的声音。虽然是第一次听，但是有些熟悉的感觉。"
    nvle "什么鬼啊？！一个陌生城市的陌生人第一次见面就送东西给我。"
    nvle "这个东西，是窃听器吗？或者说是隐藏摄像头？"
    nvle "不对，说不定是炸弹！"
    nvl clear
    nvle "虽然以前经常在脑海里预演过这类突发事件。但那只是自己胡思乱想而已。现在居然真的就出现在我眼前！"
    nvl clear
    nvle "这个人有可能是恐怖分子的人，命令我装上炸弹，然后。。。。。"
    nvle "一个寒颤不禁席卷全身，全身的汗毛倒起，鸡皮疙瘩让我非常的难受。"
    nvl clear
    nvle "不过这也终归是我的妄想而已。说不定这个摊主只是在清理卖剩的商品呢。想到这，我开始放慢了呼吸，试图让自己平静下来。"
    nvle "万一摊主是个好人呢？我在心里安慰着自己。"
    nvl clear
    "恶意揣测别人的好意是不对的。我就勉为其难的收下吧。特别是想到进入学校以后我的手机还得上缴。有一块手表也更方便看时间。"
    l "谢谢！"
    hide hold_watch
    with dissolve
    "我接过了手表。是一块黑色的电子表。"
    $ years = "2022.9.19"
    $ times = "12:20"
    $ weeks = _("周一")
    show screen watch
    with dissolve
    "开机了。不过貌似仅仅只能显示时间。有点失望，还以为能玩玩俄罗斯方块什么的。虽然长得像个智能手表。但一点也不智能............."
    with vpunch
    nvle "...................！！！！"
    nvl clear
    play music title fadein 1.0 fadeout 1.0
    nvle "我...........我想起来了.............."
    nvle "全部..........都想起来了...................."
    nvle "这发生过的所有的一切..............."
    nvl clear
    "我抬头看向摊主..........不.............是看向未来的我.........."
    t "你...........想起来了吗？"
    l "嗯................我全都想起来了.........."
    l "谢谢你............未来的我........把这么珍贵的东西交给了我........"
    l "这么珍贵的记忆.............."
    play music sora fadein 1.0 fadeout 1.0
    "我激动的痛哭流涕。"
    t "那............想起来了就进学校吧.............."
    l "嗯..................."
    play sound odoro
    with vpunch
    l "我是.............经历了这一切的..........林洛！！！"
    hide screen watch
    with dissolve
    scene bg_none
    with fade
    nvle "................"
    play music title fadein 1.0 fadeout 1.0
    play sound run
    scene bg_school_basketball
    with fade2
    $ times = "12:25"
    show screen watch
    with dissolve
    "我大步踏进学校。满足地欣赏着这一切。"
    "我一次次的努力.....还有过去的我，未来的我的一次次努力............"
    "总算换来了我.......和平安宁的校园生活........"
    "我必须好好利用这来之不易的幸福才行！！"
    "就像以前看过的那部动画里说的一样："
    "我们所经历的每个日常，都是连续不断的奇迹！"
    "我终于切身体会并且感受到了！！"
    hide screen watch
    with dissolve
    play sound suzu
    scene bg_tukue
    with fade2
    nvle ".............."
    nvl clear
    $ times = "17:30"
    show screen watch
    with dissolve
    "不知不觉中，下课铃声响了起来。"
    "该正式出发了！！"
    hide screen watch
    with dissolve
    nvle ".........................."
    nvl clear
    nvle "................................"
    nvl clear
    $ times = "17:37"
    show screen watch
    with dissolve
    play music sora fadein 1.0 fadeout 1.0
    scene bg_sorawomiru
    with fade2
    "放学了。班长叶梓澄依旧站在那条道路上，仰望着天空。"
    "头发随着树叶一起，随风飘动。"
    "曾经的她，是抱憾着，思念着。"
    "如今的她，或许有其他的心情在里面吧............."
    "曾经的我或许会害怕与他人交流，但是我现在已经.....蜕变了......."
    l "班长！今天过的如何？"
    scene bg_sorawomiru2
    with dissolve
    c "很好！只是走到这里有感而发......这风中飘扬的树叶.......也太美了...."
    c "但是却有一种感觉.....就好像.....我曾无数次.....无数次地站在这里.....无数次.....无数次地....被你遥望着......"
    c "这大概就是.....既视感吧......"
    l "是啊.....我也曾感觉.....无数次地见到你站在这里......"
    l "无数次地仰望天空......只不过可能每次的理由都不太相同吧........."
    hide screen watch
    with dissolve
    nvle "................"
    nvl clear
    $ times = "17:41"
    show screen watch
    with dissolve
    scene bg_kinoshita
    with fade2
    show kexi_pose mono yubi at jin
    with dissolve
    play sound odoro
    with vpunch
    voice v1
    x "林洛！！！"
    l "怎么了？"
    voice v3
    x "那个...我就长话短说了。你，，，或者你的亲属。以前是否来过沁野市。"
    play sound odoro
    with vpunch
    l "有来过哟！！"
    hide kexi_pose
    show kexi_pose mono mouth1 eyes5 yubi at jin
    with dissolve
    voice v3
    x "是吗？太好了........终于......"
    $ config.allow_skipping = False
    voice v3
    x "再次相见了呢.............."
    $ nise_end = False
    $ end = 6
    $ persistent.end6 = True
    hide screen quick_menu_full
    hide screen watch
    with dissolve
    $ quick_menu = False
    $ quick_menu_full_= False
    play music "music/end.ogg" fadeout 1.0 fadein 1.0
    scene bg_none
    with fade2
    call disable_shortcut from _call_disable_shortcut_14
    show end6
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
    call enable_shortcut from _call_enable_shortcut_13
    $ config.allow_skipping = True
    if persistent.hajimari_end:
        return
    else:
        $ persistent.hajimari_end = True
        play sound tips
        show screen extraconfirm("[endsay]",MainMenu(confirm=False))
        pause
        return