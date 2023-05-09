label chapter2:
    scene bg_none
    hide screen quick_menu_full
    $ quick_menu = False
    show chapter2
    with fade2
    $ renpy.pause(5, hard=False)
    hide chapter2
    with fade2
    scene bg_none
    $ quick_menu = True
    call enable_shortcut from _call_enable_shortcut_2
    scene bg_school_basketball
    with dissolve
    play music "music/omou.ogg" fadeout 1.0 fadein 1.0
    $ times = "12:29"
    show screen watch
    with dissolve
    $ save_name = "{font=Huayuan.Gothic.Bold.ttf}章节二：死而又生的起始{/font}"
    "这！这是怎么回事？"
    "我诧异地站在原地。"
    play sound suzu
    play sound "audio/yakamashii.ogg"
    $ times = "12:30"
    "直到下课铃响起，才将我的意识拉回现实。"
    nvle "到底......"
    nvle "发生了什么......"
    nvle "难道我之前......一直在做梦？"
    nvl clear
    "不行不行！我得赶紧确定一下！！"
    stop sound
    scene bg_none
    with fade
    play music school fadeout 1.0 fadein 1.0
    "目视着吃午饭的人群都走光了以后，我小心翼翼地走过广场。"
    scene bg_2_3
    with dissolve
    $ times = "12:32"
    "走到了教室前面。"
    "是我的班主任！正在教室里整理教案。"
    show sensei1_pose at jin
    with dissolve
    voice v3
    s "你就是新来的转学生吗？"
    l "啊......李老师..."
    voice v3
    s "嗯？我有跟你说过我姓李吗？"
    l "这......"
    nvle "这一切的一切都让我回想起来我第一次转学过来的时候了..."
    nvle "只能说是一模一样的情景......"
    nvl clear
    l "啊......老师你好我叫林洛..."
    "我试图引开话题。"
    voice v3
    s "林洛是吧？刚刚保安打电话的时候有跟我说过。我是你的班主任，李老师。"
    show bg_class_naka
    with dissolve
    voice v3
    s "你先坐那个位置吧！正好那里现在没人！"
    hide bg_class_naka
    with dissolve
    "好！谢谢老师！"
    scene bg_tukue
    with dissolve
    $ times = "12:35"
    "我轻车熟路地来到了我的“新座位”。"
    "我得冷静一下，理清一下我现在的状况。"
    "再次看了看手表的时间，确认今天是19号，星期一。"
    nvle "难道我......"
    $ persistent.tips50 = True
    nvle "时间穿越了？{a=showmenu:tips50}{color=#F18D7D}死亡回归{/color}{/a}了？"
#词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    nvl clear
    scene bg_toire
    with fade
    $ times = "12:40"
    "我来到了卫生间。对着镜子仔细观察我的脸。"
    $ persistent.tips51 = True
    "嗯......左右眼瞳色一致。看来不是{a=showmenu:tips51}{color=#F18D7D}影子{/color}{/a}的力量。"
#词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    "开始回想起迄今为止的状况。"
    show bg_kuruma_matu
    with fade
    play music "music/omou.ogg" fadeout 1.0 fadein 1.0
    "早上，也就是9月26号，星期一。我乘坐了一辆公交车。"
    hide bg_kuruma_matu
    with fade
    scene bg_none
    with fade
    "然后......"
    "似乎是，在十字路口的位置被一辆货车撞了。"
    $ persistent.tips52 = True
    "但是我并没有在车上看见{a=showmenu:tips52}{color=#F18D7D}端锅{/color}{/a}的。"
#词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    "那种痛感真实的不像做梦。现在想起来还后怕。"
    "然后...我就回到了这里！19号！星期一！"
    "为什么......"
    "是因为什么......"
    scene bg_toire
    with fade
    $ times = "12:44"
    "我用冷水洗了把脸，试图让自己冷静一下。"
    play music "music/title.ogg" fadeout 1.0 fadein 1.0
    "！！！"
    nvle "难道是上天听到了我的诉求。所以给了我一次机会吗？"
    nvle "给了我一次拯救覃可汐的机会！"
    nvle "给了我一次避免悲剧发生的机会！"
    nvle "我一定要救覃可汐！！！"
    nvl clear
    scene bg_none
    with fade
    play music school fadeout 1.0 fadein 1.0
    "......"
    scene bg_class_naka
    with fade
    $ times = "12:51"
    play sound "audio/yakamashii.ogg"
    "我回到教室的时候，班上同学基本都吃完饭回来了。"
    play music sora fadeout 1.0 fadein 1.0
    "啊......"
    "我快要哭出来了......"
    "覃可汐，正坐在我旁边的座位上，正在修建她的指甲。"
    "太好了......"
    "再一次见到了活生生的覃可汐。"
    play sound run
    $ times = "12:52"
    "我快步走到覃可汐的座位旁边，"
    scene bg_tukue2
    with fade
    play sound "audio/run.ogg"
    play music kexi fadeout 1.0 fadein 1.0
    l "覃可汐！......"
    nvle "话到嘴边还是说不出口。"
    nvle "毕竟在目前这个时间，覃可汐和我也还只是初次认识而已。"
    nvl clear
    show kexi_pose eyes4 at jin
    play audio odoro
    with vpunch
    voice v1
    x "啊~！？你......"
    play music lanzhu fadeout 1.0 fadein 1.0
    voice v3
    x "你怎么知道我的名字！？"
    voice v3
    x "还有......你是新来的转校生吗？"
    l "是！我叫林洛！是新来的转校生！"
    l "请多关照！"
    hide screen watch
    with dissolve
    scene bg_none
    with fade
    "本来打算发生事故的那天再去的。"
    "但是心已经静不下来了！"
    $ times = "12:56"
    show screen watch
    with dissolve
    "我打完招呼就转身出了教室。"
    "必须提前排除安全隐患！也就是这一切悲剧发生的源头！"
    "覃可汐是死于高空坠落的花盆。"
    play sound "audio/run.ogg"
    "我顺着覃可汐遇难地点的垂直坐标一层层地进行着排查。"
    play sound "audio/run.ogg"
    $ times = "12:59"
    scene bg_kai
    with fade
    "二楼。没有。"
    play sound "audio/run.ogg"
    $ times = "13:01"
    scene bg_kai2
    with fade
    "三楼。没有。"
    play sound "audio/run.ogg"
    $ times = "13:03"
    scene bg_kai3
    with fade
    "四楼。没有。"
    "只剩最后两个楼层了。肇事所在的花盆一定在上面。"
    "我这么想着，顺着楼梯准备上五楼。"
    nan "同学啊！你这是在干什么？"
    $ times = "13:04"
    scene bg_kainogo
    with vpunch
    "额啊！？"
    show otoko
    with dissolve
    "一个中年男人叫住了我，看起来像是这个学校的老师。"
    voice v5
    s "我看你一直在各个楼层之间转来转去的。你知不知道啊！我们学校不允许串楼层的！......"
    "好烦。"
    l "老师......我是.....我......"
    "该死！编不出什么理由！"
    voice v1
    s "你是哪个班的？"
    l "我......"
    "不管了！！"
    "我没有理会这个老师的质问。转身冲上了五楼。"
    $ times = "13:07"
    play sound "audio/run.ogg"
    show screen suduxian
    with dissolve
    scene bg_none
    with fade
    scene bg_kai4
    with dissolve
    s "诶！？你跑什么？"
    "男老师在后面追了上来。"
    s "你哪个班的？班主任是谁啊？谁叫你对老师这个态度的啊？"
    $ times = "13:09"
    scene bg_huapen
    with vpunch
    "五楼！找到了！"
    hide screen suduxian
    with dissolve
    scene bg_plant
    with dissolve
    play music school fadeout 1.0 fadein 1.0
    "教室外的栅栏上，正放着一盆植物。我并不认识是什么植物。"
    "有着深绿色的茎和绿色厚大的叶片。"
    "什么都无所谓了。"
    scene bg_plant_omochi
    with dissolve
    "我捧起了这个盆栽。"
    play sound suzu
    $ times = "13:10"
    "就在同时。午睡铃响了起来。"
    play sound "audio/yakamashii.ogg"
    "犹如天助。走廊上的同学都陆陆续续回到了教室里。即便有的同学诧异地看着我。"
    "得把这个盆栽放在一个安全的位置才行。"
    "有了！"
    stop sound
    $ times = "13:12"
    scene bg_kai_plant
    with fade
    "我把盆栽放在了楼梯口的角落里。"
    "我们安全了。暂时。"
    "我如此想到。"
    show bg_kai_plant
    $ times = "13:13"
    with vpunch
    play music lanzhu fadeout 1.0 fadein 1.0
    voice v3
    s "你！！你你你这是在干什么在？"
    voice v3
    s "谁叫你这么干的？把学校的盆栽搬到这里来是什么意思？"
    "啊！可恶！哪个喋喋不休的老师追上来了。"
    $ times = "13:14"
    scene bg_kainogo
    with dissolve
    show otoko
    with dissolve
    l "啊......老师...我是三班的！"
    l "班主任让我把这个盆栽先撤下来，这不最近天气很热嘛......"
    l "班主任说放学以后打算亲自来浇浇水......"
    "我不禁捏了把汗，希望我的谎言不要被看穿。"
    voice v3
    s "小李吗......是她的话...那没事了......"
    voice v5
    s "不过跟你们班主任讲一声，不要再在午休期间搞这个了！吃饭的时候人流量大。拿着花盆也不安全......"
    voice v3
    s "而且让学生来干。现在的年轻教师真是啊......"
    voice v3
    s "万一手松了摔坏了怎么办"
    voice v3
    s "我得找个时间跟她好好谈谈......"
    "理智战胜了恐惧。又或者是因为恐惧所以很理智呢？"
    "都无所谓了。我用一副人畜无害的营业式表情编出的谎言，似乎已经让这位老师信服。"
    l "那个.....老师......午睡时间了.......我可以走了吗？"
    voice v1
    s "嗯！你走吧！"
    voice v5
    s "哦对了！转告一下你班主任，告诉她如果想浇水就自己来浇.......而且学校的盆栽，花盆什么的...是有值日生的..."
    voice v1
    s "不需要多操心......"
    "值日生！！！"
    "猛地回想起来覃可汐遇害那天。"
    "也恰好是值日生！"
    play music "music/omou.ogg" fadeout 1.0 fadein 1.0
    "难道！"
    "覃可汐是被人谋害的吗？！！"
    "脊背开始发凉......"
    nvle "难道是有人看覃可汐不爽，想借刀杀人？"
    nvle "脑内的超展开又开始了......"
    nvle "但是这种可能性不是没有。"
    nvle "假定存在。那！"
    nvl clear
    nvle "嫌疑最大的自然就是————"
    nvle "同为周五值日的，负责给花盆浇水的值日生了！"
    nvle "虽然也有路过的学生推倒花盆的可能性......"
    nvl clear
    scene bg_none
    $ times = "13:18"
    with fade
    play music school fadeout 1.0 fadein 1.0
    "总之！先试着排查一下覃可汐的仇人吧！如果仇人确实存在的话，即便花盆被撤下来了，还是会想其他方法杀害覃可汐的不是吗？"
    "我一路上这样思考着。不知道什么时候已经自然地，自己走回了教室。"
    $ times = "13:20"
    scene bg_stand_kyoudan
    with dissolve
    "我蹑手蹑脚地推开教室门。同学们早已开始午睡。"
    scene bg_tukue
    with dissolve
    "慢慢地走近我的座位。"
    "先等到下午吧。还要上台介绍我自己呢。"
    "额！！"
    $ times = "13:22"
    scene bg_kexi_mi2
    with vpunch
    play music sora fadeout 1.0 fadein 1.0
    "我坐到座位上的那一刻，原本在睡午觉的覃可汐突然把头转了过来。睁开眼看向我。"
    "看着她那睁大的充满着好奇的双眼。我的心情愈发复杂。"
    "只能先假装没看见。"
    scene bg_none
    with dissolve
    "我扭头朝着墙那头，趴着睡觉了。"
    hide screen watch
    with dissolve
    "................."
    $ times = "14:10"
    play sound suzu
    play music school fadeout 1.0 fadein 1.0
    show screen watch
    with dissolve
    scene bg_tukue
    with fade
    "伴随着清脆的铃声。短暂的午睡结束了。"
    play sound "audio/yakamashii.ogg"
    "同学们都陆陆续续醒过来了。课间逐渐变得吵闹。"
    "有越来越多的人注意到我了。注意到我这个转学生了。"
    stop sound
    $ times = "14:16"
    x "林洛？林洛！"
    scene bg_tukue2
    with dissolve
    show kexi_pose at jin
    with dissolve
    "覃可汐叫住了我，把头凑了过来。"
    "和我四目相对。我不由得紧张了起来。因为在现在这个时间段，覃可汐认识我的总时间不会超过一小时。"
    play music kexi fadeout 1.0 fadein 1.0
    voice v1
    x "林洛......那个......"
    voice v3
    x "你真的是转校生吗？"
    voice v3
    x "你以前有来过沁野市吗？"
    nvle "啊！是原本覃可汐会在今天放学后问我的问题......似乎由于我的各种行动，导致这个事件被提前了。"
    nvl clear
    l "啊......也许吧......也许我们真的有见过面呢......"
    "因为我确确实实，跟覃可汐见过面了。只不过那是我遭遇车祸之前的事了。"
    "放到现在来看到底见没见过......从我的主观上来说，见过了。对覃可汐而言，则是没见过。"
    $ times = "14:18"
    show kexi_pose eyes4 at jin
    play audio odoro
    with vpunch
    voice v1
    x "啊！？"
    "覃可汐一脸惊讶的神情。"
    "啊？难道我哪里说错了吗？难道我不能说我见过了她？"
    voice v3
    x "我还没问我们是否以前见过面呢！虽然正打算开口问......"
    voice v3
    x "不过你都这么说了。我的心里也有答案了。或许真的是见过了吧！"
    hide kexi_pose
    show kexi_pose2 mouth1 at jin
    with dissolve
    voice v3
    x "所以.....林洛......非常感谢......"
    "............."
    $ times = "14:20"
    play sound suzu
    "这个时候，上课铃响了起来。"
    scene bg_tukue
    with dissolve
    play music sora fadeout 1.0 fadein 1.0
    nvle "非常感谢.............？"
    nvle "覃可汐这话...是什么意思？"
    nvle "只能下课了再问问了。"
    nvl clear
    $ times = "14:21"
    "班主任拿着教材走了进来。"
    s "这节课，我们要欢迎一位新同学。"
    play music school fadeout 1.0 fadein 1.0
    "班主任说罢，便做着姿势欢迎我上台。"
    $ times = "14:23"
    scene bg_stand_kyoudan
    with dissolve
    l "大家好。我叫林洛。来自芷柚市。因父母工作的原因，搬家来到沁野市。"
    l "希望能在新的班级里和大家友好相处！谢谢！"
    "我光速说完，然后点头鞠躬。"
    play sound "audio/hakusyu.ogg"
    "班主任似乎也没料到我言语如此简洁。只能尴尬着给我鼓掌。"
    $ times = "14:25"
    "班上的同学们也顺势鼓起了掌。"
    s "希望大家能跟新同学好好相处！"
    s "新同学你有什么不懂的也尽管找同学们帮忙！这位是班长叶梓澄。有事找她就可以了！"
    "看向叶梓澄忧郁的神色。我猛地想起了叶梓澄的遭遇。"
    nvle "我记得，叶梓澄会在几天后收到自己父亲死亡的消息。"
    nvle "也就是说，现在这个时间，叶梓澄的父亲很有可能还活着。"
    nvle "或许我不光能拯救覃可汐。也能顺带避免叶梓澄父亲的死亡。"
    nvl clear
    "我暗自下定了决心。必须开始争分夺秒了。"
    "因为我很可能就只有这一次重来的机会。"
    $ times = "14:27"
    scene bg_tukue
    with fade
    "我回到座位上以后就开始构思着具体的计划。"
    "同时拯救覃可汐，以及叶梓澄父亲的计划。"
    show bg_school_hiroba2
    with dissolve
    play music speak fadeout 1.0 fadeout 1.0
    nvle "首先。覃可汐会在这周五，也就是四天后的中午，在做值日的时候被楼上的花盆砸中。"
    hide bg_school_hiroba2
    nvle "在这一点上，我已经清楚了花盆的具体位置，并将花盆撤了下来。"
    nvle "但是还是很悬。因为随时可能会有人把花盆放回原处。尤其是，如果那天真的是受人为干预才导致的花盆掉下去。"
    nvle "那至少那个妄图加害覃可汐的人，不会放过这个机会。"
    nvl clear
    nvle "而且由我之前对覃可汐的各种干预，覃可汐向我提问的这个事件被提前了。所以如果我的行动偏差太大。很有可能会导致对方提前下手。"
    nvle "所以我不能打草惊蛇，得从现在开始尽量保持和我所经历过的记忆一致的行动。至少明面上得这样做。"
    nvle "覃可汐的事目前是打算这样处理了。现在棘手的事情是叶梓澄的父亲应该怎么救。"
    nvle "我记得是星期三的时候，叶梓澄会被叫到办公室。应该就是在那个时候，叶梓澄得知了她父亲的死讯。"
    nvl clear
    nvle "也就是说，必须在今天就开始行动了。不然怎么都来不及了。"
    nvle "但是我除了知道叶梓澄的父亲会死以外，没有其他任何情报了。"
    nvle "得先找叶梓澄了解一下情况。"
    play sound suzu
    $ times = "15:00"
    scene bg_tukue
    with fade
    play music school fadein 1.0 fadeout 1.0
    "下课了。"
    "想起上课前覃可汐说的那句“非常感谢”。这是什么意思？"
    "难道我试图拯救覃可汐的想法被她看透了？这...这怎么可能！难不成覃可汐有读心术不成？"
    $ persistent.tips18 = True
    "{a=showmenu:tips18}{color=#F18D7D}覃可汐•福杰......{/color}{/a}"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    "我还是先询问一下吧......可能会获得新的线索。"
    stop sound
    scene bg_tukue2
    with dissolve
    "我转过来面向覃可汐的座位。"
    show kexi_pose at jin
    with dissolve
    l "覃可汐......那个......"
    hide kexi_pose
    show kexi_pose2 mouth4 at jin
    play audio odoro
    with vpunch
    voice v1
    x "？"
    $ persistent.tips19 = True
    voice v5
    x "哇哦~转校来的第一天就主动跟新同学搭话！你原来也是个{a=showmenu:tips19}{color=#F18D7D}社牛{/color}{/a}吗？厉害！完全看不出来！"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    hide kexi_pose2
    show kexi_pose2 mouth3 at jin
    with dissolve
    voice v1
    x "啊哈哈哈哈......"
    "被覃可汐突如其来的笑声打断了我的提问。"
    "好不容易鼓起的勇气......"
    "不行！这可不行！跟覃可汐的未来相比，我的面子什么都不是。无论我以前是什么态度。从现在开始我所做的一切都必须朝着“覃可汐存活下来”这个未来发展才可以！"
    play music kexi fadein 1.0 fadeout 1.0
    $ times = "15:01"
    l "覃可汐你听我说。那个......你说的“非常感谢”是......是什么意思？方便明说吗？......"
    l "那个......不方便明说的话就算了....如果你也有什么难言之隐的话......"
    hide kexi_pose2
    show kexi_pose eyes2 at jin
    with dissolve
    voice v3
    x "什么啊?哦!你说的是上课之前的那个吗？"
    hide kexi_pose
    show kexi_pose eyes5 mouth3 at jin
    play audio odoro
    with vpunch
    voice v3
    x "你果然已经忘掉了吗？"
    hide kexi_pose
    show kexi_pose eyes3 mouth3 at jin
    play audio odoro
    with vpunch
    voice v3
    x "等等......我真是个笨蛋......这怎么可能......"
    hide kexi_pose
    show kexi_pose eyes2 at jin
    play audio odoro
    with vpunch
    voice v3
    x "我绝对是认错人了哈哈！"
    hide kexi_pose
    show kexi_pose at jin
    voice v3
    x "真是抱歉呢林洛！先前是我太过激动了没有过脑子思考......"
    hide kexi_pose
    show kexi_pose eyes2 at jin
    with dissolve
    voice v5
    x "我认错人了!就是这样!毕竟......你没有发育不良或者其他什么症状的对吧......"
    hide kexi_pose
    show kexi_pose eyes3 at jin
    with dissolve
    x "对吧.......对吧......对吗？"
    "额啊！？"
    $ times = "15:02"
    with vpunch
    "这是什么突如其来的提问？"
    l "没有！"
    l "我一直活的很健康!没有什么疾病和症状！"
    hide kexi_pose
    show kexi_pose2 at jin
    with dissolve
    voice v3
    x "嗯!好吧!那确实是我搞错了!抱歉..............."
    nvle "是这样吗......覃可汐只是单纯认错了人而已......"
    nvle "把我错认成了其他的人。所以才会主动找我搭话吗？原来是这样。"
    nvle "这个应该不会影响到以后事件的发展吧~希望不会！"
    nvl clear
    $ times = "15:03"
    scene bg_tukue
    with fade
    "这件事情基本有了结果。接下来就是得找班长叶梓澄了解关于她父亲的事情了。"
    play music school fadein 1.0 fadeout 1.0
    scene bg_class_naka
    with dissolve
    "我起身走到班长座位面前。"
    show zicheng_pose1  eyes3 at jin
    with dissolve
    "班长仍然是一副苦瓜脸，这幅情景倒是跟上次一样。"
    "等会！？上次？"
    play music lanzhu fadein 1.0 fadeout 1.0
    "我想起来了！上次，也就是时间回溯前的星期一，我找叶梓澄搭话的理由是："
    "询问关于给我硬塞手表的那位摊主的事！"
    hide zicheng_pose1
    show zicheng_pose1 eyes7 mouth3 at jin
    with dissolve
    play music school fadein 1.0 fadeout 1.0
    voice v3
    c "怎么了？新同学？哦！我记得你叫林洛是吧！你好！林洛！"
    voice v3
    c "我是这个班的班长！名字是叶梓澄。你找我有什么事吗？"
    hide zicheng_pose1
    show zicheng_pose2 eyes2 at jin
    with dissolve
    voice v3
    c "让我猜猜......你想了解更多关于这个学校的事情？"
    "我的思考被叶梓澄主动的搭话打断了。"
    l "班长......你听我说......"
    hide zicheng_pose2
    show zicheng_pose1 eyes3 mouth3 at jin
    with dissolve
    c "嗯！我听着呢！"
    l "可以告诉我一些有关你父亲的线索吗？"
    l "我知道你父亲现在失踪了。"
    hide zicheng_pose1
    show zicheng_pose1 eyes6 mouth3 at jin
    with dissolve
    "叶梓澄的营业式笑容突然收了回去。"
    voice v3
    c "可以拜托你跟我出去一趟吗？"
    l "呃~"
    $ times = "15:04"
    scene bg_none
    with fade
    play sound run
    "叶梓澄不由分说的抓住我的手，在其他同学的众目睽睽之下拉着我出了教室门。"
    $ times = "15:05"
    scene bg_1f_kai
    with fade
    "把我拉到了上二楼的楼梯的转角。"
    show zicheng_pose1 eyes6 at jin
    with dissolve
    play music lanzhu fadein 1.0 fadeout 1.0
    voice v3
    c "是AADR派你来的吗？"
    "叶梓澄用强硬的语气向我质问道。"
    "这种语气和我所认识的知书达理的叶梓澄完全不同。就像变了一个人一样。"
    l "呃！"
    scene bg_zicheng_yaru
    with dissolve
    "叶梓澄用双手抓住了我的左右手，将我推倒在墙上。"
    "强有力的手劲让我无法动弹。"
    with vpunch
    l "呃啊~班长你这是干什么？"
    "叶梓澄似乎把我当作了她的敌人。"
    c "我父亲不就是被你们AADR的人绑架了吗？你们还来调查我父亲干什么？难道我父亲不在你们那里？"
    l "等等等等等等等会........班长......."
    l "我我我我我我不是AADR的人......请相信我！"
    with vpunch
    c "你说谎！！！"
    "叶梓澄朝我吼道。"
    c "如果你只是普通的转校生，并且是外地过来的转校生。怎么可能知道关于我父亲的事情！"
    with vpunch
    c "可不要把我看扁了啊混蛋！！"
    "叶梓澄的语气愈发严厉。"
    "这下变成僵局了。"
    "确实我是根本没有理由，也没有渠道了解到关于叶梓澄父亲的事情的。"
    "果然只能实话实说了。"
    with vpunch
    l "我来自未来！！"
    l "我大声说道。"
    "但是肯定叶梓澄不会相信的吧......毕竟这么荒谬的理由。"
    c "哦？"
    $ times = "15:06"
    scene bg_1f_kai
    with dissolve
    show zicheng_pose1 eyes7 mouth3 at jin
    with dissolve
    "叶梓澄紧捏着的手突然放松开来。"
    nvle "真的吗？"
    nvle "她相信了？"
    nvl clear
    l "真的！请相信我！我可以想办法证明！"
    l "你的饭卡上面的图案分别是战场原白仪和斧乃木正弦！"
    hide zicheng_pose1
    show zicheng_pose1 mouth5 at jin
    play audio odoro
    with vpunch
    c "啊！！"
    hide zicheng_pose1
    show zicheng_pose1 mouth5 other2 at jin
    with dissolve
    hide zicheng_pose1
    show zicheng_pose2 mouth3 at jin
    with dissolve
    "叶梓澄的脸突然泛红，头扭了过去。"
    hide zicheng_pose2
    show zicheng_pose1 eyes7 mouth3 at jin
    with dissolve
    "过了一会，又转回来继续看向我。"
    voice v3
    c "这不足以让我信服。还有其他证据吗？"
    "想起来我和叶梓澄一起度过的时光不过短短几天。关于叶梓澄的东西根本了解的不多。"
    "实在是没有更多可以让我自证的关于叶梓澄的信息了。我总不能说两天后叶梓澄父亲的尸体会被找到吧。那肯定会黑上加黑了。"
    l "那个.....没有了......但是请相信我!我来自七天后的未来！！"
    hide zicheng_pose1
    show zicheng_pose2 other2 at jin
    play audio odoro
    with vpunch
    voice v3
    c "真的吗？那你从未来回到现在的时间装置在哪！"
    l "啊！！？我......我也不知道.....我眼睛一闭一睁,就回到过去了。"
    play music speak fadein 1.0 fadeout 1.0
    nvle "于是我把我所经历过的未来的七天时间里所发生的事情一五一十地告诉了叶梓澄。"
    nvl clear
    hide zicheng_pose2
    $ times = "15:09"
    show zicheng_pose2 at jin
    with dissolve
    voice v3
    c "情况我大概清楚了。所以你只是一个不知不觉就被卷进来的普通人？"
    "这句话是什么意思？听叶梓澄这语气，仿佛叶梓澄并不是一个普通人。"
    play sound suzu
    $ times = "15:10"
    "！！"
    "这个时候，上课铃声却不看气氛地响了起来。"
    hide zicheng_pose2
    show zicheng_pose1 eyes7 mouth3 at jin
    with dissolve
    voice v5
    c "林洛！关于更详细的事情，放学后再跟我聊吧。我暂时相信你没有恶意。希望你不要让我失望。"
    l "哦......"
    hide zicheng_pose1
    with dissolve
    "说完叶梓澄便扭头离开了。我也紧随其后。"
    play music sora fadein 1.0 fadeout 1.0
    scene bg_none
    with fade
    stop sound
    nvle "心里有一点说不上的失落。那种被别人怀疑的眼光看待的不安感。"
    nvle "本以为叶梓澄会和我一起帮她父亲幸免于难的。"
    nvle "不过这得怪我，突然就开口询问，是谁都会怀疑的吧。"
    nvl clear
    nvle "不过更奇怪的一点是，叶梓澄似乎从我说出自己来自未来以后，就有一点相信的态度。如果是普通人听我这么说以后。"
    $ persistent.tips21 = True
    nvle "不是嘲讽就是骂我是神经病吧。或者是批判我是被{a=showmenu:tips21}{color=#F18D7D}二次元{/color}{/a}幻想入脑了的无药可救的傻子。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    nvl clear
    play sound suzu
    $ times = "17:30"
    scene bg_tukue
    with fade
    play music school fadein 1.0 fadeout 1.0
    "怀着各种疑惑，终于等到了放学。"
    scene bg_tukue2
    with dissolve
    show zicheng_pose1 at jin
    with dissolve
    "叶梓澄主动走到我的座位旁边。"
    voice v3
    c "林洛！事情去校门口谈吧。我也有很多事情需要向你了解。"
    hide zicheng_pose1
    show zicheng_pose1 at jin:
        xcenter 0.3
    with dissolve
    show kexi_pose eyes4 at jin:
        xcenter 0.6
    play audio odoro
    $ times = "17:31"
    show zicheng1_shadow at jin:
        xcenter 0.3
    with vpunch
    voice v3
    x "哇哦！班长你这是要跟转校生去约会了吗？好快的进展！"
    hide kexi_pose
    show kexi_pose2 mouth4 at jin:
        xcenter 0.6
    with dissolve
    voice v3
    x "没看出来呢！原来班长是这么主动的人！"
    "旁边的覃可汐凑过来打岔了。"
    hide zichceng_pose1
    show zicheng_pose1 eyes4 mouth5 other2 at jin:
        xcenter 0.3
    with dissolve
    hide zicheng1_shadow
    show kexi2_shadow at jin:
        xcenter 0.6
    voice v5
    c "覃可汐并不是你想的这样的！我和林洛是有事情要谈。嗯.......没错！要商量关于校内各种公共设施，以及校规的事情。"
    hide zicheng_pose1
    show zicheng_pose2 mouth3 other1 at jin:
        xcenter 0.3
    with dissolve
    voice v5
    c "毕竟是第一天来我们学校嘛。万一以后违反了什么校规，然后又反过来说是因为我没告诉他，那最后被处罚的可能就有我了。"
    "这口吻，说的我仿佛是个坏学生一样。"
    hide kexi2_shadow
    voice v3
    x "行吧！总之班长你要加油哦！"
    hide kexi_pose2
    with dissolve
    "覃可汐识趣地离开了，但总感觉她似乎误会了什么。"
    hide zicheng_pose2
    $ times = "17:32"
    show zicheng_pose1 mouth3 at jin
    with dissolve
    voice v1
    c "走吧！"
    $ times = "17:42"
    scene bg_schoolmae
    with fade
    "出校门口的时候，天空已经渐渐被染上了橘红色。"
    play music speak fadein 1.0 fadeout 1.0
    show zicheng_pose1 eyes7 mouth3 at jin
    with dissolve
    voice v3
    c "林洛。来继续之前的话题吧！"
    "叶梓澄用坚定的眼神看向我。"
    voice v5
    c "你说过，星期三的时候我会被班主任叫到办公室，并获得关于我父亲的死讯的消息。然后会请假回家参加葬礼对吧。"
    with vpunch
    l "没错！"
    voice v3
    c "那未来的我，有告诉过你，关于我父亲的相关信息吗？"
    l "嗯......"
    "我在脑海中搜索着记忆。"
    "并没有过。毕竟这涉及到个人隐私，我不可能没有任何理由地开口询问，对方也没有任何理由要告诉我。"
    hide zicheng_pose1
    show zicheng_pose2 at jin
    with dissolve
    $ times = "17:43"
    voice v5
    c "其实。我父亲的职业是一名大学老师，兼职民间科研工作者。在这个城市，拥有一座私人研究所。"
    voice v3
    c "倒不如说，当老师是为了给科学研究筹集经费所做的兼职罢了。"
    voice v3
    c "但是研究项目只有我们一家知道。在完全成功之前是不会公布到外界的。"
    l "研究项目......是......"
    voice v3
    c "研究将构成原子的物质悉数转换成特殊的数据化的粒子，并支持传输和还原。"
    voice v3
    c "我知道你可能听不懂，大概就是："
    voice v3
    c "原子的数据化转换和传输。"
    $ times = "17:44"
    hide zicheng_pose2
    show zicheng_pose1 eyes7 mouth3 at jin
    with dissolve
    $ persistent.tips23 = True
    voice v3
    c "你有玩过{a=showmenu:tips23}{color=#F18D7D}也儿夕传说{/color}{/a}吗？"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    $ persistent.tips24 = True
    voice v3
    c "{a=showmenu:tips24}{color=#F18D7D}也儿夕传说：旷野之炊{/color}{/a}。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    l "有玩过。"
    $ persistent.tips25 = True
    $ persistent.tips39 = True
    $ persistent.tips41 = True
    voice v5
    c "那就好理解了。这个研究项目就是致力于实现将{a=showmenu:tips25}{color=#F18D7D}林库{/color}{/a}送到{a=showmenu:tips39}{color=#F18D7D}高塔{/color}{/a}，或者送到{a=showmenu:tips41}{color=#F18D7D}神庙{/color}{/a}的效果。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     
#词典
    "谢谢。已经秒懂了。"
    l "了解了。但是......"
    nvle "我对这个项目仿佛很熟悉。"
    nvl clear
    with vpunch
    l "啊！"
    with vpunch
    l "这不就是AADR正在干的事吗？"
    l "在未来的某节物理课上，老师提到过这个组织！"
    hide zicheng_pose1
    show zicheng_pose2 at jin
    with dissolve
    voice v3
    c "没错！所以我怀疑正是AADR把我父亲抓走了。"
    voice v3
    c "从前天前开始，父亲就和我断了联系。电话打不通，消息也没回。"
    voice v3
    c "我去父亲的研究所查看的时候，发现大门都被撬开了。研究所里面的器材，要么消失了，要么被弄坏了。"
    hide zicheng_pose2
    show zicheng_pose2 other2 at jin
    with dissolve
    $ times = "17:45"
    voice v3
    c "我这才意识到，我父亲可能被谁盯上了。"
    voice v3
    c "从研究所回来以后，我就报了案。"
    l "前天？那或许还有机会。"
    l "你父亲大概是被AADR带走了吧。"
    voice v1
    c "我怀疑就是。"
    l "在未来，电视会报道AADR会在电视发表他们的最新研究成果。"
    l "这个研究成果，看来就是掠夺的你父亲的研究成果没跑了。"
    hide zicheng_pose2
    show zicheng_pose1 mouth3 at jin
    with dissolve
    voice v1
    c "我有考虑到过。"
    voice v3
    c "问题是，我的父亲现在到底身在何方。"
    l "我记得AADR在全世界都有分部。你有调查过，AADR离这里最近的分部是哪儿吗？"
    hide zicheng_pose1
    show zicheng_pose2 at jin
    with dissolve
    voice v1
    c "就在芷柚市。"
    l "啊！？"
    $ times = "17:46"
    "终于知道为什么我是怀疑目标了。"
    l  "所以有可能，你的父亲被带到了芷柚市？"
    l "但是，在未来发现你父亲的遗体的地方应该是沁野市的警察才对。"
    "问题变得棘手了起来。"
    hide zicheng_pose2
    show zicheng_pose1 at jin
    with dissolve
    voice v3
    c "林洛。你知道在未来，警察发现我父亲遗体的地方在哪吗？"
    "这个我确实不知道。"
    l "你父亲失踪前，没有在研究所内留下什么提示信息吗？"
    hide zicheng_pose1
    show zicheng_pose2 at jin
    with dissolve
    voice v3
    c "留下提示信息？这确实像我父亲的作风。"
    voice v1
    c "那............"
    hide zicheng_pose2
    show zicheng_pose1 mouth1 at jin
    play audio odoro
    with vpunch
    voice v3
    c "现在我带你去我父亲的研究所找找吧！"
    hide zicheng_pose1
    show zicheng_pose2 at jin
    with dissolve
    voice v1
    c "但是在那之前。"
    voice v3
    c "我想知道你是怎么实现从未来回到现在的。"
    voice v3
    c "是肉体的移动还是精神上的移动。"
    l "有什么区别吗？"
    $ times = "17:47"
    voice v5
    c "如果是肉体移动的话，同一时间内绝对会有两个你。如果是精神移动的话，则只存在你一个。"
    l "精神上的移动，其实更接近于游戏里的“读档”。"
    l "那我应该是精神上的移动吧。在我经历车祸以后，回到了刚入学进校门的那一刻。"
    voice v3
    c "问题就是，支持你进行时间移动的载体。是什么。"
    voice v3
    c "我之所以会相信你说的话。有一个很重要的原因是。"
    voice v3
    c "我父亲在以前告诉过我，时间旅行是可能的。如果用我父亲的研究成果的话。"
    voice v3
    c "我父亲没有多说什么。只说了时间旅行是可能的，却没有详细介绍原理。"
    voice v3
    c "但是！我相信我父亲说的话。"
    voice v3
    c "我甚至怀疑，你的存在就是我父亲留的一手。"
    l "啊这不可能吧......你的意思是，我之所以可以从未来回到现在，都是得益于你父亲？"
    hide zicheng_pose2
    show zicheng_pose1 mouth3 at jin
    with dissolve
    $ times = "17:48"
    voice v1
    c "大概吧。"
    hide zicheng_pose1
    show zicheng_pose2 at jin
    with dissolve
    voice v3
    c "你身上，有没有什么可疑的物品？"
    voice v3
    c "或者说，是有可能是支持你进行时间旅行的物品？"
    voice v5
    c "需要注意的是，这个物品必须是，在你出车祸的时候在你身上。并且在你入学的时候依然在你身上。"
    voice v3
    c "达不到这个条件的物品请排除。"
    l "物品......啊！！"
    with vpunch
    l "我的手表！！"
    show hold_watch:
        xcenter 0.2
        ycenter 0.5
    with dissolve
    "我举起了我手上戴的电子表给叶梓澄看。"
    l "在我刚入学的时候，也就是今天上午。"
    l "校门口有个摆摊的残疾人，硬塞给了我这块手表。"
    hide zicheng_pose2
    show zicheng_pose2 other2 at jin
    with dissolve
    voice v1
    c "处处都很可疑呢......"
    l "难道这个摆摊的摊主就是你的父亲？"
    hide zicheng_pose2
    show zicheng_pose2 at jin
    play sound odoro
    with vpunch
    hide zicheng_pose2
    show zicheng_pose1 eyes7 mouth3 at jin
    with dissolve
    voice v3
    c "啊......我不清楚。但是有这个可能。"
    hide zicheng_pose1
    with dissolve
    "说着，我指了指旁边的一块地方。"
    l "他就是在这里摆摊的。但是这个时候已经不见了。"
    $ times = "17:49"
    show zicheng_pose2 at jin
    with dissolve
    voice v1
    c "有监控吗？"
    l "保安室肯定有监控。但是......怎么可能给看。"
    voice v3
    c "找个理由就可以了吧！"
    with vpunch
    l "对哟！"
    nvle "但是让我跟陌生人主动对话，很要命。"
    nvl clear
    "内心经历了各种思想斗争以后，我强迫自己，必须这样做！"
    $ times = "17:51"
    scene bg_school_door
    with dissolve
    play sound run
    "我和叶梓澄从校门口跑向保安室的窗口。"
    play music richang fadein 1.0 fadeout 1.0
    l "保安叔叔你好！我是今天刚入学的转校生。今天上午我的身份证好像掉在校门口了。但是现在已经找不到了。"
    l "我可以看看校门口今天上午的监控吗？拜托了！"
    "临阵磨枪现编了个理由，希望有用。"
    "啊！我感觉被我自己说话的语气恶心到了~"
    b "啊？身份证？我今天上午没在外面地上看到有谁掉了身份证啊？"
    l "可能是你去看的时候被别人捡走了吧。"
    l "看看监控，可以吗？"
    with vpunch
    play music lanzhu fadein 1.0 fadeout 1.0
    b "不行！"
    b "如果身份证丢了，就去挂失。就算给你看了监控，又有什么用？"
    b "这外面人来人往的，你就算看到谁捡了身份证，你还能再次找到他？"
    c "也不一定是被人捡了。说不定是掉到了哪个犄角旮旯。但是不看监控很难确定掉到了哪里。"
    "叶梓澄帮我圆场了。"
    c "而且，他报了一个游泳竞赛，就在明天要去到场。而且必须手持身份证才让进赛场。"
    c "挂失的话根本，来不及了。保安叔叔。"
    c "让我们看看监控吧！真的只看校门口今天上午的监控。"
    b "嗯......那好吧！"
    b "看你们面相，不像是坏孩子。那就给你们看看吧。"
    b "先说好！如果找到身份证了，就不能看了。"
    c "行！谢谢叔叔。"
    "计划居然成功了。"
    "但是游泳竞赛是什么鬼啊！我根本不会游泳啊！"
    $ times = "17:53"
    scene bg_none
    with fade
    play music speak fadein 1.0 fadeout 1.0
    "保安在监控屏幕前，切到了今天上午的时间段。"
    "这个窗口就是显示校门口的。"
    $ times = "17:55"
    scene bg_zicheng_terebi
    with dissolve
    "我和叶梓澄坐在屏幕前，仔细移动着监控录像的时间轴。"
    "将录像移动到从我进入镜头作为开始。"
    "整段录像都显示，这个摊主在给我送完手表以后。就开始收摊了。"
    "校门口的监控只能看出摊主收摊以后抱着收起来的布料，往左边推着轮椅，出了监控范围。"
    "将录像时间轴往前面拉，也显示摊主在早自习时间段都过了以后才过来摆摊。并且摊位上空无一物。"
    "很明显不正常。"
    "这个摊主绝对有问题。"
    $ times = "17:57"
    l "接下来打算怎么做？顺着他的轨迹查看监控录像？"
    c "条件允许的话当然可以...."
    c "但是很遗憾，条件并不允许！"
    c "其他的监控恐怕只有警察才有权查看了，光这点难度就很大。"
    c "就算成功了，也会消耗掉大量时间，最后可能错过救人的最佳时机。"
    l "那....."
    c "去我父亲实验室看看吧！"
    "也对。当务之急还是叶梓澄父亲以及覃可汐的事。"
    "这个可疑的摊主暂时放在一边。"
    $ times = "17:59"
    scene bg_school_door
    with dissolve
    play music richang fadein 1.0 fadeout 1.0
    l "谢谢保安！我找到身份证掉在哪了！总之谢谢您允许我们看监控！"
    b "找到了就好啊！以后注意不要再弄丢了！"
    l "嗯！！"
    hide screen watch
    with dissolve
    scene bg_none
    with fade
    "从保安室出来以后。我和叶梓澄打算乘车去他父亲的实验室。"
    "由于摊主一点可追溯的线索都没有了。只能先去实验室调查叶梓澄父亲是否有留下什么线索。"
    stop music
    $ times = "18:32"
    scene bg_kennkyuujya
    with dissolve
    play sound higurashi loop fadeout 1.0 fadein 1.0
    play music kexi fadein 1.0 fadeout 1.0
    "我们到研究所门口的时候，天色已经快慢慢黑下来了。夕阳将天空染成血红色。"
    "没想到这个研究所的选址如此偏僻。从公路沿着一条小路分支一直爬到半山腰。"
    "研究所就掩藏在半山腰的山体下面。周围都是高大的树木。"
    l "这么隐蔽的吗？"
    show zicheng_pose2 at jin
    with dissolve
    voice v3
    c "嗯。我父亲喜欢安静地进行研究。所以选在了这个远离喧嚣的地方。"
    voice v5
    c "也许就是因为研究所周围没有其他住户，所以......才会导致即使AADR来了也没其他人知道吧......唉~"
    hide zicheng_pose2
    $ times = "18:34"
    show bg_kennkyuujya:
        xzoom 1.0  yzoom 1.0
        linear 1.0 xcenter 0.7 ycenter 0.55 xzoom 1.5 yzoom 1.5 
    "研究所大门的锁已经被撬开了。"
    scene bg_kennkyuujya
    with dissolve
    l "所以AADR这个机构。这么暴力的吗？"
    show zicheng_pose2 at jin
    with dissolve
    voice v3
    play music speak fadein 1.0 fadeout 1.0
    c "以前我了解到这个机构的时候，知道它们在全世界招募相关的科研学者。"
    voice v3
    c "大部分都是靠AADR开出的高薪才选择加入AADR。"
    l "所以。AADR其实是希望你父亲加入它们？"
    voice v1
    c "也许是吧。"
    voice v3
    c "但是为什么要武力带走我父亲，这就不得而知了。"
    l "估计是项目谈崩了吧。"
    l "更多细节，恐怕只有你的父亲可以知道了。"
    scene bg_none
    with fade
    stop sound
    "叶梓澄推开研究所的大门。带着我走了进去。"
    $ times = "18:37"
    scene bg_kennkyuujya_naka
    with dissolve
    play music ruins fadein 1.0 fadeout 1.0
    "室内杂乱不堪。"
    "地上有各种瓶瓶罐罐的玻璃碎片。各种仪器和架子七倒八散。"
    "一副经历过劫掠的样子。"
    "找找有什么可以提供帮助的线索。"
    "堆放研究资料的书架也侧翻在了地上。"
    "书架原本应该在的位置的墙后面，是一条像暗道一样的东西，楼梯直通地下。"
    show zicheng_pose2 at jin
    with dissolve
    voice v1
    c "完全被搜刮带走了呢。"
    hide zicheng_pose2
    show zicheng_pose1 eyes7 at jin
    with dissolve
    voice v5
    c "这个书架上，原本是密密麻麻堆放着父亲的研究资料......以及......我最喜欢看的小说......"
    voice v1
    c "全部被带走了。"
    l "这......"
    hide zicheng_pose1
    show zicheng_pose2 at jin:
        xcenter 0.35
    with dissolve
    voice v3
    c "我一直都不知道书架后面有这样一条密道。"
    voice v3
    c "所以上次见到的时候还很疑惑。"
    l "啊？你都不知道吗？"
    voice v3
    c "我父亲从来没跟我提起过这个。"
    voice v3
    c "看来应该是AADR的人在翻东西的时候发现的呢。"
    l "里面可能有什么？"
    voice v3
    c "我查看的时候什么都没有，就算里面原本有什么，也肯定被AADR的人拿走了吧。"
    l "也对。但是进去看看或许可以有什么可以提供帮助的线索。"
    hide zicheng_pose2
    show zicheng_pose1 mouth3 at jin
    with dissolve
    voice v1
    c "那走吧。"
    $ times = "18:40"
    scene bg_kaite
    with fade
    "我掏出手机打开了照明灯，顺着密道一直往下走，叶梓澄紧随其后。"
    $ times = "18:41"
    scene bg_chikashitu
    with dissolve
    "到达了一个地下室。"
    "我在墙上摸索着灯开关。"
    show bg_chikashitu_light
    with dissolve
    "灯打开了。"
    "映入眼帘的依然是被翻乱的场景。"
    "但是墙上延伸出来两根断开的粗线。看起来是给什么仪器供电的设备。"
    "靠墙的还有一个小柜子。理所当然的，抽屉悉数被拉了出来，翻得一干二净。"
    "有一个电脑桌，但是上面只剩下孤零零的显示器了。原本应该放电脑主机的位置，空空荡荡。"
    l "看来有价值的资料都被AADR带走了呢。"
    l "可能你的父亲，并没有来得及留下什么。"
    $ times = "18:42"
    show zicheng_pose1 eyes7 at jin
    with dissolve
    voice v1
    c "也许是吧。"
    "叶梓澄脸上露出了失望的神色。"
    nvle "但是我突然意识到了什么。"
    nvl clear
    with vpunch
    play sound odoro
    l "或许有留下！"
    "我开口道。"
    play music speak fadein 1.0 fadeout 1.0
    l "我们进研究所的时候，可以看到，门是被撬开的对吧。"
    voice v1
    c "嗯。"
    l "这说明，AADR还是花了一番功夫才进到研究所内。"
    hide zicheng_pose1
    show zicheng_pose2 mouth1 at jin
    with dissolve
    voice v3
    c "我父亲一般在室内进行研究的时候，大门都不会锁，只会轻掩。"
    l "或许是你的父亲听到了什么风声。"
    with vpunch
    l "是因为你母亲的事情吧。"
    hide zicheng_pose2
    show zicheng_pose1 eyes7 mouth5 at jin
    with vpunch
    c "你知道我母亲的事情？"
    l "一个星期前，你的母亲被人杀害了。对吧。"
    hide zicheng_pose2
    show zicheng_pose1 eyes7 mouth4 at jin
    with dissolve
    "叶梓澄叹了口气。"
    voice v3
    c "嗯。被本地的一个混混......杀害了....."
    voice v3
    c "虽然警察通过监控拍到了可能是嫌疑人的背影，但是，即便在全市进行搜查都找不到这个人的踪迹了。"
    l "潜逃了？"
    l "或许正是你母亲的去世，让你的父亲嗅到了一点风声。"
    $ times = "18:44"
    hide zicheng_pose1
    show zicheng_pose2 eyes2 at jin
    with dissolve
    voice v3
    c "我父亲平时都是准时回家的。但自从我母亲遇害以后，只到父亲失踪前，都整天只呆在实验室里面了。"
    l "你父亲可能是在试图对抗AADR？"
    voice v3
    c "或许是。不，一定是！我父亲一定是想在AADR找上门前搏一搏。"
    hide zicheng_pose2
    show zicheng_pose2 at jin
    with dissolve
    l "但是目前的情况，你父亲多年的研究成果似乎都被AADR拿走了呢。"
    l "如果你父亲要留下线索的话。你觉得会留在哪？"
    voice v3
    c "现在这个情况，室内已经被弄得一团糟了。就算线索留在里面，很可能也会被AADR发现。"
    hide zicheng_pose2
    show zicheng_pose1 eyes4 mouth3 at jin
    with vpunch
    voice v1
    c "！！"
    hide zicheng_pose1
    show zicheng_pose1 eyes4 mouth1 at jin
    with dissolve
    voice v3
    c "我好像有头绪了！"
    scene bg_none
    play sound run
    "叶梓澄说完。便向着地下室入口跑去。"
    l "呼~呼~"
    $ times = "18:47"
    scene bg_kennkyuujya
    with fade
    "我跟随叶梓澄出了研究所门口。"
    l "叶梓澄。难道说？"
    "出研究所的时候，天已经暗了下来。"
    $ persistent.tips46 = True

    "如果是平时这个时候我还不回家，那就等着吃{a=showmenu:tips46}{color=#F18D7D}皮带炖肉{/color}{/a}了。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     
#词典
    "但是我必须尽我最大的努力改变未来的惨剧。"
    $ times = "18:49"
    scene bg_zicheng_te_gi
    with dissolve
    play sound yabu
    "叶梓澄走到了研究所外面堆放的灌木丛旁边。伸手朝里面摸索着。"
    stop sound
    play sound odoro
    with vpunch
    c "果然有！"
    "叶梓澄说着，从草丛里拿出一个透明塑封袋。"
    scene bg_kennkyuujya
    with dissolve
    show zicheng_pose2 at jin
    with dissolve
    show rejibukuro:
        xcenter 0.2
        ycenter 0.3
    with dissolve
    l "这难道就是你父亲留下来的线索？"
    "塑封袋里装着一本笔记本。"
    voice v5
    c "嗯！一般我父亲都会把开研究所大门的钥匙藏在这个灌木丛里面。每次短暂离开研究所的时候也会把要去处理的事项写在纸上藏在这个灌木丛里面。"
    $ times = "18:51"
    "回到研究所，叶梓澄翻开了笔记本。扉页写着："
    show bg_note_w102
    with dissolve
    nvle "{b}W-1 02{/b}"
    nvl clear
    l "这个编号......是什么意思？"
    c "我...我也不清楚。我父亲平时的研究报告都是直接电脑打印的，也没见过这个格式的编号。"
    c "这个笔记里面的文字都是亲自手写的。"
    l "会不会.....这是你父亲秘密研究项目的笔记？在秘密的地下室里。"
    c "翻开看一看吧！"
    $ times = "18:52"
    show bg_note_7_12
    with dissolve
    play sound book
    play music sora fadein 1.0 fadeout 1.0
    if persistent.time_end1:
        $ persistent.time = 2
    else:
        $ persistent.time = 0
    $ persistent.tips49 = True

    nvle "7月12日。 \n{a=showmenu:tips49}{color=#F18D7D}时间刻校正仪{/color}{/a}还是有点过于危险了，在我将其改造到不足以对世界造成困扰之后再公之于众吧。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     
#词典
    nvl clear
    show bg_note_7_28
    with dissolve
    play sound book
    $ times = "18:54"
    nvle "7月28日。\n这几天的研究已经表明了，向+1维度注入的零子，会在更晚的时间之后才会对目前所处纬度造成干涉。"
    nvle "究竟是零子在到达更高维度的途中消耗了时间呢，还是说，零子在+1维度发生作用需要时间？"
    nvle "或者是？\n+1维度的时间流逝速度实际上要比我们所处维度要慢？"
    nvl clear
    play sound book
    nvle "............"
    nvl clear
    scene bg_kennkyuujya_naka
    with fade
    play music ruins fadein 1.0 fadeout 1.0
    "研究笔记写的很密，基本每页都有关于每次开展研究的记录。"
    play music speak fadein 1.0 fadeout 1.0
    $ times = "18:55"
    $ persistent.time = 1
    l "{a=showmenu:tips49}{color=#BFBFFF}时间刻校正仪{/color}{/a}......是什么？"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say2
    with dissolve
    hide screen tips_say2
    with tipsanime
#词典
    l "还有......+1维度又是什么东西？零子又是什么？"
    show zicheng_pose1 eyes7 mouth3 at jin
    with dissolve
    voice v3
    c "零子我听我父亲跟我说过！"
    voice v3
    c "是我父亲给“由原子再构成而来的可以进行光速运动的特殊粒子”取的名字。"
    l "所以，这个零子，就是你父亲的研究成果吗？"
    hide zicheng_pose1
    show zicheng_pose2 at jin
    with dissolve
    voice v3
    c "对！但是有一点我比较不理解。"
    voice v3
    c "将物质再构成为零子，和零子的光速运动，以及零子的还原成物质的研究项目，其实几年前就已经成功了。"
    voice v3
    c "但是我的父亲却一直没有公布研究成果。并且这几年的研究也没有再跟我说过了。"
    hide zicheng_pose2
    show zicheng_pose2 eyes2 mouth1 other2 at jin
    with dissolve
    voice v3
    c "倒不如说，我父亲从三年前的某一天开始，就变得很奇怪，简直像换了一个人。"
    l "或许答案就藏在这本研究笔记里吧！"
    $ times = "18:58"
    scene bg_none
    with fade
    "叶梓澄继续翻阅着。"
    play sound book
    "有一页尤为特别。笔记本的书签所夹着的那一页。"
    scene bg_note_daisen
    with fade
    l "你父亲不太可能是无意之中夹的书签吧。如果是单纯记录写笔记的进度的话，书签所夹的页面后面依然有大量笔记怎么说。"
    c "看来这是我父亲希望我着重注意的内容呢~"
    "从夹书签的那一页开始翻阅。"
    $ times = "18:59"
    scene bg_note_daisen2
    with dissolve
    play sound book
    with vpunch
    "啊！两页之间，夹着一张纸团！看起来像是从笔记后面空白页面之中撕下来的一小张！"
    play music sora fadein 1.0 fadeout 1.0
    "上面用潦草的字迹写着："
    scene bg_note_kami:
        ypos 0
    with dissolve
    play sound book
    show bg_note_kami:
        ypos 0
    nvle "“我的女儿，当你看到这本笔记的时候，我大概已经遇到了不测了。"
    nvle "AADR这个组织，通过某种途径，了解到了我研究项目以及所取得的成果。"
    nvle "我猜测，这件事跟你母亲的被害有关。所以请原谅我在你母亲去世以后一直夜不归宿。因为我得做好应对AADR的准备。"
    nvl clear
    $ times = "19:01"
    show bg_note_kami:
        linear 1.0 ypos -290
    nvle "因为AADR在了解到它们所追求的东西，已经被我研究出来了的话，是会不计手段的进行强取豪夺的。"
    nvle "先说结论。AADR是不可战胜的。至少以个人的力量是做不到的。"
    nvle "这个机构在全世界都有分部。"
    nvl clear
    $ times = "19:03"
    show bg_note_kami:
        ypos -290
        linear 1.0 ypos -290-290
    nvle "所以。如果某一天你无法联系到我了，请不要来找我了。"
    nvle "我爱你。我亲爱的女儿。"
    nvle "所以我留下了这本笔记。希望你可以继承我的研究。从这页开始，记录的是关于制造对抗AADR的武器的理论方面的研究成果。"
    nvl clear
    $ times = "19:05"
    show bg_note_kami:
        ypos -290-290
        linear 1.0 ypos -290-290-500
    nvle "希望能对你有所帮助。"
    nvle "永远爱你的，爸爸。"
    nvl clear
    scene bg_kennkyuujya_naka
    with dissolve
    show zicheng_pose1 eyes2 mouth4 at jin
    with dissolve
    voice v1
    c "父亲......"
    "随着叶梓澄父亲所留下的文字的阅读，叶梓澄的眼泪也开始滴落了下来。"
    voice v3
    c "让我不要去找他了....."
    l "你父亲早就预见到自己可能会遭遇不测吗？"
    l "既然你父亲都说了AADR是无法战胜的，但却又说留下了关于制造对抗AADR的武器的理论方面的研究成果。这是否存在矛盾？"
    voice v3
    c "我看看，是什么研究成果？"
    $ times = "19:08"
    "叶梓澄继续阅读着笔记。"
    play music speak fadein 1.0 fadeout 1.0
    play sound book
    scene bg_note_3_27
    with dissolve
    $ times = "19:09"
    nvle "3月27日。\n多次的实验结果都指向了同一个答案。位于我们所处的0维度之上的，名为+1维度的更高维度，其中的时间流速要稍慢于我们所处的0维度。"
    nvl clear
    play sound book
    show bg_note_4_19
    with dissolve
    $ times = "19:12"
    nvle "4月19日。\n以零子论为基础的时间旅行是可能的。实现原理是需要将时间旅行者完整转换为零子形态，通过时间刻校正仪内的零之石，注入到+1维度上。"
    nvle "接着在+1维度内光速运动并从+1维度那一侧主动抽出到我们所处的0维度上来。就能到达我们所处维度的位于过去的时间。"
    nvl clear
    nvle "但是目前在技术上的难点，是："
    show bg_note_4_19_2
    with dissolve
    nvl clear
    play sound book
    nvle "目前根据我的理论所制造的零子转换装置，无法完整转换质量太大的物体，人类目前质量相对而言，很难通过我目前制造的零子转换装置全部转换成零子。"
    nvle "即便转换了，所生成的用零子编译成的原子匹配分布表的容量也过大了，目前的技术无法生成数据量如此巨大的原子匹配分布表。"
    nvl clear
    nvle "就算解决了这个难点。还需要解决，所转换成的零子如何在+1维度那一侧主动抽出的问题。"
    nvle "这是需要我继续研究的问题。"
    nvl clear
    hide screen watch
    with dissolve
    nvle "..............."
    nvl clear
    $ times = "19:20"
    show screen watch
    with dissolve
    scene bg_kennkyuujya_naka
    with dissolve
    show zicheng_pose1 eyes2 at jin
    with dissolve
    voice v3
    c "这是？时间机器的制作原理？"
    l "时.........时间机器........."
    "我内心既是震惊也是害怕。但同时还有点莫名兴奋。"
    "心中的中二病之魂要燃烧了。"
    hide zicheng_pose1
    show zicheng_pose1 eyes7 mouth3 at jin
    with dissolve
    voice v3
    c "父亲......原来您一直瞒着我们，一直在默默研究着这么伟大的东西吗？"
    "叶梓澄擦去了脸上的泪水。"
    l "所以，对抗AADR的武器，指的就是时间机器？"
    hide zicheng_pose1
    show zicheng_pose2 at jin
    with dissolve
    voice v3
    c "如果是因为我母亲被害，导致的我父亲的研究项目被泄露给AADR的话。"
    l "你父亲所希望的是？希望你通过你父亲的理论，制造出时间机器？"
    voice v3
    c "说是希望。其实，时间机器已经被造出来了，不是吗？"
    $ times = "19:22"
    l "你的意思是？"
    show hold_watch:
        xcenter 0.2
        ycenter 0.3
    with dissolve
    "我伸出手，继续看了看我的手表。"
    "但是不管怎么看还是就像一块普通的电子表。"
    hide hold_watch
    with dissolve
    voice v3
    c "虽然尚不清楚你这块手表具体的实现原理是什么。但是，很可能跟我父亲提出的时间机器的原理有关。"
    voice v3
    c "我的意思是。你这块手表，可能出自来自未来的我，或者其他得知了我父亲的时间机器原理的人之手。"
    voice v1
    c "目的就是："
    voice v1
    with vpunch
    c "对抗AADR！"
    l "所以......给我手表的那个摊主......其实来自未来？"
    voice  v3
    c "这样一来，事情逐渐说得通了。"
    $ times = "19:23"
    l "所以那个摊主给我这个手表。是希望我能改变未来？是希望我能阻止你父亲被AADR抓走？"
    l "但是那个摊主只给了我手表，什么指示都没有告诉我啊！"
    l "说是说了。但是只说了，让我去找叶梓澄！让我去找你！"
    hide zicheng_pose2
    show zicheng_pose1 eyes7 mouth3 at jin
    with dissolve
    voice v3
    c "那个摊主是这么说的吗？"
    voice v3
    c "看来，那个人也许跟未来的我认识呢。"
    voice v3
    c "不过你能拿到这块手表。至少说明，目前走向跟我父亲所计划的一样。"
    voice v3
    c "他在被AADR抓走之前，就已经计划好了一切。"
    voice v3
    c "这种计划，也就只有提出时间机器原理的我父亲可以想到了。"
    l "那现在开始，我们需要做什么来改变未来。"
    hide zicheng_pose1
    show zicheng_pose2 at jin
    with dissolve
    voice v3
    c "我想想......现在这种情况......"
    voice v5
    c "要么，找到并救出我父亲。但是说实话，这个方法估计不行了。研究资料已经被拿走了，而且父亲就算现在救了出来，AADR肯定也不会善罢甘休。"
    voice v5
    c "要么，找到白天给你手表的那个摊主。但是难度依旧很大。除非一直沿着街道调查监控录像。但是他这么做，一定有他自己的想法和苦衷吧。"
    voice v3
    c "要么，调查并弄清你的手表的各种信息。起码得知道，手表将你送回过去的机制是什么，是否在时间上可控？"
    $ times = "19:24"
    l "这应该怎么调查手表？拆卸？"
    hide zicheng_pose2
    show zicheng_pose2 mouth3 at jin
    with dissolve
    "班长突然摆出了一脸嫌弃的表情。"
    voice v3
    c "真直白呢，林洛。"
    voice v3
    c "如果你认为我们现在的技术可以足够做到拆卸未来科技并组装回来的话，你可以试试。"
    l "这......感觉很难做到。"
    hide zicheng_pose2
    show zicheng_pose1 eyes7 mouth4 at jin
    with dissolve
    voice v3
    c "如果真的把时间机器弄坏了。那就完蛋了。死局了。"
    "叶梓澄摆正了语气，说道。"
    hide zicheng_pose1
    show zicheng_pose2 at jin
    with dissolve
    voice v3
    c "我认为，既然是时间机器，就应该不是只能使用一次。"
    voice v3
    c "或许再大致还原你第一次启动时间机器的条件，就能再次使用。"
    voice v3
    c "同时，根据你的描述，我推测你佩戴的这个时间机器手表，应该是被动启动。"
    l "被动启动？你是指？"
    voice v3
    c "可能是一直在检测某种数值，一旦发现数值异常就启动什么的。当然并不排除手表本身有一个倒计时。"
    voice v3
    c "你只是恰好在倒计时的时候出车祸了而已。"
    voice v5
    c "而且，单纯靠这块手表很难想象能在短时间内将整个身躯转换成零子。当然，未来的科技谁知道呢？说不定已经可以把完整的时间机器做到西卡之石的大小了。"
    voice v5
    c "不过，在你出车祸的时候的那些伤痕，都消失了这一点来看，这个手表很可能只是传输了关键的信息。说不定是传输了你的意识送回过去的身体里了。"
    voice v3
    play sound odoro
    with vpunch
    $ times = "19:26"
    l "时间机器？"
    $ persistent.tips63 = True

    l "但是它是手表而不是{a=showmenu:tips63}{color=#F18D7D}电话电磁炉{/color}{/a}。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     
#词典
    hide zicheng_pose2
    show zicheng_pose1 mouth1 at jin
    with dissolve
    $ persistent.tips64 = True

    voice v3
    c "这一切都是{a=showmenu:tips64}{color=#F18D7D}斯坦因之窗{/color}{/a}的选择！"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     
#词典
    "不愧是老二次元，恐怖如斯。阅番量真不是盖的。"
    voice v3
    c "没想到你也是个很有趣的人呢~就像覃可汐一样。"
    hide zicheng_pose1
    show zicheng_pose2 at jin
    with dissolve
    voice v5
    c "根据大致推测出来的结果。你的手表可能就是这个运行原理。但是究竟怎么样。很可能得再使用一次手表的机能才行了。"
    play music sora fadein 1.0 fadeout 1.0
    l "覃可汐......."
    l "是啊，我最初的目的就是想改变覃可汐死亡的未来。"
    l "但是了解到了这么多东西以后。我开始担心。覃可汐会不会受到世界线收束的影响了。"
    l "我想救覃可汐，但是......会受到世界线收束吗？"
    "叶梓澄认真思考了一会。"
    play music speak fadein 1.0 fadeout 1.0
    voice v5
    c "不！怎么可能！现实和虚构世界还是不一样的。现在连多世界诠释都没办法证明。更别说世界线以及世界线收束这些东西。完全没有依据。"
    l "希望如此。"
    voice v3
    c "你想拯救覃可汐的心情我可以理解。"
    hide zicheng_pose2
    show zicheng_pose1 eyes7 mouth4 at jin
    with dissolve
    play music sora fadein 1.0 fadeout 1.0
    $ times = "19:28"
    voice v3
    c "覃可汐...是班上和我最聊得来的人.....性格开朗，待人大方......还经常主动帮我处理班级事务。"
    voice v3
    c "但是现在，处于一个不上不下的境地。"
    hide zicheng_pose1
    show zicheng_pose2 eyes2 mouth1 at jin
    with dissolve
    voice v3
    c "AADR已经带走了我的父亲。所以就算救了覃可汐。未来也不会有多大改变了。"
    voice v3
    c "AADR还是会像父亲担心的一样，用我父亲的科研成果干出不知道什么事来吧~如果是造福人类的事也好。"
    play music speak fadein 1.0 fadeout 1.0
    voice v5
    c "但是我觉得，既然AADR能在未来用我父亲的研究成果造福人类。那未来的人怎么会坚持造出时间机器回到现在，并给你一块能回到过去的手表呢？"
    "叶梓澄有条不紊地推理着。不愧是科研工作者的女儿啊~"
    hide zicheng_pose2
    show zicheng_pose1 eyes7 mouth3 at jin
    with dissolve
    $ times = "19:30"
    voice v3
    c "所以我大胆猜测：AADR在未来很可能用我父亲的研究成果，不是在造福人类，而是在危害人类！"
    voice v3
    c "反正我是不相信一个靠武力绑架杀害科学家的人，会做对人类有利的事情！"
    l "那班长，你有什么能够破局的方法吗？"
    hide zicheng_pose1
    show zicheng_pose2 at jin
    with dissolve
    voice v3
    c "确实有，但是有风险。"
    l "具体是什么？"
    voice v1
    c "那我开始说了。"
    voice v3
    c "既然你的手表是被动触发，然后把你送回星期一也就是今天的刚进校门的时候。"
    voice v3
    c "我觉得那个来自未来的给你手表的摊主，不会笨到，让你只在我父亲已经被AADR抓走之后的时间内想办法对抗AADR。"
    voice v3
    c "毕竟从未来的世界来到现在，肯定费了不少的精力吧。不会傻到管生不管养的。"
    voice v5
    c "所以我推测。你的手表很可能支持继续将你送回过去。但是这块手表传送到的时间到底是绝对时间还是相对时间，我还不清楚。"
    l "绝对时间和相对时间？"
    voice v3
    c "绝对时间则是，手表设置的送回的时间段就是你刚进校门的那个时间。"
    voice v5
    c "相对时间则是，手表设置的送回时间段是从手表启动机能开始往前推移一段时间。从你出车祸的时间往前推的话，我估计大概是一个星期的长度。"
    voice v3
    c "所以，我希望你做的方法是："
    play music sora fadein 1.0 fadeout 1.0
    voice v3
    c "重演一次，你最开始经历的一周的时间。"
    voice v3
    c "然后验证你的手表能否把你送回周一刚进校门的那一刻。"
    voice v3
    c "也就是说，你需要准确地见证覃可汐的死去，准确地在下周一搭乘那辆会出车祸的公交车。"
    voice v3
    c "如果成功将你送回过去了。那么，我需要你做的事是："
    voice v3
    c "从校门出去，直接找摊主了解详细情况。然后回学校将所有东西和所有经历，告诉给那个时候的我！"
    voice v3
    c "这个方法的风险很大！但是！这是我能想到的最好的的方法了！"
    voice v5
    c "因为我不相信这块手表无法手动设置可以送回的时间。因为如果连这个都做不到的话，就不可能回到我父亲被AADR带走前，并进行阻止了。"
    l "那为什么必须要看着覃可汐死去？只需要我在下周一准确坐上那辆会出车祸的公交车就行了吧！"
    voice v5
    c "因为这都是为了保证未来时间的走向跟你经历过的一致，才能保证还原手表的回到过去的机能。如果覃可汐没有死，可能会由于各种蝴蝶效应，导致下周一的车祸不会出现。"
    l "这.........."
    hide zicheng_pose2
    show zicheng_pose1 eyes7 at jin
    with dissolve
    $ times = "19:33"
    voice v5
    c "林洛.................我也不希望看覃可汐死掉啊！但是现在的死去是为了改变未来以后不会死去。"
    voice v3
    c "这样吧。你和我都先各自冷静地思考一下。你等会再告诉我结论。"
    voice v3
    c "是否愿意采用我的方法，以及，是否愿意不干涉覃可汐的悲剧。"
    scene bg_none
    with fade
    "...................."
    "..............."
    $ times = "19:38"
    scene bg_kennkyuujya_gate
    with fade
    play music kexi fadein 1.0 fadeout 1.0
    "我走出了研究所。顺便呼吸一下新鲜空气。"
    "天色早已黑成一片。研究所内的灯光在我身下拍出长长的投影。"
    "如果我会吸烟的话，这个时候我应该是掏出一根烟然后开始抽吧。"
    "回想着目前的进度。"
    play music speak fadein 1.0 fadeout 1.0
    nvle "只经历了一次死亡，就已经获得了这么多的信息量。看来之前选择去解决叶梓澄父亲的问题果然是正确的啊~"
    nvle "然后，如果每次回到的时间点都是今天的话，那不管怎么样都已经来不及救叶梓澄的父亲了。"
    nvle "未来叶梓澄的父亲的死亡，跟AADR以及叶梓澄父亲自己的研究项目有关系。"
    nvl  clear
    nvle "但是，覃可汐确实是无辜的吧。跟叶梓澄父亲的研究项目也好，AADR想要得到的东西也好，完全没有关系对吧。"
    nvle "只是一个普通的高中生而已。没有跟这些麻烦的东西扯上关系。"
    nvl clear
    nvle "但是！！"
    nvle "却会死掉！"
    nvl clear
    nvle "既然覃可汐和叶梓澄父亲的研究项目没关系，那我采取措施避免覃可汐的偶然事故也不会影响到什么吧~"
    nvle "但是万一蝴蝶效应，导致最后未来朝着更坏的方向发展了。"
    nvle "从长远来看，避免叶梓澄的父亲被AADR抓走，比救覃可汐......更重要......似乎是这样的......"
    nvl clear
    "啊！好复杂！大脑要宕机了！"
    play music sora fadein 1.0 fadeout 1.0
    $ times = "19:40"
    nvle "覃可汐做错了什么，而我又做错了什么，要再看一遍覃可汐的死去。"
    nvle "因为AADR可能在未来危害世界，所以就将阻止事情发生的重担压在我的身上。"
    nvle "我也只是一个普通的高中生啊！只想好好度过学校时光！为什么会卷入这么复杂的事件！为什么那个摊主要特地给我时间机器手表啊......"
    nvl clear
    play music title2 fadein 1.0 fadeout 1.0
    "牢骚发完了，该认真思考对策了。"
    "首先为了确认手表的机能，我必须再经历一次下周一那场噩梦般的车祸。"
    "其次，如果手表再次成功将我带回了过去。我必须趁摊主还在的时候直接质问他更多详细情况。"
    "接着我需要将我获得的所有信息告知那个时候的叶梓澄，并一起讨论更往后的对策。"
    hide screen watch
    with dissolve
    scene bg_none
    with fade
    play music ruins fadein 1.0 fadeout 1.0
    "......"
    ".............."
    "...................."
    $ times = "19:43"
    scene bg_kennkyuujya
    with fade
    show screen watch
    with dissolve
    show zicheng_pose1 at jin
    with dissolve
    voice v1
    c "林洛...你考虑好了吗？"
    l "嗯........."
    l "我决定......"
menu:
     "同意（旁观覃可汐的死亡）":
      jump agree
     "不同意（插手避免覃可汐的死亡）":
      jump disagree
default disagree = False
#
label disagree:
    l "我决定...采用你提出的方法。但是。"
    l "覃可汐这件事上。我果然还是无法冷眼旁观。"
    play music sora fadein 1.0 fadeout 1.0
    l "对不起，叶梓澄。请原谅我。但是我无论如何都不能再看着覃可汐死去了。"
    l "即便在下次回到过去以后，一切都会一笔勾销。"
    l "至少，能让我心里图个安稳。"
    $ times = "19:45"
    hide zicheng_pose1
    show zicheng_pose1 eyes2 mouth4 at jin
    with dissolve
    voice v1
    c "林洛......"
    voice v3
    c "你......跟我道歉个什么劲啊？......"
    hide zicheng_pose1
    show zicheng_pose1 eyes4 mouth4 at jin
    with dissolve
    "叶梓澄擦了擦眼角。"
    voice v3
    c "你能这样说,我反而感到很欣慰。看出来你是真的，希望覃可汐能活下来。"
    voice v3
    c "该道歉的反而是我才对。"
    voice v3
    c "覃可汐确实跟我父亲的事情无关。就算救了覃可汐，应该也不会对未来产生什么大的影响。"
    voice v3
    c "林洛。手表戴在你手上。那个摊主也是选择把手表托付给你。所以，遵从自己内心的选择吧！"
    voice v3
    c "未来的主动权，在你自己的手上！"
    "没错！路是自己走出来的，就算下地狱也一样！"
    play music home fadein 1.0 fadeout 1.0
    hide screen watch
    with dissolve
    scene bg_none
    with dissolve
    "我和叶梓澄喊了夜班的出租车，离开了研究所。"
    "看了我的手机，果不其然，一列列未接来电。是我妈打过来的。"
    "回到家的时候找的理由是，被班主任留在学校补习课程了。"
    "幸运的是我妈信了，而且没有找班主任打电话确认。当然她并没有班主任的手机号就是了。"
    "在我辗转反侧地思考中，星期二到来了。"
    $ years = "2022.9.20"
    $ times = "07:10"
    $ weeks = _("周二")
    play music school fadein 1.0 fadeout 1.0
    $ times = "07:21"
    show screen watch
    with dissolve
    scene bg_2_3
    with fade
    "早早地就到了教室。"
    $ times = "07:22"
    scene bg_tukue
    with dissolve
    "和叶梓澄互换了眼神。"
    play sound run
    "覃可汐这个点还没有到教室。"
    "覃可汐救援计划！{size=50}开始！{/size}"
    play music sora fadein 1.0 fadeout 1.0
    nvle "虽然在我下次使用手表以后，这一周所发生的事情又会一笔勾销。"
    nvle "但是至少可以进行一次模拟，又或者说，可以等叶梓澄的父亲的事情解决以后，就有经验可以真真正正地救覃可汐了。"
    nvle "覃可汐会在本周五中午十二点，死于高空坠落的花盆。"
    nvl clear
    nvle "这很可能只是一个偶然事件。"
    nvle "因此最简单的解决办法是：不将覃可汐安排到星期五的值日。"
    nvle "但是这个办法或许有点带逃避的色彩了。"
    nvl clear
    nvle "如果调走了覃可汐，那周五的值日谁来做？花盆会不会最后砸在被交换的值日生身上？"
    $ times = "07:25"
    x "林洛！你来这么早！"
    x "真是个爱学习的好孩子呢？"
    play sound odoro
    with vpunch
    "在思考的时候，覃可汐进来了。"
    play music school fadein 1.0 fadeout 1.0
    "覃可汐将书包放在了座椅上，便朝我凑了过来。"
    scene bg_tukue2
    with dissolve
    "这......未来已经变动了。很可能是因为昨天的对话和我的异常行为。"
    show kexi_pose eyes4 mouth1 at jin
    with dissolve
    voice v3
    x "原来不是在学习吗？"
    hide kexi_pose
    show kexi_pose2 mouth4 at jin
    play sound odoro
    with vpunch
    voice v3
    x "对不起林洛！我错怪你了。还以为你在背着我偷偷学习。"
    hide kexi_pose2
    show kexi_pose mouth1 at jin
    with dissolve
    voice v3
    x "看到你没有在学习，那我就放心了。嗯，放心了。"
    "怎么反而很开心的样子！？"
    l "原来，你也并不是个爱学习的人吗？"
    hide kexi_pose2
    show kexi_pose mouth3 at jin
    with dissolve
    play sound odoro
    with vpunch
    voice v3
    x "学习？我最讨厌的就是学习了。"
    hide kexi_pose
    show kexi_pose eyes5 at jin
    with dissolve
    $ persistent.tips55 = True
    $ persistent.tips56 = True
    voice v5
    x "唉~高中生活对我来说跟劳动改造一样！谁受得了啊~如果不是条件不允许，我可能就{a=showmenu:tips55}{color=#F18D7D}黑化{/color}{/a}成{a=showmenu:tips56}{color=#F18D7D}沙皇{/color}{/a}了。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    play sound odoro
    with vpunch
    voice v1
    x "等等......也？"
    $ times = "07:27"
    voice v3
    x "林洛你也讨厌学习吗？"
    l "讨厌！只是达不到沙皇“打死不读书”的程度而已。"
    hide kexi_pose
    show kexi_pose2 mouth3 at jin
    with dissolve
    voice v3
    x "哈哈哈哈~"
    voice v3
    x "我们真是臭味相投呢~"
    hide kexi_pose2
    show kexi_pose eyes4 mouth1 at jin
    with dissolve
    voice v3
    x "那个林洛，你的爱好是什么？"
    l "我不是什么都爱好，我只爱好我爱好的！"
    play sound odoro
    with vpunch
    voice v3
    x "啊啊啊啊啊啊啊啊啊啊啊啊！！"
    play sound odoro
    with vpunch
    voice v1
    x "是故事厨！！！"
    play sound school_suzu
    $ times = "07:30"
    scene bg_tukue
    with fade
    "就这样，我们畅谈到了上课。"
    $ times = "07:31"
    "在课上，我终于腾出精力来继续思考对策了。"
    stop sound
    play music speak fadein 1.0 fadeout 1.0
    nvle "不排除扔下来的花盆是人为导致。"
    nvle "但是......校内都有监控。如果真的是有人蓄意谋害覃可汐，应该会被当场抓获吧......"
    nvle "我对这个新学校的情况不太了解，不敢妄下论断，也不敢保证是否有什么隐情。"
    nvl clear
    nvle "这是碰都不能碰的话题。"
    nvl clear
    nvle "当下来看的话。果然最直接的解决办法还是："
    nvle "在星期五中午之前撤掉那个花盆！"
    nvle "就这样。我一边尽量保持和覃可汐的关系，一边考察覃可汐出事的事发地点周围以及每层楼的花盆的位置。"
    nvl clear
    nvle "至于我昨天搬下去的花盆。今天果然被放回了原处。"
    nvle "还是在周五当天处理吧。"
    nvle "至于和覃可汐的讨论的话题，我都尽量保持和我经历过的一致。"
    nvl clear
    hide screen watch
    with dissolve
    scene bg_none
    with fade
    nvle "........."
    $ years = "2022.9.21"
    $ times = "09:01"
    $ weeks = _("周三")
    nvl clear
    show screen watch
    with dissolve
    play music sora fadein 1.0 fadeout 1.0
    s "叶梓澄！你来一下办公室。"
    scene bg_tukue
    with fade
    "星期三了。不出意外的，班主任将叶梓澄叫到了办公室。"
    "这次的叶梓澄，或许是已经提前做好了心理准备。即便是得知了自己父亲的死讯，依旧保持着一副平和的面庞。"
    scene bg_tukue
    with fade
    $ times = "09:03"
    "叶梓澄回到教室以后。径直走到了我的座位前面。"
    play sound desk
    "轻敲了我的桌角。"
    scene bg_tukue2
    with dissolve
    show zicheng_pose1 eyes3 mouth3 at jin
    with dissolve
    voice v3
    c "出来一下。我有话跟你说。"
    show kexi_pose at jin:
        xpos 0.8
    with dissolve
    show zicheng1_shadow at jin
    voice v3
    x "班长？班主任找你出去是有什么事吗？"
    hide zicheng1_shadow
    "覃可汐凑了过来。用一副关心的语气问道。"
    "叶梓澄凝视了一会覃可汐。"
    hide zicheng_pose1
    show zicheng_pose1 mouth1 at jin
    with dissolve
    "接着脸上摆出了营业式微笑。"
    show kexi1_shadow at jin:
        xpos 0.8
    voice v3
    c "没事......谢谢你为我担心。"
    hide kexi_pose
    show kexi_pose eyes4 at jin:
        xpos 0.8
    with dissolve
    hide kexi1_shadow
    show zicheng1_shadow at jin
    voice v3
    x "是吗？好的！"
    hide kexi_pose
    show kexi_pose mouth1 at jin:
        xpos 0.8
    with dissolve
    voice v5
    x "但是班长.........如果你有什么困难的话，不要藏在心里自己一个人承担哟！向我说出来吧！我会尽我所能帮助你的！"
    hide zicheng_pose1
    show zicheng_pose1 eyes2 mouth5 at jin
    with dissolve
    hide zicheng1_shadow
    show kexi1_shadow at jin:
        xpos 0.8
    voice v1
    c "覃可汐......"
    "叶梓澄的脸上，泪珠终于滴落了下来。再也止不住地。流了出来。"
    voice v3
    c "覃可汐........我........."
    scene bg_kexi_te_zicheng
    with dissolve
    $ times = "09:04"
    "覃可汐一把把叶梓澄揽在了怀里，像母亲一样，轻轻拍打着叶梓澄的背。"
    x "嗯......没事的，叶梓澄......谁让我是你的朋友呢......"
    "我的内心深受触动。"
    nvle "覃可汐......我不会让你死掉的！"
    nvl clear
    play music school fadein 1.0 fadeout 1.0
    scene bg_none
    with fade
    "我跟着叶梓澄出了教室。"
    $ times = "09:05"
    scene bg_1f_kai
    with fade
    play music speak fadein 1.0 fadeout 1.0
    show zicheng_pose1 eyes7 mouth4 at jin
    with dissolve
    voice v3
    c "和你的描述一样。发现了...我父亲的遗体。"
    voice v3
    c "而且遗体并不完整，只找到了一只手臂。"
    l "到目前为止。时间的走向都大致跟我所经历过的一致。"
    voice v3
    c "我已经申请离校回家了。所以在那之前。我得跟你把话说清楚。"
    voice v3
    c "我这几天仔细翻阅了我父亲留下来的笔记。查看了除时间机器以外的内容。"
    voice v3
    c "尤其是笔记上所记载的关于“时间刻校正仪”的内容。"
    voice v3
    c "从笔记上所记载的内容来推断。"
    hide zicheng_pose1
    show zicheng_pose1 eyes7 mouth3 at jin
    with dissolve
    voice v3
    c "这个时间刻校正仪。是我父亲制造的仪器。"
    l "这个.....我觉得这一条可以省略。肯定是你父亲制造的。"
    hide zicheng_pose1
    show zicheng_pose1 eyes3 other1 at jin
    with dissolve
    play sound odoro
    with vpunch
    $ persistent.tips57 = True
    voice v3
    c "别打岔。我不是在{a=showmenu:tips57}{color=#F18D7D}原地tp{/color}{/a}。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    hide zicheng_pose1
    show zicheng_pose2 at jin
    with dissolve
    voice v3
    c "时间刻校正仪具有两种机能。"
    voice v3
    c "一种机能是往更高维度注入零子。"
    voice v3
    c "一种机能是从更高维度抽出零子。"
    $ persistent.tips58 = True
    voice v3
    c "我父亲将我们这个维度的编号命名为0。这个编号也是所谓的“{a=showmenu:tips58}{color=#F18D7D}时间刻{/color}{/a}”。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     
    
#词典
    voice v3
    c "而这个更高维度的时间刻则为+1。"
    l "我懂了。原来我们是0。"
    play sound odoro
    hide zicheng_pose2
    show zicheng_pose1 eyes6 other1 at jin
    with vpunch
    voice v1
    c "你先听我说！"
    hide zicheng_pose1
    show zicheng_pose2 at jin
    with dissolve
    voice v5
    c "我父亲认为，+1时间刻的维度，其不能被我们所处的0时间刻的维度所观测到。但是这两个维度之间却可以相互作用。"
    $ persistent.time = 3
    voice v3
    c "{a=showmenu:tips49}{color=#BFBFFF}时间刻校正仪{/color}{/a}的功能便是如此。用作两个维度间数据交换的桥梁。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say2
    with dissolve
    hide screen tips_say2
    with tipsanime
#词典
    voice v3
    c "注入零子的功能便是0时间刻维度作用于+1时间刻维度。"
    voice v3
    c "而抽出零子的功能则是+1时间刻维度作用于0时间刻维度。"
    voice v3
    c "通过往+1时间刻维度注入零子，会导致0时间刻维度产生变化。"
    l "你的意思是？用这个仪器，把零子注入到+1时间刻维度以后，我们所处的这个世界会被影响到？"
    play sound odoro
    with vpunch
    voice v1
    c "对。"
    voice v3
    c "但是具体有哪些影响，我父亲没写在里面。"
    voice v5
    c "往+1时间刻维度注入零子以后，再抽出之前注入的所有零子。可以终止+1时间刻维度对0时间刻维度的干涉。"
    scene bg_kame
    with dissolve
    c "要比喻的话......大概就是 。+1时间刻维度是一口缸。最开始的时候里面是空的。"
    scene bg_kame2
    with dissolve
    c "零子则是水。往+1时间刻维度注入零子就是把水舀进水缸里。从+1时间刻维度抽出之前注入的零子，就是把水缸里的水再舀出来。"
    $ persistent.time = 4
    l "{a=showmenu:tips49}{color=#BFBFFF}时间刻校正仪{/color}{/a}就相当于盛水的水瓢对吧！"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say2
    with dissolve
    hide screen tips_say2
    with tipsanime
#词典
    c "厉害啊林洛，都学会抢答了！"
    scene bg_1f_kai
    with dissolve
    show zicheng_pose2 at jin
    with dissolve
    voice v3
    c "差不多就是这个意思。"
    voice v3
    c "现在我父亲已经遇害了。也就是说，这个时间刻校正仪很可能现在已经在AADR手里了。"
    voice v3
    c "如果未来AADR会利用时间刻校正仪，来做某种影响未来世界的事情。"
    voice v3
    c "估计就是，利用的+1时间刻维度对我们所处的0时间刻维度的干涉。通过时间刻校正仪来改变这个世界的形状。"
    hide zicheng_pose2
    show zicheng_pose1 eyes7 mouth3 at jin
    with dissolve
    voice v5
    c "所以林洛。希望再拜托你一件事。你下次回到过去以后，帮忙调查一下时间刻校正仪的更详细的事情，可以吗？主要是调查对我们世界的干涉是什么。"
    voice v3
    c "我觉得给你手表的摊主大概率知道。然后......照例把调查结果.....告诉给过去的我。"
    l "那个......"
    nvle "我突然想起了什么。"
    nvl clear
    l "如果我下次成功回到过去了。我该怎么把信息传达给你呢？怎么让过去的你信服？"
    hide zicheng_pose1
    show zicheng_pose2 at jin
    with dissolve
    voice v3
    c "此言在理。谨慎的过去的我，可能会对你持有高度警戒。这样的话......"
    voice v1
    c "嗯........"
    hide zicheng_pose2
    show zicheng_pose1 mouth5 other1 at jin
    with dissolve
    $ persistent.tips59 = True
    voice v5
    c "你...............你告诉过去的我。我现在最想要的东西是宝可魔 方/圆的游戏卡带。最希望交换得到的宝可魔是{a=showmenu:tips59}{color=#F18D7D}鸡嘴火龙{/color}{/a}。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    voice v3
    c "你这样说，过去的我绝对会相信你的话了。"
    l "哦...好！"
    $ persistent.tips60 = True
    l "但是......{a=showmenu:tips60}{color=#F18D7D}鸡嘴火兽{/color}{/a}我已经有了。等事情结束以后，通讯交换给你进化吧！"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    voice v3
    c "那....约定好咯！"
    scene bg_none
    with fade
    "................."
    play sound suzu
    play music school fadein 1.0 fadeout 1.0
    $ times = "09:10"
    scene bg_tukue
    with fade
    "上课了。"
    "叶梓澄已经收拾完了东西，离开了学校。"
    "我现在需要做的事情就是等待星期五的到来了。"
    play music title fadein 1.0 fadeout 1.0
    hide screen watch
    with dissolve
    scene bg_none
    with fade
    "剩下这几天，我都尽量还原了我之前所做的事情。"
    "游戏机也借给了覃可汐。"
    $ years = "2022.9.23"
    $ times = "06:36"
    $ weeks = _("周五")
    play music home fadein 1.0 fadeout 1.0
    show screen watch
    with dissolve
    scene bg_home
    with fade
    "星期五到了！"
    scene bg_tvnews
    with dissolve
    tv "AADR美国总部今日展示了他们研究团队的最新研究成果。据悉该研究成果将颠覆未来人们的时空观念......"
    "电视上播放着AADR的新闻。"
    $ times = "06:41"
    scene bg_none
    with fade
    play sound run
    "我抓紧时间吃完早餐以后就直奔学校。"
    $ times = "07:05"
    play music school fadein 1.0 fadeout 1.0
    scene bg_2_3
    with fade
    l "呼~呼~呼~呼~"
    scene bg_tukue
    with dissolve
    "覃可汐还没来。"
    "我记得会跟叶梓澄一块来的。如果是正常情况的话。"
    $ times = "07:28"
    scene bg_tukue2
    with dissolve
    play sound odoro
    $ times = "07:29"
    show kexi_pose mouth1 at jin
    with vpunch
    voice v3
    x "呼~呼~赶上了。"
    l "又通宵打游戏了？"
    show bg_neko
    with dissolve
    voice v3
    x "那个......可不可以......"
    l "没事！你再玩一天吧！"
    play sound odoro
    with vpunch
    x "谢谢！"
    scene bg_none
    with fade
    nvle "剩下的话题便是讨论去漫展的事情了。"
    nvl clear
    play sound suzu
    $ times = "12:30"
    scene bg_tukue
    with fade
    "一转眼到了正午。"
    "和覃可汐约好了12：50在教室见面。"
    stop sound
    $ times = "12:38"
    scene bg_kai4
    with dissolve
    play sound run
    "我也假装去吃饭了。实际上我在各个楼层之间考察花盆的摆放情况。"
    $ times = "12:45"
    scene bg_none
    with fade
    "12点45了。我起身去了教室。"
    "我是故意比原来的我去得早的。"
    $ times = "12:46"
    scene bg_2_3
    with fade
    $ times = "12:47"
    scene bg_class_mae
    with dissolve
    show kexi_pose mouth1 at jin
    with dissolve
    voice v3
    x "啊！林洛你来这么早吗？不错不错！"
    voice v3
    x "那？走吧！早点打扫早点休息！"
    hide kexi_pose
    show kexi_pose2 mouth4 at jin
    with dissolve
    play sound odoro
    with vpunch
    voice v3
    x "我们要悄悄地打扫卫生，然后惊艳所有人。"
    l "那走吧！"
    play sound run
    $ times = "12:49"
    scene bg_school_soto
    with dissolve
    l "我负责右边这块，你负责左边这块可以吗？"
    show kexi_pose2 mouth4 at jin
    with dissolve
    voice v3
    x "嗯！我都无所谓。"
    nvle "我也是故意交换打扫位置的。"
    nvle "说实话我的手开始紧张的发抖了。"
    nvle "成败在此一举。"
    nvl clear
    l "那个！"
    voice v3
    x "怎么了林洛？"
    play sound odoro
    with vpunch
    l "我突然肚子好疼。对不起了。我先去上个厕所。你先继续。"
    play sound odoro
    hide kexi_pose
    show kexi_pose eyes4 mouth3 at jin
    with vpunch
    voice v3
    x "啊.......好吧！"
    play sound run
    play music lanzhu fadein 1.0 fadeout 1.0 
    $ times = "12:51"
    scene bg_none
    with fade
    "我跑进了教学楼。"
    play sound run
    scene bg_kai4
    with fade
    "并不是去了厕所。而是跑到了五楼。"
    play sound run
    $ times = "12:52"
    scene bg_plant
    with dissolve
    "不出所料。花盆还是正摆在阳台边缘。仿佛随时准备坠落下去一样。"
    scene bg_plant_omochi
    with dissolve
    "我小心翼翼地抱起花盆，放在了脚边。然后，在这里原地等待着。"
    "吃饭的学生陆续回来了。一些学生用诧异的眼光看着我。但是我不会放手。"
    $ times = "12:53"
    scene bg_none
    with fade
    "我死死抱着花盆。并监视着楼下广场上覃可汐的一举一动。"
    "她很认真地打扫着广场。"
    "叶梓澄回来了，正在跟覃可汐打招呼。"
    "招呼打完以后。叶梓澄走进教学楼，抬起了头，看向了五楼的我。"
    ".........."
    "..........."
    "............"
    $ times = "12:54"
    "一分钟过去了。"
    $ times = "12:55"
    "两分钟过去了。"
    $ times = "12:56"
    "三分钟过去了。"
    $ times = "12:57"
    "四分钟过去了。"
    "覃可汐还活着。并且左边的广场也依旧打扫完了。看起来正打算过来打扫原本我应该打扫的右侧区域。"
    "我将花盆抱起来，暂时放在了楼梯转角的地上。接着快速冲下了楼。"
    "目前来看，危机应该是解除了。大概率就是一个偶然事件。"
    play music school fadein 1.0  fadeout 1.0 
    $ times = "12:59"
    scene bg_school_hiroba_naka
    with fade
    show kexi_pose eyes2 mouth3 at jin
    with dissolve
    l "啊哈哈哈哈哈~不好意思来晚了......"
    hide kexi_pose
    show kexi_pose2 mouth3 at jin
    with dissolve
    voice v3
    x "没事！不过下次打扫卫生你得加时哦！"
    "覃可汐露出了小恶魔一般的笑容。"
    l "好吧~"
    "我脸上露出失望的神色。但这只是为了掩盖我内心的激动而已。"
    "叶梓澄见我下来了，也从楼里走了出来。"
    $ times = "13:00"
    show zicheng_pose2 at jin:
        xpos 0.2
    with dissolve
    voice v3
    c "林洛！你跑哪去了？快去打扫卫生！"
    voice v3
    c "覃可汐都已经扫完了！"
    voice v3
    c "覃可汐你先回教室吧！反正你的清洁区已经扫完了。"
    hide kexi_pose2
    show kexi_pose mouth1 at jin
    with dissolve
    show zicheng2_shadow at jin:
        xpos 0.2
    voice v3
    x "那我就不客气咯~加油啊林洛！"
    hide kexi_pose2
    show kexi_pose mouth3 at jin
    with dissolve
    voice v3
    x "如果你不希望我在你回教室之前翻阅你画画的本子的话~"
    hide zicheng2_shadow
    "又是小恶魔的笑。"
    "说实话，让覃可汐翻翻反而更好。毕竟这是覃可汐珍贵的相处时光。虽然已经确认危机解除了。"
    "但是下次回到过去以后说不定就不会有这种时光了。"
    hide kexi_pose
    with dissolve
    hide zicheng_pose2
    with dissolve
    $ times = "13:03"
    play sound souji
    "我接过扫把以后，便开始了打扫。"
    "内心是抑制不住的喜悦。一种前所未有的成就感。"
    stop sound
    play sound run
    scene bg_2_3
    with dissolve
    "打扫完清洁区以后，我急匆匆地赶往了教室。"
    $ times = "13:07"
    scene bg_kexi_look
    with dissolve
    x "嗯？这么着急回来睡午觉吗？"
    x "还是说？你画画的本子里有什么不可告人的秘密？"
    "覃可汐端正坐在她的座位上。正翻阅着我拿来画画的本子。"
    play sound odoro
    with vpunch
    "还活着！"
    "此时时间已经快接近下午一点了。"
    l "太好了........."
    x "？"
    $ persistent.tips61 = True
    x "你是{a=showmenu:tips61}{color=#F18D7D}抖M{/color}{/a}吗？为什么我随便翻你的绘画本，你却说太好了。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    play sound book
    $ times = "13:09"
    scene bg_tukue2
    with dissolve
    play sound odoro
    show kexi_pose mouth3 at jin
    with vpunch
    "覃可汐快速把本子盖上，放回了我的座位。"
    voice v3
    x "妈耶~不敢看了。从你的痴汉脸上我感受到一股不祥的气息。"
    l "没事，你看吧。"
    $ times = "13:10"
    play sound suzu
    "午睡时间到了。"
    "覃可汐也后怕着转过头去开始午睡了。"
    scene bg_tukue
    with dissolve
    play music speak fadein 1.0 fadeout 1.0
    "覃可汐的事情解决了。下一个待办事项就是："
    "准时搭乘下周一那辆公交车。"
    "我吞了吞口水。"
    "这意味着。"
    "我必须再次经历那种痛苦，以及死亡。"
    "我开始犹豫了。"
    "既然覃可汐已经救下来了，我真的还有必要继续做下去吗？"
    "未来的事情......跟现在的我没有关系吧........."
    "我只需要过好我的校园生活就圆满了......"
    "......"
    play sound odoro
    with vpunch
    "不可以！！"
    play music sora fadein 1.0 fadeout 1.0
    play sound odoro
    with vpunch
    "叶梓澄会伤心的！！"
    "而且如果任由现在的事态发展下去。我也就只能度过一个和平的学生时期了。"
    "鬼知道AADR会在未来干出什么事。"
    play sound suzu
    $ times = "14:20"
    scene bg_tukue
    with fade2
    "我这样想着，一直没睡着。思考到了下午上课。"
    play music school fadein 1.0 fadeout 1.0 
    $ times = "14:32"
    "天气依旧很闷热。但是天上乌云密布。"
    "用我学过的知识来解释的话，就是要下雨了，空气中水蒸气成分剧增。堵住了毛孔阻挡了人体散热，所以非常热。"
    "教室里的风扇哗啦啦地转着，老师在讲台上叽喳喳地讲着。"
    play sound fan loop fadein 1.0 fadeout 1.0
    $ times = "14:43"
    nan "吱吱吱吱吱吱——————"
    nan "吱吱吱吱吱——————————"
    nan "吱吱吱————————吱吱吱——————————"
    "？"
    "不知道从什么时候开始，教室里出现了奇怪的声音。"
    s "什么声音？"
    "老师也发现了不对。"
    "声音好像是从上面传来的。"
    "我抬起头，观察着天花板。"
    $ times = "14:45"
    scene bg_tennjou
    with dissolve
    "随着吊扇的转动，吱吱声接连不断。"
    s "靠边的同学，把吊扇关一下。好像有点出问题了。"
    "靠近开关的同学关掉了吊扇。"
    nan "吱吱吱吱————————"
    nan "吱吱吱————————————————————"
    "随着吊扇转速的减慢，吱吱声逐渐变小...."
    stop sound
    scene bg_none
    with fade
    play sound ochiru
    stop music
    $ times = "14:46"
    with vpunch
    nan "嘭！！"
    with vpunch
    x "啊！！"
    "突然一阵猛烈的巨响，仿佛发生了什么。"
    play sound yakamashii loop fadein 1.0 fadeout 1.0 
    "教室里又开始喧闹了。"
    "等我回过神来以后，往声源方向看去......"
    stop sound
    play music dead fadein 1.0 fadeout 1.0
    with vpunch
    "啊啊啊啊啊啊啊啊啊啊啊啊！！！！！！"
    scene bg_kexi_shinn2 at shake:
        zoom 1.1
    with fade2
    show bg_syuucyuu:
        alpha 1.0
        linear 1.0 alpha 0.5
        linear 1.0 alpha 1.0
        repeat
    with dissolve
    "一个吊扇挣脱了固定的装置，直直掉了下来。"
    "并且刚好，砸中了覃可汐，和她的后排和右边的同学。"
    "但是吊扇的扇叶，刚好命中了覃可汐的头部。"
    "扇叶，略带倾斜地，插入了覃可汐的头。"
    "覃可汐的头部渗出了血来，昏了过去。"
    "她旁边的受到影响的学生。则是被扇叶和吊扇中心拍打到了头部。"
    nvle "怎么会.........."
    nvle "我明明已经......."
    nvle "怎么还是会......."
    nvl clear
    nvle "为什么.........."
    $ times = "14:47"
    scene bg_none
    with fade
    "老师连忙下了讲台,前来查看情况。"
    s "覃可汐？覃可汐？"
    "发现没有回应以后，老师掏出手机开始拨打急救电话。"
    hide screen watch
    with dissolve
    scene bg_none
    with fade2
    "覃可汐和另外两名同学被救护车送往了医院。"
    "今天下午的课也紧急暂停了。班上提前放了学。"
    play music sora fadein 1.0 fadeout 1.0
    $ times = "17:40"
    show screen watch
    with dissolve
    scene bg_schoolmae
    with fade2
    show zicheng_pose1 eyes2 mouth4 at jin
    with dissolve
    voice v3
    c "林洛...覃可汐她.....又...."
    l "为什么..............."
    l "明明我已经让覃可汐免于高空坠落的花盆了....."
    l "为什么还是会........."
    l "明明在我经历过的最初的时间里，教室里的吊扇并没有出现问题......"
    l "想起来了，那次是因为覃可汐被花盆砸中了，所以教室里下午并没有开吊扇......"
    l "为什么......"
    l "如果说高空坠落的花盆......是偶然事故的话.......坏掉的吊扇......难道也是偶然？"
    voice v3
    c "林洛......"
    hide zicheng_pose1
    show zicheng_pose1 eyes2 mouth5 other2 at jin
    with dissolve
    voice v5
    c "林洛.......你先别责备自己......覃可汐只是被送往了医院......说不定......只是受了伤而已......"
    l "希望是这样......"
    $ times = "17:42"
    hide zicheng_pose1
    show zicheng_pose1 eyes2 mouth1 other2 at jin
    with dissolve
    voice v3
    c "那就这样吧！明天我们一起去医院看望覃可汐吧！顺便了解一下详细情况！"
    l "好............"
    voice v3
    c "好！明天早上，这个校门口见！"
    play music home fadein 1.0 fadeout 1.0
    hide screen watch
    with dissolve
    scene bg_home
    with fade
    "悻悻回到了家中。"
    nvle "真的有这么巧合的事情吗？"
    nvle "连续两次遭遇意外事故。"
    nvle "........."
    nvl clear
    nvle "难道说？真的存在想谋害覃可汐的人？"
    nvle "其在尝试花盆行凶失败以后，便在教室的吊扇上做了手脚？"
    nvle "等明天去探望覃可汐以后再说这些吧。"
    nvl clear
    scene bg_none
    with fade
    "这样想着。我不知不觉进入了睡梦中。"
    ".............."
    "..............."
    "................"
    $ years = "2022.9.24"
    $ times = "01:14"
    $ weeks = _("周六")
    show screen watch
    with dissolve
    play sound ketaisong loop fadein 1.0 fadeout 1.0
    with vpunch
    "嗯？"
    "手机铃声响了。"
    "但是天都还没亮，又或许说，我都没感觉自己睡了多久。"
    scene bg_home
    with fade2
    stop sound
    play sound ketai3
    $ times = "01:15"
    show ketai_zicheng2
    with dissolve
    l "喂？"
    "是叶梓澄打来的电话。"
    voice v3
    c "林洛.......覃可汐她........."
    l "覃可汐怎么了？"
    play music sora fadein 1.0 fadeout 1.0
    voice v1
    c "死了......"
    voice v3
    c "医生说......没抢救过来.......损伤到了大脑......."
    l "........."
    "我说不出话来。"
    voice v1
    c "林洛......"
    play music title2 fadein 1.0 fadeout 1.0
    voice v3
    c "事情既然还是发生了......我希望你......"
    voice v3
    c "先不要管覃可汐的事情了......因为你还有机会......"
    voice v3
    c "所以......请将从这次所经历的事情中所获得的经验，带回到你的下次轮回中去........可以吗？"
    l "好！"
    "我开口了。"
    "既然覃可汐又一次被剥夺了生命，那我就没有再留恋这个未来的理由了。"
    "我需要做的事，是抓住机会，再次回到过去。"
    $ times = "01:17"
    voice v1
    c "林洛......"
    l "？  什么？"
    $ persistent.tips62 = True
    voice v3
    c "不要忘了我......如果你去到的只是一个{a=showmenu:tips62}{color=#F18D7D}平行宇宙{/color}{/a}的话......"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    l "平行宇宙......不会存在的！我坚信没有这种东西！"
    l "这个世界是独一无二的。未来的我，将会和过去的你，再次相遇。"
    l "和过去的你相遇！不是别人！是独一无二的你啊！"
    voice v1
    c "林洛........"
    voice v3
    c "如果真的是这样......那就太好了......"
    voice v3
    c "不会忘记我........真的太好了......"
    l "我会回到过去！将你陪我所做的努力......全都告诉给过去的没有这段记忆的你的！"
    voice v1
    c "嗯......"
    voice v1
    c "我相信你！"
    l "嗯......"
    hide screen watch
    with dissolve
    $ years = "2022.9.26"
    $ times = "07:00"
    $ weeks = _("周一")
    show screen watch
    with dissolve
    play music home fadein 1.0 fadeout 1.0
    scene bg_home
    with fade2
    "星期一了。我这几天做足了心理准备。"
    play music title2 fadein 1.0 fadeout 1.0
    $ times = "07:16"
    scene bg_kuruma_matu
    with dissolve
    "我在车站面前等待着命中注定的那辆公交车。"
    with vpunch
    "来了。"
    play sound car_stop
    scene bg_none
    with fade2
    "公交车缓缓停到我前面。"
    "我大吸了一口新鲜空气，便上了车。"
    play sound run
    "一切都准备好了。直接来吧！"
    stop sound
    play sound "audio/yakamashii.ogg"
    $ times = "07:20"
    n "听说了吗？昨天西路那边十字路口出了车祸，骑电动车的那个直接被撞飞几十米了！"
    "能听到这段对话，说明我并没有坐错车。"
    "我已经极力安慰麻痹自己了。但是我的手脚还是像条件反射似的止不住的颤抖。"
    "那就闭眼吧。"
    "什么都不去想。"
    "静静的等待。"
    play sound "audio/kuruma.ogg"
    $ times = "07:23"
    with vpunch
    "嘭！！！！！！！！！！！！"
    with vpunch
    "！！！！！！！！！！！！！！！！！！！！！！"
    hide screen watch
    with dissolve
    with vpunch
    "来了........."
    with vpunch
    "来........了........."
    stop sound
    $ persistent.disagree = True
    jump chapter2_5
label agree:
    l "我决定.........采用你提出的方法。"
    l "我想明白了。你是正确的。"
    l "我们现在对我这块手表的机能方面的东西还处于摸索阶段。"
    l "稍微有点出入，可能就会导致无法触发手表的功能。最终导致无法回到过去。"
    l "在根基已经被夺走的情况下，就算让覃可汐暂时的避开事件，恐怕也还是治标不治本罢了。"
    play music sora fadein 1.0 fadeout 1.0
    $ times = "19:45"
    nvle "对不起了......覃可汐......"
    nvle "你如果知道了我这样做，就尽情恨我吧。但是我非这样做不可。"
    nvle "请原谅我对你的袖手旁观。"
    nvl clear
    voice v3
    c "好的。我明白了。"
    voice v3
    c "未来就交给你了！"
    play music home fadein 1.0 fadeout 1.0
    hide screen watch
    with dissolve
    scene bg_none
    with dissolve
    "我和叶梓澄喊了夜班的出租车，离开了研究所。"
    "看了我的手机，果不其然，一列列未接来电。是我妈打过来的。"
    "回到家的时候找的理由是，被班主任留在学校补习课程了。"
    "幸运的是我妈信了，而且没有找班主任打电话确认。当然她并没有班主任的手机号就是了。"
    "在我对覃可汐的不安中，星期二到来了。"
    $ years = "2022.9.20"
    $ times = "07:10"
    $ weeks = _("周二")
    play music school fadein 1.0 fadeout 1.0
    $ times = "07:21"
    show screen watch
    with dissolve
    scene bg_2_3
    with fade
    "早早地就到了教室。"
    $ times = "07:22"
    scene bg_tukue
    with dissolve
    "叶梓澄原来的愁眉已经消散了不少。大概是因为从阴霾中看到了希望的关系。"
    "我不会让这唯一的希望变成绝望的。"
    scene bg_none
    with fade
    hide screen watch
    with dissolve
    $ persistent.tips65 = True
    play music title fadein 1.0  fadeout 1.0
    "为了尽量防止未来因为{a=showmenu:tips65}{color=#F18D7D}蝴蝶效应{/color}{/a}而改变。我尽量保持着和覃可汐以及班上其他同学的人际关系。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    "甚至什么时候吃饭，什么时候去洗手间也尽量保持一致。"
    nvle "........."
    $ years = "2022.9.21"
    $ times = "09:01"
    $ weeks = _("周三")
    nvl clear
    show screen watch
    with dissolve
    play music sora fadein 1.0 fadeout 1.0
    s "叶梓澄！你来一下办公室。"
    scene bg_tukue
    with fade
    "星期三了。不出意外的，班主任将叶梓澄叫到了办公室。"
    "这次的叶梓澄，或许是已经提前做好了心理准备。即便是得知了自己父亲的死讯，依旧保持着一副平和的面庞。"
    scene bg_tukue
    with fade
    $ times = "09:03"
    "叶梓澄回到教室以后。径直走到了我的座位前面。"
    play sound desk
    "轻敲了我的桌角。"
    scene bg_tukue2
    with dissolve
    show zicheng_pose1 eyes3 mouth3 at jin
    with dissolve
    voice v3
    c "出来一下。我有话跟你说。"
    show kexi_pose at jin:
        xpos 0.8
    with dissolve
    show zicheng1_shadow at jin
    voice v3
    x "班长？班主任找你出去是有什么事吗？"
    hide zicheng1_shadow
    "覃可汐凑了过来。用一副关心的语气问道。"
    "叶梓澄凝视了一会覃可汐。"
    hide zicheng_pose1
    show zicheng_pose1 mouth1 at jin
    with dissolve
    "接着脸上摆出了营业式微笑。"
    show kexi1_shadow at jin:
        xpos 0.8
    voice v3
    c "没事......谢谢你为我担心。"
    hide kexi_pose
    show kexi_pose eyes4 at jin:
        xpos 0.8
    with dissolve
    hide kexi1_shadow
    show zicheng1_shadow at jin
    voice v3
    x "是吗？好的！"
    hide kexi_pose
    show kexi_pose mouth1 at jin:
        xpos 0.8
    with dissolve
    voice v5
    x "但是班长.........如果你有什么困难的话，不要藏在心里自己一个人承担哟！向我说出来吧！我会尽我所能帮助你的！"
    hide zicheng_pose1
    show zicheng_pose1 eyes2 mouth5 at jin
    with dissolve
    hide zicheng1_shadow
    show kexi1_shadow at jin:
        xpos 0.8
    voice v1
    c "覃可汐......"
    "叶梓澄的脸上，泪珠终于滴落了下来。再也止不住地。流了出来。"
    voice v3
    c "覃可汐........我........."
    scene bg_kexi_te_zicheng
    with dissolve
    $ times = "09:04"
    "覃可汐一把把叶梓澄揽在了怀里，像母亲一样，轻轻拍打着叶梓澄的背。"
    x "嗯......没事的，叶梓澄......谁让我是你的朋友呢......"
    "我的内心深受触动。"
    nvle "覃可汐......我会把未来引导到一个你能无忧无虑的生活下去的世界的！"
    nvle "但是这次...请稍微受点苦痛！"
    nvl clear
    play music school fadein 1.0 fadeout 1.0
    scene bg_none
    with fade
    "我跟着叶梓澄出了教室。"
    $ times = "09:05"
    scene bg_1f_kai
    with fade
    play music speak fadein 1.0 fadeout 1.0
    show zicheng_pose1 eyes7 mouth4 at jin
    with dissolve
    voice v3
    c "和你的描述一样。发现了...我父亲的遗体。"
    voice v3
    c "而且遗体并不完整，只找到了一只手臂。"
    l "到目前为止。时间的走向都大致跟我所经历过的一致。"
    voice v3
    c "我已经申请离校回家了。所以在那之前。我得跟你把话说清楚。"
    voice v3
    c "我这几天仔细翻阅了我父亲留下来的笔记。查看了除时间机器以外的内容。"
    voice v3
    c "尤其是笔记上所记载的关于“时间刻校正仪”的内容。"
    voice v3
    c "从笔记上所记载的内容来推断。"
    hide zicheng_pose1
    show zicheng_pose1 eyes7 mouth3 at jin
    with dissolve
    voice v3
    c "这个时间刻校正仪。是我父亲制造的仪器。"
    l "这个.....我觉得这一条可以省略。肯定是你父亲制造的。"
    hide zicheng_pose1
    show zicheng_pose1 eyes3 other1 at jin
    with dissolve
    play sound odoro
    with vpunch
    $ persistent.tips57 = True
    voice v3
    c "别打岔。我不是在{a=showmenu:tips57}{color=#F18D7D}原地tp{/color}{/a}。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    hide zicheng_pose1
    show zicheng_pose2 at jin
    with dissolve
    voice v3
    c "时间刻校正仪具有两种机能。"
    voice v3
    c "一种机能是往更高维度注入零子。"
    voice v3
    c "一种机能是从更高维度抽出零子。"
    $ persistent.tips58 = True
    voice v3
    c "我父亲将我们这个维度的编号命名为0。这个编号也是所谓的“{a=showmenu:tips58}{color=#F18D7D}时间刻{/color}{/a}”。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     
    
#词典
    voice v3
    c "而这个更高维度的时间刻则为+1。"
    l "我懂了。原来我们是0。"
    play sound odoro
    hide zicheng_pose2
    show zicheng_pose1 eyes6 other1 at jin
    with vpunch
    voice v1
    c "你先听我说！"
    hide zicheng_pose1
    show zicheng_pose2 at jin
    with dissolve
    voice v5
    c "我父亲认为，+1时间刻的维度，其不能被我们所处的0时间刻的维度所观测到。但是这两个维度之间却可以相互作用。"
    $ persistent.time = 3
    voice v3
    c "{a=showmenu:tips49}{color=#BFBFFF}时间刻校正仪{/color}{/a}的功能便是如此。用作两个维度间数据交换的桥梁。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say2
    with dissolve
    hide screen tips_say2
    with tipsanime
#词典
    voice v3
    c "注入零子的功能便是0时间刻维度作用于+1时间刻维度。"
    voice v3
    c "而抽出零子的功能则是+1时间刻维度作用于0时间刻维度。"
    voice v3
    c "通过往+1时间刻维度注入零子，会导致0时间刻维度产生变化。"
    l "你的意思是？用这个仪器，把零子注入到+1时间刻维度以后，我们所处的这个世界会被影响到？"
    play sound odoro
    with vpunch
    voice v1
    c "对。"
    voice v3
    c "但是具体有哪些影响，我父亲没写在里面。"
    voice v5
    c "往+1时间刻维度注入零子以后，再抽出之前注入的所有零子。可以终止+1时间刻维度对0时间刻维度的干涉。"
    scene bg_kame
    with dissolve
    c "要比喻的话......大概就是 。+1时间刻维度是一口缸。最开始的时候里面是空的。"
    scene bg_kame2
    with dissolve
    c "零子则是水。往+1时间刻维度注入零子就是把水舀进水缸里。从+1时间刻维度抽出之前注入的零子，就是把水缸里的水再舀出来。"
    $ persistent.time = 4
    l "{a=showmenu:tips49}{color=#BFBFFF}时间刻校正仪{/color}{/a}就相当于盛水的水瓢对吧！"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say2
    with dissolve
    hide screen tips_say2
    with tipsanime
#词典
    c "厉害啊林洛，都学会抢答了！"
    scene bg_1f_kai
    with dissolve
    show zicheng_pose2 at jin
    with dissolve
    voice v3
    c "差不多就是这个意思。"
    voice v3
    c "现在我父亲已经遇害了。也就是说，这个时间刻校正仪很可能现在已经在AADR手里了。"
    voice v3
    c "如果未来AADR会利用时间刻校正仪，来做某种影响未来世界的事情。"
    voice v3
    c "估计就是，利用的+1时间刻维度对我们所处的0时间刻维度的干涉。通过时间刻校正仪来改变这个世界的形状。"
    hide zicheng_pose2
    show zicheng_pose1 eyes7 mouth3 at jin
    with dissolve
    voice v5
    c "所以林洛。希望再拜托你一件事。你下次回到过去以后，帮忙调查一下时间刻校正仪的更详细的事情，可以吗？主要是调查对我们世界的干涉是什么。"
    voice v3
    c "我觉得给你手表的摊主大概率知道。然后......照例把调查结果.....告诉给过去的我。"
    l "那个......"
    nvle "我突然想起了什么。"
    nvl clear
    l "如果我下次成功回到过去了。我该怎么把信息传达给你呢？怎么让过去的你信服？"
    hide zicheng_pose1
    show zicheng_pose2 at jin
    with dissolve
    voice v3
    c "此言在理。谨慎的过去的我，可能会对你持有高度警戒。这样的话......"
    voice v1
    c "嗯........"
    hide zicheng_pose2
    show zicheng_pose1 mouth5 other1 at jin
    with dissolve
    $ persistent.tips59 = True
    voice v5
    c "你...............你告诉过去的我。我现在最想要的东西是宝可魔 方/圆的游戏卡带。最希望交换得到的宝可魔是{a=showmenu:tips59}{color=#F18D7D}鸡嘴火龙{/color}{/a}。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    voice v3
    c "你这样说，过去的我绝对会相信你的话了。"
    l "哦...好！"
    $ persistent.tips60 = True
    l "但是......{a=showmenu:tips60}{color=#F18D7D}鸡嘴火兽{/color}{/a}我已经有了。等事情结束以后，通讯交换给你进化吧！"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    voice v3
    c "那....约定好咯！"
    scene bg_none
    with fade
    "................."
    play sound suzu
    play music school fadein 1.0 fadeout 1.0
    $ times = "09:10"
    scene bg_tukue
    with fade
    "上课了。"
    "叶梓澄已经收拾完了东西，离开了学校。"
    "我现在需要做的事情就是等待下个星期一的到来了。"
    hide screen watch
    with dissolve
    scene bg_none
    with fade
    play music title fadein 1.0 fadeout 1.0 
    "剩下这几天，我都尽量还原了我之前所做的事情。"
    "游戏机也借给了覃可汐。"
    $ years = "2022.9.23"
    $ times = "06:36"
    $ weeks = _("周五")
    play music home fadein 1.0 fadeout 1.0
    show screen watch
    with dissolve
    scene bg_home
    with fade
    "不安中，星期五到了！"
    $ times = "07:29"
    play music school fadein 1.0 fadeout 1.0
    scene bg_tukue2
    with dissolve
    show kexi_pose mouth1 at jin
    with dissolve
    voice v3
    x "对了林洛！明天的ChieAnime你去吗？"
    hide screen watch
    with dissolve
    scene bg_none
    with dissolve
    "上午和覃可汐尽情讨论了很多东西。看着覃可汐最后的微笑。"
    play sound suzu 
    scene bg_tukue
    with fade
    $ times = "12:30"
    show screen watch
    with dissolve
    play music sora fadein 1.0 fadeout 1.0
    "命运的转折点。中午到了。"
    "我需要做的事就是什么都不做。"
    "只需要看着覃可汐在我眼前死去。"
    "这是计划的一部分。"
    stop sound
    hide screen watch
    with dissolve
    scene bg_none
    with fade
    "......"
    scene bg_tukue2
    with fade
    show screen watch
    with dissolve
    show kexi_pose mouth1 at jin
    with dissolve
    voice v3
    x "所以，就拜托你吃饭的时候快一点点啦！12点50在教室见！"
    l "啊好！"
    scene bg_gohan_tukue
    with fade
    $ times = "12:40"
    "我去食堂吃饭了。"
    "吃的和上次一样的饭菜，坐的和上次一样的座位。"
    scene bg_2_3
    with fade
    $ times = "12:48"
    "在一样的时间点跑回教室。"
    play sound run
    l "呼~呼~"
    "还有一样的腹部剧痛。但是已经无所谓了。"
    scene bg_class_naka
    with dissolve
    show kexi_pose mouth1 at jin
    with dissolve
    $ times = "12:49"
    voice v3
    x "守约了呢！真不错！"
    voice v3
    x "扫把和铲子给你！我们走吧！"
    "覃可汐微笑着。"
    voice v3
    x "怎么了？你看起来像是有什么心事的样子。"
    l "啊.....没事！在想晚上应该吃什么！"
    l "需要做什么？"
    "我虽然已经知道要怎么做了，但还是为了还原过去，所以问道。"
    hide kexi_pose
    show kexi_pose2 mouth1 at jin
    with dissolve
    voice v5
    x "很简单的！把教室正外面的广场打扫一下！然后看看有没有垃圾，清理一下就可以啦！走吧！"
    l "理解了！走吧!"
    hide kexi_pose2
    show kexi_pose2 mouth4 at jin
    with dissolve
    voice v5
    x "要记得一件事哦！必须在午睡之前打扫干净才行。不然检查卫生的干部来了就得扣分了。"
    hide kexi_pose2
    show kexi_pose2 mouth3 at jin
    with dissolve
    voice v3
    x "不过我相信你可以的。"
    "覃可汐微笑着向我打气。"
    scene bg_school_hiroba
    $ persistent.cg11_unlocked = True
    with dissolve
    $ times = "12:52"
    "广场上依旧是很多的人。都是吃完饭以后回来的。"
    "我打扫着广场左侧。覃可汐则负责右侧。"
    "计划最后在中间会合。"
    "跟我所经历过的时间一样的闷热感。"
    "黑压压的乌云，仿佛随时都会降下雨来。或许就是上天在准备祭奠覃可汐的礼炮。"
    show zicheng_pose1 eyes7 at jin
    with dissolve
    voice v1
    c "林洛......"
    c "............"
    hide zicheng_pose1
    show zicheng_pose1 eyes2 mouth1 at jin
    with dissolve
    voice v3
    c "在值日吗？加油啊！"
    "叶梓澄很清楚接下来会发生什么，但还是故作微笑。"
    $ times = "12:55"
    scene bg_none
    with fade2
    "时间差不多要到了。"
    "我不自觉地闭上了双眼。难以忍心再看一遍覃可汐的死亡。"
    play sound "audio/hasai.ogg"
    $ times = "12:56"
    with vpunch
    "嘭！"
    x "啊！！！！"
    play sound yakamashii fadein 1.0 fadeout 1.0 
    "周围的人群开始喧闹了起来。"
    "但是我依然紧闭着眼。"
    "抓着扫把的手在颤抖。"
    stop sound
    nvle "抱歉......覃可汐......"
    hide screen watch
    nvl clear
    nvle "......"
    nvl clear
    play music kexi fadein 1.0 fadeout 1.0
    $ times = "17:44"
    show screen watch
    with dissolve
    scene bg_schoolmae
    with fade
    "放学后和叶梓澄约好在校门口见面。"
    show zicheng_pose1 eyes2 mouth4 at jin
    with dissolve
    voice v1
    c "林洛......"
    voice v3
    c "覃可汐已经........"
    "叶梓澄强忍着泪水没有哭出来。"
    voice v3
    c "已经......“准确的”死去了......"
    l "接下来交给我吧！叶梓澄！"
    nvle "毕竟我可不能让覃可汐白死一次。我会通过我的努力，创造一个覃可汐不会死去的世界！"
    nvl clear
    voice v3
    c "好.......改变未来的战斗。在这个未来上的最后一块拼图......就交给你了......"
    c "................"
    voice v1
    c "最后，林洛，我想。"
    l "什么？"
    voice v3
    c "这大概是身处这里的我和你最后的一次见面了。"
    $ persistent.tips62 = True
    voice v3
    c "如果存在所谓{a=showmenu:tips62}{color=#F18D7D}平行宇宙{/color}{/a}的话......"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    l "平行宇宙这种东西......怎么证明其是否存在呢？"
    voice v3
    c "抱歉......无法证明......"
    l "怎么会呢？我坚信，这个世界是独一无二的。未来的我，将会和过去的你，再次相遇。"
    l "和过去的你相遇！不是别人！是独一无二的你啊！"
    hide zicheng_pose1
    show zicheng_pose1 eyes2 mouth1 other2 at jin
    with dissolve
    voice  v1
    c "林洛........"
    voice v3
    c "如果真的是这样......那就太好了......"
    voice v3
    c "不会忘记我........真的太好了......"
    play music title fadein 1.0 fadeout 1.0
    play sound yousuru
    $ times = "17:46"
    with vpunch
    scene bg_zicheng_te_linluo
    with dissolve
    l "呃啊！！"
    "叶梓澄突然抱了上来,就在黄昏之时的校门口。"
    "我都没来得及做好心理准备，被叶梓澄突然的动作吓了一跳。"
    l "好.....我不会忘了你的！"
    l "我会回到过去！将你陪我所做的努力......一一告知过去的没有这段记忆的你！"
    c "嗯......"
    c "我相信你！"
    l "嗯......"
    hide screen watch
    scene bg_none
    with fade2
    $ years = "2022.9.26"
    $ times = "07:00"
    $ weeks = _("周一")
    scene bg_home
    with fade2
    show screen watch
    with dissolve
    play music home fadein 1.0 fadeout 1.0
    "命运的周一到了。"
    "这几天我已经做好了充足的准备。"
    "再次铭记叶梓澄告知我的事情。"
    play music title2 fadein 1.0 fadeout 1.0
    $ times = "07:16"
    scene bg_kuruma_matu
    with dissolve
    "我在车站面前等待着命中注定的那辆公交车。"
    with vpunch
    "来了。"
    play sound car_stop
    scene bg_none
    with fade2
    "公交车缓缓停到我前面。"
    "我大吸了一口新鲜空气，便上了车。"
    play sound run
    "一切都准备好了。直接来吧！"
    stop sound
    play sound "audio/yakamashii.ogg"
    $ times = "07:20"
    n "听说了吗？昨天西路那边十字路口出了车祸，骑电动车的那个直接被撞飞几十米了！"
    "能听到这段对话，说明我并没有坐错车。"
    "我已经极力安慰麻痹自己了。但是我的手脚还是像条件反射似的止不住的颤抖。"
    "那就闭眼吧。"
    "什么都不去想。"
    "静静的等待。"
    play sound "audio/kuruma.ogg"
    $ times = "07:23"
    with vpunch
    "嘭！！！！！！！！！！！！"
    with vpunch
    "！！！！！！！！！！！！！！！！！！！！！！"
    hide screen watch
    with dissolve
    with vpunch
    "来了........."
    with vpunch
    "来........了........."
    stop sound
    $ persistent.disagree = False
    jump chapter2_5
label chapter2_5:
    "在一阵阵连环爆炸声中。我已经头晕目眩。"
    "果然还是很痛啊！"
    l "呃~"
    "呼吸逐渐变得淡薄。"
    "想最后再看一眼我的手表是否正常......但是不仅眼睛睁不开，而且手也使不上劲了，没有了知觉。"
    "就这样吧..........七天前见!"
    "我放弃了抵抗。静静地等待着死神的降临。"
    stop music
    "...................."
    "............................."
    "..........."
    "...."
    ".................."
    ".........."
    scene bg_none
    with fade2
    with vpunch
    l "呼！！！！"
    l "呼！！！！呼！！！！呼！！！！！呼！！！！！"
    "全身的疼痛已经没了踪影。"
    scene bg_school_basketball
    show eye
    $ renpy.pause(2.7, hard=True)
    hide eye
    with dissolve
    "我缓缓睁开眼睛。校内的风光映入了我的眼帘。"
    play music title fadein 1.0 fadeout 1.0
    l "呼！！！！！呼！！！！！"
    with vpunch
    "叶梓澄你看.......成功了！！！！"
    "成功了！！！！真的太好了！！！！！"
    "这意味着，覃可汐又活了过来。"
    "确认一下手表。"
    $ years = "2022.9.19"
    $ times = "12:27"
    $ weeks = _("周一")
    show screen watch
    with dissolve
    "现在的时间是："
    "2022年9月19日  12：27  星期一！！！"
    "跟上次一分不差。"
    "庆祝完了。该做正事了。"
    "我努力回想着和叶梓澄讨论过的事情。"
    "虽然跟覃可汐的死无关，但是跟叶梓澄的父亲和沁野市的未来有关系的作战方法。"
    "那天，也就是我上次经历的这个星期一的晚上。"
    play sound with1
    scene bg_kennkyuujya_naka
    with dissolve
    show zicheng_pose2 at jin
    show noko
    voice v3
    c "所以，我希望你做的方法是："
    play music sora fadein 1.0 fadeout 1.0
    voice v3
    c "重演一次，你最开始经历的一周的时间。"
    voice v3
    c "然后验证你的手表能否把你送回周一刚进校门的那一刻。"
    voice v3
    c "也就是说，你需要准确地见证覃可汐的死去，准确地在下周一搭乘那辆会出车祸的公交车。"
    voice v3
    c "如果成功将你送回过去了。那么，我需要你做的事是："
    voice v3
    c "从校门出去，直接找摊主了解详细情况。然后回学校将所有东西和所有经历，告诉给那个时候的我！"
    play music speak fadein 1.0 fadeout 1.0
    play sound with1
    scene bg_school_basketball
    with dissolve
    "叶梓澄和我是这样说的。"
    "从校门出去！"
    $ times = "12:29"
    "我再次看了看时间。"
    "12点29！！"
    "现在那个摊主一定还在校门外面。也就是说。这是找他了解这一切的最好机会。"
    play music speak fadein 1.0 fadeout 1.0
    nvle "但是马上就要下课了。而且我该如何从校门出去？"
    nvle "从我前两次的记忆来看，这个学校的管理很严格。"
    nvle "进去了除非放学时候不然就别想出去了。"
    nvl clear
    nvle "赶紧去找老师请假？"
    nvle "不行！哪有刚转学过来第一次遇到老师就说要请假的。"
    nvle "而且等手续批下来的时候，摊主估计早就收摊离开了。"
    nvl clear
    nvle "那......翻墙？"
    nvl clear
    scene bg_none
    with dissolve
    scene bg_school_basketball
    with dissolve
    "我抬头望了望附近的高墙。"
    "不仅高，而且插满了玻璃碎片。到处也都是摄像头。"
    nvle "而且如果因为翻墙被处分了，大概也没有机会找到叶梓澄告知详情了吧。"
    nvl clear
    "果然......只有这一步了吗？"
    "虽然在经历了两次轮回以后，我的对外交际能力已经比最开始好得多了。"
    "但是凭空捏造一个理由去让保安放我出去......"
    "上次是叶梓澄也在场........."
    play sound odoro
    with vpunch
    "林洛啊林洛！拿出你的勇气和决心！"
    play sound odoro
    with vpunch
    "嗯！我必须去做！"
    play sound run
    scene bg_school_nakato
    with dissolve
    play sound suzu
    "我转身走到了校门口保安室。与此同时，下课铃声响了起来。"
    play music lanzhu fadein 1.0 fadeout 1.0
    b "这位同学，你怎么刚进去就往回走了？"
    "那个，我在外面买东西的时候，把钱包落下了。"
    "我得去把找回来。"
    "意外发现我在说谎方面有不错的天赋。一旦正儿八经撒起谎来，就可以做到面不改色。"
    b "嗯......"
    b "快去找吧！"
    play sound saku
    play music richang fadein 1.0 fadeout 1.0
    "保安利索地关掉了电子门的护栏。"
    l "谢谢！"
    "本来想加个称谓“保安叔叔”的，但还是开不了口。"
    play sound run
    scene bg_schoolmae
    with dissolve
    "我快步踏出了校门。寻找着那个摊主的踪影。"
    nvle "让我看看你的庐山真面目吧！"
    nvl clear
    "我在校门口附近张望。"
    with vpunch
    "找到你了！"
    with vpunch
    "摊主果然还在那里！"
    play sound run
    play music lanzhu fadein 1.0 fadeout 1.0
    "我大步走上前来。"
    l "你是谁？"
    $ times = "12:30"
    l "我低头探进遮阳伞内，质问道。"
    show linluo_old_pose other1 at jin
    with dissolve
    voice v3
    t "看来你已经经历过了呢~"
    with vpunch
    voice v1
    t "回到过去！"
    with vpunch
    l "你果然知道这块手表具有回到过去的能力。"
    voice v3
    t "对。我知道。所以我才将这块手表交给了你。"
    l "所以你到底是谁？"
    l "我知道你来自未来，未来到底发生了什么事？"
    voice v3
    t "我是林洛！来自未来的.........林洛！"
    play sound yabu
    hide linluo_old_pose
    show linluo_old_pose at jin
    with dissolve
    "说话间，摊主摘掉了遮挡他脸部的帽子，露出了原本的模样。"
    play sound odoro
    with vpunch
    "什么.......这......"
    $ persistent.tips66 = True
    nvle "这个摊主突然的话，把我大脑搞{a=showmenu:tips66}{color=#F18D7D}宕机{/color}{/a}了。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    nvl clear
    with vpunch
    l "等等.........你是..............我？"
    voice v3
    t "对！我是你！"
    "......."
    "我看向摊主的脸，一副略显苍白的中年模样。确实和我有几分相似。"
    "我一时不知道该从何下手提问什么了。"
    voice v5
    t "你能走到我面前来，就说明你已经经历过了许多磨难，并且已经获取到了很多真相吧。"
    "摊主，不对，是未来的我先开口了。"
    voice v3
    t "我来自10年后的未来。回到2022年的目的只有一个。"
    voice v1
    t "那就是："
    voice v3
    t  "改变 被AADR实行独裁统治的世界的未来。"
    "果然是AADR吗？"
    l "AADR...这个组织...到底在未来干了什么？"
    l "能让你特地回到十年前的现在。"
    play music speak fadein 1.0 fadeout 1.0
    voice v5
    t "AADR利用它们所掠夺的研究成果，胁迫全世界的统治者成为它们的附庸。并以威慑的方式接管了美国政府。建立了人类历史上第一个完全统一的世界帝国。"
    voice v3
    t "虽然他们所吹嘘的是建立一个人类共同进步，没有思想的隔阂的世界。"
    $ times = "12:31"
    voice v3
    t "但这只是虚伪的说辞罢了。"
    voice v3
    t "表面上看，AADR是通过非战争的方式统一了全世界。"
    voice v3
    t "但通过研究的武器胁迫各国政府签署协议，实在称不上是和平统一。"
    voice v3
    t  "并且AADR在接管世界以后，开始实行霸权统治，不断靠武力奴役人们，并建立了它们内部的一套等级制度。"
    voice v3
    t "当然世界各地也是反抗不断。"
    voice v3
    t "但是AADR镇压反抗的方式也是通过他们的武器，不惜伤害无辜地打击所有抗议地区。"
    voice v3
    t "这种暴君统治，导致十年后的2032年，全世界人口骤减了2/5。"
    voice v3
    t "未来的我和叶梓澄侥幸活了下来，并且一直在暗地里对抗AADR，从事着时间机器的研发。只为改变这个未来。"
    l "那.......AADR所用来统一世界，以及镇压反抗的武器究竟是什么？"
    "难道是？"
    with vpunch
    voice v3
    t "时间刻校正仪。"
    l "果然吗？"
    l "我从叶梓澄父亲的研究笔记里了解到了时间刻校正仪具有把零子输送到+1时间刻维度的能力。"
    l "并且+1时间刻维度的零子数增加，会对我们所处的0时间刻维度产生干涉。"
    voice v3
    t "你的进度已经到这里了吗？"
    l "嗯！但是研究笔记里并没有说这个干涉到底是什么。"
    voice v3
    t "我来告诉你吧！"
    with vpunch
    voice v3
    t "覃可汐就是死于这个干涉！"
    l "什么？"
    l "覃可汐.........死于干涉？"
    l "死于由时间刻校正仪向+1时间刻维度输送零子导致的干涉？"
    voice v1
    t "嗯......"
    $ times = "12:32"
    voice v3
    t "你还是乐观地觉得覃可汐只是死于偶然事故对吧！"
    voice v3
    t "但是抱歉，你的幻想被打破了。"
    voice v3
    t "覃可汐的死不是偶然。而是时间刻校正仪被AADR夺走之后的必然。"
    voice v3
    t "这个所谓的干涉！就是增加我们所处纬度的分子结构之间的不稳定性。"
    voice v3
    t "用通俗的话来解释，就是："
    voice v5
    t "会导致各种意外事故，包括天灾人祸的产生概率大大增加。增加的频率跟往+1时间刻维度所注入的零子数量有关。"
    voice v3
    t "这便是......+1时间刻维度对0时间刻维度的干涉的外在表现。"
    voice v3
    t "而第一个受干涉影响的地区.....就是沁野市。"
    voice v3
    t "沁野市会在这个星期五，开始受到干涉影响。"
    voice v3
    t "你看我现在坐着轮椅。是因为我的腿，就是过去的我受干涉影响，变成了残疾。"
    voice v3
    t "不过万幸活了下来。才得以在未来开发出时间机器。"
    l "所以......这个干涉，并不是作用于全世界？"
    voice v3
    t "至少时间刻校正仪刚被夺走的时候，只能作用于使用时间刻校正仪注入过零子的地区。"
    voice v3
    t "因为+1时间刻维度其实是平行于我们所处的0时间刻维度之上的，就是一楼和二楼的关系。"
    voice v5
    t "但是后来AADR应该是对时间刻校正仪进行了某种改造，使其就算不在哪个地区，也能精准对哪个地区产生干涉了。"
    l "你开发的时间机器，也是使用了往+1时间刻维度注入零子的原理吗？"
    voice v3
    t "对！理论基础都来自叶梓澄父亲所保留下来的那份研究笔记。"
    l "关于你所说的东西，让我先消化理解一下。"
    l "AADR利用时间刻校正仪统治了未来的世界。你和未来的叶梓澄开发了时间机器回到现在，目的是为了改变被AADR统治的这个未来？"
    voice v1
    t "嗯。"
    l "那未来的叶梓澄呢？没跟你一起乘坐时间机器吗？"
    "..........."
    "伴随着未来的我的沉默，我似乎猜到了什么。"
    play music sora fadein 1.0 fadeout 1.0
    voice v1
    t "死了........."
    l "是吗？死因呢？"
    $ times = "12:33"
    voice v3
    t "制造时间机器的计划被AADR发现了。是叶梓澄给我争取了搭乘时间机器的时间。"
    "........"
    voice v3
    t "但是没关系的。只要改变了未来，叶梓澄就不会死掉了。"
    l "为什么在我所经历的干涉中，我死了，而你虽然残疾但是一直活到了最后？"
    voice v3
    t "这就是受蝴蝶效应所导致的。"
    l "那.....那为什么....你说覃可汐的死是必然？明明也可以通过蝴蝶效应去阻止覃可汐的死亡对吧！"
    voice v3
    t "覃可汐跟其他人的情况不一样！"
    voice v3
    t "实际上我和叶梓澄有走访调查等方式了解过覃可汐出事之前的行动轨迹。"
    voice v3
    t "很正常，与AADR乃至叶梓澄的父亲都没有交集。"
    play music speak fadein 1.0 fadeout 1.0
    voice v1
    t "但是。"
    voice v3
    t "我们从警察处获取到的关于覃可汐的尸检结果显示，覃可汐的体内存在某种物质。"
    scene bg_zero_stone
    with dissolve
    $ persistent.tips67 = True
    voice v3
    t "其在微观下观测，结构和外观很类似用于制造时间机器和时间刻校正仪的核心部件：{a=showmenu:tips67}{color=#F18D7D}零之石{/color}{/a}。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    l "零之石是什么？"
    voice v5
    t "这是时间刻校正仪和时间机器的最核心的部分。虽然来源和形成原因是个谜，但是叶梓澄的父亲使用这种物质开发出了时间刻校正仪。"
    voice v3
    t "我所乘坐的时间机器的主要机能也靠零之石来实现。"
    voice v3
    t "大概说的话就是。零之石具有一种很奇特的性质。会将涂抹在其上面的零子“吞噬”掉。"
    voice v3
    t "但实际却是，零子涂抹在零之石的表面以后，会透过零之石，进入到+1时间刻维度。"
    l "所以这个所谓“零之石”，是我们所处0时间刻维度与+1时间刻维度之间架设的桥梁一般的存在？"
    scene bg_schoolmae
    with dissolve
    show linluo_old_pose at jin
    with dissolve
    $ persistent.tips68 = True
    voice v3
    t "你有玩过{a=showmenu:tips68}{color=#F18D7D}NC{/color}{/a}吗？"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    play sound odoro
    with vpunch
    voice v3
    t "等会，你肯定玩过了，毕竟你是过去的我。"
    scene bg_nc
    with dissolve
    $ persistent.tips69 = True
    $ persistent.tips70 = True
    $ persistent.tips71 = True
    voice v5
    t "你把零之石想象成类似{a=showmenu:tips69}{color=#F18D7D}上界传送门{/color}{/a}和{a=showmenu:tips70}{color=#F18D7D}未地传送门{/color}{/a}之间的{a=showmenu:tips71}{color=#F18D7D}传送门方块{/color}{/a}就好理解了。和传送门不同的则是，零之石只会让零子通过。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    scene bg_schoolmae
    with dissolve
    show linluo_old_pose at jin
    with dissolve
    l "所以？不管是时间刻校正仪还是时间机器，它们往更高维度注入零子的机能的实现，都是靠的零之石的桥梁功能吗？"
    voice v1
    t "嗯。"
    l "那......从覃可汐身体里发现类似零之石的东西.......意味着什么？"
    scene bg_zero_stone
    with dissolve
    voice v5
    t "虽然我一直都没弄清覃可汐体内的零之石碎屑的来源是什么，但是这种碎屑单体颗粒大小非常小，却零散分布于覃可汐的体内。"
    $ persistent.tips72 = True
    voice v3
    t "或许因为单个零之石碎屑的大小足够小，所以身体并没有产生{a=showmenu:tips72}{color=#F18D7D}排异反应{/color}{/a}。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    voice v3
    t "这些零之石碎屑，就是造成覃可汐遇害的罪魁祸首。"
    $ times = "12:34"
    $ persistent.tips73 = True
    voice v5
    t "因为一旦让+1时间刻维度对0时间刻维度产生干涉。作为传递干涉的窗口的零之石本身，就会发生{a=showmenu:tips73}{color=#F18D7D}共鸣{/color}{/a}。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    voice v3
    t "这种共鸣的外在表现就是会吸引附近的灾厄，也就是使零之石附近的不稳定因素活跃度迅速增加....."
    voice v5
    t "单个零之石产生的共鸣几乎可以忽略不计。但是覃可汐体内无数的零之石碎屑，每一颗碎屑都相当于一扇传递干涉的窗口。"
    voice v3
    t "当这么多的零之石碎屑同时产生共鸣，就会在干涉产生之后吸收大量灾厄。"
    scene bg_schoolmae
    with dissolve
    show linluo_old_pose at jin
    with dissolve
    voice v3
    t "也就是说，从产生干涉的那一刻起，覃可汐本身就变成了一个招灾体质！会不断吸引灾厄降临自身。"
    voice v3
    t "所以......无论怎么做，由AADR导致的干涉产生的共鸣，都会最终杀死覃可汐。"
    voice v5
    t "我想，你应该已经通过自己的实际行动证明了吧！不阻止时间刻校正仪的干涉的话，即便阻止了会导致覃可汐死亡的因素，也依然会有新的因素导致覃可汐死去。"
    if persistent.disagree:
       label chapter2_5_1:
            play music sora fadein 1.0 fadeout 1.0
            l "嗯......"
            l "最开始的覃可汐死于高空坠物的花盆。"
            l "我就尝试着事先拿掉了花盆......但最后覃可汐还是死了。"
            with vpunch
            l "死于教室内坠落的吊扇。"
            voice v3
            t "果然呢。看来叶梓澄的这方面的推论是正确的！"
            voice v3
            t "如果不想办法阻止AADR启动时间刻校正仪对我们所处纬度进行干涉，覃可汐就会死去。"
            jump chapter2_6
    else:
       label chapter2_5_2:
            play music sora fadein 1.0 fadeout 1.0
            "........."
            l "对不起...........我为了验证我是否能准确地回到过去.......选择了袖手旁观......"
            voice v3
            t "你没有错。毕竟随意改变时间的轨迹，可能会导致历史走向另外的一条车辙。"
            l "如果你说的是对的。那就算我阻止了高空坠落的花盆......覃可汐大概也会死掉吧......"
            voice v3
            t "没错。这是叶梓澄在搜集了足够的资料和缜密的论证以后得出的关于覃可汐死亡原因的结论。"
            l "班长......果然还是一直在意着覃可汐么......"
            jump chapter2_6
label chapter2_6:
    play music speak fadein 1.0 fadeout 1.0
    l "所以如果想避免覃可汐的死亡......必须阻止AADR夺走叶梓澄父亲的时间刻校正仪......对吗？"
    play sound odoro
    with vpunch
    voice v1
    t "没错！"
    l "我能做得到吗？"
    voice v1
    t "你...不可能！"
    voice v1
    t "我也不可能。"
    voice v5
    t "AADR是可以为了达到目的不择手段的组织。如果想正面阻止AADR夺走时间刻校正仪，很难。或者说基本不可能。"
    l "我带着警察去呢？"
    $ times = "12:35"
    voice v3
    t "最多只能取得暂时的效果。AADR不会放走这块肥肉的。"
    l "那.......那该怎么做？"
    l "你都专门乘坐时间机器回来了，那你肯定有头绪吧！"
    voice v1
    t "嗯......"
    voice v3
    t "我需要你收集线索，找到AADR盯上叶梓澄父亲的契机。"
    l "你的意思是？通过切断AADR和叶梓澄父亲的联系，从而改变时间刻校正仪被AADR夺走的未来吗？"
    voice v1
    t "没错！"
    l "你都这么说了！所以我这块手表，是可以设置回溯的时间点的对吧！"
    voice v1
    t "是可以的。"
    voice v3
    t "但是受机器大小和技术的限制，最多只能把你送回半个月前，也就是15天前。"
    l "如果调查以后发现AADR在15天以前就知道了叶梓澄父亲的研究项目了呢？"
    voice v3
    t "如果是那样的话就没办法了。那就在AADR来之前毁掉时间刻校正仪吧！！！"
    $ persistent.tips74 = True
    voice v3
    t "如果最后是这种情况，这就是{a=showmenu:tips74}{color=#F18D7D}计划C{/color}{/a}！"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    l "我明白了！"
    l "但是我还想知道更多！ "
    voice v3
    t  "你问吧！我知道的东西都会告诉你的。"
    l "我这个手表是如何实现把我送回过去的？"
    l "也跟时间机器的原理一样吗？"
    voice v5
    t  "原理一样。但是你的手表只是个发送端。会不断将你的大脑内海马体内的记忆拷贝存储为带有数据的零子，保存在手表内。"
    voice v5
    t "在检测到佩戴者心跳停跳两分钟，或者检测到手表受到猛烈重击或者高低温损害的一瞬间，将存储的最后的记忆。"
    voice v3
    t "发送到我的时间机器内。通过时间机器的机能之一，将接收到的零子送回过去。"
    voice v3
    t "被送回过去的记忆会搜寻数值与本人最匹配的大脑并转换成脑电波，存储进搜寻到的大脑。"
    voice v3
    t "用简单的话说的话。会在你死的时候把你的记忆复制一份并发送到过去的你的脑子里。"
    voice v3
    t "货真价实的回到过去的时间机器！"
    l "是这样吗？"
    $ times = "12:36"
    l "那当你和我处在同一时空的时候，记忆的传输不会串号吗？在检索到有两个本人的大脑的时候！"
    voice v1
    t "人是会变的。"
    $ persistent.tips75 = True
    voice v3
    t "计算机中不是存在一种名为“{a=showmenu:tips75}{color=#F18D7D}哈希值{/color}{/a}”的东西吗？"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    voice v3
    t "你的大脑跟我的大脑，内部的记忆虽有共同的地方，但是更多的是不共同的记忆。"
    voice v3
    t "我脑中的记忆，是堆积过很多年的，这个过程中也消失过很多记忆。"
    voice v3
    t "就跟哈希值类似，最后系统检测出来的还是独一无二的个体。"
    $ persistent.tips76 = True
    l "就跟...{a=showmenu:tips76}{color=#F18D7D}忒修斯之船{/color}{/a}一样吗？"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    voice v3
    t "倒也不完全一样，记忆的忒修斯之船，组成部分是记忆数据的不断更换，但其实脑细胞是会一直存活的。"
    l "总之不会让记忆进错脑子对吧！"
    voice v1
    t "没错！"
    l "但是我还有更多疑问。"
    voice v3
    t "你问吧，我能回答的话都会回答你的。"
    l "为什么你都回到了现在的时代了，还是要让我来完成这个事情，你肯定有准备对抗AADR的武器吧！"
    voice v3
    t "因为我能搭乘时间机器就已经够勉强了。我目前的身体状况并不足以支撑我去做这种事。"
    voice v3
    t "至于对抗AADR的武器......就是你手上这块手表，没有其他的了。"
    l "那，为什么选择了我，而不是这个时代的叶梓澄。不管是知识储备还是应对紧急情况的能力，叶梓澄都要比我强很多吧。"
    voice v3
    t "你和她才刚认识这么点时间，就已经看出了叶梓澄的才能吗？"
    voice v3
    t "其实，我已经不想再让叶梓澄牵扯进这个事件了。"
    voice v3
    t "如果我把手表交给她，这便意味着，叶梓澄将会经受不断地轮回，我已经不想让她再承受这种痛苦了。"
    voice v3
    t "而且我相信过去的我，也就是你的能力！"
    voice v3
    t "也相信，你有着对抗AADR和拯救覃可汐的决心。"
    "............."
    l "好！我会改变未来的。用我自己的努力！"
    l "但是..."
    l "我还有关于这个手表的机能的问题。"
    l "这个手表，传输记忆到过去的时间，是绝对时间还是相对时间？"
    voice v3
    t "绝对时间！并且手表所显示的时间会跟我时间机器里面的时间同步。"
    voice v3
    t "而我时间机器里的时间又是实时获取所在时间段的各项数据精准地计算出来的。"
    l "还有问题。这块手表难道就只能被动触发吗？能不能我主动触发，让记忆发送回过去？"
    voice v1
    t "是可以的！"
    l "那你为什么一开始不告诉我这些？我已经经历了两次死亡了，很痛苦的！"
    "我脾气起来了。为什么未来的我要这样整我。"
    voice v3
    t "这确实是我的问题，但是我是考虑到。初次见面的你不太可能听我讲这么多东西。"
    voice v3
    t "有些事情，只有亲身经历过一遍，才能理解，不是吗？"
    play music title fadein 1.0 fadeout 1.0
    voice v3
    t "已经说了这么多了。"
    voice v3
    t "你该出发了。"
    voice v3
    t "该回学校了。"
    voice v3
    t "我就在这里，等你的关于AADR的动机的调查结果。"
    voice v3
    t "你先把手表摘下来一下。"
    l "啊？干什么？"
    $ times = "12:37"
    voice v3
    t "摘下来给我就行！"
    l "哦...好！"
    hide screen watch
    with dissolve
    "........."
    "............"
    voice v3
    t "好了！戴上吧！"
    voice v3
    t "现在的时间是12点38！"
    voice v3
    t "我把你的手表的记忆送回时间点设置为了今天的12点40！"
    voice v3
    t "也就是两分钟以后！"
    $ times = "12:38"
    show screen watch
    with dissolve
    voice v3
    t "好了！你在这里呆三分钟了再进学校吧！"
    l "所以我下次轮回，会直接回到12点40吗？"
    voice v1
    t "嗯。"
    voice v3
    t "如果想主动触发记忆传送。就在手表的显示屏上面画下手势吧。"
    "........."
    nvle "未来的我给我在空中演示了一遍。"
    nvl clear
    l "懂了！遇到希望回到过去的时候，只需要手放在手表上画出这个手势，就可以回到过去了对吧！"
    play sound odoro
    with vpunch
    voice v1
    t "没错！"
    voice v3
    t "大概就这样吧！我在这里等你的好消息！"
    voice v3
    t "这对我来说，只需要等两分钟以后，对你来说，则可能是一个星期的时间了！"
    l "那~两分钟后再见！！"
    $ times = "12:41"
    scene bg_school_basketball
    with dissolve
    "12点41了，我大步走进了校门。"
    nvle "我手上戴的，不是手表，而是未来！"
    nvle "AADR！我会打碎你们的阴谋的！！"
    nvl clear
    jump chapter3