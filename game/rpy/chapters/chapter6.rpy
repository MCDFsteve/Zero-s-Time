label chapter6:
    hide screen quick_menu_full
    call disable_shortcut from _call_disable_shortcut_11
    $ persistent.chapter6 = True
    $ persistent.chapter=6
    $ persistent.extra_chapter6 = True
    $ persistent.achievement_chapter5 = True
    image chapter6 ="chapters/chapter6.webp"
    scene bg_none
    $ quick_menu = False
    show chapter6
    with fade2
    $ renpy.pause(5, hard=False)
    hide chapter6
    with fade2
    scene bg_none
    $ quick_menu = True
    call enable_shortcut from _call_enable_shortcut_10
    $ save_name = "{font=Huayuan.Gothic.Bold.ttf}章节六：衔尾蛇缠的终末{/font}"
    "我抱着全身的决心，猛烈地按下了回车。"
    play sound enter
    $ config.allow_skipping = True
    "随着我手指按到回车键上，舱内开始震动。"
    play sound shindou loop fadein 1.0 fadeout 1.0
    with vpunch
    mono "隆.....隆...隆.....隆....."
    "这是一种很闷的响声，伴随着轻微的震动。"
    play music title2 fadein 1.0 fadeout 1.0
    "跟之前的三人行不一样的是，这次只有我一个人了。来自未来的叶梓澄和我都不存在于这个世界上了。"
    "或者说，是现在还未存在，在即将到来的十年后，才开始存在。"
    play sound odoro
    with vpunch
    "虽然他们不存在了，但是留下的时间机器还在这里！"
    "而我！将用着这时间机器来完成最关键的，也是真正的，最后的任务。"
    "之前说了太多次最后的任务，但这次确是，真真正正的最后的任务。"
    "虽然任务完成以后....我便会被困在十年前......"
    nvle "被囚禁在十年前的世界......"
    nvl clear
    play sound odoro
    with vpunch
    "但是无所谓了！"
    play music omou fadein 1.0 fadeout 1.0
    "震动越来越强烈，也感觉到自己的意识越来越被剥离。"
    "视野越来越模糊，自己的呼吸声越来越弱。"
    nvle "一种奇妙的......濒死感。"
    nvle "仿佛看到自己的手在逐渐被溶解，变成黑白色的片状粒子。"
    nvle "发着微弱的，梦幻的光芒。"
    nvl clear
    play music sora fadein 1.0 fadeout 1.0
    l "啊....真是美丽啊....."
    l "我自身的躯体.....原来也可以如此美丽......"
    "这样想着,我安详地“睡着”了。"
    stop sound fadeout 1.0
    nvle "..............."
    nvl clear
    nvle "....................."
    nvl clear
    nvle "..............."
    nvl clear
    nvle "在睡梦中,又回想起了我最开始所接触到的那个梦境。"
    scene bg_kawa at shake
    with fade2
    play sound kawa loop fadein 1.0 fadeout 1.0
    nvle "我站在河岸边。"
    nvle "覃可汐在河中，大声呼救着。"
    nvle "湍急的河流不断吞噬着覃可汐的身体。但她依旧挣扎着。"
    nvl clear
    with vpunch
    x "救我！"
    x "林......洛................."
    nvle "........................"
    nvl clear
    with vpunch
    nvle "我会救你的！！！"
    with vpunch
    nvle "这是我对你的约定！！！"
    nvl clear
    stop sound fadeout 1.0
    scene bg_none
    with fade2
    nvle "..................."
    nvl clear
    nvle "......................"
    nvl clear
    play music home fadein 1.0 fadeout 1.0
    "没人叫醒我了......我也不清楚是什么时候苏醒过来的......"
    scene bg_taimumashin_linluo
    show eye
    $ renpy.pause(2.7, hard=True)
    hide eye
    with dissolve
    "我在迷迷糊糊中,睁开了双眼。"
    "仪表盘上显示着：目标地点已到达。"
    "到了？"
    "我颤颤巍巍站起身，按下了舱门的开关。"
    play sound shindou
    scene white
    with dissolve
    "一阵缓缓的响声中，舱门缓缓打开。"
    stop sound fadeout 1.0
    "刺眼的阳光，闪的我头晕目眩。"
    scene bg_sora
    with dissolve
    "缓缓地睁开双眼，看向这晴朗的天空。"
    play music sora fadein 1.0 fadeout 1.0
    "这就是来自十年前的天空..........."
    with vpunch
    "来自..........2012年的天空！！"
    $ persistent.tips118 = True
    nvle "还记得当年还有人传，{a=showmenu:tips118}{color=#F18D7D}2012年是世界末日{/color}{/a}。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    nvle "现在看来也并没说错什么。"
    nvle "世界末日的开端？"
    nvl clear
    nvle "................"
    nvl clear
    "覃可汐会在明天溺水。"
    "所以今天我计划先办其他事情。"
    play music kexi fadein 1.0 fadeout 1.0
    scene bg_taimumashin
    with dissolve
    "我走出了时间机器，依旧是熟悉的树林。"
    play sound yabu loop fadein 1.0 fadeout 1.0
    scene bg_none
    with fade
    "穿过沙沙响的树丛，来到了熟悉的研究所门口。"
    stop sound
    scene bg_kennkyuujya hare
    with fade2
    "与十年后的区别便是，看起来明显新了许多，就像刚修建起来的一样。"
    "不对，这就是刚修建起来的。"
    scene bg_kennkyuujya hare:
        xzoom 1.0  yzoom 1.0
        linear 1.0 xcenter 0.65 ycenter 0.11 xzoom 1.9 yzoom 1.9
    with dissolve
    "我想回到自己家一样，习惯性地走近，手熟地敲着门。"
    play sound door
    with vpunch
    mono "咚咚咚！！！"
    play sound door
    with vpunch
    mono "咚咚咚！！！"
    stop sound
    play sound odoro
    with vpunch
    cb "啊？谁？"
    play sound opendoor
    "见过的叶梓澄父亲开门最快的一次。"
    stop sound
    scene bg_kennkyuujya hare
    with dissolve
    show zicheng_chichi
    with dissolve
    voice v1
    cb "你是？"
    "叶梓澄父亲看起来简直就像年轻了十岁一样。"
    "又忍不住说废话了。"
    l "我可以进去说吗？"
    voice v3
    cb "嗯......进来吧.....是哪个高中过来社会实践的？"
    play music home fadein 1.0 fadeout 1.0
    scene bg_none
    with fade2
    nvle "............."
    nvle "...................."
    nvle "......................"
    nvl clear
    scene bg_kennkyuujya_naka2
    with fade2
    show zicheng_chichi
    with dissolve
    play sound odoro
    with vpunch
    voice v3
    cb "什么.............这.........这..............."
    nvle "我将我所经历的的一切，都告诉给了叶梓澄的父亲。"
    nvle "2012年的叶梓澄父亲。"
    nvl clear
    play music speak fadein 1.0 fadeout 1.0
    voice v3
    cb "但是我现在正在写这篇论文。"
    voice v3
    cb "你的的意思是，我这篇论文会导致未来有一个叫AADR的组织出现，其在更远的未来会统治全人类？"
    l "就是这样。"
    voice v3
    cb "既然你是从未来过来的......你的时间机器在哪里？不然我根本难以信服......尤其是让我撕掉我费尽心血的论文......"
    l "在这个研究所附近的树林里。"
    play music kexi fadein 1.0 fadeout 1.0
    scene bg_none
    with fade2
    nvle "..........."
    nvl clear
    nvle ".............."
    nvl clear
    scene bg_taimumashin
    with fade
    show zicheng_chichi
    with dissolve
    play sound odoro
    with vpunch
    voice v1
    cb "这？"
    hide zicheng_chichi
    nvle "到达了时间机器所在地以后，叶梓澄父亲仔细观察和接触了很久。"
    nvl clear
    play music speak fadein 1.0 fadeout 1.0
    show zicheng_chichi
    with dissolve
    voice v3
    cb "真是不敢相信.......我所研究的东西.....可以在未来做出这种东西！！"
    voice v3
    cb "看来你说的似乎是真的。"
    "什么叫似乎....我都已经看了这么多东西了。"
    play music kexi fadein 1.0 fadeout 1.0
    "突然想起来了一个重要东西。"
    play sound run_kai
    scene bg_none
    with fade
    "我走进时间机器，在里面取出了一本笔记本。"
    stop sound
    "没错，就是叶梓澄父亲研究时间刻校正仪的本子。"
    scene bg_taimumashin
    with fade
    show zicheng_chichi
    with dissolve
    show note:
      xcenter 0.2
      ycenter 0.3
    with dissolve
    "我把笔记本递给他看。"
    cbnvl "............"
    nvl clear
    hide note
    play music speak fadein 1.0 fadeout 1.0
    play sound odoro
    with vpunch
    voice v1
    cb "啊！！"
    play sound odoro
    with vpunch
    voice v3
    cb "这确实是我的笔迹！"
    voice v3
    cb "既然是未来的我希望这样做的......那我还有什么不做的理由呢？"
    voice v3
    cb "零子的研究还能继续对吧.....但是这篇论文绝对不能发表。"
    voice v3
    cb "放心吧！我会照做的。"
    play music home fadein 1.0 fadeout 1.0
    scene bg_none
    with fade
    nvle "..................."
    nvl clear
    nvle "最关键的影响世界走向的任务反而完成的很轻松。"
    nvle "接下来就是对世界无足轻重，但是对我非常重要的任务了。"
    nvl clear
    play music kexi fadein 1.0 fadeout 1.0
    scene bg_none
    with fade
    "我根据记忆中的路线，走到了这个时间点的覃可汐的家附近。"
    "现在还是星期五下午三点多，覃可汐应该还在上学。"
    "我所了解到的覃可汐的出事时间是明天上午，也就是星期六的上午。"
    "邻居家的小孩会叫上她一起去河边玩耍。"
    "所以我得阻止玩耍这一既定事实的达成。"
    scene bg_kexihome
    with fade
    "我假装等人，在家附近的公路旁边坐着查看情况。"
    "又或者说，我确实是在等人。"
    "不知道如果把话说清楚以后，覃可汐的母亲会相信我说的话吗？"
    nvle "........."
    "覃可汐母亲出门了。应该是去接覃可汐放学。"
    l "等......等等........."
    play music sora fadein 1.0 fadeout 1.0
    l "................"
    play sound odoro
    with vpunch
    l "等等！"
    play sound odoro
    with vpunch
    l "等一下！阿姨！"
    play sound odoro
    with vpunch
    m "嗯？"
    "覃可汐母亲被我叫住了。"
    show kexihaha_pose at jin
    with dissolve
    voice v1
    m "你是？"
    l "这几天天比较热，要注意别让小孩去河边玩啊........"
    voice v1
    m "哦..........."
    nvle "就这样吧......我希望能起效。"
    nvl clear
    play music home fadein 1.0 fadeout 1.0
    scene bg_none
    with fade2
    nvle "..................."
    nvl clear
    scene bg_taimumashin_linluo
    with fade2
    "到了晚上，我回到了时间机器。"
    "打算先睡到明天早上，然后去查看情况。"
    "看看我的告诫是否起效了。"
    nvle "................."
    nvl clear
    with vpunch
    "这是？本来想看看有什么显示时间的东西。"
    "舱内的一个柜子里，放着一块手表。"
    show watch_miru:
      xcenter 0.2
      ycenter 0.3
    with dissolve
    "一块熟悉，又许久未见的手表。"
    "我就像看到了老朋友一样。"
    hide watch_miru
    with dissolve
    "戴上手表，显示了现在的时间。"
    $ years = "2012.9.14"
    $ times = "22:19"
    $ weeks = _("周五")
    show screen watch
    with dissolve
    "记得很久以前，因为实在是过了太久太久的时间了。"
    "未来的那个我说过，手表显示的是绝对时间。"
    "所以现在的年份是2012年。"
    "如果救人失败，或许可以用手表设置一个还原点。"
    "但是我不清楚如何设置。"
    nvle "........."
    nvl clear
    play music home fadein 1.0 fadeout 1.0
    scene bg_taimumashin_linluo
    with fade
    nvle "我尝试在仪表盘上询问AI。"
    nvl clear
    ai "您需要了解的是关于记忆溯流功能还是记忆备份恢复功能？"
    ai "记忆溯流功能是可以通过拷贝与大脑记忆相同数据的零子，经由时间机器的功能发送到过去的时间点......."
    ai "记忆备份恢复功能是可以通过拷贝与大脑记忆相同数据的零子，并设置为自动或手动将记忆发送回大脑，不用经过时间机器的功能......."
    nvle ".................."
    nvl clear
    "原来把记忆发送回过去......还有这么一个官方名称......."
    "至于记忆备份恢复功能.....或许......事情都结束以后......有用得上的地方......"
    nvle "......................"
    nvl clear
    play sound yowa loop fadein 1.0 fadeout 1.0
    hide screen watch
    scene bg_none
    with fade
    nvle "在伴随着舱外微弱的夜晚蟋蟀声中，我进入了梦乡。"
    nvl clear
    nvle "................."
    nvl clear
    stop sound
    nvle "........................"
    nvl clear
    scene bg_taimumashin_linluo
    with fade2
    play sound odoro
    with vpunch
    l "呼！！！！！！！！！！！！！！！"
    "不知道是什么时候睡着的。"
    "抬起手看着手表的时间。"
    $ years = "2012.9.15"
    $ times = "10:13"
    $ weeks = _("周六")
    show screen watch
    with dissolve
    play music lanzhu fadein 1.0 fadeout 1.0
    play sound odoro
    with vpunch
    "糟糕！！！十点多了！！"
    "距离覃可汐预定的出事时间只有不到一个小时。"
    "顾不得干其他事情了！！"
    hide screen watch
    with dissolve
    scene white
    with dissolve
    show screen suduxian
    with dissolve
    play sound run loop fadein 1.0 fadeout 1.0
    "我赶忙冲出时间机器，开始狂奔向覃可汐的家。"
    "从时间机器的位置下山到镇上的公路大概是40分钟的步行时长。"
    "从镇上公路到覃可汐的家大概又是20分钟的步行时长。"
    "我必须加快脚步了！！！"
    "但同时我也在心底里祈祷着。"
    "祈祷着覃可汐的母亲有听进我的提醒。"
    hide screen suduxian
    stop sound
    stop music fadeout 1.0
    screen bg_none
    with fade2
    play music title2 fadein 1.0 fadeout 1.0
    nvle "................"
    nvl clear
    play sound run loop fadein 1.0 fadeout 1.0
    nvle "我不断奔跑着。"
    nvle "........呼..............呼............"
    nvle "不断奔跑着。"
    nvl clear
    nvle "一刻也不敢懈怠。"
    nvle "生怕迟了一步。"
    nvle "呼.............呼............................."
    nvl clear
    stop sound
    scene bg_river
    with fade2
    "......................"
    "跑到了河边.............我暂时地得以大口喘息的机会。"
    "从桥上过河以后就快到覃可汐的家了。"
    "我这般想着。"
    nvle "........."
    nvl clear
    play music lanzhu fadein 1.0 fadeout 1.0
    nan "哥哥.........我朋友.....掉河里了......."
    play sound odoro
    with vpunch
    "？？？？！！！！！"
    "我正打算过河的时候，几个小孩满头大汗地找到我。"
    "我顺着他们所指的方向看去————"
    "一个小女孩正在河中搅动着，挣扎着。"
    play sound odoro
    with vpunch
    nan "呜呜~"
    with vpunch
    nan "救.....救..."
    with vpunch
    nan "救救......我....."
    play music title2 fadein 1.0 fadeout 1.0
    scene bg_none
    with fade
    l "呼！呼！"
    play sound run
    "我拼劲全身的力气奔跑到河岸边上。"
    with vpunch
    "刚好赶上！！还有机会！！"
    play sound mizu_help 
    "我纵身一跃进河中。"
    nvle "为了面对此时此刻，我已经拼命练习了几个月的游泳了！一切都是为了现在！！"
    nvle "一切的一切.....不论是未来的我和叶梓澄的一次次努力......还是叶梓澄父亲给时间机器制造的能源...."
    nvle "都是为了现在！！！"
    nvl clear
    "我努力地靠近覃可汐的身后，慢慢靠近。"
    play sound kawa loop fadein 1.0 fadeout 1.0
    scene bg_river_help at shake2
    with fade
    nan "救.....救...."
    "就快成功了！！！"
    "用手臂托住了她的身体躯干。"
    "另一只手则托住她的下巴，让其露出水面得以呼吸空气。"
    scene bg_none
    with fade2
    stop sound
    play music sora fadein 1.0 fadeout 1.0
    l "呼......呼....."
    l "呼......................."
    nvle "小心翼翼中......"
    nvle "我成功将她带离了河中央。"
    nvle "小心翼翼地............."
    nvl clear
    nvle "将覃可汐带离了河边。"
    nvle "跟随着我的小孩们将这一切看在眼里。"
    nvle "一边说着谢谢一边跑去寻找大人来帮忙。"
    nvl clear
    nvle "先平放在草地上吧。"
    nvle "我回想着自己学习了很久的专业知识，进行着救援。"
    nvle "顾不得什么羞耻，我清理完覃可汐的口腔，进行着人工呼吸，并缓缓按压着胸腔。"
    nvl clear
    nvle "在清理的过程中，仿佛有见到闪光的粒子。"
    nvle "啊...............也对啊..........这个河段的河底沉睡着时间机器的原材料：零之石。"
    nvle "又想起了叶梓澄父亲说过的，零之石浸泡在水中会在水里留下微量的零之石。"
    nvl clear
    nvle "同时想起了最早见到的未来的我，也就是摊主说过的话。"
    nvl clear
    scene bg_schoolmae
    show linluo_old_pose at jin
    play music speak fadein 1.0 fadeout 1.0
    show noko
    with fade2
    voice v3
    t "我们从警察处获取到的关于覃可汐的尸检结果显示，覃可汐的体内存在某种物质。"
    voice v3
    t "其在微观下观测，结构和外观很类似用于制造时间机器和时间刻校正仪的核心部件：零之石。"
    l "那......从覃可汐身体里发现类似零之石的东西.......意味着什么？"
    voice v3
    t "虽然我一直都没弄清覃可汐体内的零之石碎屑的来源是什么，但是这种碎屑单体颗粒大小非常小，却零散分布于覃可汐的体内。"
    voice v3
    t "或许因为单个零之石碎屑的大小足够小，所以身体并没有产生排异反应。"
    voice v3
    t "这些零之石碎屑，就是造成覃可汐遇害的罪魁祸首。"
    voice v5
    t "因为一旦让+1时间刻维度对0时间刻维度产生干涉。作为传递干涉的窗口的零之石本身，就会发生共鸣。"
    voice v3
    t "这种共鸣的外在表现就是会吸引附近的灾厄，也就是使零之石附近的不稳定因素活跃度迅速增加....."
    voice v5
    t "单个零之石产生的共鸣几乎可以忽略不计。但是覃可汐体内无数的零之石碎屑，每一颗碎屑都相当于一扇传递干涉的窗口。"
    voice v3
    t "当这么多的零之石碎屑同时产生共鸣，就会在干涉产生之后吸收大量灾厄。"
    voice v3
    t "也就是说，从产生干涉的那一刻起，覃可汐本身就变成了一个招灾体质！会不断吸引灾厄降临自身。"
    voice v3
    t "所以......无论怎么做，由AADR导致的干涉产生的共鸣，都会最终杀死覃可汐。"
    scene bg_none
    with fade2
    play music sora fadein 1.0 fadeout 1.0
    nvle "原来是这样啊............我全都明白了.........."
    nvle "明白了为什么覃可汐体内会出现零之石的碎屑........."
    play sound odoro
    nvle "源头也是这次溺水！！！"
    nvl clear
    scene bg_none
    with fade2
    nvle ".............."
    nvl clear
    scene bg_none
    with fade2
    x "呜......."
    nvle "她终于逐渐开始有了意识....."
    nvl clear
    scene bg_kexi_oboe
    with fade2
    nvle "慢慢地睁开了眼睛。"
    nvl clear
    x "呜.....你..."
    l "我...........我的名字是......林洛......"
    x "林.....林洛......."
    with vpunch
    l "嗯！！"
    nvle "这时候，看着远处已经有大人朝这边过来了。"
    nvl clear
    l "覃可汐！！十年后再见吧！！请在这之前......好好地活下去！！"
    nvle "我该走了。她目前应该至少脱离了生命危险。"
    nvl clear
    scene bg_none
    with fade2
    play sound run
    "我起身，不顾她的呼喊，朝着反方向跑开。"
    nvle "............."
    nvl clear
    play sound run
    "奔跑了很久很久，确认不会有人注意到我以后，才稍微地坐在地上休息一会。"
    play sound run
    "接着便是继续奔跑。"
    "我的任务已经完成了，该回去决定我接下来需要做的事情了。"
    scene bg_taimumashin_linluo
    with fade2
    nvle "................."
    play music home fadein 1.0 fadeout 1.0
    "回来了终于..........."
    "这样的话......一切都结束了......"
    "我努力到现在....终于......"
    play music sora fadein 1.0 fadeout 1.0
    "时间过的真快啊......回想起我第一次被牵扯进这个事件的时候....."
    "那个注定我永生难忘的九月......"
    "那个青涩的我，怀抱着对新的高中生活的无限遐想........."
    "但是现在的我......再也回不去那种生活了........."
    "我坐在时间机器内，感叹着这一切。"
    play music lanzhu fadein 1.0 fadeout 1.0
    play sound odoro
    with vpunch
    "嗯？"
    scene bg_taimumashin_linluo
    with fade2
    "仪表盘上还显示着昨天查询的信息。"
    play music speak fadein 1.0 fadeout 1.0
    ai "记忆溯流功能是可以通过拷贝与大脑记忆相同数据的零子，经由时间机器的功能发送到过去的时间点......."
    ai "记忆备份恢复功能是可以通过拷贝与大脑记忆相同数据的零子，并设置为自动或手动将记忆发送回大脑，不用经过时间机器的功能......."
    nvle "...................."
    nvl clear
    "抬起了带着手表的手。"
    $ times = "12:27"
    show screen watch
    with dissolve
    "即便戴着在河里游了一圈，但依然可以正常显示时间。"
    "看来是防水的。"
    "此时的我.......产生了一个想法......"
    "我经历了这么多磨难.....但是我还是想......想回到那个日常的校园生活中去....."
    play music sora fadein 1.0 fadeout 1.0
    nvle "我哭了。"
    nvle "泪水不自觉地从脸颊滑落。"
    nvle "想回去读书了......"
    nvl clear
    nvle "有生以来第一次产生这种想法。"
    nvle "如果有选择的话....."
    nvl clear
    nvle "..........."
    nvl clear
    nvle "选择.......现在不就在自己手上吗.............."
    nvle "记忆备份恢复功能.........."
    nvle "将我现在的记忆备份进手表............"
    nvl clear
    nvle "十年后交还给.......十年后的我..........."
    nvle "不过这样的话.....是我太自私了吗？"
    nvle "把我这段回忆.....强行塞进那个我的脑袋里............"
    nvl clear
    nvle "但是这种自私的东西.....我似乎已经做的够多了......一次次把未来的自己的记忆......."
    nvle "没有经过过去的我的同意就.......硬塞进去......."
    nvle "也对......我现在脑袋里的关于这一切的记忆.....也都不是我的.....也是被硬塞进去的......"
    nvl clear
    nvle "那我现在到底算谁呢？我到底是什么样的存在呢？"
    nvle "又想起了曾经谈论过的话题。"
    nvle "忒修斯之船问题......"
    nvl clear
    nvle "即便记忆发生了改变，承载记忆的载体，依旧还是那个载体。"
    nvle "但是.........."
    nvle "我的存在，到底是以什么为判断基准的呢？"
    nvl clear
    $ persistent.tips119 = True
    nvle "像{a=showmenu:tips119}{color=#F18D7D}沼泽人{/color}{/a}问题一样。如果在外人看来，我就是我，那我即便不是我的个体，也是不是我呢？"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    $ persistent.tips120 = True
    $ persistent.tips121 = True
    nvle "又比如{a=showmenu:tips120}{color=#F18D7D}数字生命{/color}{/a}，{a=showmenu:tips121}{color=#F18D7D}数字灵魂{/color}{/a}这种问题，数字化的我，是否算真正的我呢，对我本身来说肯定不是，数字生命只是一个复制了我记忆的AI，但对外人来说呢？"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    $ persistent.tips122 = True
    $ persistent.tips123 = True
    nvle "就像{a=showmenu:tips122}{color=#F18D7D}蒸汽朋克1877{/color}{/a}这个游戏里{a=showmenu:tips123}{color=#F18D7D}黄斑三郎{/color}{/a}一样......数字化的黄斑三郎，对它本身来说，究竟算不算黄斑三郎呢？但是对外人来说，毫无疑问他是。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    nvl clear
    nvle "所以我将我现在的记忆，去装进未来的我的大脑，那未来的我，应该算是我....还是说只是一个拥有我记忆的其他人........."
    nvl clear
    nvle "................."
    nvl clear
    nvle "所以.................."
    nvl clear
menu:
     "将记忆备份进手表":
      jump chapter6_end6
     "不备份":
      jump chapter6_end5