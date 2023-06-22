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
    $ config.allow_skipping = True
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
    c "六天前，也就是9月13号。"
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
    l "你母亲在9月13号那天，出门的动机是什么？"
    voice v3
    c "那天是星期二，我在上学，所以我也不清楚动机是什么。"
    voice v3
    c "但是平时那个时候的话，应该是不会出门的。"
    voice v3
    c "警察得到的结果，事发时间是下午两点多。"
    voice v3
    c "那个时候太阳也是一天中最热的时候。的确就算是一般的家庭主妇都不会选择出门。"
    l "好了。现在有了一个新的目标了。"
    l "我们现在要了解清楚。"
    l "你母亲，在9月13号下午两点之前，出门的目的是什么？以及为什么要经过巷子。"
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
    scene bg_schoolmae yubi
    with fade2
    $ times = "17:41"
    show screen watch
    with dissolve
    play music kexi fadein 1.0 fadeout 1.0
    "我和叶梓澄约定好了。放学以后来到了校门口见面。"
    "这命运的校门口。"
    play sound run
    $ times = "17:42"
    show zicheng_pose1 mono mouth1 at jin:
        xcenter 0.3
    with dissolve
    c "久等了，林洛！"
    play sound run
    show kexi_pose mono mouth1 at jin:
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
    show kexi_pose2 mono mouth4 at jin:
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
    show zicheng_pose2 mono at jin:
        xcenter 0.3
        yoffset 0
        linear 0.1 xoffset 0 yoffset -50
        linear 0.1 yoffset 0 xzoom 1.1 yzoom 1.1
        linear 0.1 xoffset 0 yoffset -25
        linear 0.1 yoffset 0 xzoom 1.2 yzoom 1.2
    hide kexi_pose2
    show kexi_pose2 mono mouth1 at jin:
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
    show zicheng_pose2 mono at jin:
        xzoom 1.2 yzoom 1.2
        xcenter 0.3
        yoffset 0
        linear 0.1 xoffset 0 yoffset -50
        linear 0.1 yoffset 0 xzoom 1.1 yzoom 1.1
        linear 0.1 xoffset 0 yoffset -25
        linear 0.1 yoffset 0 xzoom 1.0 yzoom 1.0
    hide kexi_pose2
    show kexi_pose2 mono mouth4 at jin:
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
    show kexi_pose2 mono mouth3 at jin:
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
    show zicheng_pose2 mono at jin:
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
    show kexi_pose2 mono mouth4 at jin:
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
    show kexi_pose2 mono mouth4 at jin:
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
    show kexi_pose2 mono mouth4 at jin:
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
    show kexi_pose2 mono mouth1 at jin:
        xcenter 0.6
    with vpunch
    voice v1
    x "我懂了！"
    "覃可汐觉得自己明白了什么，会心一笑。"
    hide kexi_pose2
    show kexi_pose2 mono mouth1 at jin:
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
    show kexi_pose2 mono mouth3 at jin:
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
    show kexi_pose2 mono at jin:
        xcenter 0.6
    with dissolve
    voice v3
    x "是这样吗？好吧！"
    voice v3
    x "我倒是觉得这样写很有趣，不是吗？"
    hide kexi_pose2
    show kexi_pose2 mono mouth4 at jin:
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
    show zicheng_pose2 mono mouth3 other1 at jin:
        xcenter 0.3
    with dissolve
    voice v3
    c "你这话说的！警察也不是笨蛋！首先排查的就是住所。"
    hide kexi2_shadow
    show zicheng2_shadow at jin:
        xcenter 0.3
    hide kexi_pose2
    show kexi_pose2 mono mouth1 at jin:
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
    show zicheng_pose2 mono at jin:
        xcenter 0.3
    with dissolve
    voice v3
    c "不得不穿过巷子的原因吗？"
    hide kexi2_shadow
    show zicheng2_shadow at jin:
        xcenter 0.3
    hide kexi_pose2
    show kexi_pose2 mono at jin:
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
    show kexi_pose2 mono mouth4 at jin:
        xcenter 0.6
        yoffset 0
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset -50
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset 0
    voice v3
    x "没错。"
    hide kexi_pose2
    show kexi_pose2 mono at jin:
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
    show kexi_pose mono eyes4 mouth3 at jin:
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
    show kexi_pose mono mouth1 at jin:
        xcenter 0.6
    with dissolve
    voice v3
    x "那我就先回家了，明天继续吧！？"
    play sound run
    hide zicheng2_shadow
    hide kexi_pose
    with dissolve
    hide zicheng_pose2
    show zicheng_pose1 mono mouth5 at jin
    with dissolve
    hide zicheng_pose2
    show zicheng_pose1 mono eyes7 mouth3 at jin
    with dissolve
    $ times = "18:02"
    "看着覃可汐逐渐走远，叶梓澄长舒了一口气。"
    hide zicheng_pose1
    show zicheng_pose2 mono at jin
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
    show zicheng_pose1 mono eyes4 mouth3 other1 at jin
    with dissolve
    voice v1
    c "林洛......"
    l "嗯？"
    voice v3
    c "虽然我不知道......你穿越时间之前遇到的我......是怎么看你的......"
    hide zicheng_pose1
    show zicheng_pose1 mono eyes2 mouth1 other2 at jin
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
    show zicheng_pose1 mono eyes4 mouth1 other2 at jin
    with dissolve
    voice v3
    c "那.....林洛......一起加油吧~！"
    voice v3
    c "不管是为了你自己，还是为了覃可汐，还是为了.........."
    voice v3
    c "为了........"
    hide zicheng_pose1
    show zicheng_pose1 mono eyes7 mouth5 other2 at jin
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
    $ times = "10:21"
    $ weeks = _("周二")
    scene bg_schoolmae
    with fade
    show screen watch
    with dissolve
    play music richang fadein 1.0 fadeout 1.0
    "天气很晴朗。我跟叶梓澄约好了避开上学高峰期在校门口见面。"
    "总不能在家里集合，跟我爸妈不太好解释为什么没去上学，不如就装成去上学的样子。"
    "但是在上学时间段去学校，万一被老师撞见了就露馅了。"
    $ times = "10:24"
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
    show zicheng_pose2 mono at jin
    with dissolve
    voice v3
    c "我昨天去找了警察要到了更多的资料。"
    voice v3
    c "包括我母亲最后见面的人。"
    voice v3
    c "以及最先发现我母亲遇害的人。"
    $ times = "10:25"
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
    show zicheng_pose2 mono at jin:
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
    hide screen watch
    with dissolve
    scene bg_none
    with fade
    "我跟随叶梓澄，搭上了一辆出租车。"
    "............"
    "............"
    $ times = "11:01"
    play sound car_stop
    show screen watch
    with dissolve
    c "到地方了。"
    l "额？"
    stop sound 
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
    $ times = "11:02"
    "巷子内部昏暗潮湿，两侧墙上的涂刷也掉落了不少，露出了红色的砖体。"
    "并没有看到可以证明这里是案发现场的东西。"
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
    $ times = "11:05"
    "我跟随叶梓澄，慢慢走出了小巷。"
    play music kexi fadein 1.0 fadeout 1.0
    $ times = "11:08"
    scene bg_dingwei_house
    with fade
    "跟着她，来到了一栋房子面前。"
    play sound door
    mono "昸！昸！昸！"
    "门上没有门铃，所以叶梓澄用手敲打着紧闭着的门。"
    show zicheng_pose1 mono mouth1 at jin:
        xcenter 0.7
    with dissolve
    $ times = "11:09"
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
    $ times = "11:11"
    scene bg_dingwei_house_naka
    with dissolve
    play music speak fadein 1.0 fadeout 1.0
    show zicheng_pose1 mono eyes7 mouth3 at jin:
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
    $ persistent.tips87 = True
    d "对.......你母亲经常会趁你和你父亲都不在家的时候，和我约好去打{a=showmenu:tips87}{color=#F18D7D}麻将{/color}{/a}。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    d "出事的那天也是如此。"
    hide zicheng1_shadow
    voice v3
    c "那打麻将的地点是你家吗？"
    show zicheng1_shadow at jin:
        xcenter 0.3
    d "不是，是我家附近的一家麻将馆。"
    hide zicheng1_shadow
    $ times = "11:12"
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
    nvle "论短视频外放的危害。我在心里如此想到。"
    nvl clear
    d "还有什么，你都问吧！我知道的东西都会回答的。"
    d "不过，我有一个请求，希望你们能答应。"
    $ times = "11:13"
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
    $ times = "11:14"
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
    $ times = "11:15"
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
    $ times = "11:17"
    scene bg_dingwei_house
    with dissolve
    play music kexi fadein 1.0 fadeout 1.0
    nvle "我和叶梓澄从丁唯家里以后。叶梓澄和我继续商讨接下来的行动。"
    nvle "临近正午的太阳，依旧刺眼和炎热。"
    nvle "我也叶梓澄坐在一楼的台阶处乘着凉。"
    nvl clear
    nvle "顺便讨论着事项。"
    $ times = "11:18"
    nvl clear
    l "怎么样？这个丁唯，有可能是杀害你母亲的幕后黑手吗？"
    play music speak fadein 1.0 fadeout 1.0
    show zicheng_pose2 mono at jin
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
    show zicheng_pose1 mono eyes7 mouth3 at jin
    with dissolve
    "叶梓澄抬起头，说到。"
    $ times = "11:20"
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
    show zicheng_pose1 mono eyes7 at jin
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
    l "但是案发时间是周二下午啊！"
    l "她是怎么路过学校外面的那个巷子并目击到案发现场的？"
    l "案发现场距离学校，大概也有半个小时的车程吧~"
    hide zicheng_pose1
    show zicheng_pose2 mono at jin:
        yoffset 0
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset -50
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset 0
    voice v3
    c "这就是我们接下来要调查的地方了。"
    l "那现在回学校去吧！？"
    "虽然我内心是很不愿意回去的。"
    $ times = "11:22"
    "但是继续呆在外面也无法获得新的线索了。"
    hide zicheng_pose2
    show zicheng_pose2 mono mouth1 at jin
    with dissolve
    voice v1
    c "林洛！！"
    play music kexi fadein 1.0 fadeout 1.0
    hide zicheng_pose2
    show zicheng_pose1 mono mouth1 at jin
    with dissolve
    voice v3
    c "再聊会天吧~"
    voice v3
    c "现在时间也还够。"
    l "但是......"
    voice v3
    c "说不定能给你提供一些有用的东西呢~"
    l "好吧。"
    nvle "现在不聊，以后可能也没有机会聊了，至少对这个时间的叶梓澄来说。"
    nvl clear
    hide zicheng_pose1
    show zicheng_pose2 mono at jin
    with dissolve
    voice v1
    c "你热吗？"
    l "啊~？有...有点..."
    $ times = "11:23"
    voice v3
    c "那好，等我一会！"
    play sound run
    hide zicheng_pose2
    with dissolve
    "说完叶梓澄便离开了。"
    play sound run
    $ times = "11:28"
    hide screen watch
    show screen watch
    with dissolve
    scene bg_dingwei_house
    with fade2
    "过了好一会，终于回来了。"
    $ persistent.tips88 = True
    "手里还顺便拿着两瓶{a=showmenu:tips88}{color=#F18D7D}苏打水{/color}{/a}。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    show zicheng_pose1 mono mouth1 at jin:
        yoffset 0
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset -50
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset 0
    voice v1
    c "给！"
    $ times = "11:29"
    l "谢谢！"
    "我接过了水，即便我很讨厌喝苏打水这种东西。"
    l "那你要和我聊些什么呢？"
    scene bg_zicheng_suwaru
    with dissolve
    "叶梓澄坐了下来，开始说了。"
    c  "你跟我说过吧~如果放着现在的事态不管，任其继续发展下去的话....."
    c "覃可汐就会因事故而死去....."
    c "覃可汐是我搬家到沁野市来以后认识的第一个朋友....."
    with vpunch
    l "啊？你也是转校生？"
    c "以前是......"
    $ times = "11:30"
    l "以前是.......这是什么意思......?"
    c "在我小学一年级下学期的时候，就跟着我父母一起....搬家来到了沁野市....."
    c "覃可汐...便是我转学到的小学的...认识的第一个同学..."
    c "也是玩的最好的一个......"
    c "我父母也是经常带着覃可汐一块，出去玩~"
    c "毕竟覃可汐家里的条件不太好，她父母没空也没财力带给覃可汐这些..."
    c "我和覃可汐一起，升学到了同一所初中，再又考上了同一所高中......"
    c "可以说.....覃可汐就是我最重要的朋友了.....也是我的青梅竹马....."
    c "比起朋友，更像是我的家人一样......"
    nvle "我总算可以理解一点了......."
    nvl clear
    scene bg_dingwei_house
    with dissolve
    show zicheng_pose1 mono eyes7 mouth3 at jin
    with dissolve
    voice v3
    c "有一个陈年旧事，是关于覃可汐的......"
    l "是什么......？"
    play music sora fadein 1.0 fadeout 1.0
    voice v3
    c "同样是十年前的事情了......"
    voice v3
    c "那是我转学后的第二个学期......"
    voice v3
    c "的一个周末......"
    voice v3
    c "当时我跟着我父母一起，去覃可汐的家里，接覃可汐一起出去玩......"
    voice v3
    c "但是到家的时候得知...覃可汐已经跟着附近的小孩子们一起出去玩水去了..."
    voice v3
    c "也怪我但是只是心血来潮，想给她一个惊喜，没有提前联系。"
    voice v3
    c "就在她家附近的那条河......"
    voice v3
    c "毕竟当时天气炎热..."
    voice v3
    c "然后没过多久，一同前去的小孩就跑回来...说覃可汐溺水了......让大人去救...."
    play sound odoro
    with vpunch
    play music lanzhu fadein 1.0 fadeout 1.0
    l "等等....溺水？"
    $ times = "11:32"
    voice v1
    c "是..."
    play music omou fadein 1.0 fadeout 1.0
    scene bg_mizu
    with fade
    nvle "想起我在那个...第一次目睹覃可汐的死亡的前一天的晚上.....做的那个噩梦...."
    nvl clear
    "这算是巧合....还是？"
    play music speak fadein 1.0 fadeout 1.0
    scene bg_dingwei_house
    with fade
    show zicheng_pose1 mono eyes7 at jin
    with dissolve
    voice v3
    c "是溺水了......但是等我父亲赶忙赶到事发现场的时候....."
    hide zicheng_pose1
    show zicheng_pose1 mono eyes4 mouth1 at jin
    with dissolve
    voice v3
    c "覃可汐却已经被什么人给救了上来......"
    play sound odoro
    with vpunch
    l "被谁？"
    l "当时路过的大人吗？"
    hide zicheng_pose1
    show zicheng_pose1 mono eyes7 mouth3 at jin
    with dissolve
    voice v3
    c "不知道，被救上来的覃可汐躺在河边草丛里，还保留着意识。"
    voice v3
    c "至于是谁救的...以及救人者去了哪......就不得而知了......"
    play music sora fadein 1.0 fadeout 1.0 
    nvle "原来覃可汐还有这种曲折的过去吗？"
    nvl clear
    voice v3
    c "嗯.....但也就是自那以后，覃可汐就像变了一个人..."
    voice v3
    c "从沉默阴暗变成了乐天型人格了......"
    "或许是从大难不死中感受到了生命的宝贵吧......."
    hide zicheng_pose1
    show zicheng_pose1 mono at jin
    with dissolve
    voice v3
    c "抱歉给你讲了这些可能没什么用的东西..."
    l "没什么.....不如说...我还想听更多......"
    play music kexi fadein 1.0 fadeout 1.0
    hide zicheng_pose1
    show zicheng_pose2 mono at jin
    with dissolve
    voice v3
    c "嗯.......有件事还是印象深刻。"
    voice v3
    c "不知道能不能成为线索......."
    l "什么事？"
    play music speak fadein 1.0 fadeout 1.0
    voice v3
    c "那是一年前，放学后的覃可汐和我在回我家的时候，正好遇到了从研究所回来的我父亲。"
    $ times = "11:34"
    hide zicheng_pose2
    show zicheng_pose2 mono eyes2 mouth1 other2 at jin
    with dissolve
    voice v3
    c "我父亲看见覃可汐以后竟然还问我这是谁....明明经常见面的.......父亲却说不认识覃可汐..."
    l "因为工作太忙了....忘记了？"
    voice v3
    c "谁知道呢....但当时覃可汐确实挺失落的.....那天以后就很少来我家玩了...."
    nvle "............."
    hide zicheng_pose2
    show zicheng_pose1 mono mouth1 at jin:
        yoffset 0
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset -50
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset 0
    with dissolve
    play music kexi fadein 1.0 fadeout 1.0
    voice v3
    c "嗯！就这样了！我们该走了吧！"
    "我听得入了迷，不知道什么时候手里的苏打水就喝的见底了。"
    nvle "额！！"
    nvle "可恶！这是因为单线程大脑的原因吗！？"
    nvle "一直专注于听故事而忘掉了我不喜欢喝苏打水这个事情。"
    nvl clear
    hide zicheng_pose1 
    show zicheng_pose1 mono eyes4 mouth1 at jin
    with dissolve
    voice v3
    c "还是感谢你肯听我倾诉！"
    l "说出来了，心里也舒服一点吧..."
    l "放心！我不会让覃可汐的悲剧再次发生的！"
    hide zicheng_pose1
    show zicheng_pose1 mono eyes4 mouth1 at jin:
        yoffset 0
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset -50
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset 0
    voice v1
    c "相信你！"
    $ times = "11:35"
    hide screen watch
    with dissolve
    scene bg_none
    with fade
    "............"
    play sound run
    $ times = "12:05"
    show screen watch
    with dissolve
    scene bg_2_3
    with fade2
    "半小时后，我们回到了学校。"
    $ times = "12:07"
    scene bg_tukue
    with fade2
    play music school fadein 1.0 fadeout 1.0
    "回学校的时候还在上课。所以只能先回到座位上。"
    nvle "可恶！~我本来是打算在校门口或者卫生间里呆到下课以后再回去的！"
    nvle "但是叶梓澄坚持先回座位等到下课！"
    nvle "很不情愿，但还是采取了叶梓澄的方案。顺便还被她嘲笑了。"
    nvl clear
    $ times = "12:00"
    scene bg_school_basketball
    show zicheng_pose1 mono mouth1 at jin
    show noko
    voice v3
    c "啊哈哈！林洛原来你这么怕生啊！"
    voice v3
    c "那怎么跟我这么聊的来！？"
    play sound odoro
    with vpunch
    l "因为对我来说，你是熟人了！"
    voice v3
    c "哈哈哈~"
    $ times = "12:07"
    scene bg_tukue
    with fade
    nvle "一想起来就后怕。"
    nvle "这也是我想在学校外面呆到放学了再去找班主任的原因。"
    nvle "最后还是顶着全班同学对我的目光，慢慢地回到了座位上。"
    nvl clear
    hide screen watch
    with dissolve
    scene bg_none
    with fade
    "......"
    $ times = "12:30"
    show screen watch
    with dissolve
    play sound suzu
    scene bg_tukue
    with fade
    "下课了。"
    stop sound
    play sound run
    hide screen watch
    with dissolve
    scene bg_none
    with fade
    $ times = "12:35"
    show screen watch
    with dissolve
    "在叶梓澄的带领下，来到了班主任的办公室。"
    play sound door
    mono "咚咚咚！"
    c "老师你在吗？"
    play sound opendoor
    s "怎么了班长？有什么事吗？"
    s "哦！你今天请假了是吧！那是来销假的吗？"
    c "嗯！"
    s "进来吧！"
    play sound run
    play music home fadein 1.0 fadeout 1.0
    $ times = "12:37"
    scene bg_jimushitu
    with fade
    show sensei1_pose at jin
    with dissolve
    voice v3
    s "林洛也在啊！那你们......请假去做的是同一个事情？"
    hide sensei1_pose
    show sensei1_pose eyes2 at jin
    with dissolve
    voice v3
    s "算了，别在学校里做就行。在这个表上签字吧。"
    nvle "我觉得班主任肯定误会了什么。"
    nvl clear
    scene bg_none
    with fade
    play sound utusu
    "签完字以后，叶梓澄开口了。"
    stop sound 
    scene bg_jimushitu
    with fade
    show zicheng_pose1 mouth1 at jin:
        xcenter 0.2
    with dissolve
    voice v3
    c "李老师......我有件事情想向您咨询一下。"
    show sensei1_pose at jin:
        xcenter 0.6
    with dissolve
    show zicheng1_shadow at jin:
        xcenter 0.2
    voice v3
    s "是学习上的事情吗？随便问吧，只要是我知道的，都会回答的。"
    hide zicheng1_shadow
    show sensei1_shadow at jin:
        xcenter 0.6
    voice v1
    c "不是......"
    play music speak fadein 1.0 fadeout 1.0
    hide zicheng_pose1
    show zicheng_pose1 mouth3 at jin:
        xcenter 0.2
    with dissolve
    voice v3
    c "我听说......关于我母亲的事情......您是当时的目击者......"
    s "............................."
    hide sensei1_shadow
    show zicheng1_shadow at jin:
        xcenter 0.2
    voice v1
    s "嗯......"
    voice v3
    s "那天下午没有我的课，所以我出门打算采购一点蔬菜......"
    voice v3
    s "因为我家比较特殊，平时如果我下午没有课的话，午饭都是在下午三点多准备。"
    hide zicheng1_shadow
    show sensei1_shadow at jin:
        xcenter 0.6
    voice v3
    c "不是正午准备午饭吗......."
    hide sensei1_shadow
    show zicheng1_shadow at jin:
        xcenter 0.2
    voice v3
    s "对。出事的那个巷子，正好位于我家前往镇上菜市场的路线中间。"
    hide zicheng1_shadow
    show sensei1_shadow at jin:
        xcenter 0.6
    voice v3
    c "买菜是走路去的吗？"
    $ times = "12:39"
    hide sensei1_shadow
    show zicheng1_shadow at jin:
        xcenter 0.2
    voice v3
    s "是啊~因为实际上也就一千米左右的路程，来去就当锻炼身体了。"
    voice v3
    s "然后......就在我路过巷子的时候就听到了奇怪的声音。"
    voice v3
    s "走进巷子里就发现有一个混混在用手掐着你母亲的脖子......"
    hide zicheng1_shadow
    show sensei1_shadow at jin:
        xcenter 0.6
    voice v1
    c "后来呢？"
    hide sensei1_shadow
    show zicheng1_shadow at jin:
        xcenter 0.2
    voice v3
    s "这个混混看我来了，就连忙跑了出去，然后我就报了警了。"
    voice v3
    s "报警的时候我才发现，你母亲已经没了呼吸......"
    "................."
    voice v3
    s "如果那个时候我发现的更早的话.....或许就不会......"
    hide zicheng1_shadow
    show sensei1_shadow at jin:
        xcenter 0.6
    voice v1
    c "是这样吗........."
    voice v3
    c "那你在现场除了看到那个混混以外，还有其他可疑人物吗？"
    hide sensei1_shadow
    show zicheng1_shadow at jin:
        xcenter 0.2
    voice v3
    s "我当时冲进去确实只看到那个混混，没有其他人了......"
    hide zicheng1_shadow
    show sensei1_shadow at jin:
        xcenter 0.6
    voice v3
    c "好的.....我知道了......"
    hide sensei1_shadow
    show zicheng1_shadow at jin:
        xcenter 0.2
    voice v1
    s "嗯。"
    voice v3
    s "叶梓澄...难道你打算自己来调查凶手吗？"
    $ times = "12:41"
    hide zicheng1_shadow
    show sensei1_shadow at jin:
        xcenter 0.6
    hide zicheng_pose1
    show zicheng_pose2 at jin:
        xcenter 0.2
    with dissolve
    voice v3
    c "嗯.....老师，其实我父亲这几天....失踪了..."
    voice v3
    c "我怀疑我父亲的失踪跟我母亲的遇害有关系。所以我......想把我母亲的案子查清楚。"
    hide sensei1_shadow
    show zicheng2_shadow at jin:
        xcenter 0.2
    voice v3
    s "但是你母亲这个事情，难点不是凶手是谁，难点是......凶手在哪......"
    hide zicheng2_shadow
    show sensei1_shadow at jin:
        xcenter 0.6
    voice v3
    c "嗯......我知道的......"
    hide zicheng_pose2
    show zicheng_pose1 mouth1 at jin:
        xcenter 0.2
        yoffset 0
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset -50
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset 0
    with dissolve
    voice v3
    c "那老师......我先回教室了......"
    $ times = "12:42"
    hide sensei1_shadow
    show zicheng1_shadow at jin:
        xcenter 0.2
    voice v7
    s "嗯~一定要控制好自己的情绪啊~我是很能理解你的心情的......我的心情也是很难受的。毕竟前几个月才从芷柚市调到这个学校来，学生就遭遇了这种事......"
    hide zicheng1_shadow
    show sensei1_shadow at jin:
        xcenter 0.6
    voice v3
    c "谢谢老师...."
    play music school fadein 1.0  fadeout 1.0
    hide screen watch
    with dissolve
    scene bg_none
    with fade
    "............"
    "离开办公室以后，叶梓澄把我带到了楼梯间转角。"
    $ times = "12:46"
    show screen watch
    with dissolve
    scene bg_1f_kai
    with fade
    $ persistent.tips89 = True
    nvle "{a=showmenu:tips89}{color=#F18D7D}经典地图{/color}{/a}。额，忍不住在内心里吐槽了。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    nvl clear
    play music speak fadein 1.0 fadeout 1.0
    show zicheng_pose1 eyes4 mouth3 at jin
    with dissolve
    voice v1
    c "林洛......"
    $ times = "12:47"
    l "找到突破口了吗？"
    voice v3
    c "不......事情陷入瓶颈了......"
    voice v3
    c "这样下去的话......或许只有一个办法了。"
    hide zicheng_pose1
    show zicheng_pose1 eyes6 at jin
    with dissolve
    voice v3
    c "林洛...拜托你..."
    play music title fadein 1.0 fadeout 1.0
    voice v3
    c "直接去询问凶手吧！"
    play sound odoro
    with vpunch
    l "额啊！！"
    l "所以我需要......回到你母亲出事的那一天吗？"
    hide zicheng_pose1
    show zicheng_pose2 eyes2 mouth1 other2 at jin
    with dissolve
    voice v3
    c "嗯。揭示真相的话，恐怕只有这一个办法了。"
    $ times = "12:48"
    voice v3
    c "但是有很多风险。"
    l "未来可能会被大幅改变对吧！"
    hide zicheng_pose2
    show zicheng_pose2 at jin
    with dissolve
    voice v3
    c "嗯！如果你阻止了凶手杀害我母亲，未来的我和你可能不会造出时间机器，不会回到你转学那一天把手表给你。"
    voice v3
    c "如果是这种情况的话......再遇到什么情况就完全变的不可挽回了吧！？"
    voice v3
    c "这相当于一场豪赌了。"
    voice v3
    c "如果赌输了，你阻止了凶手，但凶手的幕后雇主又派了其他人来。"
    hide zicheng_pose2
    show zicheng_pose1 at jin
    with dissolve
    play music sora fadein 1.0 fadeout 1.0
    hide zicheng_pose1
    show zicheng_pose1 eyes7 mouth4 at jin
    with dissolve
    voice v3
    c "既然赌赢很难......那就......不赌了吧~"
    l "你.....是什么意思？"
    hide zicheng_pose1
    show zicheng_pose1 eyes2 mouth3 at jin
    with dissolve
    "叶梓澄缓缓流泪，说到。"
    voice v3
    c "我需要你回到过去，在问出凶手的幕后指使者的情况下，尽量最小化地改变未来。"
    voice v3
    c "也就是说......你得在......凶手出巷子以后盘问他，并且问完以后还得放他离开。"
    with vpunch
    l "这.............."
    with vpunch
    l "没有其他办法了吗？"
    $ times = "12:50"
    if persistent.disagree:
       label chapter3_5_1:
            l "你的意思是？不去阻止凶手杀死你母亲？"
            c ".........."
            voice v3
            c "要最小限度地影响未来......不然可能你的手表就不会回来了。"
            voice v3
            c "没事的....你不用考虑我的感受......"
            hide zicheng_pose1
            show zicheng_pose1 eyes2 mouth1 at jin
            with dissolve
            voice v3
            c "我相信你会将这一切......全部的时间轨迹全部抹除重写的......"
            voice v3
            c "所以没事的。"
            jump chapter3_6
    else:
       label chapter3_5_2:
            l "你的意思是......再让我袖手旁观一次吗？"
            l "覃可汐那次......还有你母亲这次......"
            voice v3
            c "这样做都是为了......保留失败后重来的机会......"
            voice v3
            c "我心里比你更不好受.......但是必须冷静。"
            l "好吧。"
            jump chapter3_6
label chapter3_6:
    hide zicheng_pose1
    show zicheng_pose1 eyes2 mouth1 at jin
    with dissolve
    play music title2 fadein 1.0 fadeout 1.0
    voice v3
    c "你做得到吗？"
    l "只能试试了！"
    voice v3
    c "如果你失败了，就跑吧！然后在未来拿到手表以后再次尝试去做！"
    with vpunch
    l "好！"
    nvle "新的重担压到了我的身上。"
    nvle "只不过这次我的任务，是直接找凶手问出直接结果。"
    $ times = "12:51"
    nvle "这个结果将直接影响到后面新的决策。"
    nvl clear
    nvle ".........."
    nvl clear
    voice v3
    c "准备好了吗？"
    voice v3
    c "准备好了那就启动你的这块手表的功能，回到过去吧！"
    $ config.allow_skipping = False
    with vpunch
    l "嗯！"
    $ times = "12:52"
    hide screen watch
    with dissolve
    show screen watch_loop1 nopredict
    with dissolve
    play sound watch loop
    "我记得触发记忆输送的方法是......在手表的表盘上画出这个手势。"
    "所以，我必须将手放到手表的表盘上面......"
    "在回到过去之前......再看看这个时间的叶梓澄最后一眼吧......"
    play music sora fadein 1.0 fadeout 1.0
    scene bg_2_3
    with dissolve
    "回到教室前面，透过窗口看看这个时间的覃可汐最后一眼......"
    l "喂......叶梓澄......你觉得平行宇宙是存在的吗？"
    l "你说会不会，我发送了记忆回过去以后，我依旧站在这个原地，你也依旧在这。"
    l "回到过去执行任务的也就只是过去的那个，不同平行宇宙的那个我而已。这里的我，依旧在这里。"
    show zicheng_pose2 at jin
    with dissolve
    voice v1
    c "谁知道呢......"
    "叶梓澄说道。"
    l "嗯......先启动手表再说吧......"
    "..................."
    "..................."
    $ config.allow_skipping = True
    "..................."
    jump loop1_false
label loop1_true:
    stop music
    stop sound
    hide screen quick_menu_full
    $ quick_menu = False
    call disable_shortcut from _call_disable_shortcut_7
    #play sound "audio/loop.ogg"
    play music loop_bgm
    show screen loop1_screen nopredict
    $ renpy.pause(10, hard=True)
    hide screen loop1_screen
    stop music
    $ quick_menu = True
    call enable_shortcut from _call_enable_shortcut_7
    hide screen watch_loop1
    $ years = "2022.9.19"
    $ weeks = _("周一")
    $ times = "12:40"
    show screen watch
    scene bg_none
    with fade
    play music title2 fadein 1.0 fadeout 1.0
    with vpunch
    l "啊。"
    l "呼~呼~呼~呼~"
    scene bg_schoolmae
    show eye
    $ renpy.pause(2.7, hard=True)
    hide eye
    with dissolve
    nvle "这次的旅行比前几次显得轻松许多。"
    nvl clear
    play music speak fadein 1.0 fadeout 1.0
    voice v3
    t "从你的表情来看，你从未来回来了呢~"
    show linluo_old_pose at jin
    with dissolve
    "我抬起头，看到的正是摊主，应该说是十年后的我才对吧。"
    l "嗯！我回来了！"
    voice v3
    t "调查结果怎么样？"
    l "我了解到了叶梓澄的母亲遇害那一天的事情。"
    l "但是无法判断杀害叶梓澄母亲的凶手背后是否有AADR的力量。"
    l "也就是说，叶梓澄母亲的遇害，可能是AADR夺取时间刻校正仪的开端，也可能不是，还有更早的事件。"
    voice v3
    t "未来的叶梓澄......也是这么认为的。"
    voice v3
    t "倒不如说从一开始我们制造时间机器的直接目的就是为了阻止叶梓澄的母亲被杀害。"
    voice v3
    t "但是后面随着时间推移，我们都逐渐冷静了下来。"
    voice v3
    t "毕竟光有猜测是不够的，尤其是在这场涉及全人类的赌博之中。"
    l "所以你们也怀疑叶梓澄母亲的遇害是开端，但是希望我去亲自验证吗？"
    voice v1
    t "嗯......"
    voice v3
    t "你那边的叶梓澄有跟你说什么吗？"
    voice v3
    t "如果不足以得出结论，但你却又回到了这里。"
    l "总不可能再度过一遍一周的时间吧！？"
    l "班长希望我......回到她母亲被杀害的那一天......"
    voice v3
    t "哦？希望你救下她母亲吗？"
    $ times = "12:42"
    l "希望我在事后询问凶手的杀人动机是什么。"
    voice v3
    t "真不愧是叶梓澄呢~在那种情况下还能得出这种冷静的结论！"
    voice v1
    t "难度呢？"
    l "调查发现凶手是一个街头混混，没有杀人前科，猜测没错的话，凶手做完案以后应该处于很慌乱的状态。"
    l "不然不至于被人目击以后，快速地跑出案发现场。"
    voice v3
    t "所以你需要和跑出案发现场的凶手进行交涉？"
    voice v3
    t "成功概率有多大？"
    l "未知。"
    voice v3
    t "失败以后怎么办？"
    l "拔腿就跑。不排除凶手会对我使用暴力。"
    l "逃跑以后，再次等到今天这个时间点，然后找你获取手表。"
    voice v3
    t "反复尝试吗？"
    l "虽然很繁琐也很危险，但倒不如说这是最安全的一种方法了。对未来干涉最小的方法。"
    nvle "我的内心也很不安稳。"
    nvle "让我盘问一个素未谋面的陌生人，而且对方还是个杀人凶手。"
    nvl clear
    l "手表的传输期限是十五天对吧！"
    voice v1
    t "没错！"
    l "叶梓澄母亲遇害时间是六天前。"
    l "我计划将记忆发送到遇害前几天，这样可以给我更多的时间做准备。"
    l "有物质上的准备，也有思想上的准备。"
    voice v1
    t "嗯！"
    voice v3
    t "你要记住，只要未来没有发生大幅变动，我就会在今天，在这个地方，等待你！"
    voice v3
    t "你如果交涉失败了，就等到今天以后将事情的来龙去脉都告诉我吧！我会相信你说的话的！"
    l "好！反正如果交涉成功了，获取到了有效信息，也依旧必须跟你从头到尾重新讲一遍的不是吗？"
    hide screen watch
    with dissolve
    "摊主接过我的手表，将回溯的时间调整到了十天以前。"
    $ times = "12:44"
    show screen watch
    with dissolve
    play sound odoro
    with vpunch
    voice v1
    t "开始吧！"
    $ config.allow_skipping = False
    "我戴上手表，绘制图案。"
    hide screen watch
    with dissolve
    stop music
    hide screen quick_menu_full
    $ quick_menu = False
    call disable_shortcut from _call_disable_shortcut_8
    #play sound "audio/loop.ogg"
    play sound loop_bgm
    show screen loop2_screen nopredict
    with fade
    $ renpy.pause(23, hard=True)
    hide screen loop2_screen
    $ quick_menu = True
    call enable_shortcut from _call_enable_shortcut_8
    scene bg_none
    with fade
    ".................."
    $ config.allow_skipping = True
    with vpunch
    l "呼！！"
    "我惊醒过来，巡视着周围。"
    scene bg_oldschool
    show eye
    $ renpy.pause(2.7, hard=True)
    hide eye
    with dissolve
    play sound yakamashii loop
    play music home fadein 1.0 fadeout 1.0
    "我正坐在教室内，四周都是喧闹声。"
    "这熟悉又陌生的教室。"
    "我回到了我转学前的学校。"
    nvle "芷柚市蜜溢区高级中学。"
    nvl clear
    scene bg_oldschool_time
    with dissolve
    "看了看讲台上的钟表，现在的时间，是我转学到沁野市的十天前。"
    "也就是："
    "9月9日。"
    "时间则是12点43，这个点还是下课期间。"
    "也是午饭时间。"
    "我却是以午睡的姿势醒来的。"
    "想起来了，那个时候的我，因为晚上熬夜太困了，没吃午饭，一直在睡觉。"
    stop sound
    scene bg_none
    with fade2
    play music title2 fadein 1.0 fadeout 1.0
    nvle "放学后我就直接回到了家。"
    nvle "因为我一直厌恶着这座学校。也不会对这所学校有一丝留念。"
    nvle "为了应对各种可能发生的情况，我看了很多体术相关的教学视频。"
    nvl clear
    nvle "但是很遗憾，学不会，就剩四天时间，也不容易学会。"
    nvle "只好放弃靠武力取胜了。"
    nvle "还好我后面还有充足的几天时间，足够我进行物质上的准备了。"
    nvl clear
    nvle "我提前买好了前往沁野市的火车票。为了避免更大的影响，是我偷偷用零花钱买的，还好刚刚够。"
    nvle "或许直接蛮力接触凶手不太可行。"
    nvle "如果我假设是凶手的同伙，或者是凶手幕后指使人派来的人的话，凶手会相信吗？"
    nvl clear
    nvle "但目前来看这是最容易接触凶手并掏出情报的方法了。"
    nvle "嗯！值得一试！"
    nvl clear
    nvle "就这样计划着，一转眼到了事发的那一天，也就是周一。"
    nvle "我早上假装自己去上学，但实际上我已经向学校请了病假，因为只有半天，所以学校并没有给我父母联系。"
    nvl clear
    scene bg_ressya
    with fade
    nvle "就这样，我一边瞒着学校，一边瞒着父母，坐上了火车。"
    nvle "一路上很紧张，以至于平时坐车的晕眩感都减弱了。"
    nvl clear
    scene bg_eki
    with fade2
    nvle "经历过漫长的煎熬以后，火车终于在沁野站停下来了。"
    nvle "我背着我随身携带的唯一的挎包，里面装着我的手机，以及防狼喷雾，虽然是网购的，但是给我制造逃跑的时间还是足够了。"
    $ persistent.tips92 = True
    nvle "因为时间不够，所以忍受着高价在{a=showmenu:tips92}{color=#F18D7D}京西{/color}{/a}下的单。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     
#词典
    nvl clear
    nvle "虽然贵是贵了，但是送的快，下完单第二天就取到了货。"
    scene bg_eki
    with dissolve
    nvle "手机看了看时间，现在是上午十一点，还来得及。但是仍然不能放松警惕。"
    nvl clear
    scene bg_eki
    nvle "我喊了一辆出租车。"
    nvle "虽然我很不想坐，但是这点代价相较于需要获得的情报来说，简直就是微不足道。"
    nvl clear
    scene bg_none
    with fade
    nvle "车上即便又强烈的晕眩感和想要吐出来的感觉，但我还是忍了。"
    nvl clear
    scene bg_machi2
    with fade2
    nvle "拜托师傅将我送到了那个巷子外面公路的对面位置。"
    nvl clear
    "现在时间是十二点多。"
    "我坐在路边的长椅上，一边假装玩手机一边关注着公路对面的情况。"
    scene bg_machi2
    with fade2
    "不知道过去了多长时间。"
    "反正我额头上的汗珠一滴滴地往地上流，肚子也愈发感到饥饿。"
    play sound odoro
    with vpunch
    "额！"
    nvle "我看着一个穿着风衣，戴着遮阳帽的女人，提着挎包走进了巷子。"
    nvl clear
    with vpunch
    "我立马警惕了起来。"
    "但是我现在还不能行动！"
    nvle "根据已知的情报，凶手是在目击者进巷子以后才慌忙地逃出巷子的。"
    nvle "而恰好，目击证人是我未来的班主任。"
    nvle "所以我需要继续等到我的班主任的出现并走进巷子。"
    nvl clear
    scene bg_machi2
    with fade2
    "焦急地等了大约三分钟，我看着我的班主任提着菜篮子，走过了巷子口。"
    "随之则是意料之中的画面。"
    "班主任朝巷子里看了一眼，随后冲进了巷子。"
    play sound odoro
    with vpunch
    "就是现在！！！"
    play sound run
    show screen suduxian
    with dissolve
    scene bg_machi
    with dissolve
    hide screen suduxian
    with dissolve
    "我赶紧从椅子上站起来，趁着路上车辆不多，穿过公路，蹲守在了巷子旁边。"
    scene bg_machi
    with fade
    "十几秒后，听到了急促的呼吸声与跑步声。我紧张地摸了摸包里的喷雾。"
    nan "呼！呼！"
    with vpunch
    l "来了！！"
    play music lanzhu fadein 1.0 fadeout 1.0
    play sound run
    "看到有人从里面出来了。"
    "在他走出几步之后，我快跑上去，拦在了他面前。"
    show npc2
    with vpunch
    play sound odoro
    with vpunch
    nan "！！！"
    with vpunch
    nan "哪来的小鬼！别挡路！！"
    with vpunch
    l "我是组织的人！"
    "我开口道。"
    nan "什么组织？动画片看上脑了吗？让开！给我让开！"
    nvle "看对方的脾气逐渐暴躁，我有点想退缩了。"
    nvle "但是为了获取情报，我还是坚持站在原地。"
    nvl clear
    l "我是派来监察你工作成果的，派你来的的那个人，派的我！"
    nan "有完没完啊！给我让开！不然等会警察来了！！"
    scene bg_machi
    with vpunch
    play sound run
    "对方双手将我推开，然后继续逃跑。"
    nvle "看他这言行举止，完全不想是受命前来杀人的。"
    nvle "我开始犹豫是继续向前追去，还是看事发现场一眼。"
    nvl clear
    play music sora fadein 1.0 fadeout 1.0
    "还是看看吧！"
    scene bg_machi_mi
    with dissolve
    "我探头看向巷子里。"
    "巷子深处，叶梓澄的母亲倒在地上，旁边我的班主任正在和警察通话。"
    "一切正常！果然还是继续追上凶手问个底吧！"
    play sound odoro
    with vpunch
    play music lanzhu fadein 1.0 fadeout 1.0   
    "啊？"
    play sound odoro
    with vpunch
    "这是........."
    nvle "我正打算离开的时候，我看见班主任从叶梓澄母亲的衣兜里，摸出了一部手机。"
    nvle "在打开手机，看了几分钟以后，揣进了自己的兜里。"
    nvl clear
    "这.................."
    nvle "从凶手的话语，以及班主任的态度来看。"
    nvle "我未来的班主任.......难道就是......"
    nvl clear
    "我内心受到极大震撼。"
    nvle "在和叶梓澄调查的时候，调查了这么多，却从来没有怀疑过班主任........"
    nvle "或许这是班主任对我们的温柔，导致了我们下意识地认为其不会做这样的事情吧......"
    nvle "但很明显，我们错了。"
    nvl clear
    nvle "班主任......从她的所作所为来看，毫无疑问，她就是一切的开端！"
    nvle "............."
    nvl clear
    play sound run
    scene bg_none
    with fade
    nvle "我连忙离开案发现场，趁着班主任没察觉到我之前。"
    nvle "但是这个时候我突然意识到了一件事情。"
    nvle "监控探头毫无疑问已经拍到了我。"
    nvl clear
    "拍到了拦截凶手的我。"
    "希望对未来不会造成什么影响。"
    play music home fadein 1.0 fadeout 1.0
    scene bg_ressya
    with fade2
    "坐着返程的火车，我终于冷静了下来。"
    "开始思考今天的发生的这一切。"
    nvle "叶梓澄说过，她母亲出事以后身上手机已经不见了。"
    nvle "我找凶手谈话的时候，对方也一副完全不搭理我的话的样子。"
    nvle "好像完全不理解我在说什么一样。"
    nvl clear
    nvle "虽然我自己也完全不理解我在说什么。"
    nvle "所以......叶梓澄母亲的手机....其实是被目击者，也就是班主任......"
    nvl clear
    with vpunch
    "拿走了！！"
    "如果班主任跟AADR有联系的话，一切都说得清楚了................"
    "物理老师...事件目击者...拿走了现场的手机..."
    nvle "而且我还想起了上课的时候,班主任在物理课上确实有提到过AADR这个组织......"
    nvl clear
    "真相逐渐浮出水面了。"
    nvle "班主任是AADR有关的人，在其偶然目睹叶梓澄母亲被杀以后，报警的过程中偶然发现了叶梓澄母亲的手机。"
    nvle "在翻阅手机内内容以后，发现了叶梓澄父亲的研究项目是AADR一致梦寐以求的东西。"
    nvle "最后导致了AADR的人进入叶梓澄父亲的研究所，绑架了叶梓澄父亲并搜刮了研究资料和科学仪器。"
    nvl clear
    nvle "{size=100}解——————————{/size}"
    nvl clear
    "我在心中如此想到。"
    play music title2 fadein 1.0 fadeout 1.0
    "我必须将这件事告知给十年后的我，以及未来的叶梓澄。"
    "以便进一步商量对策，以及————"
    "特别提防我未来的班主任！！"
    play music home fadein 1.0 fadeout 1.0
    scene bg_none
    with fade2
    nvle "我回家之后确实挨了一顿骂，但这都是小事。"
    nvle "几天后警察确实找到了我询问情况。"
    nvle "不过他车上没有空调就是了。"
    nvl clear
    nvle "问我和犯罪嫌疑人的关系，我只是说碰巧路过，觉得可疑所以把拦下来了。"
    nvle "估计是因为查到我和凶手在之前没有任何交集，所以警察相信了我说的话。虽然确实没有任何交集就是的了。"
    nvle "还表扬了一下我。"
    nvl clear
    nvle "........"
    nvl clear
    "在时间的流逝和我这几天的坐立不安中，那一天到来了。"
    play sound "audio/car_stop.ogg"
    car "{color=#C1394F}尊敬的旅客您好！沁野市高级中学站到了！请各位旅客有序下车！谢谢！{/color}"
    play music richang fadein 1.0 fadeout 1.0
    scene bg_schoolmae
    with fade
    play sound run
    "我一下车，就主动走向了那个摊位。"
    stop sound
    with vpunch
    l "呼~呼~太好了~"
    l "还在~这里~"
    nvle "这说明我并没有对时间的走向做出过多的干涉，太好了。"
    nvl clear
    play sound run
    with vpunch
    "我刚走到他身前，手臂就被抓住了。"
    play music lanzhu fadein 1.0 fadeout 1.0
    show linluo_old_pose other1 at jin
    with dissolve
    voice v3
    t "这块手表送你了。戴上吧。"
    with vpunch
    l "来自未来的我！"
    with vpunch
    l "终于等到你了！"
    with vpunch
    l "啊？你没有被我的话吓到吗？"
    hide linluo_old_pose
    show linluo_old_pose  at jin
    with dissolve
    voice v3
    t "我可是未来的你！你经历过的事情，就是我经历过的事情！"
    l "也对。"
    play music title2 fadein 1.0 fadeout 1.0
    voice v3
    t "步入正题吧！未来的人类的灾难，AADR组织对人类的奴役..."
    voice v3
    t "这一切的源头就是："
    voice v3
    t "班主任偶遇了杀人事件，而恰好班主任是AADR相关人员，拿到了叶梓澄母亲手机里的研究资料，所以引起了未来的质变。"
    l "那现在该如何去做，也有了一个确定的方向了！"
    voice v3
    t "我和叶梓澄这十年来的努力......终于要..........."
    t "............."
    voice v3
    t "那，下一个任务，也或许也是最终任务，就交给你了！"
    voice v3
    t "任务目标：回到事发当天，并救下叶梓澄的母亲！从而阻止跟AADR有关系的，你转学班上的班主任，拿到叶梓澄父亲的研究资料！！"
    nvle "终于到了这个时候了！啊！看到了吗？来自未来的叶梓澄！来自未来的，覃可汐！"
    nvle "我马上就要做到了！"
    nvle "做到改变时间的走向了！"
    nvl clear
    nvle "做到改变人类的未来了！"
    nvl clear
    "我的手已经激动的发抖了。"
    "但我还是尽量深呼吸让自己冷静下来。"
    "呼~马上就能终结我这不断回溯的命运了，在黑暗中我看到了光芒。"
    "只要阻止凶手作案，就可以直接影响到整个人类的未来，这就是蝴蝶效应的魅力所在啊~！"
    l "但是我........"
    l "我要不还是找叶梓澄先讨论一下吧！~"
    voice v3
    t "你最好还是不要这样做......"
    voice v3
    t "你的班主任或许也发现了你出现在监控里，出现在案发现场的事情！"
    voice v3
    t "当你进学校，当她看到你的脸的时候，可能未来又会被大幅改变！"
    voice v3
    t "毕竟她是AADR的人！"
    l "也对........"
    l "但是？"
    l "你作为未来的的我，能现在能在这里，不就说明了班主任不会对我做什么吗？"
    l "或者说班主任不会怀疑到我头上来。"
    voice v3
    t "时间的方向可是不断在变动的。"
    voice v3
    t "过去的我不会被发觉，但是现在的你不一样了，你见到了经历过过去的现在的我。"
    l "果然还是担心蝴蝶效应吗？"
    with vpunch
    voice v1
    t "对。"
    nvle "叶梓澄.......覃可汐.......等事情结束之后.....再一起去漫展吧~"
    nvle "这也是推动我不断前进的动力。"
    nvl clear
    voice v3
    t "你有信心去完成吗？"
    l "凶手的作案工具只有双手，所以我计划用钝器击晕凶手，然后直接报案。"
    l "目的则是：赶在班主任之前，让我成为目击者，不，成为阻止行凶者！"
    voice v3
    t "那，你想回到哪个时间点？"
    l "十天前吧！我上次就是回到的十天之前。"
    l "已经走过的路，再走起来总会熟悉一点。"
    play sound odoro
    with vpunch
    voice v1
    t "好！"
    $ years = "2022.9.19"
    $ weeks = _("周一")
    $ times = "12:32"
    show screen watch
    with dissolve
    "摊主调试了一会手表以后，递给了我。"
    l "那！我开始了！"
    l "让这不幸的宿命，让这轮回的命运————"
    l "皆终结于此地吧！"
    $ config.allow_skipping = False
    "我熟练地在手表上绘制了手势。"
    jump chapter4
   