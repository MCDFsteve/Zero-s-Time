label chapter3:
    hide screen quick_menu_full
    hide screen watch
    call disable_shortcut from _call_disable_shortcut_3
    $ persistent.chapter3 = True
    $ persistent.chapter==3
    $ persistent.extra_chapter3 = True
    $ persistent.achievement_chapter2 = True
    image chapter3 ="chapters/chapter3.webp"
    scene bg_none
    $ quick_menu = False
    show chapter3
    with fade2
    $ renpy.pause(5, hard=False)
    hide chapter3
    with fade2
    scene bg_none
    $ quick_menu = True
    call enable_shortcut from _call_enable_shortcut_3
    $ save_name = "{font=Huayuan.Gothic.Bold.ttf}章节三：收束迷宫的展露{/font}"
    play music school fadein 1.0 fadeout 1.0
    $ times = "12:45"
    show screen watch
    scene bg_2_3
    with fade2
    "我走进教室的时候，里面已经空无一人了。"
    scene bg_tukue
    with dissolve
    "我只好自己走到我的座位上坐着。"
    $ times = "12:47"
    scene bg_tukue
    with dissolve
    "过了一会，班主任来了。"
    show sensei1_pose eyes2 at jin
    with dissolve
    voice v1
    s "你是？"
    l "老师你好，我叫林洛。是新来的转校生。"
    hide sensei1_pose
    show sensei1_pose at jin
    with dissolve
    voice v3
    s "哦~之前保安打电话跟我说了。"
    voice v3
    s "我是你的新班主任，叫我李老师就可以了。"
    voice v3
    s "既然你自己选了一个座位的话，那你就坐那里吧！刚好那个位置是空出来的。"
    l "好的！谢谢老师！"
    $ persistent.tips77 = True
    nvle "毕竟这个座位我已经坐了两个礼拜了。已经有{a=showmenu:tips77}{color=#F18D7D}肌肉记忆{/color}{/a}了。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    nvl clear
    $ times = "12:49"
    scene bg_tukue
    with fade2
    play music speak fadein 1.0 fadeout 1.0
    "我现在首要的事情，就是继续执行叶梓澄的计划。"
    "计划的上半部分：回到过去。我已经完成了。"
    "接下来是下半部分：将我获得的所有情报告诉给这个时间的叶梓澄。"
    scene bg_tukue
    with fade2
    $ times = "12:55"
    play sound run
    "在漫长的等待中，叶梓澄终于回到了教室。"
    "跟随着一起的，则是覃可汐。"
    "我得找一个合适的时机，告诉叶梓澄这些事情。"
    play music school fadein 1.0 fadeout 1.0
    scene bg_tukue2
    with dissolve
    show kexi_pose eyes4 mouth3 at jin
    with dissolve
    play sound odoro
    with vpunch
    voice v3
    x "诶？这个位置？" 
    voice v3
    x "你是新来的转校生吗？"
    l "嗯。"
    hide kexi_pose
    show kexi_pose at jin
    with dissolve
    voice v3
    x "转校生......你的名字是？"
    l "林洛。"
    hide kexi_pose
    show kexi_pose2 mouth1 at jin
    with dissolve
    voice v3
    x "林洛......真是个不错的名字呢~那，希望你能融入到我们这个学校的氛围中！"
    l "嗯！我会努力的！"
    hide kexi_pose2
    show kexi_pose eyes4 at jin
    with dissolve
    voice v3
    x "嗯......你......好眼熟？"
    $ times = "12:56"
    voice v3
    x "你是从外地转学来的吗？还是说就是沁野市本地人？"
    nvle "出现了！每次初见覃可汐都会听到的提问！"
    nvle "不得不说，这也算一种奇妙的缘分吧！"
    nvl clear
    l "也许.....有见过吧！"
    hide kexi_pose
    play sound odoro
    show kexi_pose eyes4 mouth3 at jin
    with vpunch
    voice v3
    x "啊嘞！？我都没问是不是见过面！是读心术吗？"
    hide kexi_pose
    show kexi_pose2 mouth1 at jin
    with dissolve
    voice v3
    x "不过......既然你都这么说了.....也许是吧......"
    nvle "跟上一次通过手表回到过去相比，我自己也感觉到，自己对覃可汐的事情并没有那么关心了。"
    nvle "可能是因为，这次的我，已经有了一个明确的目标吧！"
    nvle "比起上次那个单纯天真的我。现在的我已经明白了。"
    nvl clear
    nvle "想要避免覃可汐的逝去，并不是一件容易的事。"
    nvle "这次的未来也不是我要选择的那个未来。毕竟获取到AADR关于叶梓澄父亲研究项目的相关信息以后，就要继续回到过去了。"
    nvle "在这次的时间里，还是不要保留太多感情比较好。这也是为了大局的一部分。"
    nvl clear
    "我心里想到。"
    nvle "这......"
    nvle "我似乎想起了什么。"
    nvle "我并没有询问来自未来的我一个很重要的问题。"
    nvl clear
    nvle "我每次回到过去的话。"
    nvle "那个被我抛弃的未来，是会被过去的改变的未来所覆盖，还是说？"
    nvle "单独独立出来成为一个分支的平行世界？"
    nvl clear
    nvle "怎么样都好，等下次回到过去以后，再询问他吧！"
    nvl clear
    $ times = "13:10"
    scene bg_tukue
    with fade
    play sound suzu
    "在我思考的时候，午睡铃已经响了。"
    "覃可汐和叶梓澄也都回到了自己的座位上。"
    stop sound
    hide screen watch
    with dissolve
    scene bg_none
    with fade
    $ times = "14:21"
    show screen watch
    with dissolve
    "到了下午，我依旧是上台做自我介绍。"
    hide screen watch
    with dissolve
    play sound suzu
    scene bg_zicheng_tukue
    with dissolve
    $ times = "15:00"
    show screen watch
    with dissolve
    "一下课，我立刻找到叶梓澄。"
    "虽然前几次我确实也是找了。"
    show zicheng_pose1 eyes7 at jin
    with dissolve
    "叶梓澄依旧是满面愁容的样子。至于发愁的原因，我也知道是什么了。"
    $ times = "15:01"
    l "班长......可以出来一趟吗？"
    hide zicheng_pose1
    show zicheng_pose1 eyes7 mouth1 at jin
    with dissolve
    voice v3
    c "啊！是转校生啊！我记得你叫.....林洛？"
    voice v3
    c "说吧！有什么是需要我帮忙的吗？"
    l "跟我出来吧！"
    c "............."
    voice v3
    c "嗯嗯.....行！如果在教室里你不好开口的话！"
    voice v3
    c "那走吧！去哪！"
    l "走廊上二楼的楼梯转角怎么样？"
    voice v3
    c "嗯....好吧！不过新来的转校生就清楚学校的构造，确实让我有点意外呢！"
    l "哈哈......"
    "不知道怎么解释就只能尬笑了。"
    scene bg_1f_kai
    with dissolve
    show zicheng_pose1 eyes7 mouth1 at jin
    with dissolve
    $ times = "15:03"
    "到了转角。"
    "我顿了顿口气。说道："
    l "我接下来要说的话，请你务必相信！"
    voice v3
    c "嗯...你先说！"
    play music lanzhu fadein 1.0 fadeout 1.0
    l "你现在最想要的的东西是宝可魔 方/圆的游戏卡带。最希望交换得到的宝可魔是鸡嘴火龙。"
    l "你的饭卡正面是战场原白仪，反面是斧乃木正弦。"
    l "你父亲是一名科研人员，在沁野市的一座山的半山腰修建了一所私人研究所。"
    l "现在失踪了。并且你怀疑是被AADR所带走。"
    hide zicheng_pose1
    show zicheng_pose1 eyes3 mouth3 at jin
    with dissolve
    "叶梓澄的营业式笑容凝固了。"
    hide zicheng_pose1
    show zicheng_pose1 eyes4 other2 mouth5 at jin
    with dissolve
    "脸也不自觉红了起来，将头扭向一旁。"
    hide zicheng_pose1
    show zicheng_pose2 mouth3 at jin
    with dissolve
    "这个场景在我上次经历的时候见过。"
    "过了一会才开口。"
    hide zicheng_pose2
    show zicheng_pose2 at jin
    with dissolve
    voice v3
    c "你......是怎么知道这些信息的？尤其是我的.........喜好！"
    play music speak fadein 1.0 fadeout 1.0
    l "我来自未来！通过根据你父亲所提出原理研制的时间机器，回到的这里。"
    hide zicheng_pose2
    show zicheng_pose2 mouth3 at jin
    with dissolve
    voice v1
    c "这........."
    $ times = "15:04"
    voice v3
    c "虽然很难信任你！但是谅你绝对不可能知道我想要的东西......"
    l "毕竟是未来的你告诉我的！"
    voice v3
    c "那...那你回到这个时间点的目的是什么？"
    l "目的是执行，未来的你提出的：拯救你父亲的计划！"
    l "同时也是，拯救沁野市的计划，拯救全人类的计划！"
    l "你...能明白是什么意思吧！？"
    hide zicheng_pose2
    show zicheng_pose2 at jin
    with dissolve
    voice v1
    c "嗯........."
    voice v3
    c "拯救我父亲？所以你知道我父亲现在的下落了吗？"
    l "现在的下落我并不了解，但是。"
    voice v3
    c "你父亲会在两天后，也就是星期三，被警察找到遗体。"
    c "..........."
    voice v3
    c "那你是怎么回到这里来的？如果我父亲已经遇害了的话。"
    voice v3
    c "又是怎么知道我父亲时间机器的原理的呢？"
    l "那是因为.................."
    hide screen watch
    with dissolve
    scene bg_none
    with fade2
    "........................."
    "我向叶梓澄说明了一切我能说明的东西......"
    "..........................."
    $ times = "15:08"
    show screen watch
    with dissolve
    scene bg_1f_kai
    with fade
    show zicheng_pose2 at jin
    with dissolve
    voice v3
    c "所以......在我父亲的研究所里可以找到，有关研发时间机器的笔记？"
    voice v3
    c "未来的你，和未来的我一起，研发出了时间机器，并回到了这个时代。"
    voice v3
    c "这样做的目的是改变我父亲死去的未来。因为我父亲的死会导致未来AADR统治全人类。"
    voice v3
    c "而你手上这块手表，就是用来将你的记忆送回过去的你身体里的，微型时间机器，吗？"
    l "嗯！"
    voice v5
    c "虽然很抱歉，我并没有任何关于你的记忆，无论是你说的和你度过的那两次的一星期时间，还是和你一起去我父亲的研究所的事。"
    voice v3
    c "毕竟这些事情，已经变成了未发生的状态了。"
    voice v3
    c "所以，来自你上次所经历过的未来的我，拜托你将这一切都告诉给现在的我的目的就是。"
    voice v3
    c "找出AADR会盯上我父亲的研究的契机对吧！"
    l "没错！找出这一切的最根本的原因，然后，由我来避开这个原因。"
    voice v3
    c "你这块手表可以将你的记忆，发送给过去的你自己，但是最多只能发送回十五天前，对吧！"
    l "没错！所以如果AADR在比15天更早的时间就盯上了你的父亲的话。"
    l "那我恐怕就只有毁掉你父亲研发的时间刻校正仪这一条路可走了。至少可以避免AADR对其的滥用。"
    $ times = "15:10"
    play sound suzu
    c "......"
    voice v1
    c "林洛。"
    voice v1
    c "已经上课了。"
    voice v3
    c "更多的事情，下节课下课继续在这里说吧！"
    l "嗯。好！"
    stop sound
    scene bg_2_3
    with dissolve
    scene bg_tukue
    with dissolve
    play music school fadein 1.0 fadeout 1.0
    "我跟着叶梓澄回了教室。"
    $ times = "15:11"
    "我刚一坐到座位上。就感受到一阵异样的目光。"
    scene bg_kexi_miru
    with dissolve
    "是覃可汐。但是我没空去管覃可汐在想什么了。"
    "虽然很对不起她，但我现在必须要专注于找到线索。"
    hide screen watch
    with dissolve
    play sound suzu
    "终于等到了下课。"
    $ times = "15:50"
    show screen watch
    with dissolve
    scene bg_1f_kai
    with fade
    stop sound
    play music speak fadein 1.0 fadeout 1.0 
    show zicheng_pose2 at jin
    with dissolve
    $ times = "15:52"
    voice v3
    c "继续之前的话题吧！"
    voice v3
    c "AADR是研究原子的数字化转换的，而我父亲成功发现了原子可以转换成零子。"
    l "你父亲有对外宣传过零子有关的文章或者发言吗？"
    voice v5
    c "应该不会的。我父亲亲口跟我说过。零子相关的研究还在继续，父亲希望等关于传输和还原零子相关的研究变得可行和安全之后，再将其发表在论文中。"
    l "也就是说，并没有对外界公开！"
    l "那......你母亲也是研究人员吗？"
    voice v1
    c "嗯。"
    l "关于你母亲相关的事情，方便进一步说吗？"
    voice v1
    c "嗯..."
    voice v3
    c "七天前，也就是9月12号。"
    hide ziccheng_pose2
    show zicheng_pose2 eyes2 at jin
    with dissolve
    voice v3
    c "我母亲被发现，倒在了一个巷子里。脖子上有手印和指甲抓出来的血痕。"
    $ times = "15:54"
    l "未来的你跟我说过这件事，嫌疑人被监控拍下来了，但是并没有被抓到。"
    voice v1
    c "没错。"
    l "遗体被发现的时候，身上的有价值的东西，还在吗？"
    voice v3
    c "没有。钱包和手机都不翼而飞了。"
    voice v3
    c "林洛......你觉得，是AADR通过我母亲了解到的我父亲的研究项目的吗？"
    l "嗯......一般而言的确会这样想。"
    l "但是AADR有什么动机去杀害你的母亲呢？"
    l "难道还有更早的关于你父亲研究项目的信息？"
    $ times = "15:56"
    voice v1
    c "不知道。"
    l "是不是你母亲，在遇害之前跟什么人说过了你父亲的研究项目，然后那个人，又或许是其他人，向AADR告密了......"
    l "又或许......那个人就是AADR的人？"
    l "你母亲除了在研究所上班以外，还有其他工作吗？"
    voice v3
    c "没有了。跟我父亲不同。我母亲除开研究所以外就只在家里，负责打理家中事务。"
    l "那？"
    $ times = "15:58"
    l "你母亲在9月12号那天，出门的动机是什么？"
    voice v3
    c "那天是星期一，我在上学，所以我也不清楚动机是什么。"
    voice v3
    c "但是平时那个时候的话，应该是不会出门的。"
    voice v3
    c "警察得到的结果，事发时间是下午两点多。"
    voice v3
    c "那个时候太阳也是一天中最热的时候。的确就算是一般的家庭主妇都不会选择出门。"
    l "好了。现在有了一个新的目标了。"
    l "我们现在要了解清楚。"
    l "你母亲，在9月12号下午两点之前，出门的目的是什么？以及为什么要经过巷子。"
    l "等会。"
    l "虽然这样问可能会勾起你的不好回忆，但是。"
    "看着叶梓澄的惆怅的眼神，我又不敢开口询问了。担心再次伤到她的心。"
    "从我告诉她，他的父亲未来会死掉的时候，就已经受到了一次打击了吧。"
    "看得出来，叶梓澄尽量不表现得难过。"
    c "没事，你问吧，"
    "叶梓澄看我一直犹豫不决，主动开口了。"
    $ times = "15:59"
    l "好。"
    l "你母亲出事的地点，是那个巷子，还是说......是从什么地方把遗体搬进了巷子？"
    voice v5
    c "警察现场勘察的时候没有找到地上存在拖拽的血迹什么的。"
    voice v3
    c "巷子里也存在很多打斗的痕迹。"
    l "看来...是发生在巷子里的。"
    l "那，巷子内外有监控吗？"
    voice v3
    c "没有。最近的监控也是出巷子几十米的地方才有一个。"
    voice v3
    c "虽然拍到了嫌疑人，但是搜查的时候却找不到任何踪迹了。"
    l "那有拍到你母亲什么时候，跟谁一起进的巷子吗？"
    voice v3
    c "有。但是只有母亲一个人，背着挎包。"
    l "服饰呢？"
    voice v3
    c "是平时出门见同学朋友才会穿的一套正装。"
    l "正装......"
    $ times = "16:00"
    play sound suzu
    "又上课了。"
    voice v3
    c "要不，放学后再聊吧！连续的讨论才有助于思维的活跃。"
    voice v3
    c "老是被上课打断。"
    l "嗯！"
    hide screen watch
    with dissolve
    scene bg_schoolmae
    with fade2
    $ times = "17:41"
    show screen watch
    with dissolve
    play music kexi fadein 1.0 fadeout 1.0
    "我和叶梓澄约定好了。放学以后来到了校门口见面。"
    "这命运的校门口。"
    play sound run
    $ times = "17:42"
    show zicheng_pose1 mouth1 at jin:
        xcenter 0.3
    with dissolve
    c "久等了，林洛！"
    play sound run
    show kexi_pose mouth1 at jin:
        xcenter 0.6
    with dissolve
    l "嗯。"
    play sound odoro
    with vpunch
    l "嗯？"
    play sound odoro
    with vpunch
    "覃可汐为什么也跟了过来。"
    show zicheng1_shadow at jin:
        xcenter 0.3
    voice v3
    x "你们两个，以前认识？"
    voice v3
    x "我看你们一下课就跑出去聊天，一直到上课才回来。"
    voice v3
    x "是在聊什么啊？"
    hide kexi_pose
    show kexi_pose2 mouth4 at jin:
        xcenter 0.6
    with dissolve
    voice v3
    x "有兴趣跟我分享吗？"
    voice v3
    x "嗯？可以吗？可以吗？"
    "叶梓澄抢先拒绝了她。"
    hide zicheng1_shadow
    show kexi2_shadow at jin:
        xcenter 0.6
    voice v3
    c "但是，我拒绝！"
    $ times = "17:44"
    voice v3
    c "不行！覃可汐你先回家吧！我和林洛讨论的东西跟你没啥关系的。"
    "没啥关系，这是叶梓澄的谎言。"
    hide kexi2_shadow
    show zicheng1_shadow at jin:
        xcenter 0.3
    voice v3
    x "不嘛！这么遮遮掩掩的，难不成是？"
    "覃可汐露出了邪魅的笑容。"
    l "叶梓澄，我看要不？"
    hide zicheng1_shadow
    hide zicheng_pose1
    show zicheng_pose2 at jin:
        xcenter 0.3
        yoffset 0
        linear 0.1 xoffset 0 yoffset -50
        linear 0.1 yoffset 0 xzoom 1.1 yzoom 1.1
        linear 0.1 xoffset 0 yoffset -25
        linear 0.1 yoffset 0 xzoom 1.2 yzoom 1.2
    hide kexi_pose2
    show kexi_pose2 mouth1 at jin:
        xcenter 0.6
        yoffset 0
        linear 0.1 xoffset 0 yoffset -50
        linear 0.1 yoffset 0 xzoom 0.9 yzoom 0.9
        linear 0.1 xoffset 0 yoffset -25
        linear 0.1 yoffset 0 xzoom 0.8 yzoom 0.8
    show kexi2_shadow at jin:
        xcenter 0.6
        yoffset 0
        linear 0.1 xoffset 0 yoffset -50
        linear 0.1 yoffset 0 xzoom 0.9 yzoom 0.9
        linear 0.1 xoffset 0 yoffset -25
        linear 0.1 yoffset 0 xzoom 0.8 yzoom 0.8
    "我靠近叶梓澄的耳边，小声商量着。"
    l "要不让覃可汐也一起，帮忙思考和推理一下？"
    voice v3
    c "这不行吧！如果让她知道了自己即将......"
    l "有一种东西，叫角色扮演......"
    ".........."
    voice v3
    c "嗯......那好吧！"
    hide zicheng_pose2 
    show zicheng_pose2 at jin:
        xzoom 1.2 yzoom 1.2
        xcenter 0.3
        yoffset 0
        linear 0.1 xoffset 0 yoffset -50
        linear 0.1 yoffset 0 xzoom 1.1 yzoom 1.1
        linear 0.1 xoffset 0 yoffset -25
        linear 0.1 yoffset 0 xzoom 1.0 yzoom 1.0
    hide kexi_pose2
    show kexi_pose2 mouth4 at jin:
        xcenter 0.6
        xzoom 0.8 yzoom 0.8
        yoffset 0
        linear 0.1 xoffset 0 yoffset -25
        linear 0.1 yoffset 0 xzoom 0.9 yzoom 0.9
        linear 0.1 xoffset 0 yoffset -50
        linear 0.1 yoffset 0 xzoom 1.0 yzoom 1.0
    show zicheng2_shadow at jin:
        xzoom 1.2 yzoom 1.2
        xcenter 0.3
        yoffset 0
        linear 0.1 xoffset 0 yoffset -50
        linear 0.1 yoffset 0 xzoom 1.1 yzoom 1.1
        linear 0.1 xoffset 0 yoffset -25
        linear 0.1 yoffset 0 xzoom 1.0 yzoom 1.0
    hide kexi2_shadow
    voice v3
    x "啊嘞嘞？！已经开始有亲密接触了吗？关系发展真是迅速啊！"
    voice v3
    x "难道是？在我之前就发展关系了？叶梓澄！居然对我隐瞒了这么久！"
    voice v3
    x "我之前都不知道的！"
    hide zicheng2_shadow
    show kexi2_shadow at jin:
        xcenter 0.6
    voice v3
    c "覃可汐！你听我说！"
    hide kexi2_shadow
    show zicheng2_shadow at jin:
        xcenter 0.3
    voice v3
    x "听你狡辩是吧！好！我要看看你怎么编！"
    hide zicheng2_shadow
    show kexi2_shadow at jin:
        xcenter 0.6
    voice v3
    c "林洛，我和他是今天才认识的。"
    $ times = "17:46"
    voice v3
    c "我之前也一直喜欢看小说，这个你也是清楚的吧！"
    voice v3
    c "刚好林洛他现在正在构思一个小说，希望我帮他完善相关剧情。"
    voice v3
    c "希望用我丰富的“知识储备”，帮他构思什么的！"
    voice v3
    c "所以我说你误会了！"
    hide kexi_pose2
    show kexi_pose2 mouth3 at jin:
        xcenter 0.6
    with dissolve
    hide kexi2_shadow
    show zicheng2_shadow at jin:
        xcenter 0.3
    voice v3
    x "是什么类型的小说？恋爱吗？"
    hide zicheng2_shadow
    show kexi2_shadow at jin:
        xcenter 0.6
    play sound odoro
    hide zicheng_pose2
    show zicheng_pose2 at jin:
        xcenter 0.3
        yoffset 0
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset -50
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset 0
    with vpunch
    voice v1
    c "不是！"
    with vpunch
    "啊！好快的否定！"
    hide kexi2_shadow
    l "是悬疑和推理题材的小说。"
    "我帮忙圆场到。"
    l "覃可汐，我们现在还是很缺人，你看你有兴趣参与进来吗？"
    hide kexi_pose2
    show kexi_pose2 mouth4 at jin:
        xcenter 0.6
    with dissolve
    show zicheng2_shadow at jin:
        xcenter 0.3
    voice v3
    x "嗯......好啊！我还是玩过不少推理游戏的！"
    $ times = "17:48"
    $ persistent.tips78 = True
    $ persistent.tips79 = True
    voice v3
    x "像{a=showmenu:tips78}{color=#F18D7D}正转裁判{/color}{/a}啊，{a=showmenu:tips79}{color=#F18D7D}炮丸论破{/color}{/a}啊什么的。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    voice v3
    x "推理类动画我也没少看哦！"
    $ persistent.tips80 = True
    $ persistent.tips81 = True
    $ persistent.tips82 = True
    voice v3
    x "{a=showmenu:tips80}{color=#F18D7D}名侦探柯北{/color}{/a}啊，{a=showmenu:tips81}{color=#F18D7D}复活笔记{/color}{/a}啊，{a=showmenu:tips82}{color=#F18D7D}火菓{/color}{/a}啊~"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    play sound odoro
    with vpunch
    l "好好好！缺的就是你这种人才！"
    $ persistent.tips83 = True
    "{a=showmenu:tips83}{color=#F18D7D}人材{/color}{/a}！我在脑海里小声说道。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    hide kexi_pose2
    show kexi_pose2 mouth4 at jin:
        xcenter 0.6
        yoffset 0
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset -50
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset 0
    voice v3
    x "呐~说吧！大概是什么剧情？"
    hide zicheng2_shadow
    l "嗯......"
    nvle "我大脑进行着飞速的运算。想着要怎么瞎编。"
    nvl clear
    with vpunch
    l "嗯。"
    "我顿了顿口气。看着覃可汐期待的眼神。"
    play music speak fadein 1.0 fadeout 1.0
    l "我创作的小说里的主角，是一名侦探。"
    l "他碰到了一件棘手的案子。"
    l "一个人遇害了，但是我构思不出凶手的作案动机。"
    l "这个受害者，在本该呆在家里的时间段，被发现遇害在了一个巷子里。"
    l "然后监控没有拍摄到详细的作案过程，虽然拍到了像是凶手的嫌疑人，但是搜查的时候这个人已经找不到了。"
    l "这是目前，主角所遇到的难题。"
    l "被害人被发现的时候，穿着只有去见关系好的人的时候才会穿在身上的正装，并且身上的金钱和手机都没了。"
    show zicheng2_shadow at jin:
        xcenter 0.3
    voice v1
    x "嗯......"
    voice v3
    x "根据你所提供的信息来看。"
    $ times = "17:48"
    voice v3
    x "根本就是没有悬念的事情吧。不是拍到了嫌疑人吗？"
    voice v3
    x "嫌疑人，谋财害命，在巷子里杀害了被害人，然后拿走了金钱和手机。"
    voice v3
    x "警察抓不到他，可能是因为在案发以后就已经逃离了案发所在地区，脱离了当地警察的管辖范围。"
    voice v3
    x "已经不需要推理的，已经有很明确的目标了，那就是抓住嫌疑人啊！"
    voice v3
    x "但是你这么设计的话。这个嫌疑人有点蠢啊！"
    l "这话怎么说？"
    voice v5
    x "拿走金钱可以理解，但是现在这个时代，手机反而是很不利于自己逃离的设备。毕竟现在的手机找回功能，就算设备关机了也能通过定位锁定凶手位置。"
    l "那万一是凶手带走手机方便销毁呢？"
    voice v3
    x "你的意思是？被害者通过手机录下了对凶手不利的信息？"
    l "有这个可能吧！不然不会特地把手机也拿走了。而且现在大多数手机都会设置密码锁，虽然密码锁可以暴力解开就是了。"
    voice v3
    x "你这么说确实。凶手把手机也带走，可能就是为了销毁证据。"
    l  "好，这样解释就能说得通为什么凶手在杀害受害者以后要这样行动了。"
    l "那下一步，我得构思凶手的作案动机是什么。"
    voice v5
    x "我觉得作案动机很明显了，就是谋财害命，不然不管是蹲点在小巷里也好，还是拿走受害者的钱财也好，都很难用其他动机来解释。"
    l "你觉得，如果凶手带走钱财只是在故意混淆呢？故意隐藏自己真正的作案动机。"
    l "例如......凶手真正关心的只是手机内的资料，拿走钱财只是想干扰警察的办案。"
    voice v3
    x "这个感觉......怎么来安排作案动机都差不多吧......"
    voice v3
    x "作案动机什么的，你写警察抓到凶手以后不就全出来了。"
    hide kexi_pose2
    show kexi_pose2 mouth4 at jin:
        xcenter 0.6
        yoffset 0
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset -50
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset 0
    voice v3
    x "啊哈~如果这算推理小说的话，那会被圈内人笑话的~"
    $ times = "17:50"
    "我无言以对。"
    nvle "果然我编的理由还是太牵强了吗？"
    nvle "果然当务之急是找到凶手吗？还是说我只要马上回到过去，制止凶手犯案，事情就会全部解决了吗？"
    nvle "但是万一我阻止了凶手，还会有新的凶手......"
    nvl clear
    voice v3
    x "到处都是监控，就算混淆了作案动机，也早晚会被警察抓住然后审讯吧！"
    voice v3
    x "但是你说却没被抓住。"
    hide zicheng2_shadow
    show kexi2_shadow at jin:
        xcenter 0.6
    voice v3
    c "对！警察提取了监控内凶手的资料，在全市内顺着监控搜查，都没有结果。"
    "叶梓澄如此说着。"
    hide kexi2_shadow
    show zicheng2_shadow at jin:
        xcenter 0.3
    voice v3
    x "一般凶手被监控所拍到的话，警察应该可以顺着监控挨个追踪凶手的踪迹吧！包括开的什么车，走的哪条路。"
    voice v3
    x "怎么会抓不到呢？"
    voice v3
    x "还是说？你在构思的时候，希望这个凶手不会被抓到？"
    play sound odoro
    hide kexi_pose2
    show kexi_pose2 mouth1 at jin:
        xcenter 0.6
    with vpunch
    voice v1
    x "我懂了！"
    "覃可汐觉得自己明白了什么，会心一笑。"
    hide kexi_pose2
    show kexi_pose2 mouth1 at jin:
        xcenter 0.6
        yoffset 0
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset -50
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset 0
    voice v3
    x "这个凶手后面还有重要戏份对吧！"
    voice v3
    x "是最终反派吗？"
    voice v3
    x "还是说？警察无权抓他？"
    hide kexi_pose2
    show kexi_pose2 mouth3 at jin:
        xcenter 0.6
    with dissolve
    $ persistent.tips84 = True
    $ persistent.tips85 = True
    voice v3
    x "让我猜猜？你构思的故事里也有一套类似{a=showmenu:tips84}{color=#F18D7D}生理测量者{/color}{/a}的，{a=showmenu:tips85}{color=#F18D7D}犯罪参数{/color}{/a}的东西？"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    voice v3
    x "然后这个凶手是稀有的免疫检测体质，所以警察不能直接抓他吗？"
    voice v3
    x "这样来推断的话。真相大白了！！"
    $ persistent.tips86 = True
    voice v3
    x "这个凶手肯定已经被做成{a=showmenu:tips86}{color=#F18D7D}百脑汇{/color}{/a}了吧！"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    $ times = "17:52"
    "果然覃可汐已经脱离现实逻辑开始朝着虚幻发展了。"
    l "那个......不是......我小说的时代背景就是我们生活的这个时代，不是什么赛博朋克和未来世界，也不存在犯罪参数这东西。"
    l "就是一个普普通通的，跟现代一样的一套治安管理体系！"
    hide kexi_pose2
    show kexi_pose2 at jin:
        xcenter 0.6
    with dissolve
    voice v3
    x "是这样吗？好吧！"
    voice v3
    x "我倒是觉得这样写很有趣，不是吗？"
    hide kexi_pose2
    show kexi_pose2 mouth4 at jin:
        xcenter 0.6
    with dissolve
    voice v3
    x "那凶手没被抓到的真正原因到底是什么？"
    voice v3
    x "监控把凶手跟丢了？"
    hide zicheng2_shadow
    show kexi2_shadow at jin:
        xcenter 0.6
    voice v3
    c "差不多是这样。"
    voice v3
    c "警察办案的时候顺着沿路的监控调查。但是发现嫌疑人在跑到一个监控盲区以后就再也没在其他监控里出现过了。"
    hide kexi2_shadow
    show zicheng2_shadow at jin:
        xcenter 0.3
    voice v3
    x "然后警察去查了那个盲区了吗？"
    hide zicheng2_shadow
    show kexi2_shadow at jin:
        xcenter 0.6
    voice v3
    c "当然有查，但是那块地方是一家私人企业的地下车库。"
    voice v3
    c "车库里只有向上通往地面的路口。"
    voice v3
    c "也就是说，凶手进了这个里面以后，是不可能久留的。"
    hide kexi2_shadow
    show zicheng2_shadow at jin:
        xcenter 0.3
    voice v3
    x "既然是车库，那肯定有很多车辆吧！凶手搭乘里面的车辆跑了呢？"
    voice v3
    c "都查过了。包括车库里出入的每一辆车，但是没有收获。"
    voice v3
    c "而且这个车库的车流量还算比较大，车辆出入很是频繁。"
    hide kexi2_shadow
    show zicheng2_shadow at jin:
        xcenter 0.3
    voice v3
    x "如果凶手躲进了汽车后备箱等无法被监控拍到的地方呢？"
    hide zicheng2_shadow
    show kexi2_shadow at jin:
        xcenter 0.6
    voice v3
    c "这个也很难查，除非挨个追踪和排查每一辆车辆。"
    voice v3
    c "而且万一凶手的同伙，开的不是自己的车就更难查了。"
    hide kexi2_shadow
    show zicheng2_shadow at jin:
        xcenter 0.3
    voice v3
    x "原来是这样跟丢的吗？嗯........."
    $ times = "17:54"
    voice v3
    x "不过地下车库没有监控摄像头已经很奇怪了。"
    voice v3
    x "不过，凶手费这么大的周折，那被害人肯定很有钱吧！值得凶手不择手段地去杀人。"
    hide zicheng2_shadow
    show kexi2_shadow at jin:
        xcenter 0.6
    voice v3
    c "实际上，被害人的收入很普通，至少绝对算不上有钱。"
    hide kexi2_shadow
    show zicheng2_shadow at jin:
        xcenter 0.3
    voice v3
    x "那......难道说？凶手其实是不小心杀掉了被害人？"
    hide zicheng2_shadow
    l "嗯？为什么这样说？"
    show zicheng2_shadow at jin:
        xcenter 0.3
    voice v3
    x "当然这只是我个人的通过已知条件推导出来的可能原因。"
    voice v3
    x "凶手并不是故意杀掉被害人的。"
    voice v3
    x "你还设定了什么东西吗？"
    voice v3
    x "例如，监控有没有拍到凶手用的什么凶器，以及，死者的死亡原因是什么？"
    "这个我也不知道了，只能让叶梓澄帮我回答。"
    hide zicheng2_shadow
    show kexi2_shadow at jin:
        xcenter 0.6
    voice v3
    c "没有拍到凶手的作案工具。也不会拍到。"
    voice v3
    c "这是因为："
    voice v3
    c "被害人的死亡原因是————————"
    voice v3
    c "窒息。"
    voice v3
    c "也就是......被掐死了。"
    with vpunch
    "啊？这个细节，叶梓澄并没有在之前透露过。"
    nvle "从覃可汐的反应来看，叶梓澄似乎并没有在母亲去世以后将详细情况告诉给覃可汐过。"
    nvl clear
    hide kexi2_shadow
    show zicheng2_shadow at jin:
        xcenter 0.3
    voice v3
    x "这样的话.........."
    voice v3
    x "案件细节大概可以分为两种情况了。"
    voice v3
    x "情况一，凶手是为了抢夺财物，但是失手杀死了被害人。"
    $ times = "17:54"
    voice v3
    x "情况二，凶手的真正目的是被害人手机里的东西，为了得到这些东西，不惜杀掉被害人。"
    voice v3
    x "关于凶手的资料，既然警察都锁定了是谁，应该拿得到吧！"
    hide zicheng2_shadow
    show kexi2_shadow at jin:
        xcenter 0.6
    voice v3
    c "凶手就是当地的一个无业混混，曾经有过几次因盗窃和拦路抢劫而入刑的犯罪记录，并且在案发前两星期才刚出狱。"
    hide kexi2_shadow
    show zicheng2_shadow at jin:
        xcenter 0.3
    voice v3
    x "这样么？"
    voice v3
    x "但是就算是混混，也会有一个住的地方吧！"
    hide zicheng2_shadow
    show kexi2_shadow at jin:
        xcenter 0.6
    hide zicheng_pose2
    show zicheng_pose2 mouth3 other1 at jin:
        xcenter 0.3
    with dissolve
    voice v3
    c "你这话说的！警察也不是笨蛋！首先排查的就是住所。"
    hide kexi2_shadow
    show zicheng2_shadow at jin:
        xcenter 0.3
    hide kexi_pose2
    show kexi_pose2 mouth1 at jin:
        xcenter 0.6
    with dissolve
    voice v3
    x "啊哈哈哈哈~也是呢~"
    voice v3
    x "所以根据他的案底来看，其实更倾向于情况一吧！"
    voice v3
    x "无论是被害者的死法，还有凶手之前的犯案记录。"
    hide zicheng2_shadow
    voice v3
    l "那什么条件下会出现情况二？"
    show zicheng2_shadow at jin:
        xcenter 0.3
    voice v3
    x "当然有条件。例如："
    voice v3
    x "有人需要手机里的东西，所以雇佣凶手去作案。"
    voice v3
    x "怎么样？"
    l "你想的很好！我会吸纳你的这部分想法的。"
    voice v3
    x "还有很多问题！我需要更多线索来辅助我进行思考。"
    $ times = "17:56"
    nvle "看着覃可汐认真的样子，感觉像是变了一个人一样。"
    nvl clear
    voice v3
    x "你说过，被害人遇害的时间，在平时的这个时段是应该呆在家里对吧！"
    voice v3
    x "身上的正装，表示被害人可能有什么重要的人要见面。"
    voice v5
    x "在小巷里遇害，则说明被害人和准备见面，或者是已经见过面的人的见面地点，有可能必须经过这条小巷才能到达。"
    voice v3
    x "反正就是有，不得不穿过巷子的原因！"
    hide zicheng2_shadow
    show kexi2_shadow at jin:
        xcenter 0.6
    hide zicheng_pose2
    show zicheng_pose2 at jin:
        xcenter 0.3
    with dissolve
    voice v3
    c "不得不穿过巷子的原因吗？"
    hide kexi2_shadow
    show zicheng2_shadow at jin:
        xcenter 0.3
    hide kexi_pose2
    show kexi_pose2 at jin:
        xcenter 0.6
    with dissolve
    voice v3
    x "以及，如果事实是情况二，也就是凶手受雇杀人。那么。"
    voice v3
    x "雇佣者或者凶手，一定有一个知道被害人的行动路径。"
    hide zicheng2_shadow
    show kexi2_shadow at jin:
        xcenter 0.6
    voice v3
    c "也就是说，一定知道被害人会穿过巷子吗？"
    voice v3
    c "穿过这条没有监控的巷子。"
    hide kexi2_shadow
    show zicheng2_shadow at jin:
        xcenter 0.3
    hide kexi_pose2
    show kexi_pose2 mouth4 at jin:
        xcenter 0.6
        yoffset 0
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset -50
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset 0
    voice v3
    x "没错。"
    hide kexi_pose2
    show kexi_pose2 at jin:
        xcenter 0.6
    with dissolve
    voice v3
    x "如果凶手和被害人之间并没有在之前有过关联的话。"
    voice v3
    x "就很可能，雇佣凶手的人对受害人很熟悉，并且很需要受害人手机内的东西，资料啊通话啊什么的。"
    voice v3
    x "但是这一点其实有点站不住脚，死者是窒息而死吧。有受雇的杀手会选择掐死被害人吗？"
    voice v3
    x "怎么也没有选择一把锋利的刀子，或者一杆枪来的快吧！？"
    $ times = "17:58"
    voice v3
    x "而且被掐死还存在很多不确定性，可能需要跟被害人搏斗，以及可能最后杀不死被害人。"
    voice v3
    x "除非......雇佣凶手的人，只需要拿到数据就可以了，被害人是死是活，都无所谓。"
    voice v3
    x "这意味着这个雇佣杀手的人，可能背后拥有更强大的力量，从而使其可以不用畏惧被害人的报警。"
    nvle "覃可汐还在头头是道地推理着，但是天色渐渐暗了下来。"
    nvl clear
    play music kexi fadein 1.0 fadeout 1.0
    $ times = "17:59"
    l "要不今天就到这里吧！覃可汐！"
    play sound odoro
    hide kexi_pose2
    show kexi_pose eyes4 mouth3 at jin:
        xcenter 0.6
    with vpunch
    voice v3
    x "啊~我才刚找到推理的感觉~"
    hide zicheng2_shadow
    show kexi1_shadow at jin:
        xcenter 0.6
    voice v3
    c "没错！天色很晚了，也该散伙了。"
    hide kexi1_shadow
    show zicheng2_shadow at jin:
        xcenter 0.3
    voice v1
    x "好吧！"
    voice v3
    x "一定要采纳我的话哦！"
    l "一定会的！"
    voice v3
    x "嗯嗯~那就好~"
    hide kexi_pose
    show kexi_pose mouth1 at jin:
        xcenter 0.6
    with dissolve
    voice v3
    x "那我就先回家了，明天继续吧！？"
    play sound run
    hide zicheng2_shadow
    hide kexi_pose
    with dissolve
    hide zicheng_pose2
    show zicheng_pose1 mouth5 at jin
    with dissolve
    hide zicheng_pose2
    show zicheng_pose1 eyes7 mouth3 at jin
    with dissolve
    $ times = "18:02"
    "看着覃可汐逐渐走远，叶梓澄长舒了一口气。"
    hide zicheng_pose1
    show zicheng_pose2 at jin
    with dissolve
    play music speak fadein 1.0 fadeout 1.0
    voice v3
    c "林洛，你怎么看待覃可汐的推理？"
    l "很有参考价值。"
    voice v3
    c "嗯！那你也回家吧。"
    voice v3
    c "我想再去找警察了解一下关于这个案子的更多的信息。"
    voice v3
    c "你觉得.....凶手会是我母亲去见面的那个人吗？"
    l "有这种可能！"
    l "不然常规无法解释为什么你母亲必须经过那个巷子。以及凶手那娴熟的逃跑手法。"
    l "那......你知道你母亲那一天去见的谁吗？"
    voice v3
    c "不知道。毕竟可以用来调查的手机也被拿走了。"
    $ times = "18:03"
    l "嗯........"
    l "你母亲见的最多的朋友是谁？"
    l "警察也可以通过你母亲手机号码的通话记录什么的，查到一点蛛丝马迹吧！"
    l "如果你母亲见的那个人，其实是在为AADR卖命，倒是可以解释的通了。"
    l "套出关于零子的研究的话以后，邀请你母亲出去见面，再雇佣杀手去杀掉她，封口并且获得手机的的更多资料。"
    l "然后AADR总部获得了资料以后，就派人去研究所抢夺仪器和资料，绑架你父亲。"
    l "如果真的是这种情况的话......就得找那个你母亲见面的人对质了呢~"
    voice v3
    c "嗯！我去找警察问问详细的后续调查资料。"
    play music sora fadein 1.0 fadeout 1.0
    hide zicheng_pose2
    show zicheng_pose1 eyes4 mouth3 other1 at jin
    with dissolve
    voice v1
    c "林洛......"
    l "嗯？"
    voice v3
    c "虽然我不知道......你穿越时间之前遇到的我......是怎么看你的......"
    hide zicheng_pose1
    show zicheng_pose1 eyes2 mouth1 other2 at jin
    with dissolve
    $ times = "18:04"
    voice v3
    c "但是对现在的我来说......你真的帮了我很多......"
    voice v3
    c "我本以为母亲的死，和父亲的失踪......都将成为永远不会改变的事实......"
    voice v3
    c "是你给了我希望......"
    voice v3
    c "已经......不知道该怎么感谢你了！"
    nvle "看着叶梓澄这副情形，我深感不妙。"
    nvle "叶梓澄似乎觉得自己欠了我一个人情。"
    nvl clear
    l "干嘛感谢我。"
    l "我能有今天，还是多亏了你啊！"
    l "这是事实。"
    l "我这块能传输记忆到过去的手表，是你发明的。"
    l "未来的我之所以能把这块手表交到我手里，也是多亏了你，发明了时间机器。"
    l "所以要说的话，是我欠你一个人情才对。"
    $ times = "18:06"
    l "没有你的帮助，我也没想到自己可以完成这么伟大的事情。"
    l "我从小就很孤独，没有什么朋友，学习也很平庸。"
    l "看动画片和打游戏便是我唯一的陪伴和消遣了，因为在现实中没有人愿意跟我一起玩耍。"
    l "在第一次结识你和覃可汐之后，我才感受到。"
    l "朋友的温暖。"
    l "原来拥有朋友，是这种感觉吗？"
    l "拥有知心的人，可以互相讨论兴趣爱好，互相倾诉自己的不快和压力。"
    l "是你，以及覃可汐，让我找到了我人生中新的意义。"
    l "所以在覃可汐突然出现意外以后，我才会那么痛苦，那也是我第一次体会到知心的友人跟我永别的痛苦。"
    l "老实说，当我知道我还能拯救覃可汐的时候，我第一次感觉到，我并不是对社会毫无用处的人。"
    l "现在的我，也可以通过自己的努力，去拯救周围的人。我终于是有用的了。"
    l "而这一切，还是多亏了你！叶梓澄......"
    l "叶梓澄......你有在听.....吗？"
    l "比较抱歉，跟你说了这么多跟解决问题无关的话。"
    voice v3
    c "没......我也是第一次收到别人的倾诉......第一次了解到别人对我的看法......"
    hide zicheng_pose1
    show zicheng_pose1 eyes4 mouth1 other2 at jin
    with dissolve
    voice v3
    c "那.....林洛......一起加油吧~！"
    voice v3
    c "不管是为了你自己，还是为了覃可汐，还是为了.........."
    voice v3
    c "为了........"
    hide zicheng_pose1
    show zicheng_pose1 eyes7 mouth5 other2 at jin
    with dissolve
    voice v1
    c "我..."
    voice v3
    c "总之！一起努力吧！！"
    l "啊~嗯！好！"
    l "我会坚持下去的！"
    nvle "叶梓澄似乎说了什么不得了的话。"
    nvle "但是已经无所谓了。"
    $ times = "18:08"
    nvle "我现在得假装没听到她说的什么，不然也太难堪了。"
    nvl clear
    play music home fadein 1.0 fadeout 1.0
    hide screen watch
    with dissolve
    scene bg_none
    with fade
    "和叶梓澄分别以后。我回到了家。"
    scene bg_pasokon
    with fade
    $ times = "21:34"
    show screen watch
    with dissolve
    play sound key loop fadein 1.0 fadeout 1.0
    nvle "用电脑在网上查阅着关于叶梓澄父母的相关信息。"
    nvle "因为还存在着一种可能。就是叶梓澄的父母可能在网上主动或被动，将研究项目泄露给了AADR。"
    nvle "不管是直接通过搜索引擎还是翻阅各大学术网站，关键词检索都没有什么有用的信息。"
    nvl clear
    $ times = "21:40"
    nvle "叶梓澄父亲也只能查到显示是一名大学在职老师。"
    nvle "叶梓澄母亲更是什么基本信息都查不到。用着叶梓澄告诉我的名字输进去，检索结果一个都没有。"
    nvle "关于叶梓澄母亲遇害的相关报道，被害人姓名也都是使用的化名。"
    nvl clear
    $ times = "21:46"
    nvle "凶手仍在逃中。"
    nvle "凶手的大头照和名字倒是查得到。"
    nvle "那AADR是如何提前知道叶梓澄父母的研究项目的呢？"
    nvl clear
    $ times = "21:51"
    nvle "而且.......照着AADR这蛮横的做事风格。"
    nvle "如果知道了叶梓澄父母的研究项目，也不会拐弯抹角的先杀掉叶梓澄母亲，再袭击研究所吧~"
    nvle "难道说？"
    nvl clear
    nvle "是叶梓澄母亲在跟与她见面的那个人那里泄露了信息？"
    nvle "这样才能解释的通，为什么先杀了叶梓澄母亲，再袭击研究所。"
    nvle "但是........."
    nvl clear
    $ times = "21:59"
    nvle "既然叶梓澄母亲已经将信息泄露给了这个人，那为什么还要选择杀掉叶梓澄母亲？是有什么非做不可的理由吗？"
    nvle "毕竟自己作为和叶梓澄母亲最后约定见面的人，如果叶梓澄母亲出了事，嫌疑最大的肯定是自己。"
    nvle "必须拿到手机里的信息？"
    nvl clear
    $ times = "22:04"
    nvle "还是想不通，叶梓澄母亲手机里可以有的信息，直接去研究所肯定得到的更多。"
    nvle "那就是？"
    nvle "叶梓澄母亲和朋友的有关泄露消息的内容，被那位朋友的周围有人获得了？"
    nvl clear
    $ times = "22:11"
    nvle "存在这个可能。"
    nvle "不管结果如何，我觉得都必须去亲自拜访一下那位叶梓澄母亲生前最后见面的那位朋友了。"
    nvl clear
    stop sound
    hide screen watch
    with dissolve
    scene bg_home
    with fade2
    $ times = "22:30"
    show screen watch
    with dissolve
    show ketai_zicheng2
    with dissolve
    c "嗯......好吧！我会去跟班主任请假的！"
    l "嗯！"
    hide ketai_zicheng2
    with dissolve
    play sound ketai3
    "挂断了和叶梓澄的电话。"
    $ times = "22:32"
    stop sound
    "我拜托叶梓澄明天跟我去亲自找到那位叶梓澄母亲的朋友。所以让她去申请明天请假一天。"
    "我和她都请假。"
    "额......后知后觉。班上会不会又传出不好的传言。"
    hide screen watch
    with dissolve
    $ years = "2022.9.20"
    $ times = "07:21"
    $ weeks = _("周二")
    scene bg_schoolmae
    with fade
    show screen watch
    with dissolve
    play music richang fadein 1.0 fadeout 1.0
    "天气很晴朗。我也早早地感到了校门口附近。"
    "总不能在家里集合，跟我爸妈不太好解释为什么没去上学，不如就装成去上学的样子。"
    "我和叶梓澄也是约好了在校门口见面。"
    $ times = "07:24"
    with vpunch
    c "林洛！！"
    "朝着声音来源的方向看去。"
    play sound run
    "是公交车站的方向，叶梓澄一下公交车就喊着我的名字，小跑了过来。"
    show zicheng_pose1 mouth1 at jin
    with dissolve
    voice v3
    c "我已经请好假了。"
    voice v1
    c "对了！"
    play music speak fadein 1.0 fadeout 1.0
    hide zicheng_pose1
    show zicheng_pose2 at jin
    with dissolve
    voice v3
    c "我昨天去找了警察要到了更多的资料。"
    voice v3
    c "包括我母亲最后见面的人。"
    voice v3
    c "以及最先发现我母亲遇害的人。"
    $ times = "07:25"
    l "最后见面的是谁？"
    voice v3
    c "是我母亲的大学同学，丁唯。"
    voice v3
    c "警察调取了我母亲手机号码最后的通话记录，是我母亲和丁唯的通话。"
    voice v3
    c "通话日期是我母亲遇害当天的早上。"
    l "通话内容是什么？"
    voice v3
    c "这个查不到。"
    l "但是，大概是这个丁唯让你母亲出门的吗？"
    hide zicheng_pose2
    show zicheng_pose2 at jin:
        yoffset 0
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset -50
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset 0
    voice v1
    c "走吧！"
    l "你拿到这个丁唯的所在地方了吗？"
    voice v3
    c "嗯！我知道在哪。"
    play music richang fadein 1.0 fadeout 1.0
    scene bg_none
    with fade
    "我跟随叶梓澄，搭上了一辆出租车。"
    "............"
    "............"
    c "到地方了。"
    l "额？"
    play music home fadein 1.0 fadeout 1.0
    scene bg_machi
    with fade
    "面前是一个小巷。"
    play music dead fadein 1.0 fadeout 1.0
    with vpunch
    l "这里难道是......？"
    play music ruins fadein 1.0 fadeout 1.0
    voice v3
    c "是我母亲出事的那个巷子。"
    "巷子内部昏暗潮湿，两侧墙上的涂刷也掉落了不少，露出了红色的砖体。"
    "并没有看到血迹，或者说看不到可以证明这里是案发现场的东西。"
    "大概是案发后被清理过了吧。"
    l "所以你把我带到在这里来，是希望我调查一下现场吗？"
    voice v1
    c "可以哟！"
    l "可以......？"
    voice v3
    c "但主要目的还是见我母亲的大学同学。"
    voice v3
    c "准确的说，是穿过这个巷子以后就能走到她的家。"
    l "额！！！！？"
    voice v1
    c "走吧！"
    play sound run
    "我跟随叶梓澄，慢慢走出了小巷。"
    play music kexi fadein 1.0 fadeout 1.0
    scene bg_dingwei_house
    with fade
    "跟着她，来到了一栋房子面前。"
    play sound door
    mono "昸！昸！昸！"
    "门上没有门铃，所以叶梓澄用手敲打着紧闭着的门。"
    show zicheng_pose1 mouth1 at jin:
        xcenter 0.7
    with dissolve
    voice v3
    c "在吗？阿姨？"
    stop sound
    play sound opendoor
    nvle "几秒钟后，门开了。"
    nvl clear
    show dingwei:
        xcenter 0.3
    with dissolve
    d "啊？你就是......白椎音的女儿...叶梓澄？"
    nvle "白锥音正是叶梓澄母亲的名字。"
    nvl clear
    nvle "看来找对地方了。"
    nvl clear
    d "这个时候，你不应该去上学了吗？"
    voice v3
    c "丁阿姨好。我有一些关于我母亲的事情，希望详细了解一下。"
    d "哦？是吗？这几天警察天天往我这里跑，我也说了足够多了，唉。"
    d "不过，既然你想了解更多，那就行吧！毕竟你是白椎音的女儿。"
    d "这位是？"
    voice v3
    c "这是我的朋友，他也想了解一些事情。"
    d "朋友啊......我懂了，哈哈~那进来坐吧！"
    nvle "她最好真的是懂了。"
    nvl clear
    "我心里想到。"
    scene bg_dingwei_house_naka
    with dissolve
    play music speak fadein 1.0 fadeout 1.0
    show zicheng_pose1 eyes7 mouth3 at jin:
        xcenter 0.3
    with dissolve
    voice v3
    c "那我就开始问了。"
    show dingwei:
        xcenter 0.6
    with dissolve
    voice v3
    c "我从警察那里了解到，您......在我母亲出事的那挺天上午，和我母亲约好了见面？"
    show zicheng1_shadow at jin:
        xcenter 0.3
    d "对！唉~现在想起来......依旧很后悔......如果那天我没有给她打电话......"
    d "或许就不会......碰到这种事情了......还是在快到我家的地方....."
    hide zicheng1_shadow
    voice v3
    c "见面的目的,是相约一起去打麻将对吧？"
    show zicheng1_shadow at jin:
        xcenter 0.3
    d "对.......你母亲经常会趁你和你父亲都不在家的时候，和我约好去打麻将。"
    d "出事的那天也是如此。"
    hide zicheng1_shadow
    voice v3
    c "那打麻将的地点是你家吗？"
    show zicheng1_shadow at jin:
        xcenter 0.3
    d "不是，是我家附近的一家麻将馆。"
    hide zicheng1_shadow
    voice v3
    c "所以每次都是约好了在你家会合吗？"
    show zicheng1_shadow at jin:
        xcenter 0.3
    d "对！"
    hide zicheng1_shadow
    voice v3
    c "那....我母亲有在会合，或者打麻将的途中，说过什么关于科研项目的事情吗？"
    show zicheng1_shadow at jin:
        xcenter 0.3
    d "科研项目？每次打麻将都跟我聊的是你的学习怎么怎么样，以及看的电视剧是什么，晚上打算给你做什么吃。"
    d "什么科研项目什么的，没有聊过，或许吧。"
    hide zicheng1_shadow
    voice v1
    c "或许？"
    show zicheng1_shadow at jin:
        xcenter 0.3
    d "嗯。因为这种东西，在打麻将的时候，无法集中精神听啊，就算听到了可能回头就会忘掉了。"
    hide zicheng1_shadow
    voice v1
    c "嗯........."
    voice v3
    c "我母亲出事当天，您有在家里听到附近的相关的声响吗？"
    show zicheng1_shadow at jin:
        xcenter 0.3
    d "对不起......抱歉......那天的那个时候，我还在客厅沙发上刷手机......开的外放.....所以......"
    "论短视频外放的危害。我在心里如此想到。"
    d "还有什么，你都问吧！我知道的东西都会回答的。"
    d "不过，我有一个请求，希望你们能答应。"
    hide zicheng1_shadow
    voice v1
    c "是什么？"
    show zicheng1_shadow at jin:
        xcenter 0.3
    d "相信我...你母亲的死，不是我干的。"
    d "如果说我的罪过的话......就是直接导致她遇到了凶手，在巷子里。"
    hide zicheng1_shadow
    voice v3
    c "我相信您！阿姨！"
    voice v3
    c "你放心！我一开始就没把您当作嫌疑人！"
    show zicheng1_shadow at jin:
        xcenter 0.3
    d "是吗？"
    hide zicheng1_shadow
    voice v3
    c "毕竟从我记事起，就经常来您家玩"
    voice v3
    c "我查过我母亲大学期间的记录。您和我母亲是室友。而且....从我母亲电脑里翻到的照片，也能看出，您们是很好的朋友。"
    voice v3
    c "所以我相信！您是不会这样做的！"
    show zicheng1_shadow at jin:
        xcenter 0.3
    d "好......谢谢你......为了给椎音一个公正的结果......我会全力配合你的提问的！"
    hide zicheng1_shadow
    voice v3
    c "您是否知道？我母亲有没有，仇人？"
    voice v3
    c "就是...看我目前不爽的人，或者，因为我母亲而受到挫折的人？"
    show zicheng1_shadow at jin:
        xcenter 0.3
    d "据我所知的话......没有......"
    d "你母亲在大学期间就经常帮助别人。"
    d "如果像她这类人都会结仇的话，那可能每个人都有很多仇人了。"
    hide zicheng1_shadow
    voice v3
    c "阿姨，您丈夫，是做什么工作的？"
    show zicheng1_shadow at jin:
        xcenter 0.3
    d "我丈夫的话，现在在本地一家公司做销售的职务。"
    voice v3
    c "平时有出差吗？"
    show zicheng1_shadow at jin:
        xcenter 0.3
    d "偶尔会有，不过也基本是出差到邻近的城市。"
    hide zicheng1_shadow
    c "......"
    voice v3
    c "阿姨！就这样吧！谢谢您告诉我这么多信息！"
    show zicheng1_shadow at jin:
        xcenter 0.3
    d "已经要走了吗？"
    d "要不在我这里吃完午饭了再走？"
    hide zicheng1_shadow
    voice v3
    c "不用了阿姨！谢谢您的好心，但是我们得去其他地方调查了。"
    voice v3
    c "而且马上还要回学校呢！所以抱歉啦~"
    show zicheng1_shadow at jin:
        xcenter 0.3
    d "好吧！慢走啊！"
    hide zicheng1_shadow
    voice v1
    c "嗯!"
    scene bg_dingwei_house
    with dissolve
    play music kexi fadein 1.0 fadeout 1.0
    nvle "我和叶梓澄从丁唯家里以后。叶梓澄和我继续商讨接下来的行动。"
    nvle "临近正午的太阳，依旧刺眼和炎热。"
    nvle "我也叶梓澄坐在一楼的台阶处乘着凉。"
    nvl clear
    nvle "顺便讨论着事项。"
    nvl clear
    l "怎么样？这个丁唯，有可能是杀害你母亲的幕后黑手吗？"
    play music speak fadein 1.0 fadeout 1.0
    show zicheng_pose2 at jin
    with dissolve
    voice v3
    c "缺少作案动机，又或者说。"
    voice v3
    c "我认为她缺少作案动机。"
    l "丁唯...是你母亲的大学同学，以及好朋友吧。"
    l "再加上还经常一起约着玩，确实不像会杀害你母亲。"
    l "再加上，丁唯的丈夫也是从事着跟我父亲的研究项目基本上搭不上边的工作。"
    l "那......还有谁有可能？"
    voice v3
    c "最简单的办法当然是直接找凶手问了。但是连警察都抓不到凶手......"
    voice v3
    c "找找其他突破口吧~"
    l "最先发现案发现场的人呢？"
    voice v3
    c "目击者的话不太可能吧......"
    l "但是你不觉得很奇怪吗？"
    l "目击者目击到了凶手作案，凶手采取的措施是扭头就跑，而不是灭口。"
    l "等等......所以这个目击者是直接看到了作案过程吗？"
    l "还是说？"
    l "只是发现了遗体。"
    voice v3
    c "至少从监控上来看，是目击者先走进巷子里，凶手才从巷子里跑出来。"
    l "如果是这样的话。"
    l "假设凶手只是为了劫财不小心杀掉了人，那看见目击者会逃跑可以理解。"
    l "没有心理准备嘛毕竟。"
    l "但在另一种可能，也就是凶手受雇的情况下，一样说得通。"
    l "雇主的要求只是杀掉你母亲，拿走手机，自然只需要这样做就行了。"
    l "这个雇主，肯定早就安排好了凶手事后离开案发现场的相关事务。"
    l "自然就算不杀掉目击者，也能安身离开了。"
    voice v3
    c "反而第一种假设有点奇怪，林洛。"
    hide zicheng_pose2
    show zicheng_pose1 eyes7 mouth3 at jin
    with dissolve
    "叶梓澄抬起头，说到。"
    voice v3
    c "如果凶手是不小心杀了人，那逃跑以后是如何把自己藏起来的呢？"
    voice v3
    c "藏到以至于警察的力量都找不到踪影。"
    voice v3
    c "所以依旧还是第二种情况比较合理对吧！？"
    voice v3
    c "至少根据目前得到的线索来看，是如此。"
    l "说了这么多，所以目击者是谁？"
    hide zicheng_pose1
    show zicheng_pose1 eyes7 at jin
    with dissolve
    voice v3
    c "是你认识的人。"
    l "？我认识？"
    voice v3
    c "我们都认识。"
    l "所以......是？"
    voice v3
    c "我们的班主任，李老师。"
    play sound odoro
    with vpunch
    l "？啊！！？"
    play sound odoro
    with vpunch
    l "但是案发时间是周一下午啊！"
    l "她是怎么路过学校外面的那个巷子并目击到案发现场的？"
    l "案发现场距离学校，大概也有半个小时的车程吧~"
    hide zicheng_pose1
    show zicheng_pose2 at jin:
        yoffset 0
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset -50
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset 0
    voice v3
    c "这就是我们接下来要调查的地方了。"
    l "那现在回学校去吧！？"
    "虽然我内心是很不愿意回去的。"
    "但是继续呆在外面也无法获得新的线索了。"
    hide zicheng_pose2
    show zicheng_pose2 mouth1 at jin
    with dissolve
    voice v1
    c "林洛！！"
    hide zicheng_pose2
    show zicheng_pose1 mouth1 at jin
    with dissolve
    voice v3
    c "再聊会天吧~"
    voice v3
    c "现在时间也还够。"
    l "但是......"
    "游戏即将结束。"
    return
    "说不定能给你提供一些有用的东西呢~"
    "好吧。"
    "现在不聊，以后可能也没有机会聊了，至少对这个时间的叶梓澄来说。"
    "你热吗？"
    "啊~？有...有点..."
    "那好，等我一会！"
    "说完叶梓澄便离开了。"
    "过了好一会，终于回来了。"
    "手里还顺便拿着两瓶苏打水。"
    "给！"
    "谢谢！"
    "我接过了水，即便我很讨厌喝苏打水这种东西。"
    "那你要和我聊些什么呢？"
    "叶梓澄坐了下来，开始说了。"
    "你跟我说过吧~如果放着现在的事态不管，任其继续发展下去的话....."
    "覃可汐就会死！"
    "覃可汐是我搬家到沁野市来以后认识的第一个朋友~"
    "啊？你也是转校生？"
    "以前是......"
    "以前是.......这是什么意思......?"
    "在我小学二年级的时候，就跟着我父母一起....搬家来到了沁野市....."
    "覃可汐...便是我转学到的小学的...认识的第一个同学..."
    "也是玩的最好的一个......"
    "我父母也是经常带着覃可汐一块，出去玩~"
    "毕竟覃可汐家里的条件不太好，她父母没空也没财力带给覃可汐这些..."
    "我和覃可汐一起，升学到了同一所初中，再又考上了同一所高中......"
    "可以说.....覃可汐就是我的知音，也是我最重要的朋友了....."
    "比起朋友，更像是我的家人一样......"
    "我总算可以理解一点了......."
    "有一个陈年旧事，是关于覃可汐的......"
    "是什么......？"
    "同样是十年前的事情了......"
    "那是我转学后的第二个学期......"
    "的一个周末......"
    "当时我跟着我父母一起，去覃可汐的家里，接覃可汐一起出去玩......"
    "但是到家的时候得知...覃可汐已经跟着附近的小孩子们一起出去玩水去了..."
    "就在她家附近的那条河......"
    "毕竟当时天气炎热..."
    "然后没过多久，一同前去的小孩就跑回来...说覃可汐溺水了......让大人去救...."
    "等等....溺水？"
    "是..."
    "想起我在那个...第一次目睹覃可汐的死亡的前一天的晚上.....做的那个噩梦...."
    "这算是巧合....还是？"
    "是溺水了......但是等我父亲赶忙赶到事发现场的时候....."
    "覃可汐却已经被什么人给救了上来......"
    "被谁？"
    "当时路过的大人吗？"
    "不知道，被救上来的覃可汐躺在河边草丛里，还保留着意识。"
    "至于是谁救的...以及救人者去了哪......就不得而知了......"
    "原来覃可汐还有这种曲折的过去吗？"
    "嗯.....但也就是自那以后，覃可汐就像变了一个人..."
    "从沉默阴暗变成了乐天型人格了......"
    "或许是从大难不死中感受到了生命的宝贵吧~"
    "抱歉给你讲了这些可能没什么用的东西..."
    "没什么.....不如说...我还想听更多......"
    "嗯.......关于覃可汐，几年前有几件事还是印象深刻。"
    "什么事？"
    "那是三年前，放学后的覃可汐和我在回我家的时候，正好遇到了从研究所回来的我父亲。"
    "我父亲一看见覃可汐，就不知为何在痛哭流涕了，抱着覃可汐一顿猛哭..."
    "但当时我问是不是出了什么事，却还是一句话都不说，但我父亲那么坚强的人......"
    "如果有哭出来的理由的话.....也不会轻易对别人说吧...."
    "嗯！就这样了！我们出发吧！"
    "我听得入了迷，不知道什么时候手里的苏打水就喝的见底了。"
    "额！！"
    "可恶！这是因为单线程大脑的原因吗！？"
    "一直专注于听故事而忘掉了我不喜欢喝苏打水这个事情。"
    "还是感谢你肯听我诉说！"
    "说出来了，心里也舒服一点吧..."
    "放心！我不会让覃可汐的悲剧再次发生的！"
    "相信你！"
    "............"
    "一小时后，我们回到了学校。"
    "回学校的时候还在上课。所以只能先回到座位上。"
    "可恶！~我本来是打算在校门口或者卫生间里呆到下课以后再回去的！"
    "但是叶梓澄坚持先回座位等到下课！"
    "很不情愿，但还是采取了叶梓澄的方案。顺便还被她嘲笑了。"
    "啊哈哈！林洛原来你这么怕生啊！"
    "那怎么跟我这么聊的来！？"
    "因为对我来说，你是熟人了！"
    "哈哈哈~"
    "一想起来就后怕。"
    "这也是我想在学校外面呆到放学了再去找班主任的原因。"
    "最后还是顶着全班同学对我的目光，慢慢地回到了座位上。"
    "......"
    "下课了。"
    "在叶梓澄的带领下，来到了班主任的办公室。"
    "咚咚咚！"
    "老师你在吗？"
    "怎么了班长？有什么事吗？"
    "哦！你今天请假了是吧！那是来销假的吗？"
    "嗯！"
    "进来吧！"
    "林洛也在啊！那你们......请假去做的是同一个事情？"
    "算了，别在学校里做就行。在这个表上签字吧。"
    "我觉得班主任肯定误会了什么。"
    "签完字以后，叶梓澄开口了。"
    "李老师......我有件事情向向您咨询一下。"
    "是学习上的事情吗？随便问吧，只要是我知道的，都会回答的。"
    "不是......"
    "我听说......关于我母亲的事情......您是当时的目击者......"
    "班主任的笑容消失了，转为了严肃的脸。"
    "嗯......"
    "我那天下午没有我的课，所以我出门打算采购一点蔬菜......"
    "因为我家比较特殊，平时如果我下午没有课的话，午饭都是在下午三点多准备。"
    "不是正午准备午饭吗......."
    "对。出事的那个巷子，正好位于我家前往镇上菜市场的路线中间。"
    "买菜是走路去的吗？"
    "是啊~因为实际上也就一千米左右的路程，来去就当锻炼身体了。"
    "然后......就在我路过巷子的时候就听到了奇怪的声音。"
    "走进巷子里就发现有一个混混在用手掐着你母亲的脖子......"
    "后来呢？"
    "这个混混看我来了，就连忙跑了出去，然后我就报了警了。"
    "报警的时候我才发现，你母亲已经没了呼吸......"
    "班主任的面色愈加沉重。"
    "是这样吗........."
    "那你在现场除了看到那个混混以外，还有其他可疑人物吗？"
    "我当时冲进去确实只看到那个混混，没有其他人了......"
    "好的.....我知道了......"
    "嗯。"
    "叶梓澄...难道你打算自己来调查凶手吗？"
    "嗯.....老师，其实我父亲这几天....失踪了..."
    "我怀疑我父亲的失踪跟我母亲的遇害有关系。所以我......想把我母亲的案子查清楚。"
    "但是你母亲这个事情，难点不是凶手是谁因为以及查到了，难点是......凶手在哪......"
    "嗯......我知道的......"
    "那老师......我先回教室了......"
    "嗯~一定要控制好自己的情绪啊~我是很能理解你的心情的......"
    "离开办公室以后，叶梓澄把我带到了楼梯间转角。"
    "经典地图。额，忍不住在内心里吐槽了。"
    "林洛......"
    "怎么了......找到突破口了吗？"
    "不......事情陷入瓶颈了......"
    "这样下去的话......或许只有一个办法了。"
    "林洛...拜托你..."
    "直接去询问凶手吧！"
    "额啊！！"
    "所以我需要......回到你母亲出事的那一天吗？"
    "嗯。揭示真相的话，恐怕只有这一个办法了。"
    "但是，有很多风险。"
    "未来可能会被大幅改变对吧！"
    "嗯！如果你阻止了凶手杀害我母亲，未来的我和你可能不会造出时间机器，不会回到你转学那一天把手表给你。"
    "如果是这种情况的话......再遇到什么情况就完全变的不可挽回了吧！？"
    "嗯。这相当于一场豪赌了。"
    "如果赌输了，你阻止了凶手，但凶手的幕后雇主又派了其他人来。"
    "既然赌赢很难......那就......不赌了吧~"
    "你.....是什么意思？"
    "叶梓澄缓缓流泪，说到。"
    "我需要你回到过去，在问出凶手的幕后指使者的情况下，尽量最小化地改变未来。"
    "也就是说......你得在......凶手出巷子以后盘问他，并且问完以后还得放他离开。"
    "这.............."
    "没有其他办法了吗？"
    if persistent.disagree:
       label chapter3_5_1:
            "你的意思是？不去阻止凶手杀死你母亲？"
            "嗯......"
            "要最小限度地影响未来......不然可能你的手表就不会回来了。"
            "没事的....你不用考虑我的感受......"
            "我相信你会将这一切......全部的时间轨迹全部抹除重写的......"
            "所以没事的。"
            jump chapter3_6
    else:
       label chapter3_5_2:
            "你的意思是......再让我袖手旁观一次吗？"
            "覃可汐那次......还有你母亲这次......"
            "这样做都是为了......保留你的手表......"
            "我心里比你更不好受.......但是必须冷静。"
            "留得青山在，不怕没柴烧。"
            "好吧。"
            jump chapter3_6
label chapter3_6:
    "你做得到吗？"
    "做不到也要做！"
    "如果你失败了的话，就逃跑吧！然后在未来拿到手表以后再次尝试去做！"
    "好！"
    "新的重担压到了我的身上。"
    "只不过这次我的任务，是直接找凶手问出直接结果。"
    "这个结果将直接影响到后面新的决策。"
    ".........."
    "准备好了吗？"
    "准备好了那就启动你的这块手表的功能，回到过去吧！"
    "嗯！"
    hide screen watch
    with dissolve
    show screen watch_loop1 nopredict
    with dissolve
    "我记得触发记忆输送的方法是......在表盘上画出这个手势。"
    "所以，我必须将手放到表盘上面......"
    "在回到过去之前......再看看这个时间的叶梓澄最后一眼吧......"
    "回到教室前面，透过窗口看看这个时间的覃可汐最后一眼......"
    "喂......叶梓澄......你觉得平行宇宙是存在的吗？"
    "你说会不会，我发送了记忆回过去以后，我依旧站在这个原地，你也依旧在这。"
    "回到过去执行任务的也就只是过去的那个，不同平行宇宙的那个我而已。这里的我，依旧在这里。"
    "谁知道呢......"
    "叶梓澄说道。"
    "嗯......先启动手表再说吧......"
    jump loop1_false
label loop1_false:
    "果然还是不行！"
    "让我主动，抹除这几天的珍贵时光，我反而做不到了。"
    "而且这次需要做的事情的风险...一旦我失误了......"
    "可能会再也没有翻身的机会了......"
    "林洛？你把记忆发送回过去了吗已经？"
    "嗯，发送了。"
    "但是这是我的谎言。"
    "那这个世界，似乎并没有发生变化。"
    "难道确确实实，是平行世界吗？"
    "是吧。"
    "撒谎也无所谓了，经过这几次的不断重复时间，我也累了。"
    "会有其他的拯救覃可汐的办法的。"
    "叶梓澄终于忍受不住，跪地痛哭了起来。"
    "呜呜呜~"
    "所以.....我们所做的一切,都是徒劳的吗?"
    "不会对我们现在这个世界产生任何影响......"
    "我觉得我得说点什么。"
    "叶梓澄......"
    "会有其他办法的......最坏的那个未来，现在还没有发生不是吗？"
    "至少我觉得，我们还可以拯救覃可汐。"
    "怎么救？"
    "带着覃可汐，离开沁野市吧！"
    "........."
    "在我们这个世界，能做的确实只有这件事了。"
    "那，带覃可汐去哪呢？"
    "去一个，没有纷争，远离喧嚣的地方吧~至少这个地方不会被AADR注意到！"
    "就这样，我和叶梓澄约好了，和她放学后在校门口会合。带着覃可汐一起。"
    "下午到了。"
    "喂！叶梓澄！林洛！把我叫出来，是继续讨论小说的构思和剧本吗？"
    "覃可汐你听我说！"
    "我搭上了覃可汐的肩，用郑重的口气说道。"
    "啊！~"
    "覃可汐被我突如其来的的举动吓得不轻，但很快强作镇定了。"
    "林洛...这不合适吧...其他学生在看着呢..."
    "跟我一起离开沁野市吧！"
    "啊！！！"
    "啊？？？"
    "你......你是认真的？"
    "这算是表白吗？"
    "班长.....这是怎么回事？"
    "覃可汐，跟我们离开吧，详细的事情我们以后再告诉你。"
    "嗯.....我是不是得先问问我爸妈?"
    "我觉得你父母不会同意的!所以!现在走吧!"
    "嗯.....额......"
    "依然叶梓澄也在的话......那我就先听你们的吧......"
    "但是叶梓澄...林洛...你们脸色都不是很好啊......果然是出了什么事吗？"
    "或许我可以帮忙解决呢？嗯？"
    "说出来吧！藏在心里也很不好过吧~"
    "对不起.....覃可汐......"
    "如果继续呆在沁野市的话......你会死掉的！"
    "啊？"
    "我会死掉吗......"
    "但是我相信你的话哟！叶梓澄！"
    "毕竟你是叶梓澄嘛！"
    "所以跟我们一起离开吧！"
    "到一个，你不会死掉的地方去！"
    "好吧......但是详细的事情一定要跟我讲清楚哦！叶梓澄！"
    "因为我相信你！不会做对不起我的事的！"
    "林洛！选好目的地了吗？"
    "还没，第一步先出沁野市吧！"
    "那我去拿我父亲的研究笔记？"
    "不用了....吧......."
    "有什么意义呢？"
    "也对.........."
    "但是现在距离星期五....还有段时间。"
    "先回家各自收拾东西吧！"
    "嗯......"
    "啊？收拾东西...么？"
    "那我会尽量偷偷收拾的......"
    "那我们什么时候再回来？"
    "覃可汐......"
    "我们不会再回来了......"
    "啊？"
    "覃可汐的脸黑了下来，露出了沮丧的神情。"
    "果然我还是......舍不得我爸妈......"
    "我......"
    "今天先回家吧！"
    "覃可汐！以后还会回来的！真的！"
    "很快的！"
    "嗯......"
    "分别覃可汐和叶梓澄以后，我乘上了回家的公交车。"
    "对不起了.......叶梓澄.......请允许我任性一次......"
    "15天......就15天......"
    "15天之后,我就会继续我的任务。"
    "所以请允许我，在这十五天内得到短暂的休息吧。"
    "到站了。"
    "呜~~~！"
    "是什么！！"
    "公交车刚刚走远，就感觉有人勒住了我的脖子。"
    "从我的背后。"
    "是谁！！"
    "我本来打算呼喊，但是嘴里被一块布堵住了。"
    "身体也变得昏昏沉沉......眼睛也快睁不开了......"
    "糟了............"
    "........."
    "额....."
    "啊!这是哪儿？"
    "我睁开双眼，仔细端详着周围的一切。"
    "发现自己被关在了牢笼里。"
    "额！"
    "不止是我，叶梓澄和覃可汐也......"
    "她们还昏迷着。"
    "过了十几分钟，叶梓澄和覃可汐醒过来了。"
    "在这之前我确实有想过手动叫醒她们，但是我身体却不愿意这样做。"
    "嗯.......嗯？"
    "这是？"
    "这是？"
    "醒了吗？我们好像被什么人给囚禁起来了。"
    "啊......这是什么play？"
    "我说的是正经事！"
    "我也和你们一样，被什么人给弄晕了，醒来之后就到了这里。"
    "这么说我也是，我还走在路上，突然就....."
    "我也是。当时想着完蛋了，遇到尾随痴汉了。"
    "所以是谁，为什么要这么做？"
    "铁栅栏外面是昏暗的走道，尽头慢慢没入黑暗，什么都看不到。"
    "现在几点了？"
    "不清楚！"
    "我身上的手机，还有我手上戴的手表，全都不见了。"
    "啊！我的手机也不见了！"
    "我也是！"
    "这是一个非常糟糕的消息。我的手表被拿走了。"
    "呃啊！开始后悔之前没有早点做出决策。"
    "过了一会，外面有人走了过来。"
    "叶梓澄！还有，两位关系人。"
    "林.....洛......还有....覃可汐..."
    "你是谁？为什么把我们关在这里？"
    "这也是没有办法的事情。"
    "谁让你继续调查你父母的事情的！已经快触及我们的红线了。"
    "果然是AADR吗？"
    "啊？什么AADR？你们在说什么？"
    "只有覃可汐还在一头雾水。"
    "为什么把林洛和覃可汐卷进来？"
    "因为你让他们也知道了不该知道的事情！"
    "本来组织里为了减少社会舆论，低调行动，是不打算处理掉你的！"
    "毕竟多亏了你父亲，我们得到了最想得到的东西。"
    "但现在我们不得不这样做了！"
    "把我们关在这里对你们有什么好处吗？"
    "哈哈哈哈哈哈~"
    "好处......放任你们留在外面就是对我们的坏处！"
    "虽然你们的行动根本不会对我们组织产生一分一毫的影响。"
    "但是上头说了，尽量防患于未然，所以必须处理掉你们。"
    "你们放心吧！我会把你们伪装成意外事故的！"
    "你们把我父亲怎么了？"
    "你的父亲？已经变成了他自己的研究的实验品了！"
    "不过你们也马上要步后尘了。"
    "我的话就只有这么多了。明天早上会把你们遣送到仪器所在的地方，乖乖成为实验品吧！"
    "等等！覃可汐是无辜的！她什么都不知道！请放过她！"
    "啊？"
    "开什么玩笑？放过她，然后出去以后好报警？"
    "虽然警察的事根本不算什么，但是只会给我们徒增麻烦。"
    "看着这人离去的背影，我陷入了深深的自责。"
    "我真的没想到，事情会发展成这样。"
    "我只是打算......只是打算.......能多十几天和朋友在一起的时光啊！"
    "到底是哪里出了差错？"
    "叶梓澄还在缜密思考。"
    "这不是真的吧！？"
    "叶梓澄？林洛？现在可以告诉我了吗？"
    "覃可汐你听我说，我们现在摊上麻烦了！"
    "这个AADR组织，是杀害我母亲和绑架我父亲的幕后黑手，更是会在未来杀掉你的杀人凶手！"
    "果然.....我会死掉的事情.....是真的呢......"
    "所以是跟叶叔叔的事情有关吗？"
    "叶叔叔？"
    "就是叶梓澄的爸爸.......在我和叶梓澄还上小学的时候，叶叔叔就经常带我们出去玩......"
    ""
    "虽然不知道你们是怎么知道的这么多的.....但是那我们现在该怎么办？"
    "林洛！你觉得AADR为什么会打算对我们下手？"
    "从你之前所经历的时间来看，AADR并没有干预我们的行动对吧！"
    "对！"
    "那一定就是在这次的时间，我们做了什么引起AADR对我们提高警惕的事情。"
    "如果那个人说的是真的，因为我们在调查我母亲的事情。"
    "那是怎么泄露出去的呢？"
    "AADR是怎么知道我在查呢？"
    "难道说一直就在监视我的行动？"
    "我觉得应该不是，如果一直在监控你的话！你怎么在未来造的出时间机器呢？"
    "对！那可能是我们所走访过的人中有人通风报信？"
    "还是说在课间我们讨论的时候......被AADR的人听到了？"
    "所以......林洛的构思的推理小说......都是真的？"
    "是真的.......我们希望你可以帮忙寻找我母亲去世有关的线索。"
    "但我怕直说的话你会对我有负罪感。"
    "叶梓澄.....我......"
    "善意的谎言吗......"
    "我们走访过的人......"
    "你去的警察局,还有我们一起去的,丁唯家,以及......"
    "班主任的办公室!"
    "喂!AADR的研究方向,是物理学科的吧!"
    "嗯。"
    "我们的班主任......是第一个发现案发现场并且目睹了行凶过程的人，并且......是物理老师！"
    "在我最开始所经历过的时间里，还依稀记得在一节她的物理课上，她专门给我们介绍了AADR这个组织........."
    "但是李老师她......"
    "种种迹象似乎都指向对班主任不利的地位。"
    "一起努力吧！想办法离开这里！"
    "然后......"
    "亲自对质！"
    "............"
    "然而这一天并没有到来。"
    "关押我们的监牢实际上早已处在运输设备上了。"
    "没有逃跑的机会，就被注射药物，押送到了。"
    "将物质转换成零子的，零子转换机旁边！"
    "我在昏迷前听到的最后的声音，仿佛是我班主任发出来的。"
    "我已经在学校方面给这三个学生汇报了失踪了。"
    "还是老样子，至少得留点东西下来，就跟昨天处理叶付的结果差不多就行，留条胳膊什么的。"
    "这样还能让家属死心。从而减少未来的阻碍。"
    "所以......是我和叶梓澄去她办公室的时候.......就把事情泄露给了AADR了......"
    "..............."
    "随着仪器吱吱声的响起，我感觉自己的存在不断被剥夺。"
    "然后就是无尽的虚无。"
    "感觉自己已经到达了另一个维度。"
    "一个黑暗，感觉不到任何东西的虚空。"
    "依旧很懊悔。"
    "我因为自己的一时私欲，害得事情发展到了无法挽回的方向。"
    "想再来一次机会也已经不可能了。"
    "自我的意识......慢慢消失在了这无尽的虚空之中.........."
    "永远地............................"
    "消失了.................................................."
    "......................................................................................"
    $ end = 2
    $ quick_menu = False
    play music "music/end.ogg" fadeout 1.0 fadein 1.0
    call disable_shortcut from _call_disable_shortcut_4
    scene bg_none
    show end2
    with fade2
    show endtext:
       xpos 0.3
       ypos 0.7
    with dissolve
    $ renpy.pause(4, hard=True)
    show screen game_end
    with fade2
    $ renpy.pause(189, hard=True)
    $ quick_menu = True
    call enable_shortcut from _call_enable_shortcut_4
    return
label loop1_true:
    play sound "audio/loop.ogg"
    show screen loop1_screen nopredict
    $ renpy.pause(10, hard=True)
    hide screen loop1_screen
    scene bg_none
    with fade
    "啊。"
    "呼~呼~呼~呼~"
    "这次的旅行比前几次显得轻松许多。"
    "从你的表情来看，你从未来回来了呢~"
    "我抬起头，看到的正是摊主，应该说是十年后的我才对吧。"
    "嗯！我回来了！"
    "调查结果怎么样？"
    "我了解到了叶梓澄的母亲遇害那一天的事情。"
    "但是无法判断杀害叶梓澄母亲的凶手背后是否有AADR的力量。"
    "也就是说，叶梓澄母亲的遇害，可能是AADR夺取时间刻校正仪的开端，也可能不是，还有更早的事件。"
    "未来的叶梓澄......也是这么认为的。"
    "倒不如说从一开始我们制造时间机器的直接目的就是为了阻止叶梓澄的母亲被杀害。"
    "但是后面随着时间推移，我们都逐渐冷静了下来。"
    "毕竟光有猜测是不够的，尤其是在这场涉及全人类的赌博之中。"
    "所以你们也怀疑叶梓澄母亲的遇害是开端，但是希望我去亲自验证吗？"
    "嗯......"
    "你那边的叶梓澄有跟你说什么吗？"
    "如果不足以得出结论，但你却又回到了这里。"
    "总不可能再度过一遍一周的时间吧！？"
    "班长希望我......回到她母亲被杀害的那一天......"
    "哦？希望你救下她母亲吗？"
    "希望我在事后询问凶手的杀人动机是什么。"
    "真不愧是叶梓澄呢~在那种情况下还能得出这种冷静的结论！"
    "难度呢？"
    "调查发现凶手是一个街头混混，没有杀人前科，猜测没错的话，凶手做完案以后应该处于很慌乱的状态。"
    "不然不至于被人目击以后，快速地跑出案发现场。"
    "所以你需要和跑出案发现场的凶手进行交涉？"
    "成功概率有多大？"
    "未知。"
    "失败以后怎么办？"
    "拔腿就跑。不排除凶手会对我使用暴力。"
    "逃跑以后，再次等到今天这个时间点，然后找你获取手表。"
    "反复尝试吗？"
    "虽然很繁琐也很危险，但倒不如说这是最安全的一种方法了。对未来干涉最小的方法。"
    "我的内心也很不安稳。"
    "让我盘问一个素未谋面的陌生人，而且对方还是个杀人凶手。"
    "手表的传输期限是十五天对吧！"
    "没错！"
    "叶梓澄母亲遇害时间是七天前。"
    "我计划将记忆发送到遇害前几天，这样可以给我更多的时间做准备。"
    "有物质上的准备，也有思想上的准备。"
    "嗯！"
    "你要记住，只要未来没有发生大幅变动，我就会在今天，在这个地方，等待你！"
    "你如果交涉失败了，就等到今天以后将事情的来龙去脉都告诉我吧！我会相信你说的话的！"
    "好！反正如果交涉成功了，获取到了有效信息，也依旧必须跟你从头到尾重新讲一遍的不是吗？"
    "摊主接过我的手表，将回溯的时间调整到了十天以前。"
    "开始吧！"
    "我戴上手表，绘制图案。"
    play sound "audio/loop.ogg"
    show screen loop2_screen nopredict
    with fade
    $ renpy.pause(10, hard=True)
    hide screen loop2_screen
    scene bg_none
    with fade
    ".................."
    "呼！！"
    "我惊醒过来，巡视着周围。"
    "我正坐在教室内，四周都是喧闹声。"
    "这熟悉又陌生的教室。"
    "我回到了我转学前的学校。"
    "芷柚市蜜溢区高级中学。"
    "看了看讲台上的钟表，现在的时间，是我转学到沁野市的十天前。"
    "也就是："
    "9月9日。"
    "时间则是12点43，这个点还是下课期间。"
    "也是午饭时间。"
    "我却是以午睡的姿势醒来的。"
    "想起来了，那个时候的我，因为晚上熬夜太困了，没吃午饭，一直在睡觉。"
    "放学后我就直接回到了家。"
    "因为我一直厌恶着这座学校。也不会对这所学校有一丝留念。"
    "为了应对各种可能发生的情况，我看了很多体术相关的教学视频。"
    "但是很遗憾，学不会，就剩三天时间，也不容易学会。"
    "只好放弃靠武力取胜了。"
    "还好我后面还有充足的两天时间，足够我进行物质上的准备了。"
    "我提前买好了前往沁野市的火车票。为了避免更大的影响，是我偷偷用零花钱买的，还好刚刚够。"
    "或许直接蛮力接触凶手不太可行。"
    "如果我假设是凶手的同伙，或者是凶手幕后指使人派来的人的话，凶手会相信吗？"
    "但目前来看这是最容易接触凶手并掏出情报的方法了。"
    "嗯！值得一试！"
    "就这样计划着，一转眼到了事发的那一天，也就是周一。"
    "我早上假装自己去上学，但实际上我已经向学校请了病假，因为只有半天，所以学校并没有给我父母联系。"
    "就这样，我一边瞒着学校，一边瞒着父母，坐上了火车。"
    "一路上很紧张，以至于平时坐车的晕眩感都减弱了。"
    "经历过漫长的煎熬以后，火车终于在沁野站停下来了。"
    "我背着我随身携带的唯一的挎包，里面装着我的手机，以及电击枪，虽然是网购的而且功率很低，但是给我制造逃跑的时间还是足够了。"
    "因为时间不够，所以忍受着高价在京西下的单。"
    "虽然贵是贵了，但是送的快，下完单第二天就取到了货。"
    "手机看了看时间，现在是上午十一点，还来得及。但是仍然不能放松警惕。"
    "我喊了一辆出租车。"
    "虽然我很不想坐，但是这点代价相较于需要获得的情报来说，简直就是微不足道。"
    "车上即便又强烈的晕眩感和想要吐出来的感觉，但我还是忍了。"
    "拜托师傅将我送到了那个巷子外面公路的对面位置。"
    "现在时间是十二点多。"
    "我坐在路边的长椅上，一边假装玩手机一边关注着公路对面的情况。"
    "不知道过去了多长时间。"
    "反正我额头上的汗珠一滴滴地往地上流，肚子也愈发感到饥饿。"
    "额！"
    "我看着一个穿着风衣，戴着遮阳帽的女人，提着挎包走进了巷子。"
    "我立马警惕了起来。"
    "但是我现在还不能行动！"
    "根据已知的情报，凶手是在目击者进巷子以后才慌忙地逃出巷子的。"
    "而切好，目击证人是我未来的班主任。"
    "所以我需要继续等到我的班主任的出现并走进巷子。"
    "焦急地等了大约三分钟，我看着我的班主任提着菜篮子，走过了巷子口。"
    "随之则是意料之中的画面。"
    "班主任朝巷子里看了一眼，随后冲进了巷子。"
    "就是现在！！！"
    "我赶紧从椅子上站起来，趁着路上车辆不多，穿过公路，蹲守在了巷子旁边。"
    "十几秒后，听到了急促的呼吸声与跑步声。我紧张地摸了摸包里的电击枪。"
    "呼！呼！"
    "来了！！"
    "看到有人从里面出来了。"
    "在他朝背对着我的方向走出几步之后，我快跑上去，拦在了他面前。"
    "哪来的小鬼！别挡路！！"
    "我是组织的人！"
    "我开口道。"
    "什么组织？动画片看上脑了吗？让开！给我让开！"
    "看对方的脾气逐渐暴躁，我有点想退缩了。"
    "但是为了获取情报，我还是坚持站在原地。"
    "我是派来监察你工作成果的，派你来的的那个人，派的我！"
    "有完没完啊！给我让开！不然等会警察来了！！"
    "对方双手将我推开，然后继续逃跑。"
    "看他这言行举止，完全不想是受命前来杀人的。"
    "我开始犹豫是继续向前追去，还是看事发现场一眼。"
    "还是看看吧！"
    "我探头看向巷子里。"
    "巷子深处，叶梓澄的母亲倒在地上，旁边我的班主任正在和警察通话。"
    "一切正常！果然还是继续追上凶手问个底吧！"
    "啊？"
    "这是........."
    "我正打算离开的时候，我看见班主任从叶梓澄母亲的衣兜里，摸出了一部手机。"
    "在打开手机，看了几分钟以后，揣进了自己的兜里。"
    "这.................."
    "从凶手的话语，以及班主任的态度来看。"
    "我未来的班主任.......难道就是......"
    "我内心受到极大震撼。"
    "在和叶梓澄调查的时候，调查了这么多，却从来没有怀疑过班主任........"
    "或许这是班主任对我们的温柔，导致了我们下意识地认为其不会做这样的事情吧......"
    "但很明显，我们错了。"
    "班主任......从她的所作所为来看，毫无疑问，她就是一切的开端！"
    "............."
    "我连忙离开案发现场，趁着班主任没察觉到我之前。"
    "但是这个时候我突然意识到了一件事情。"
    "监控探头毫无疑问已经拍到了我。"
    "拍到了拦截凶手的我。"
    "希望对未来不会造成什么影响。"
    "坐着返程的火车，我终于冷静了下来。"
    "开始思考今天的发生的这一切。"
    "叶梓澄说过，她母亲出事以后身上手机已经不见了。"
    "我找凶手谈话的时候，对方也一副完全不搭理我的话的样子。"
    "好像完全不理解我在说什么一样。"
    "虽然我自己也完全不理解我在说什么。"
    "所以......叶梓澄母亲的手机....其实是被目击者，也就是班主任......"
    "拿走了！！"
    "如果班主任跟AADR有联系的话，一切都说得清楚了................"
    "物理老师...事件目击者...拿走了现场的手机..."
    "而且我还想起了上课的时候,班主任在物理课上确实有提到过AADR这个组织......"
    "真相逐渐浮出水面了。"
    "班主任是AADR有关的人，在其偶然目睹叶梓澄母亲被杀以后，报警的过程中偶然发现了叶梓澄母亲的手机。"
    "在翻阅手机内内容以后，发现了叶梓澄父亲的研究项目是AADR一致梦寐以求的东西。"
    "最后导致了AADR的人进入叶梓澄父亲的研究所，绑架了叶梓澄父亲并搜刮了研究资料和科学仪器。"
    "解——————————"
    "我在心中如此想到。"
    "我必须将这件事告知给十年后的我，以及未来的叶梓澄。"
    "以便进一步商量对策，以及————"
    "特别提防我未来的班主任！！"
    "我回家之后确实挨了一顿骂，但这都是小事。"
    "几天后警察确实找到了我询问情况。"
    "不过他车上没有空调就是了。"
    "问我和犯罪嫌疑人的关系，我只是说碰巧路过，觉得可疑所以把拦下来了。"
    "估计是因为查到我和凶手在之前没有任何交集，所以警察相信了我说的话。虽然确实没有任何交集就是的了。"
    "还表扬了一下我。"
    "........"
    "在时间的流逝和我这几天的坐立不安中，那一天到来了。"
    play sound "audio/car_stop.ogg"
    car "{color=#C1394F}尊敬的旅客您好！沁野市高级中学站到了！请各位旅客有序下车！谢谢！{/color}"
    "我一下车，就主动走向了那个摊位。"
    "呼~呼~太好了~"
    "还在~这里~"
    "这说明我并没有对时间的走向做出过多的干涉，太好了。"
    "我刚走到他身前，手臂就被抓住了。"
    "这块手表送你了。戴上吧。"
    "来自未来的我！"
    "终于等到你了！"
    "啊？你没有被我的话吓到吗？"
    "我可是未来的你！你经历过的事情，就是我经历过的事情！"
    "也对。"
    "步入正题吧！未来的人类的灾难，AADR组织对人类的奴役..."
    "这一切的源头就是："
    "班主任偶遇了杀人事件，而恰好班主任是AADR相关人员，所以引起了未来的质变。"
    "那现在该如何去做，也有了一个确定的方向了！"
    "我和叶梓澄这十年来的努力......终于要..........."
    "............."
    "那，下一个任务，也或许也是最终任务，就交给你了！"
    "任务目标：回到事发当天，并救下叶梓澄的母亲！从而阻止跟AADR有关系的，你转学班上的班主任，拿到叶梓澄父亲的研究资料！！"
    "终于到了这个时候了！啊！看到了吗？来自未来的叶梓澄！来自未来的，覃可汐！"
    "我马上就要做到了！"
    "做到改变时间的走向了！"
    "做到改变人类的未来了！"
    "我的手已经激动的发抖了。"
    "但我还是尽量深呼吸让自己冷静下来。"
    "呼~马上就能终结我这不断回溯的命运了，在黑暗中我看到了光芒。"
    "只要阻止凶手作案，就可以直接影响到整个人类的未来，这就是蝴蝶效应的魅力所在啊~！"
    "但是我........"
    "我要不还是找叶梓澄先讨论一下吧！~"
    "你最好还是不要这样做......"
    "你的班主任或许也发现了你出现在监控里，出现在案发现场的事情！"
    "当你进学校，当她看到你的脸的时候，可能未来又会被大幅改变！"
    "毕竟她是AADR的人！"
    "也对........"
    "但是？"
    "你作为未来的的我，能现在能在这里，不就说明了班主任不会对我做什么吗？"
    "或者说班主任不会怀疑到我头上来。"
    "时间的方向可是不断在变动的。"
    "过去的我不会被发觉，但是现在的你不一样了，你见到了经历过过去的现在的我。"
    "果然还是担心蝴蝶效应吗？"
    "对。"
    "叶梓澄.......覃可汐.......等事情结束之后.....再一起去漫展吧~"
    "这也是推动我不断前进的动力。"
    "你有信心去完成吗？"
    "凶手的作案工具只有双手，所以我计划用钝器击晕凶手，然后直接报案。"
    "目的则是：赶在班主任之前，让我成为目击者，不，成为阻止行凶者！"
    "那，你想回到哪个时间点？"
    "十天前吧！我上次就是回到的十天之前。"
    "已经走过的路，再走起来总会熟悉一点。"
    "好！"
    "摊主接过了我的手表，调试了一会以后，递给了我。"
    "那！我开始了！"
    "让这不幸的宿命，让这轮回的命运————"
    "皆终结于此地吧！"
    "我熟练地在手表上绘制了手势。"
    play sound "audio/loop.ogg"
    show screen loop2_screen nopredict
    with fade
    $ renpy.pause(10, hard=True)
    hide screen loop2_screen
    scene bg_none
    with fade
    call disable_shortcut from _call_disable_shortcut_5
    $ persistent.chapter4 = True
    $ persistent.chapter==4
    $ persistent.extra_chapter4 = True
    $ persistent.achievement_chapte3 = True
    image chapter4 ="chapters/chapter4.webp"
    scene bg_none
    $ quick_menu = False
    show chapter4
    with fade2
    $ renpy.pause(10, hard=True)
    hide chapter4
    with fade2
    scene bg_none
    $ quick_menu = True
    call enable_shortcut from _call_enable_shortcut_5
    $ save_name = "{font=Huayuan.Gothic.Bold.ttf}章节四：命运枷锁的挣脱{/font}"
    "....................."
    "呼！"
    "又回来了，久违的，我转校前的高中。"
    "耳边传来久违的喧嚣。"
    "我不会对这个学校有什么留恋。"
    "反正没有值得我留恋的东西。"
    "没有朋友，没有知心的人，只有应试。这种学校我才不想呆下去。"
    "倒不如说整天除了上课，考试就没有其他活动了。"
    "整所学校只充斥着升学的氛围，完全没有一丝社交的空闲。"
    "在这种学校，学习和升学的压力压得我抬不起头，所以早点离开算了。"
    "..................."
    "煎熬地熬过了放学时间。"
    "我现在要全力准备。"
    "准备迎接三天后的，改变世界的那个事件！"
    "我去了附近的集市，想寻找看看有什么趁手的兵器。"
    "趁手的适合制止凶手行凶的兵器。"
    "有没有球棍什么的啊~在这秋蝉鸣泣之时！"
    "算了，这玩意不好带上火车吧！"
    "当然我没有带过的经验，所以并不清楚能不能带。"
    "或许我可以转变一下思路，阻止事件发生的话，我让叶梓澄的母亲不要往巷子里走不就可以了吗？"
    "感觉变数太大了，而且有种治标不治本的感觉。"
    "还是制止凶手行凶比较安全与稳定一些。"
    "当然我指的安全并不是我的人身安全。"
    "虽然还有另一种方法，从目击者身上下手....."
    "我在想什么？这种做法连想都不要想！太恶劣了！"
    "只需要阻止叶梓澄母亲被杀就行了，如果对凶手的反击过重的话可能就把我自己给搭进去了。"
    "可不想进橘子喝茶。"
    "但是又得让凶手丧失行动能力，以免被反扑。"
    "嗯.........."
    "有了！"
    "根据凶手的作风，只要被别人目击了，就会畏罪潜逃，毕竟本质上就是一个混混而已。"
    "新的计划有了。"
    "依旧在京西发货了一把电击枪，自卫防狼用的那种，当然绝大多情况下我是不会去用它的。"
    "仅仅是用作，在所有计划都失败以后留的后路。"
    "我照着我上次的经验，打好了假条，买好了车票。"
    "虽然我跟家长写了检讨，也担保了绝不再犯。"
    "但是担保的是过去的我，这段历史已经被现在的我给抹除了。"
    "在不断的准备与等待中，这一天又来到了。"
    "熟练地假装去学校上学，实际上却乘地铁到了火车站。"
    "乘坐着跟上次一样车次的列车，前往和上次一样的目的地。"
    "跟上次一样的时刻出发。"
    "由于没吃早餐的关系，空腹的我并没有感觉到有太晕的感觉。"
    "一个伟大的科学定律被发现。"
    "我心中想着。"
    "我紧紧抱着我的挎包，里面装着重要的物品。"
    "漫长的车程以后，终于到站了。"
    "出站后找到了上次那位出租车师傅。"
    "师傅，去这里！"
    "我将手机导航软件的界面递给他看。"
    "欧了！"
    "........."
    "又经过了一段车程以后，我回到了小巷的正前方。"
    "呕~我收回我之前说的话。"
    "好晕好想吐。"
    "感觉喉咙里卡了长袜子。"
    "虽然如果是白色过膝袜的话也不是不可以。"
    "我坐上了命运的长椅，开始审视着公路对面，小巷前方的这一切。"
    "现在的时间是十二点多。"
    "我目不转睛地盯着对面的情况。"
    "来了！"
    "叶梓澄的母亲，也就是一个穿着风衣，带着遮阳帽的女人，提着包走进了巷子。"
    "我不顾红绿灯，穿过了巷子，紧随其后进了小巷。"
    "于是，我目击到了："
    "那个...这位大哥，可以让一让吗？我需要到巷子对面去！"
    "啊~？让路？"
    "这条路是你修的吗？"
    "既然不是，那老子凭什么给你让路！"
    "你想过去......过去好啊！留下买路财！"
    "那对不起打扰了..."
    "叶梓澄母亲想转头离开巷子，被对方一手抓住。"
    "嗯？想走？"
    "你....你想干什么？"
    "想干什么？老子打牌输了钱，现在心情很不好！"
    "今天你不给我钱就别想活着离开！"
    "今天真倒霉，算是碰到臭流氓了！"
    "啊？！你再说一遍？"
    "闪开！本来想给你点面子的！"
    "你如果不放我走，那我报警了！"
    "叶梓澄母亲打算伸手掏手机。"
    "不许报警！！！"
    "却被对方用手勒住脖子。"
    "手机也从手上滑落，坠在地上发出了清脆的响声。"
    "他奶奶的！老子最恨的就是你们这群有钱人了！"
    "凭什么你们什么都不做就有这么多钱，老子累死累活干几十年到最后还是混的个人财两空！"
    "我跟你...不一样...."
    "叶梓澄母亲一边挣扎一边说道。"
    "有什么不一样！！！"
    "对方发怒了。"
    ".........."
    "啊！！"
    "好痛！！！"
    "谁打我！！！"
    "正是我。"
    "在外面等待的时候我也没闲着，在垃圾桶翻了几个玻璃瓶，在路边捡了几块干水泥块，塞进了我的挎包里。"
    "这就足够了。"
    "你是哪里来的小屁孩？？给老子滚开！！"
    "我要报警了！"
    "我掏出手机，对对方面不改色地说道。"
    "虽然在别人看来是面不改色，但我内心已经紧张的不得了了。"
    "你找死吗？"
    "你......你不许报警！！"
    "对方放开了勒叶梓澄母亲脖子的手，朝我扑了过来。"
    "住手！！！！"
    "来了！"
    "班主任的声音！"
    "可恶......今天就先放过你们！！！"
    "小混混说罢，扭头狼狈地逃出了巷子。"
    "成.....成功了......."
    "我的作战计划..............."
    "谢......谢谢......"
    "你们还好吗？这里发生了什么？"
    "真是千钧一发啊~"
    "幸好我算准了班主任会目击的时间。"
    "成功拯救了叶梓澄的母亲。"
    "这就意味着......AADR不会获得关于叶梓澄父亲的研究资料..."
    "也意味着，未来AADR不会依靠时间刻校正仪来统治世界...意味着覃可汐不会因此死去......"
    "一想到这，我不禁热泪盈眶。"
    "看到了吗？十年后的我！看到了吗？十年后的叶梓澄，还有未来的叶梓澄。"
    "我成功了。"
    "但是它们不会看到了。"
    "我在这里终结了AADR的统治，也意味着未来的我和叶梓澄不会再发明时间机器回到这个时代了..."
    "这样倒也好......我会记住你们所做出的努力的......我会永远记住的！"
    "..............."
    "....................."
    "........."
    "一转眼，又到了我转学的这一天。"
    play sound "audio/car_stop.ogg"
    car "{color=#C1394F}尊敬的旅客您好！沁野市高级中学站到了！请各位旅客有序下车！谢谢！{/color}"
    "一下车，我就赶忙朝着摊主的位置走去。"
    "但是..............."
    "没有了。原本会有一个坐着轮椅戴着帽子的人在这里，但是现在，"
    "没有了。"
    "以后也不会再有了。"
    "这对他来说，也是一种解脱吧。"
    "对未来的我来说。"
    "不需要心力憔悴制造时间机器回到这个时代，而是幸福地在未来度过。"
    "我希望是如此。"
    "我这样想着，踏步进了校园。"
    "因为没有被摊主挽留，所以这次我进学校的时候，大家还在上课。"
    "额......"
    "我又不自觉地发抖了。"
    "怎么会........"
    "为什么.........."
    "经历过这么多次磨练的我，怎么能连顶着班上同学注视的目光走进教室这件事都办不到......."
    "嗯！我必须坚持克服下去！！"
    "............"
    "随着下课铃声响起，整个教学楼也变得喧闹。"
    "我也终于可以从洗手间里出来了。"
    "对不起.....我还是.....做不到......."
    "未来的我加油吧！现在的我依旧做不到！"
    "就这样.................全新的，和平的校园生活.......开始了。"
    "............."
    c "啊~是转校生啊。你叫林洛是吧。请多关照。"
    "怎么了.........有什么事情需要帮忙吗？"
    "怎么了.............啊！？"
    "林洛.........你为什么.........为什么..........在哭啊？"
    "我.................."
    "班长你好.......以后的高中时光.......请多关照......."
    "...................."
    "............................."
    x "林洛！"
    x "那个...我就长话短说了。你，，，或者你的亲属。以前是否来过沁野市。"
    "或许有过吧.........."
    "或许我们之前确实.........见过面呢......."
    "是吗...........如果是的话..........谢谢了................"
    "林洛.......你怎么哭了？"
    "是吗？我怎么又哭了........"
    "你跟我道谢.........的理由是什么呢？"
    "谢谢你救了我！"
    "！！！！！！！！！！！！"
    "是关于什么？"
    "我也不清楚了.......记不清是梦境还是现实了........那个......总之谢谢你......."
    "如果我弄错了的话...抱歉..........."
    "................."
    "......................"
    "我依旧结识了班上的朋友，包括叶梓澄和覃可汐..................."
    "但是她们在被抹除的时间内所做的事情.......就不告诉她们了......."
    "也没必要告诉她们了............"
    "星期三到了，叶梓澄并没有被班主任喊出去。"
    "啊？林洛你怎么突然提起这个...........这........不好透露吧.....毕竟是个人隐私...."
    "所以不方便说吗......好吧......"
    "总之我父母都生活的很好啦~"
    "那就好~"
    "这我还得感谢你！"
    "啊？难道......."
    "我妈跟我谈起，上个星期的时候我妈碰到了一个混混，后来还是一个高中生和我的班主任出来见义勇为，度过了难关。"
    "我妈当时拍了照片，我一看.....这不就是你嘛......林洛！"
    "这个时间上的叶梓澄，也变得爱笑了，再也不是那副悲伤的面庞了。"
    "但是你是.....这个星期才转学过来的....."
    "所以我脑中还是存在一个疑问..."
    "来沁野市旅游的时候刚好路过而已......"
    "是这样吗.......那还是谢谢了......"
    "但是....."
    "驳倒！！！"
    "我妈拍下照片的时间是星期一，这个日期你应该还在学校上课才对！怎么可能出来旅游？"
    "！！！！我被叶梓澄的追根问底惊到了。"
    "额......开个玩笑.....别见怪......"
    "只是想模仿一下苗花诚......"
    "但是还没到学级裁判呢！！"
    "啊哈哈哈哈哈哈哈......."
    "我们都不约而同地笑了起来。"
    "真好啊~这样的校园生活~"
    "星期五到了，覃可汐也一切正常。终于！"
    "林洛！"
    "怎么了？"
    "都快放学了，还有什么要说的吗/"
    "明天的漫展别忘记咯！"
    "怎么会呢！我明天肯定来！"
    "说好咯！？"
    "你不需要准备什么服装，我家都有的！"
    "然后......游戏机明天就还你！目前我也只差四大天王了！！"
    "那二周目不打了吗？"
    "啊？二周目是什么？"
    "这游戏不是成为联盟冠军就算通关了吗？"
    "不是啊！成为联盟冠军之后还有一堆剧情呢！"
    "额.........."
    "覃可汐陷入了思考。"
    "看着覃可汐健康地活着，内心也是说不出的感觉。"
    "即便再次回想起我之前所做的一切，也依旧有点后怕。"
    "幸好一切都成功了！"
    "我！让覃可汐的未来发生了改变。"
    "这并不是什么励志演讲词，而是货真价实的事情。"
    "这来之不易的和平，则更加值得我去珍惜。"
    "这来之不易的校园生活，以及好不容易第一次获得的。"
    "朋友的感觉。"
    "几分钟后，覃可汐回过神来。"
    "看来是思考完毕了。"
    "那......要不......再让我多玩几天？"
    "当然可以。"
    "意料之中的发展。"
    "真的太感谢了！！"
    "早知道这么好玩，我暑假就不整天出去玩了。"
    "就算搬两个月的砖也得买一部游戏机的！"
    "这倒不至于。"
    "现在只能等寒假了。"
    "所以你已经提前规划好了压岁钱的用途了吗？"
    "那当然~"
    "对我来说倒是规划了也没用。"
    "对很少出门的我来说，即便是过年走亲戚，也不会走多少家。"
    "也自然不会拿到多少压岁钱，目前的个人纪录是300块就是了。"
    "你每年可以拿多少压岁钱？"
    "在拿压岁钱这方面，我算是没见过世面的了，所以问问见识广的也算正常，也算合理。"
    "大概三四千吧！"
    "也对，毕竟你这么可爱....."
    "额！！！！"
    "你就当什么都没听到！"
    "啊嘞嘞~~"
    "这可不行！虽然我确实很可爱。"
    "但是从你口中说出来，就很奇怪呢~"
    "哪里.....奇怪了......"
    "不小心说错了话，我突然不知所措了。"
    "我应该怎么做。"
    "放弃了，只能像做错事的孩子一样羞愧地把头埋在课桌里。"
    "啊！？你不会生气了？"
    "那好吧！我不会跟任何人说的！"
    "我只是开个玩笑而已~"
    "问题不在这里，我只是大脑处理器遇到了无法计算的，缺少相应板块的事件。"
    "这不就暴露了我是个童贞了吗~"
    "不知过了多久，感觉风头已经过去了，我试探性地抬头。"
    "你好啦？"
    "唔嗯！！？"
    "覃可汐一直在看着我吗？一直在等着我抬头？"
    "你也挺可爱呢~"
    "お可愛い子供~"
    "！！！大脑服务器遭到了未见过的攻击，紧急宕机！！！"
    "只得赶紧再将头埋进课桌。"
    "哟~你脸红了！"
    "难道林洛你.....是童贞吗？"
    "不要再说了......."
    "我恳求道。"
    "终于放学了。"
    "收到覃可汐整蛊的关系，我到现在还没缓过神来。"
    "已经没法正眼看着覃可汐了，只能灰溜溜地出教室。"
    "林洛你不会真的生气了吧？"
    "！我的手被谁抓住了。"
    "不用想，肯定是覃可汐。"
    "我.......我才没有生气........真的......"
    "我回过头，盯着覃可汐的脖子看。"
    "至于为什么看脖子........"
    "我羞于直视覃可汐的正脸，但是又不敢看脖子以下的部位......"
    "明天的漫展........我会去的........"
    "但是我现在有点事.........先走了........"
    "..........."
    "呼~呼~终于逃出来了！"
    "这种情况感觉比我之前所经历过的困难还要棘手！"
    "但是既然我已经答应了，明天还是早起一点吧！"
    "........"
    "找了一套还算体面的衣服。"
    "就这样吧。"
    "为了避免父母的追问，我直接说是参加学校要求的社会实践去了。"
    "不会告诉他们我今天打算去漫展。"
    "毕竟要是寻根问底起来，就有够麻烦的。"
    "感觉自己已经真正的习惯这和平的生活了。"
    "仿佛那次事件从未发生过一样。"
    "确实从未发生过，对目前的情况而言。"
    "就这样吧。不去想这些了。我已经很满足了。"
    "我熟练地搭乘车辆，前往覃可汐的家。"
    "毕竟........之前有来过......."
    "还是不去想这些事了。已经过去了。"
    ".................."
    "终于到了。我今天也是特地没有吃任何东西。"
    "晕车的状况确实有一点好转。"
    "说实话路上我也快无聊死了。"
    "坐车的时候只要我看手机，就会加重晕车的情况。"
    "这是我长年累月总结出来的经验。"
    "就只能戴着耳机看着窗外听歌而已。"
    "林洛！"
    "前来迎接我的是覃可汐。"
    "来的挺早的嘛！居然没有迷路哈哈~"
    "等会。"
    "......"
    "班长还在房子里试衣服呢~"
    "所以你现在还不能进我的卧室。"
    "覃可汐突然把脸贴近到我耳边，轻声说道："
    "当然如果你想看的话，也可以进去。"
    "！这种玩笑还是不要开的好。"
    "简直是恶魔的低语。"
    "哈哈~开玩笑开玩笑！"
    "不过料到你不可能做得出来。"
    "毕竟是.."
    "你说什么我没听到？"
    "啊什么都没说！"
    "回应的很彻底。"
    "算了，不深究这些了。"
    "等了好一会，叶梓澄出来了。"
    "有劳久等了，我们走吧！"
    "有点失望...呸！才没有！"
    "啊嘞嘞~林洛你好像很受打击的样子呢！"
    "我都说过啦！只是试穿而已！你想饱眼福的话还是忍耐到漫展吧！"
    "可汐！！不要乱说！"
    "好啦好啦！走吧！"
    "我们前往最近的车站，搭乘了前往漫展场地的公交车。"
    play sound "audio/car_stop.ogg"
    car "{color=#C1394F}尊敬的旅客您好！会展中心站到了！请各位旅客有序下车！谢谢！{/color}"
    "下车了，我长舒了一口气。"
    "真热闹啊，街道上也都是cos的人。"
    "说实话我表面上显得沉着冷静，实际上我已经慌得不行了。"
    "因为这是我第一次来漫展。"
    "此前一直是呆在家，没有朋友，自然也没人邀请我去漫展。"
    "走吧！林洛！我们去换衣服！"
    "啊！？"
    "在哪换？"
    "里面有专用的换衣间的！走吧！"
    "哦...好..."
    "什么都不熟悉的我只能被覃可汐她们领着走。"
    "好羞耻啊......我可以回去吗....."
    "早知道就拒绝的......"
    "不！"
    "绝对不能拒绝！"
    "好不容易才拥有现在的生活。"
    "我必须去学会拥抱它，适应它，毕竟不会再回到那段痛苦的时光了。"
    "等覃可汐和叶梓澄换完衣服以后,我们就到了会场内."
    "覃可汐穿的是恨蜜莉雅的cos服，精致的简直像娃娃一样。"
    "真的太可爱了......但是这种思想仅限于脑海中。"
    "仅存在于海马体和......海绵体.....？"
    "我还是赶紧切腹谢罪吧........"
    "至于叶梓澄的这身cos服，则是二雷娜的，不能说是还原，只能说是就是本人。"
    "尤其是那眼神。"
    "简直是..........."
    "喂！别光盯着我看啊！！"
    "啊！？你怎么知道我在看你！"
    "你是.....笨蛋吗？这种事情....看眼神就知道啊！！"
    "额........！？"
    "这附近最近的下水道是哪里？我申请进去躲一躲。"
    "............."
    "嗯！"
    "我们去那个地方吧！"
    "覃可汐提议道。"
    "嗯！那里人比较少，就去那吧！"
    ".........."
    "林洛！！"
    "来都来了，过来帮我们拍个照呗！？"
    "可以！~"
    "谢谢！"
    "我拿着覃可汐的手机，给她们拍了张合影。"
    "林洛你也拍一张吧！"
    "原来还包括我吗？"
    "心中感到一丝安慰。"
    "覃可汐拿出了她的自拍杆。"
    "3~2~1~"
    "茄子！！"
    "我，还有叶梓澄和覃可汐，一起比起了剪刀手。"
    "对她们来说，这或许是再熟悉不过的场面了吧~"
    "林洛！"
    "我会把照片发给你的！"
    "好！~"
    ".............."
    "...................."
    "漫展终于结束了，我等叶梓澄和覃可汐换完衣服，准备离开会场。"
    "真的快热死了。"
    "今天玩的怎么样？"
    "很开心！！"
    "是吧~！我就说嘛......你肯定会喜欢上的！！"
    "虽然很累人，但是我确实感到了这辈子从来没有体会过的快乐。"
    "或许这就是苦尽甘来的感觉吧！~"
    "话说可汐......你又买这么多周边......"
    "你家里还放得下吗？"
    "嗯................"
    "没关系的！我卧室虽然贴不下了，但我可以贴我妈卧室里！！"
    "晕~你要给你父母传教吗？"
    "嗯............有在考虑！"
    "不愧是覃可汐！"
    "但是我还是搞不懂，为什么覃可汐一个动漫的周边要买三袋。"
    "我的双手沉甸甸地提着周边，问道。"
    "这个辉日大小姐的礼品盒不便宜的吧~你为什么会买三份呢！？"
    "难道是？"
    "没错！就是！"
    "覃可汐期待着看着叶梓澄。"
    "就是？是什么？"
    "我也看向叶梓澄。"
    "一份收藏，一份自用，一份传教！"
    "还是梓澄了解我！"
    "满头雾水。"
    "这是倒霉星里面的名台词啊！！林洛你入宅看来还不够深啊！"
    "被叶梓澄批评了。"
    "对不起.........马上回去看！！"
    "你说的哦！下周一我要找你提问的！！"
    "答不上来的话......哼哼........."
    "答不上来的话........会怎样？"
    "把你游戏存档里的材料全部卖掉！！"
    "啊！！可恶！绝对不能这样干！！"
    "虽然我有amido，可以再刷回来。"
    "但是刷够这么多的材料还是要花很多时间的！"
    "不要！！"
    "这可由不得你........毕竟人质....不是..机质在我手里！！"
    "这下不看不行了！"
    "我的游戏机.....我会为了你....努力去做的....."
    "怎么突然燃起来了？"
    ".................."
    "有说有笑地坐车回到了家。"
    "久违的充实，与久违的.......日常........."
    "在这般满足中.........我进入了梦乡............."
    "...................."
    "已经习惯了很久了......."
    "没有手表的生活..........."
    "没有意外发生的生活.........."
    "一切都很正常..........一切都像普通的生活一样正常......."
    "我也和普通的高中生.........没有什么区别..............."
    "至少从我化解危机并且转学以后的一个月，我是这么想的。"
    "直到这一天的到来。"
    "这一事件的出现................."
    "时间是2022年10月21日。"
    with vpunch
    "嘭！"
    "本该是我和覃可汐卫生值日的这一天。"
    "覃可汐却......................."
    "再一次........................."
    "倒在了我面前.............................."
    c "啊......啊......"
    c "可汐......"
    c "可汐她......"
    s "大家！不要围观！不要围观！有序回到教室！"
    c "林洛......可汐她......"
    "为什么..........."
    "为什么会这样..........."
    "我不是已经成功了吗............"
    "究竟是哪里出了问题？"
    "我双膝跪地，思考着为什么会变成这样。"
    "是我哪里做错了吗？"
    "我明明执行了近乎完美的计划，改变了这一切才对......那为什么......"
    "我明明已经救了叶梓澄的母亲......切断了叶梓澄父亲与AADR的联系才对.......那为什么......"
    "为什么！！！！"
    "我大声痛哭。"
    "比前几次遇见覃可汐遇害的时候更加痛苦。"
    "因为我做了那么多的努力，最后却失败了。"
    "一败涂地。"
    "林洛..................."
    "反而是叶梓澄过来安慰我。"
    "..........."
    "也不知道过了多久，我坐在教室里，看着旁边空无一人的座位。"
    "这似曾相识的一幕，让我几乎绝望。"
    "还有什么办法可以拯救这一切吗？"
    "不会有了.........."
    "再也没有摊主了，再也没有可以传输记忆的手表了........."
    "虽然不知道是哪个环节出现了问题.............但是毫无疑问地............"
    "被我玩成了死局..................."
    "................................."
    "已经没有可以挽回的地方了..........."
    "覃可汐死去，接下来就会是范围波及整个沁野市的“诅咒”了.........死亡的诅咒........"
    "接着就是扩大范围到全世界的..........诅咒.........."
    "AADR最终依旧会奴役全人类.........."
    "最终仍然会成为既定的事项....."
    "或许这件事从一开始..........就是被注定的命运吧................."
    $ quick_menu = False
    play music "music/end.ogg" fadeout 1.0 fadein 1.0
    call disable_shortcut from _call_disable_shortcut_6
    scene bg_none
    show end3_f
    with fade2
    show endtext:
       xpos 0.3
       ypos 0.7
    with dissolve
    $ renpy.pause(4, hard=True)
    show screen game_end
    with fade2
    $ renpy.pause(189, hard=True)
    $ quick_menu = True
    call enable_shortcut from _call_enable_shortcut_6
    return
    $ persistent.chapter==5
    $ persistent.chapter==6