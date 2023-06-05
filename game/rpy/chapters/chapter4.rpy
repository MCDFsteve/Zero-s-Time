label chapter4:
    stop music
    stop sound
    hide screen watch
    with dissolve
    hide screen quick_menu_full
    $ quick_menu = False
    call disable_shortcut from _call_disable_shortcut_9
    play sound loop_bgm
    show screen loop3_screen nopredict
    with fade
    $ renpy.pause(10, hard=True)
    hide screen loop3_screen
    stop music
    scene bg_none
    with fade
    call disable_shortcut from _call_disable_shortcut_5
    $ persistent.chapter4 = True
    $ persistent.chapter==4
    $ persistent.extra_chapter4 = True
    $ persistent.achievement_chapte3 = True
    image chapter4 ="chapters/chapter4.webp"
    scene bg_none
    $ quick_menu_full_= False
    hide screen quick_menu_full
    show chapter4
    with fade2
    $ renpy.pause(10, hard=True)
    hide chapter4
    with fade2
    scene bg_none
    $ quick_menu = True
    $ quick_menu_full_= True
    call enable_shortcut from _call_enable_shortcut_5
    $ save_name = "{font=Huayuan.Gothic.Bold.ttf}章节四：博弈棋盘的翻转{/font}"
    "....................."
    with vpunch
    l "呼！"
    scene bg_oldschool
    show eye
    $ renpy.pause(2.7, hard=True)
    hide eye
    with dissolve
    play sound yakamashii loop
    play music home fadein 1.0 fadeout 1.0
    "又回来了，久违的，我转校前的高中。"
    "耳边传来久违的喧嚣。"
    nvle "我不会对这个学校有什么留恋。"
    nvle "反正没有值得我留恋的东西。"
    nvle "没有朋友，没有知心的人，只有应试。这种学校我才不想呆下去。"
    nvl clear
    nvle "倒不如说整天除了上课，考试就没有其他活动了。"
    nvle "整所学校只充斥着升学的氛围，完全没有一丝社交的空闲。"
    nvle "在这种学校，学习和升学的压力压得我抬不起头，所以早点离开算了。"
    nvl clear
    scene bg_none
    with fade2
    play music title2 fadein 1.0 fadeout 1.0
    "..................."
    "煎熬地熬过了放学时间。"
    "我现在要全力准备。"
    "准备迎接三天后的，改变世界的那个事件！"
    nvle "我去了附近的集市，想寻找看看有什么趁手的兵器。"
    nvle "趁手的适合制止凶手行凶的兵器。"
    nvle "有没有球棍什么的啊~在这秋蝉鸣泣之时！"
    nvl clear
    nvle "算了，这玩意不好带上火车吧！"
    nvle "当然我没有带过的经验，所以并不清楚能不能带。"
    nvle "或许我可以转变一下思路，阻止事件发生的话，我让叶梓澄的母亲不要往巷子里走不就可以了吗？"
    nvl clear
    nvle "感觉变数太大了，而且有种治标不治本的感觉。"
    nvle "还是制止凶手行凶比较安全与稳定一些。"
    nvle "当然我指的安全并不是我的人身安全。"
    nvl clear
    nvle "虽然还有另一种方法，从目击者身上下手....."
    nvl clear
    play sound odoro
    with vpunch
    "我在想什么？这种做法连想都不要想！太恶劣了！"
    nvle "只需要阻止叶梓澄母亲被杀就行了，如果对凶手的反击过重的话可能就把我自己给搭进去了。"
    nvle "可不想进橘子喝茶。"
    nvle "但是又得让凶手丧失行动能力，以免被反扑。"
    nvl clear
    "嗯.........."
    with vpunch
    "有了！"
    nvle "根据凶手的作风，只要被别人目击了，就会畏罪潜逃，毕竟本质上就是一个混混而已。"
    nvle "新的计划有了。"
    nvle "依旧在京西发货了防狼喷雾，当然绝大多情况下我是不会去用它的。"
    nvl clear
    nvle "仅仅是用作，在所有计划都失败以后留的后路。"
    nvl clear
    scene bg_none
    with fade2
    "我照着我上次的经验，打好了假条，买好了车票。"
    "虽然我跟家长写了检讨，也担保了绝不再犯。"
    "但是担保的是过去的我，这段历史已经被现在的我给抹除了。"
    scene bg_none
    with fade2
    "在不断的准备与等待中，这一天又来到了。"
    "熟练地假装去学校上学，实际上却乘地铁到了火车站。"
    "乘坐着跟上次一样车次的列车，前往和上次一样的目的地。"
    "跟上次一样的时刻出发。"
    scene bg_ressya
    with fade2
    "由于没吃早餐的关系，空腹的我并没有感觉到有太晕的感觉。"
    nvle "一个伟大的科学定律被发现。"
    nvl clear
    "我心中想着。"
    "我紧紧抱着我的挎包，里面装着重要的物品。"
    scene bg_eki
    with fade2
    "漫长的车程以后，终于到站了。"
    scene bg_none
    with fade
    "出站后找到了上次那位出租车师傅。"
    play sound odoro
    with vpunch
    l "师傅，去这里！"
    nvle "我将手机导航软件的界面递给他看。"
    nvl clear
    play sound odoro
    with vpunch
    di "欧了！"
    "........."
    scene bg_machi2
    with fade2
    nvle "又经过了一段车程以后，我回到了小巷的正前方。"
    nvl clear
    with vpunch
    "呕~我收回我之前说的话。"
    nvle "好晕好想吐。"
    nvle "感觉喉咙里卡了长袜子。"
    nvle "虽然如果是白袜的话也不是不可以。"
    nvl clear
    nvle "我坐上了命运的长椅，开始审视着公路对面，小巷前方的这一切。"
    nvle "现在的时间是十二点多。"
    nvle "我目不转睛地盯着对面的情况。"
    nvl clear
    scene bg_machi2
    with fade2
    play music lanzhu fadein 1.0 fadeout 1.0
    play sound odoro
    with vpunch
    "来了！"
    play sound run
    "叶梓澄的母亲，也就是一个穿着风衣，带着遮阳帽的女人，提着包走进了巷子。"
    play sound run
    show screen suduxian
    with dissolve
    scene bg_machi
    with vpunch
    hide screen suduxian
    with dissolve
    "我不顾红绿灯，穿过了巷子，紧随其后进了小巷。"
    nvle "于是，我目击到了："
    nvl clear
    play music ruins fadein 1.0 fadeout 1.0
    scene bg_machi_mi
    with dissolve
    cm "那个...这位大哥，可以让一让吗？我需要到巷子对面去！"
    play sound odoro
    with vpunch
    hh "啊~？让路？"
    play sound odoro
    with vpunch
    hh "这条路是你修的吗？"
    play sound odoro
    with vpunch
    hh "既然不是，那老子凭什么给你让路！"
    hh "你想过去......过去好啊！留下买路财！"
    cm "那对不起打扰了..."
    nvle "叶梓澄母亲想转头离开巷子，被对方一手抓住。"
    nvl clear
    play sound odoro
    with vpunch
    hh "嗯？想走？"
    play music lanzhu fadein 1.0 fadeout 1.0
    play sound odoro
    with vpunch
    cm "你....你想干什么？"
    hh "想干什么？老子打牌输了钱，现在心情很不好！"
    hh "今天你不给我钱就别想活着离开！"
    cm "今天真倒霉，算是碰到臭流氓了！"
    play sound odoro
    with vpunch
    hh "啊？！你再说一遍？"
    with vpunch
    cm "闪开！本来想给你点面子的！"
    cm "你如果不放我走，那我报警了！"
    nvle "叶梓澄母亲打算伸手掏手机。"
    nvl clear
    play sound odoro
    with vpunch
    hh "你敢！！！"
    nvle "却被对方用手勒住脖子。"
    play sound phone_ochiru
    nvle "手机也从手上滑落，坠在地上发出了清脆的响声。"
    nvl clear
    with vpunch
    hh "老子最恨的就是你们这群有钱人了！"
    with vpunch
    hh "凭什么你们什么都不做就有这么多钱，老子累死累活干几十年到最后还是混的个人财两空！"
    with vpunch
    cm "我跟你...不一样...."
    nvle "叶梓澄母亲一边挣扎一边说道。"
    nvl clear
    hh "有什么不一样！！！"
    nvle "对方发怒了。"
    nvl clear
    scene bg_none
    with fade
    nvle ".........."
    nvl clear
    play sound tatakai
    play sound odoro
    with vpunch
    hh "啊！！"
    play sound odoro
    with vpunch
    hh "好痛！！！"
    play sound odoro
    with vpunch
    hh "谁打我！！！"
    play music title2 fadein 1.0 fadeout 1.0
    scene bg_linluo_tatakai
    with fade2
    "正是我。"
    nvle "在外面等待的时候我也没闲着，在垃圾桶翻了几个玻璃瓶，在路边捡了几块干水泥块，塞进了我的挎包里。"
    nvle "这就足够了。"
    nvl clear
    play sound odoro
    with vpunch
    hh "你是哪里来的小屁孩？？给老子滚开！！"
    with vpunch
    l "我要报警了！"
    nvle "我掏出手机，对对方面不改色地说道。"
    nvle "虽然在别人看来是面不改色，但我内心已经紧张的不得了了。"
    nvl clear
    with vpunch
    hh "你找死吗？"
    hh "你......你不许报警！！"
    "对方打算朝我扑过来。"
    scene bg_none
    with fade
    play sound odoro
    with vpunch
    nan "住手！！！！"
    nvle "来了！"
    nvle "班主任的声音！"
    nvl clear
    hh "可恶......今天就先放过你们！！！"
    nvle "小混混说罢，扭头狼狈地逃出了巷子。"
    nvl clear
    nvle "成.....成功了......."
    nvle "我的作战计划..............."
    nvl clear
    scene bg_machi_ge
    with fade
    cm "谢......谢谢......"
    s "你们还好吗？这里发生了什么？"
    nvle "真是千钧一发啊~"
    nvle "幸好我算准了班主任会目击的时间。"
    nvle "成功拯救了叶梓澄的母亲。"
    nvl clear
    nvle "这就意味着......AADR不会获得关于叶梓澄父亲的研究资料..."
    nvle "也意味着，未来AADR不会依靠时间刻校正仪来统治世界...意味着覃可汐不会因此死去......"
    nvl clear
    scene bg_linluo_naku
    with dissolve
    nvle "一想到这，我不禁热泪盈眶。"
    nvl clear
    with vpunch
    play music sora fadein 1.0 fadeout 1.0
    "看到了吗？十年后的我！看到了吗？十年后的叶梓澄，还有未来的叶梓澄。"
    "我成功了。"
    "但是它们不会看到了。"
    "我在这里终结了AADR的统治，也意味着未来的我和叶梓澄不会再发明时间机器回到这个时代了..."
    "这样倒也好......我会记住你们所做出的努力的......我会永远记住的！"
    scene bg_none
    with fade2
    nvle "..............."
    nvl clear
    nvle "....................."
    nvl clear
    nvle "........."
    nvl clear
    nvle "一转眼，又到了我转学的这一天。"
    nvl clear
    stop music
    play sound "audio/car_stop.ogg"
    car "{color=#C1394F}尊敬的旅客您好！沁野市高级中学站到了！请各位旅客有序下车！谢谢！{/color}"
    stop sound
    play sound run
    scene bg_schoolmae
    with fade2
    play music omou fadein 1.0 fadeout 1.0 
    "一下车，我就赶忙朝着摊主的位置走去。"
    "但是..............."
    "没有了。原本会有一个坐着轮椅戴着帽子的人在这里，但是现在，"
    "没有了。"
    nvle "以后也不会再有了。"
    nvl clear
    play music sora fadein 1.0 fadeout 1.0
    "这对他来说，也是一种解脱吧。"
    nvle "对未来的我来说。"
    nvle "不需要心力憔悴制造时间机器回到这个时代，而是幸福地在未来度过。"
    nvle "我希望是如此。"
    nvl clear
    play sound run
    scene bg_school_basketball
    with dissolve
    "我这样想着，踏步进了校园。"
    play music school fadein 1.0 fadeout 1.0
    scene bg_2_3
    with dissolve
    "因为没有被摊主挽留，所以这次我进学校的时候，大家还在上课。"
    nvle "额......"
    nvle "我又不自觉地发抖了。"
    play music sora fadein 1.0 fadeout 1.0 
    nvle "怎么会........"
    nvl clear
    nvle "为什么.........."
    nvle "经历过这么多次磨练的我，怎么能连顶着班上同学注视的目光走进教室这件事都办不到......."
    nvle "嗯！我必须坚持克服下去！！"
    nvl clear
    play music school fadein 1.0 fadeout 1.0
    play sound suzu
    scene bg_none
    with fade
    nvle "............"
    nvl clear
    play sound yakamashii
    nvle "随着下课铃声响起，整个教学楼也变得喧闹。"
    nvle "我也终于可以从洗手间里出来了。"
    nvl clear
    "对不起.....我还是.....做不到......."
    "未来的我加油吧！现在的我依旧做不到！"
    stop sound 
    nvle "就这样.................全新的，和平的校园生活.......开始了。"
    nvle "............."
    nvl clear
    stop sound
    scene bg_zicheng_tukue
    with fade
    show zicheng_pose1 mouth1 at jin
    with dissolve
    voice v3
    c "啊~是转校生啊。你叫林洛是吧。请多关照。"
    voice v3
    c "怎么了.........有什么事情需要帮忙吗？"
    voice v3
    c "怎么了............."
    hide zicheng_pose1
    show zicheng_pose1 mouth5 eyes7 other2 at jin
    with vpunch
    play sound odoro
    with vpunch
    c "啊！？"
    play music sora fadein 1.0 fadeout 1.0
    voice v3
    c "林洛.........你为什么.........为什么..........在哭啊？"
    l "我.................."
    l "班长你好.......以后的高中时光.......请多关照......."
    scene bg_none
    with fade
    nvle "...................."
    nvle "............................."
    nvl clear
    play music kexi fadein 1.0 fadeout 1.0
    scene bg_kinoshita
    with fade2
    show kexi_pose mono at jin
    with dissolve
    voice v1
    x "林洛！"
    voice v3
    x "那个...我就长话短说了。你，，，或者你的亲属。以前是否来过沁野市。"
    l "或许有过吧.........."
    l "或许我们之前确实.........见过面呢......."
    hide kexi_pose
    show kexi_pose mouth1 mono at jin
    with dissolve
    voice v3
    x "是吗...........如果是的话..........谢谢了................"
    hide kexi_pose
    show kexi_pose2 mono at jin
    with vpunch
    play sound odoro
    with vpunch
    play music sora fadein 1.0 fadeout 1.0
    voice v3
    x "林洛.......你怎么哭了？"
    l "是吗？我怎么又哭了........"
    l "你跟我道谢.........的理由是什么呢？"
    hide kexi_pose2 
    show kexi_pose2 mouth1 mono at jin
    with dissolve
    voice v3
    x "谢谢你救了我！"
    play music title fadein 1.0 fadeout 1.0 
    with vpunch
    l "！！！！！！！！！！！！"
    l "是关于什么？"
    hide kexi_pose2
    show kexi_pose eyes4 at jin
    with dissolve
    voice v3
    x "我也不清楚了.......记不清是梦境还是现实了........那个......总之谢谢你......."
    hide kexi_pose
    show kexi_pose2 mouth1 at jin
    with dissolve
    voice v3
    x "如果我弄错了的话...抱歉..........."
    play music kexi fadein 1.0 fadeout 1.0
    scene bg_none
    with fade
    nvle "................."
    nvl clear
    nvle "......................"
    nvl clear
    play music speak fadeout 1.0 fadeout 1.0
    nvle "我依旧结识了班上的朋友，包括叶梓澄和覃可汐..................."
    nvle "但是她们在被抹除的时间内所做的事情.......就不告诉她们了......."
    nvle "也没必要告诉她们了............"
    nvl clear
    play sound suzu
    scene bg_tukue
    with fade2
    play music school fadein 1.0 fadeout 1.0
    "星期三到了，叶梓澄并没有被班主任喊出去。"
    scene bg_zicheng_tukue
    with dissolve
    show zicheng_pose1 mouth5 eyes7 at jin
    with vpunch
    play sound odoro
    with vpunch
    voice v3
    c "啊？林洛你怎么突然提起这个...........这........不好透露吧.....毕竟是个人隐私...."
    l "所以不方便说吗......好吧......"
    hide zicheng_pose1
    show zicheng_pose1 mouth1 eyes4 at jin
    with dissolve
    voice v3
    c "总之我父母都生活的很好啦~"
    l "那就好~"
    voice v3
    c "这我还得感谢你！"
    l "啊？难道......."
    voice v5
    c "我妈跟我谈起，上个星期的时候我妈碰到了一个混混，后来还是一个高中生和我的班主任出来见义勇为，度过了难关。"
    voice v3
    c "我妈当时拍了照片，我一看.....这不就是你嘛......林洛！"
    nvle "这个时间上的叶梓澄，也变得爱笑了，再也不是那副悲伤的面庞了。"
    nvl clear
    hide zicheng_pose1
    show zicheng_pose2 at jin
    with dissolve
    play music speak fadein 1.0 fadeout 1.0
    voice v3
    c "但是你是.....这个星期才转学过来的....."
    voice v3
    c "所以我脑中还是存在一个疑问..."
    play sound odoro
    with vpunch
    l "来沁野市旅游的时候刚好路过而已......"
    voice v3
    c "是这样吗.......那还是谢谢了......"
    voice v3
    c "但是....."
    hide zicheng_pose2
    show zicheng_pose2 other2 at jin:
      yoffset 0
      linear 0.05 xoffset 0 yoffset -25
      linear 0.05 xoffset 0 yoffset -50
      linear 0.05 xoffset 0 yoffset -25
      linear 0.05 xoffset 0 yoffset 0
    with dissolve
    play sound odoro
    with vpunch
    play music lanzhu fadein 1.0 fadeout 1.0
    voice v1
    c "驳倒！！！"
    voice v3
    c "我妈拍下照片的时间是星期一，这个日期你应该还在学校上课才对！怎么可能出来旅游？"
    with vpunch
    "！！！！我被叶梓澄的追根问底惊到了。"
    hide zicheng_pose2
    show zicheng_pose1 eyes7 mouth1 at jin
    with dissolve
    play music school fadein 1.0 fadeout 1.0
    voice v3
    c "额......开个玩笑.....别见怪......"
    voice v3
    c "只是想模仿一下苗花诚......"
    l "但是还没到学级裁判呢！！"
    with vpunch
    voice v3
    c "啊哈哈哈哈哈哈哈......."
    nvle "我们都不约而同地笑了起来。"
    nvl clear
    scene bg_none
    with fade
    nvle "真好啊~这样的校园生活~"
    nvl clear
    scene bg_tukue
    with fade2
    "星期五到了，覃可汐也一切正常。终于！"
    with vpunch
    play music kexi fadein 1.0 fadeout 1.0
    x "林洛！"
    l "怎么了？"
    l "都快放学了，还有什么要说的吗"
    scene bg_tukue2
    with dissolve
    show kexi_pose2 mouth4 at jin
    with dissolve
    voice v3
    x "明天的漫展别忘记咯！"
    l "怎么会呢！我明天肯定来！"
    voice v3
    x "说好咯！？"
    voice v3
    x "你不需要准备什么服装就可以的！"
    hide kexi_pose2
    show kexi_pose mouth1 at jin
    with dissolve
    voice v3
    x "然后......游戏机明天就还你！目前我也只差四大天王了！！"
    l "那二周目不打了吗？"
    hide kexi_pose
    show kexi_pose eyes3 mouth3 at jin:
      yoffset 0
      linear 0.05 xoffset 0 yoffset -25
      linear 0.05 xoffset 0 yoffset -50
      linear 0.05 xoffset 0 yoffset -25
      linear 0.05 xoffset 0 yoffset 0
    with vpunch
    play sound odoro
    with vpunch
    voice v3
    x "啊？二周目是什么？"
    voice v3
    hide kexi_pose
    show kexi_pose eyes4 mouth3 at jin:
      yoffset 0
      linear 0.05 xoffset 1 yoffset -1
      linear 0.05 xoffset -1 yoffset 1
      linear 0.05 xoffset -1 yoffset -1
      linear 0.05 xoffset 1 yoffset 1
      linear 0.05 xoffset 0 yoffset 0
      repeat
    voice v3
    x "这游戏不是成为联盟冠军就算通关了吗？"
    l "不是啊！成为联盟冠军之后还有一堆剧情呢！"
    hide kexi_pose
    show kexi_pose2 at jin:
      yoffset 0
      linear 0.05 xoffset 0 yoffset -25
      linear 0.05 xoffset 0 yoffset -50
      linear 0.05 xoffset 0 yoffset -25
      linear 0.05 xoffset 0 yoffset 0
    with vpunch
    voice v1 
    x "额.........."
    nvle "覃可汐陷入了思考。"
    play music sora fadein 1.0 fadeout 1.0
    nvle "看着覃可汐健康地活着，内心也是说不出的感觉。"
    nvle "即便再次回想起我之前所做的一切，也依旧有点后怕。"
    nvl clear
    play music title2 fadein 1.0 fadeout 1.0
    "幸好一切都成功了！"
    "我！让覃可汐的未来发生了改变。"
    "让没有未来的人，拥有了未来！"
    "这并不是什么励志演讲词，而是货真价实的事情。"
    "这来之不易的和平，则更加值得我去珍惜。"
    "这来之不易的校园生活，以及好不容易第一次获得的————"
    "朋友的感觉。"
    scene bg_tukue2
    with fade2
    show kexi_pose2 at jin
    with dissolve
    play music school fadein 1.0 fadeout 1.0 
    nvle "几分钟后，覃可汐回过神来。"
    nvle "看来是思考完毕了。"
    nvl clear
    hide kexi_pose2
    show kexi_pose mouth1 at jin
    with dissolve
    voice v3
    x "那......要不......再让我多玩几天？"
    l "当然可以！"
    nvle "意料之中的发展。"
    nvl clear
    hide kexi_pose
    show kexi_pose2 mouth1 at jin:
      yoffset 0
      linear 0.05 xoffset 0 yoffset -25
      linear 0.05 xoffset 0 yoffset -50
      linear 0.05 xoffset 0 yoffset -25
      linear 0.05 xoffset 0 yoffset 0
    with vpunch
    with vpunch
    voice v3
    x "真的太感谢了！！"
    voice v3
    x "早知道这么好玩，我暑假就不整天出去玩了。"
    voice v3
    x "就算搬两个月的砖也得买一部游戏机的！"
    l "这倒不至于。"
    hide kexi_pose2
    show kexi_pose eyes3 at jin
    with dissolve
    voice v3
    x "现在只能等寒假了。"
    l "所以你已经提前规划好了压岁钱的用途了吗？"
    hide kexi_pose
    show kexi_pose2 mouth1 at jin
    with vpunch
    play sound odoro
    with vpunch
    voice v1
    x "那当然~"
    "对我来说倒是规划了也没用。"
    "对很少出门的我来说，即便是过年走亲戚，也不会走多少家。"
    "也自然不会拿到多少压岁钱，目前的个人纪录是300块就是了。"
    l "你每年可以拿多少压岁钱？"
    "在拿压岁钱这方面，我算是没见过世面的了，所以问问见识广的也算正常，也算合理。"
    voice v3
    x "大概三四千吧！"
    l "也对，毕竟你这么可爱....."
    play sound odoro
    with vpunch
    l "额！！！！"
    l "你就当什么都没听到！"
    hide kexi_pose2
    show kexi_pose2 mouth4 at jin
    with dissolve
    voice v1
    x "啊嘞嘞~~"
    hide kexi_pose2
    show kexi_pose2 mouth3 at jin
    with dissolve
    voice v3
    x "这可不行！虽然我确实很可爱。"
    voice v3
    x "但是从你口中说出来，就很奇怪呢~"
    l "哪里.....奇怪了......"
    "不小心说错了话，我突然不知所措了。"
    "我应该怎么做。"
    scene bg_none
    with vpunch
    "放弃了，只能像做错事的孩子一样羞愧地把头埋在课桌里。"
    with vpunch
    x "啊！？你不会生气了？"
    x "那好吧！我不会跟任何人说的！"
    x "我只是开个玩笑而已~"
    "问题不在这里，我只是大脑处理器遇到了无法计算的，缺少相应板块的事件。"
    scene bg_none
    with fade2
    "不知过了多久，感觉风头已经过去了，我试探性地抬头。"
    scene bg_tukue2
    with dissolve
    play sound odoro
    with vpunch
    x "你好啦？"
    l "唔嗯！！？"
    show kexi_pose2 mouth3 at jin
    with dissolve
    play music lanzhu fadein 1.0 fadeout 1.0
    play sound odoro
    with vpunch
    "覃可汐一直在看着我吗？一直在等着我抬头？"
    voice v3
    x "你也挺可爱呢~"
    scene bg_kexi_egao
    with dissolve
    x "お可愛い子供~"
    with vpunch
    "！！！大脑服务器遭到了未见过的攻击，紧急宕机！！！"
    scene bg_none
    with fade
    "只得赶紧再将头埋进课桌。"
    x "哟~你脸红了！"
    play sound odoro
    with vpunch
    l "不要再说了......."
    "我恳求道。"
    play music school fadein 1.0 fadeout 1.0
    play sound suzu
    scene bg_tukue
    with fade2
    "终于放学了。"
    "因为覃可汐的关系，我到现在还没缓过神来。"
    play sound ruins
    scene bg_zicheng_tukue
    with dissolve
    "已经没法正眼看着覃可汐了，只能灰溜溜地出教室。"
    x "林洛你不会真的生气了吧？"
    with vpunch
    "！我的手被谁抓住了。"
    "不用想，肯定是覃可汐。"
    l "我.......我才没有生气........真的......"
    show kexi_pose2 mono at jin
    with dissolve
    "我回过头，盯着覃可汐的脖子看。"
    "至于为什么看脖子........"
    "我羞于直视覃可汐的正脸，但是又不敢看脖子以下的部位......"
    l "明天的漫展........我会去的........"
    l "但是我现在有点事.........先走了........"
    play sound run
    scene bg_none
    with fade
    nvle "..........."
    nvl clear
    play music kexi fadein 1.0 fadeout 1.0
    scene bg_schoolmae kumori
    with fade2
    "呼~呼~终于逃出来了！"
    "这种情况感觉比我之前所经历过的困难还要棘手！"
    "但是既然我已经答应了，明天还是早起一点吧！"
    play music home fadein 1.0 fadeout 1.0
    scene bg_none
    with fade2
    nvle "........"
    nvle "找了一套还算体面的衣服。"
    nvle "就这样吧。"
    nvl clear
    nvle "为了避免父母的追问，我直接说是参加学校要求的社会实践去了。"
    nvle "不会告诉他们我今天打算去漫展。"
    nvle "毕竟要是寻根问底起来，就有够麻烦的。"
    nvl clear
    nvle "感觉自己已经真正的习惯这和平的生活了。"
    nvle "仿佛那次事件从未发生过一样。"
    nvle "确实从未发生过，对目前的情况而言。"
    nvl clear
    nvle "就这样吧。不去想这些了。我已经很满足了。"
    nvl clear
    scene bg_kuruma_matu
    with fade2
    play music richang  fadein 1.0 fadeout 1.0
    play sound ame loop
    show screen ame
    with dissolve
    "完全忘记了今天是注定会下雨的......"
    "是我的错。"
    "那估计只能都在室内了。" 
    hide screen ame
    with dissolve
    scene bg_none
    with fade
    "我熟练地搭乘车辆，前往覃可汐的家。"
    "毕竟........之前有来过......."
    "还是不去想这些事了。已经过去了。"
    scene bg_none
    with fade2
    play sound car_stop
    nvle ".................."
    nvl clear
    play sound ame loop
    show screen ame
    with dissolve
    scene bg_kexihome
    with dissolve
    "终于到了。我今天也是特地没有吃任何东西。"
    "晕车的状况确实有一点好转。"
    stop sound
    play sound ame loop
    "说实话路上我也快无聊死了。"
    "坐车的时候只要我看手机，就会加重晕车的情况。"
    "这是我长年累月总结出来的经验。"
    "就只能戴着耳机看着窗外听歌而已。"
    with vpunch
    x "林洛！"
    "覃可汐在屋内呼喊着我。"
    play music home fadein 1.0 fadeout 1.0
    play sound run
    hide screen ame
    with dissolve
    scene bg_kexihome_naka
    with dissolve
    play sound ame loop volume 0.5
    "我循着声音，走进了屋内，顺便收起了雨伞。"
    show kexi_pose2 mouth4 at jin
    with dissolve
    voice v3
    x "来的挺早的嘛！居然没有迷路哈哈~"
    play sound odoro
    with vpunch
    voice v1
    x "等会！"
    x "......"
    voice v3
    x "班长还在房子里试衣服呢~"
    voice v3
    x "所以你现在还不能进我的卧室。"
    scene bg_kexi_mimi
    with dissolve
    "覃可汐突然把脸贴近到我耳边，轻声说道："
    x "{size=35}当然如果你想看的话，也可以进去。{/size}"
    with vpunch
    "！这种玩笑还是不要开的好。"
    "简直是恶魔的低语。"
    scene bg_kexihome_naka
    with dissolve
    show kexi_pose2 mouth1 at jin
    with dissolve
    voice v3
    x "哈哈~开玩笑开玩笑！"
    voice v3
    x "不过谅你也不可能做得出来....."
    hide kexi_pose2
    show kexi_pose2 mouth4 at jin
    with dissolve
    voice v1
    x "毕竟是.."
    "可恶....被小看了....."
    l "你说什么我没听到？"
    hide kexi_pose2
    show kexi_pose2 mouth4 at jin:
      yoffset 0
      linear 0.05 xoffset 0 yoffset -25
      linear 0.05 xoffset 0 yoffset -50
      linear 0.05 xoffset 0 yoffset -25
      linear 0.05 xoffset 0 yoffset 0
    with vpunch
    voice v3
    x "啊什么都没说！"
    "回应的很彻底。"
    "算了，不深究这些了。"
    scene bg_kexihome_naka
    with fade2
    nvle "等了好一会，叶梓澄出来了。"
    nvl clear
    show zicheng_cospose at jin:
      xcenter 0.3
    with dissolve
    voice v3
    c "有劳久等了，我们走吧！"
    "有点失望...呸！才没有！"
    show kexi_pose2 mouth4 at jin:
      xcenter 0.6
    with dissolve
    voice v3
    x "啊嘞嘞~林洛你好像很受打击的样子呢！"
    voice v3
    x "我都说过啦！只是试穿而已！不会穿着这个去坐车哦！"
    play sound odoro
    with vpunch
    voice v1
    c "可汐！！！"
    voice v3
    x "好啦好啦！走吧！"
    scene bg_none
    with fade2
    play music richang fadein 1.0 fadeout 1.0
    play sound ame loop
    nvle "我们撑伞前往最近的车站，搭乘了前往漫展场地的公交车。"
    nvl clear
    scene bg_anime
    with fade2
    play music home fadein 1.0 fadeout 1.0
    stop sound
    "过了很久，终于到了。"
    "说实话我表面上显得沉着冷静，实际上我已经慌得不行了。"
    "因为这是我第一次来漫展。"
    "此前一直是呆在家，没有朋友，自然也没人邀请我去漫展。"
    show zicheng_pose1 mouth1 mono at jin:
      xcenter 0.3
    with dissolve
    show kexi_pose mouth1 mono at jin:
      xcenter 0.6
    with dissolve
    show zicheng1_shadow at jin:
      xcenter 0.3
    voice v3
    x "林洛！我们去换衣服！你在这里等一会！"
    l "哦...好..."
    nvle "什么都不熟悉的我只能被覃可汐她们领着走。"
    nvle "好羞耻啊......我可以回去吗....."
    nvle "早知道就拒绝的......"
    nvl clear
    play music title2 fadein 1.0 fadeout 1.0
    with vpunch
    "不！"
    with vpunch
    "绝对不能拒绝！"
    with vpunch
    "好不容易才拥有现在的生活。"
    "我必须去学会拥抱它，适应它，毕竟不会再回到那段痛苦的时光了。"
    scene bg_anime
    with fade2
    play music home fadein 1.0  fadeout 1.0
    "等了一会，覃可汐和叶梓澄换完了衣服。"
    show kexi_cospose at jin:
      xcenter 0.6
    with dissolve
    show zicheng_cospose at jin:
      xcenter 0.3
    with dissolve
    "覃可汐穿的是恨蜜莉雅的cos服，精致的简直像娃娃一样。"
    nvle "真的太可爱了......但是这种思想仅限于脑海中。"
    nvl clear
    "至于叶梓澄的这身cos服，则是二雷娜的，不能说是还原，只能说是就是本人。"
    scene bg_anime
    with fade2
    show kexi_cospose at jin:
      xcenter 0.6
    with dissolve
    show zicheng_cospose at jin:
      xcenter 0.3
    with dissolve
    nvle "............."
    hide kexi_cospose
    show kexi_cospose at jin:
      xcenter 0.6
      yoffset 0
      linear 0.05 xoffset 0 yoffset -25
      linear 0.05 xoffset 0 yoffset -50
      linear 0.05 xoffset 0 yoffset -25
      linear 0.05 xoffset 0 yoffset 0
    with vpunch
    play sound odoro
    with vpunch
    voice v1
    x "林洛！！"
    voice v3
    x "来都来了，我们拍个照呗！？"
    play music sora fadein 1.0 fadeout 1.0
    l "我？"
    l "我....和你们.....吗？"
    voice v1
    x "唔姆！"
    l "可以......."
    nvle "我内心此时有一股说不出的复杂。"
    nvl clear
    l "谢谢！"
    scene bg_none
    with fade
    play music home fadein 1.0 fadeout 1.0 
    nvle "我拿着覃可汐的手机，给她们拍了张合影。"
    play sound kamera
    nvl clear
    x "林洛你也拍一张吧！"
    l "原来还包括我吗？"
    nvle "心中感到一丝安慰。"
    nvl clear
    nvle "覃可汐拿出了她的自拍杆。"
    nvl clear
    x "3~2~1~"
    play sound kamera
    show bg_zenbu_syashin
    with zoomin
    with vpunch
    x "茄子！！"
    play music sora fadein 1.0 fadeout 1.0
    nvle "我，还是第一次在毕业照以外的地方和其他人合照。"
    nvle "对她们来说，这或许是再熟悉不过的场面了吧~"
    nvl clear
    scene bg_anime
    with fade2
    show kexi_cospose at jin:
      xcenter 0.6
    with dissolve
    show zicheng_cospose at jin:
      xcenter 0.3
    with dissolve
    show zicheng_cos_shadow at jin:
      xcenter 0.3
    voice v1
    x "林洛！"
    voice v3
    x "我把照片发给你！"
    l "好........."
    play music kexi fadein 1.0 fadeout 1.0
    scene bg_none
    with fade
    nvle ".............."
    nvle "...................."
    nvl clear
    nvle "漫展终于结束了，覃可汐和叶梓澄换完衣服以后，我们乘车在回家的路上。"
    play sound ame loop
    nvl clear
    x "今天玩的怎么样？"
    with vpunch
    l "很开心！！"
    x "是吧~！我就说嘛......你肯定会喜欢上的！！"
    nvle "虽然很累人，但是我确实感到了从来没有体会过的快乐。"
    nvle "或许这就是苦尽甘来的感觉吧！~"
    nvl clear
    c "话说可汐......你又买这么多周边......"
    c "你家里还放得下吗？"
    x "嗯................"
    with vpunch
    x "没关系的！我卧室虽然贴不下了，但我可以贴我妈卧室里！！"
    play sound odoro
    with vpunch
    c "晕~你要给你父母传教吗？"
    play sound ame loop
    x "嗯............有在考虑！"
    nvle "不愧是覃可汐！"
    nvl clear
    l "但是我还是搞不懂，为什么你一个动漫的周边要买三袋。"
    c "难道是？"
    x "没错！就是！"
    nvle "覃可汐期待着看着叶梓澄。"
    nvl clear
    l "就是？是什么？"
    nvle "我也看向叶梓澄。"
    nvl clear
    c "一份收藏，一份自用，一份传教！"
    x "还是梓澄了解我！"
    nvle "满头雾水。"
    nvl clear
    play sound odoro
    with vpunch
    x "这是倒霉星里面的名台词啊！！林洛你入宅看来还不够深啊！"
    play sound ame loop
    nvle "被叶梓澄批评了。"
    nvl clear
    play sound odoro
    with vpunch
    l "对不起.........马上回去看！！"
    play sound ame loop
    x "你说的哦！下周一我要找你提问的！！"
    x "答不上来的话......哼哼........."
    l "答不上来的话........会怎样？"
    play sound odoro
    with vpunch
    x "把你游戏存档里的材料全部卖掉！！"
    play sound ame loop
    l "啊！！可恶！绝对不能这样干！！"
    l "虽然我有amido，可以再刷回来。"
    l "但是刷够这么多的材料还是要花很多时间的！"
    play sound odoro
    with vpunch
    l "不要！！"
    play sound ame loop
    x "这可由不得你........毕竟人质....不是..机质在我手里！！"
    play sound odoro
    with vpunch
    l "这下不看不行了！"
    play sound ame loop
    l "我的游戏机.....我会为了你....努力去做的....."
    play sound odoro
    with vpunch
    c "怎么突然燃起来了？"
    play sound ame loop
    scene bg_none
    with fade2
    nvle ".................."
    nvl clear
    play music home fadein 1.0 fadeout 1.0
    stop sound
    nvle "有说有笑地坐车回到了家。"
    nvle "久违的充实，与久违的.......日常........."
    nvle "在这般满足中.........我进入了梦乡............."
    nvl clear
    scene bg_none
    with fade2
    play music title fadein 1.0 fadeout 1.0
    nvle "...................."
    nvl clear
    nvle "已经习惯了很久了......."
    nvle "没有手表的生活..........."
    nvle "没有意外发生的生活.........."
    nvl clear
    nvle "一切都很正常..........一切都像普通的生活一样正常......."
    nvle "我也和普通的高中生.........没有什么区别..............."
    nvle "至少从我化解危机并且转学以后的一个月，我是这么想的。"
    nvl clear
    nvle "直到这一天的到来。"
    nvle "这一事件的出现................."
    nvle "{b}{size=50}{cps=5}时间是2022年10月21日。{/cps}{/size}{/b}"
    nvl clear
    scene bg_none
    with fade
    play sound "audio/hasai.ogg"
    play music omou fadein 1.0 fadeout 1.0
    with vpunch
    nan "嘭！"
    nvle "本该是我和覃可汐卫生值日的这一天。"
    nvle "覃可汐却......................."
    nvl clear
    nvle "再一次........................."
    nvl clear
    scene bg_kexi_shiru at shake:
        zoom 1.1
    nvle "倒在了我面前.............................."
    nvl clear
    with vpunch
    c "啊......啊......"
    c "可汐......"
    c "可汐她......"
    with vpunch
    s "大家！不要围观！不要围观！有序回到教室！"
    c "林洛......可汐她......"
    nvle "为什么..........."
    nvle "为什么会这样..........."
    nvle "我不是已经成功了吗............"
    nvl clear
    nvle "究竟是哪里出了问题？"
    nvl clear
    play sound odoro
    scene bg_none
    with vpunch
    nvle "我双膝跪地，思考着为什么会变成这样。"
    nvl clear
    play music sora fadein 1.0 fadeout 1.0 
    with vpunch
    l "是我哪里做错了吗？"
    "我明明执行了近乎完美的计划，改变了这一切才对......那为什么......"
    "我明明已经救了叶梓澄的母亲......切断了叶梓澄父亲与AADR的联系才对.......那为什么......"
    with vpunch
    l "为什么！！！！"
    nvle "我失声痛哭。"
    nvl clear
    nvle "比前几次的时候更加痛苦。"
    nvle "因为我做了那么多的努力，最后却失败了。"
    nvle "一败涂地。"
    nvl clear
    scene bg_zicheng_te
    with fade
    c "林洛..................."
    nvle "反而是叶梓澄过来安慰我。"
    nvl clear
    scene bg_none
    with fade2
    nvle "..........."
    nvl clear
    scene bg_tukue
    with fade2
    nvle "也不知道过了多久，我坐在教室里，看着旁边空无一人的座位。"
    nvle "这似曾相识的一幕，让我几乎绝望。"
    nvle "还有什么办法可以拯救这一切吗？"
    nvl clear
    nvle "不会有了.........."
    nvl clear
    play music omou fadein 1.0 fadeout 1.0
    nvle "再也没有摊主了，再也没有可以传输记忆的手表了........."
    nvle "虽然不知道是哪个环节出现了问题.............但是毫无疑问地............"
    nvle "被我玩成了死局..................."
    nvl clear
    nvle "................................."
    nvl clear
    nvle "已经没有可以挽回的地方了..........."
    nvle "覃可汐死去，接下来就会是范围波及整个沁野市的“诅咒”了.........死亡的诅咒........"
    nvle "接着就是扩大范围到全世界的..........诅咒.........."
    nvl clear
    play music sora fadein 1.0 fadeout 1.0  
    nvle "AADR最终依旧会奴役全人类.........."
    nvle "最终仍然会成为既定的事项....."
    nvle "或许这件事从一开始..........就是被注定的命运吧................."
    nvl clear 
    nvle "已经放弃任何抵抗了，我只能侥幸地过好剩下的时间了..........."
    nvl clear
    scene bg_schoolmae yubi
    with fade2
    nvle "我这样想着................慢慢走出了校门....................."
    $ end = 0
    hide screen quick_menu_full
    $ quick_menu = False
    $ quick_menu_full_= False
    play music "music/end.ogg" fadeout 1.0 fadein 1.0
    call disable_shortcut from _call_disable_shortcut_6
    scene bg_none
    show nise_end
    with fade2
    show endtext:
       xpos 0.25
       ypos 0.7
    with dissolve
    $ renpy.pause(4, hard=True)
    show screen game_end
    with fade2
    $ renpy.pause(90, hard=True)
    $ quick_menu = True
    $ quick_menu_full_= True
    call enable_shortcut from _call_enable_shortcut_6
    play sound odoro
    with vpunch
    nan "你是林洛对吧！"
    l "你是？"
    nan "叶梓澄！来自十年后的，叶梓澄！"
    with vpunch
    l "！！！！！！！！！！"
    stop music
    scene bg_schoolmae yubi
    with fade2
    hide screen game_end
    with dissolve
    "！！！！"
    return
    $ persistent.chapter==5
    $ persistent.chapter==6