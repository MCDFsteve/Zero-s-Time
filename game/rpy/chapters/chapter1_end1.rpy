label nowatch:
    hide noko
    hide hold_watch
    with dissolve
    $ persistent.tips01 = True
    "并不是我过于敏感了。但是一个根本不认识的人突然要给你东西，而且不是卫生纸，传单或者{a=showmenu:tips01}{color=#F18D7D}pbb砍一刀{/color}{/a}什么的，太可疑了吧。"
#词典
    
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
#词典

    "从小老师和家长都告诉我不能随便拿陌生人的东西。我可是铭记于心。"
    "一想到几分钟或者几小时或者几天后，随着手表的倒计时结束。{size=45}嘭！{/size}我连带着周围的同学一起被炸成碎片。我就倒吸一口凉气。"
    $ persistent.tips02 = True
    "又或者是某一天的假日，认识的朋友发给我一张照片或者视频，然后问“这是你”吗，然后点开一看是我在看{a=showmenu:tips02}{color=#F18D7D}本子{/color}{/a}的照片，或者是我其他什么事的私房照。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     
#词典
    $ persistent.tips03 = True
    $ persistent.tips04 = True
    "被传上了互联网，然后最终变成了{a=showmenu:tips03}{color=#F18D7D}d站{/color}{/a}的{a=showmenu:tips04}{color=#F18D7D}鬼畜{/color}{/a}素材，加入了鬼畜全明星，连带着被录下来的我的声音一起。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     
#词典

    "摊主看我不收，打算硬塞给我。"
    play sound "audio/run.ogg"
    "吓得我更担心他葫芦里卖的什么药了。拔腿跑了起来。"
    hide storer
    scene bg_school_door
    with fade
    "跑到了校门口过检测的地方。回头看着摊主一脸惊恐的神色。心里感慨逃过一劫。"
    play music richang fadeout 1.0 fadein 1.0
    show baoan_pose at jin
    with dissolve
    voice v3
    b "没见过你啊？哪个班的？"
    l "额？"
    "校门口保安不肯放我进去。最后打电话给我的新班主任确认了好半天以后才同意让我进学校。"
    "对这个学校的好感度-1。我在心里想着。"
    scene bg_school_basketball
    with fade
    "一边欣赏着校内的景色一边寻找我所在班级的教学楼。"
    "校内种植了好多植被。"
    play sound suzu
    suzu "咚~咚~"
    "伴随着清脆的铃声一起。我感觉到了地面的震动。"
    l "额！"
    scene bg_school_humans
    with dissolve
    play sound "audio/yakamashii.ogg"
    "整个教学楼的人似乎都冲了出来，我顿时被人群淹没，想前进一步都步履维艰。"
    "果然......吃饭这件事还是全国......统一啊......"
    scene bg_2_3
    with fade
    "被队伍挤得倒退了两三米。"
    "吃饭的队伍已经全走了以后我才勉强走到新班级的教室面前。"
    stop sound
    "我站在教室门口，好好端详着即将迎接我的新教室的模样。"
    "班级是三班。所以教室就在一楼。对下课吃饭的人来说简直是绝佳的地理位置。"
    scene bg_school_soto
    with dissolve
    "还有一点比较好，可以透过一楼的窗户直接看到走廊外面的广场。"
    "应该是叫广场吧。反正就是教学楼前面的一块空地。"
    "风景还可以。"
    "但是并不足让我能爱上上学。"
    scene bg_2_3
    with dissolve
    "学生都出去吃午饭了。上一节课的老师却还留在教室里。似乎还在整理教案。"
    show sensei1_pose at jin
    with dissolve
    voice v3
    s "你就是新来的转学生吗？"
    "似乎教案已经整理完了。老师正准备出教室的时候见我站在教室门口，问了我。"
    l "是"
    "我点头道。憋不出其他话了。虽然网络上我可以张口就来，沟通交流什么的信手沾来。但让我在实际生活中跟第一次见面的人交流。不如杀了我吧。"
    "但我还是得装作像一个正常人的样子。"
    "只好假装自己在玩单机游戏了。"
    "主线任务：跟老师对话。"
    l "老师你好，我叫林洛。"
    $ persistent.tips07 = True
    "我故作镇定地将老师当作{a=showmenu:tips07}{color=#F18D7D}NPC{/color}{/a}角色以后抬头看着说道。"
     #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     
#词典

    "是一个女教师，戴着眼镜。看黑板上的笔迹，应该是教物理的。"
    voice v3
    s "林洛是吧？刚刚保安打电话的时候有跟我说过。我是你的班主任，叫我李老师就可以了。"
    voice v3
    s "你先坐那个位置吧！正好那里现在没人！"
    scene bg_class_naka
    with dissolve
    "老师伸手指向了一个后排靠窗的座位。"
    scene bg_2_3
    with dissolve
    show sensei1_pose eyes2 at jin
    with dissolve
    voice v5
    s "这个点大家都去吃饭去了。你把东西收拾好了也去吃饭吧。食堂就在教学楼左侧，一条路一直走过去就到了。"
    voice v3
    s "中午好好休息顺便准备一下。下午上课的时候你做个自我介绍向大家展示一下自己吧。"
    l "好的老师！"
    "我虽然表面上面无表情。但是心里乐开了花。"
    $ persistent.tips08 = True
    "这可是后排靠窗的位子啊！主角专用座位。我就是这{a=showmenu:tips08}{color=#F18D7D}地球online{/color}{/a}的主角！"
     #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    scene bg_tukue
    with fade
    play sound suzu
    play music school fadeout 1.0 fadein 1.0
    $ persistent.music_school = True
    "在座位上坐立不安地终于熬到下午了。"
    s "这节课，我们要欢迎一位新同学。"
    scene bg_kyoudan
    with dissolve
    "班主任在讲台上说完。便看向了我，示意我上讲台。"
    "虽然很紧张。但还是不得不上去。"
    "只能硬着头皮上了。"
    play sound "audio/yakamashii.ogg"
    scene bg_stand_kyoudan
    with fade
    l "大家好...我叫林洛...来自芷柚市...因父母工作变动，搬家来到沁野市..."
    "感觉我全身都在发抖。尤其是班上同学都盯着我的脸看的时候。"
    "但我还是必须强作镇定。一定要给同学们留下好印象。"
    l "爱好是画画还有打游戏......以及...看动画..."
    "听到班上有几个同学在偷笑了。果然又是刻板印象。估计是觉得高中生了还看动画很幼稚。我的评价是看少了。"
    "当然我没有说出来，可不想在开学第一天就结仇。"
    scene bg_ojigi
    with dissolve
    l "总之...以后请...多多关照！"
    play sound "audio/hakusyu.ogg"
    "我低头鞠躬。班主任鼓起了掌。同学们也附和着。教室里充满了同学们的掌声。"
    scene bg_stand_kyoudan
    with dissolve
    stop sound
    s "大家要多多照顾新同学！新同学你有什么不懂的也尽管找同学们帮忙！这位是班长叶梓澄。有事找她就可以了！"
    scene bg_stand_kyoudan:
        xalign 0.0 yalign 0.0
        xzoom 1.0  yzoom 1.0
        linear 1.0 xalign 0.5 xzoom 1.5 yalign 0.5  yzoom 1.5 
    "班主任用手指向坐在第一排的一个女生。"
    "是一个紫色头发的女孩子，梳着单马尾。本来是面无表情的，被老师点名以后看向了我，脸上挤出了一副营业式笑容。"
    "感觉有什么心事啊......"
    play music school fadeout 1.0 fadein 1.0
    stop sound
    scene bg_tukue
    with fade
    "下课了。"
    "班上的同学各各都很陌生。"
    "但我相信这都只是暂时的，以后肯定会慢慢熟悉起来。"
    scene bg_tukue
    with fade
    play sound suzu
    "终于放学了。"
    "顺利度过了新学期的第一天。"
    "收拾完作业，拿到手机以后。我慢慢走出教室。"
    scene bg_2_3
    with dissolve
    "想尽情欣赏一下新学校的风景。"
    scene bg_school_soto yubi
    with dissolve
    "嗯？有一个人站在两边种满桂花树的那条路上。" 
    scene bg_sorawomiru
    $ persistent.cg04_unlocked = True
    with fade
    $ persistent.music_sora = True
    play music sora fadeout 1.0 fadein 1.0
    "看起来像是我转学的班上的班长。"
    "她抬头仰望着天空。脸上布满了忧伤。心里似乎藏着些什么。"
    "头发随着树叶一起，随风飘动。"
    "很想靠近以后关心几句。但是话憋在嘴里说不出口。"
    "万一被误会了怎么办。万一她以为我在向她搭讪的话就不好办了。"
    "我这样想着。"
    "擦肩而过地离开了。"
    scene bg_xinoyobu
    with dissolve
    play music school fadeout 1.0 fadein 1.0
    x "林洛！"
    "？我听到有人在喊我的名字。"
    scene bg_xinoyobu:
        xalign 0.0 yalign 0.0
        xzoom 1.0  yzoom 1.0
        linear 1.0 xalign 0.07 xzoom 1.5 yalign 0.5  yzoom 1.5
    "朝着声音来源的方向看去。是今天班上我座位旁边坐着的那个女生。也就是我的同桌。"
    "我并没有问她的名字，也不好意思开口问。"
    "她靠着校门口附近的一棵桂花树，伸手呼唤我过去。"
    l "怎么了？"
    "支线任务：去见同学。"
    "我心里这么想着。"
    scene bg_kinoshita
    with dissolve
    show kexi_pose mono yubi at jin
    with dissolve
    play music kexi fadeout 1.0 fadein 1.0
    voice v5
    x "那个...我就长话短说了。你，，，或者你的亲属。以前是否来过沁野市。"
    l "没有。"
    show kexi_pose mono eyes2 mouth3 yubi at jin
    with dissolve
    "我果断否认。我一直是土生土长的芷柚市人。我的父母是。我的祖父母也是。"
    $ persistent.tips09 = True
    "外加我父母都是工作狂。从来都没出去旅游过。对，一次都没有。结果我变成了{a=showmenu:tips09}{color=#F18D7D}家里蹲{/color}{/a}。这还得拜他们所赐。"
     #词典
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    l "怎么了？"
    "很奇怪为什么刚认识的同学会问我这种偏隐私的东西。"
    l "那个？我还不知道你的名字呢。"
    show kexi_pose mono eyes1 mouth1 yubi at jin
    with dissolve
    "反正现在不问以后肯定也得问。我克服我的恐惧，礼貌性地问了一句。"
    voice v3
    x "覃可汐。我的名字是覃可汐。"
    voice v3
    x "没来过的话...没事了。肯定是我弄错了。"
    l "也不是一定没有。"
    "我安慰道。"
    "确实有来过的可能性。说不定爸妈就经常背着我以加班的名义出去度蜜月呢。"
    voice v3
    x "我只是..觉得你有点眼熟。似乎曾经有见过面呢。"
    "这我就有信心了。绝对是她搞错了。也对，沁野市虽然是个小城镇，但是长得像的人，还是可以凑几个出来的。"
    l "覃可汐同学...那如果没事的话，明天学校见。我先回去了。"
    "我本来想夸一句名字真好听的。但是碍于面子问题没有说出口。万一被当成搭讪呢？"
    "不对。我为什么这么害怕被当成搭讪。桃花运这种东西不是越多越好吗？"
    "果然还是我的家里蹲之魂控制住了我的人格啊呜。"
    hide kexi_pose
    show kexi_pose2 mono mouth1 yubi at jin
    with dissolve
    voice v3
    x "嗯~明天见。真是不好意思占用了你很多时间..."
    scene bg_school_nakato
    with dissolve
    play sound "audio/run.ogg"
    play music school fadeout 1.0 fadein 1.0
    "覃可汐一边挥着手一边跑着出了校门。没看到是朝左还是朝右边走的了。"
    "我也紧随其后打算出校门。"
    "突然我想到了什么，朝身后张望了一下。"
    scene bg_sorawomiru2
    $ persistent.cg05_unlocked = True
    with dissolve
    play music sora fadeout 1.0 fadein 1.0
    "班长依然站在道路中间，仰望着天空。"
    play sound higurashi loop
    scene bg_schoolmae yubi
    with fade
    play sound run
    play music richang fadeout 1.0 fadein 1.0
    "出了校门。"
    "来的时候那个很可疑的摊位不见了。"
    scene bg_none
    with fade
    "今晚睡得很香。"
    "很期待以后美好的校园生活了。"
    scene bg_home
    with fade
    $ persistent.music_home = True
    play music "music/home.ogg" fadeout 1.0 fadein 1.0
    "天亮了。"
    "看了看手机的时间。"
    "啊！不小心睡过头了！得赶紧去学校。因为离得比较远。来不及吃家里的早餐了。"
    scene bg_kuruma_matu
    with fade
    play music richang fadeout 1.0 fadein 1.0
    $ persistent.tips10 = True
    "在公交站牌旁边的移动商贩那里买了点{a=showmenu:tips10}{color=#F18D7D}油陷{/color}{/a}。"
     #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    "因为公交车上禁止吃东西，而且在车上吃我会吐的。所以我打算忍到进学校以后吃。"
    scene bg_none
    with fade
    play sound "audio/car_stop.ogg"
    car "{color=#C1394F}尊敬的旅客您好！沁野市高级中学站到了！请各位旅客有序下车！谢谢！{/color}"
    scene bg_schoolmae
    with fade
    "到学校了。"
    stop sound
    "一路汽车颠簸。我现在已经没有食欲了。"
    l "呕~"
    "喉咙发酸。但还是被我憋回去了。如果学校离得再远一点我可能就控制不住了。"
    scene bg_tukue
    with fade
    play music school fadeout 1.0 fadein 1.0
    "第一节课是英语课。反正英语老师还不认识我。而且我坐在后排。正好睡一觉。"
    scene bg_none
    with fade
    "似乎不小心睡过了头。一觉醒来已经是正午了。"
    scene bg_tukue
    with dissolve
    l "呜~呃~"
    "大家似乎都去吃午饭了。我也打算去食堂。"
    scene bg_tukue2
    with dissolve
    show zicheng_pose1 mouth3 at jin
    with dissolve
    "这时班长走了过来。"
    "？班长没去吃饭吗？"
    hide zicheng
    voice v1
    c "林洛。"
    "班长似乎有事情要找我商量。"
    voice v3
    c "你被安排到每周五的班级清洁区值日了。和覃可汐一起。"
    l "什么值日？"
    "这个学校，打扫卫生需要学生自己负责吗？"
    l "好。我知道了。我们班的清洁区是哪？"
    scene bg_school_soto
    with dissolve
    "班长把我带到班级门口走廊上大致比划了一下。"
    hide zicheng_pose1
    show zicheng_pose2 at jin
    with dissolve
    voice v3
    c "是一班到五班门口的走廊外面的广场的打扫。"
    "需要打扫的区域并不多。只有两个人倒也够了。"
    hide zicheng_pose2
    with dissolve
    "班长说罢，便准备去食堂吃饭。"
    "突然她似乎想起了什么似的。又转过身来。"
    show zicheng_pose2 at jin
    with dissolve
    voice v3
    c "林洛。你办了饭卡了吗？"
    l "啊？什么饭卡？"
    show zicheng_pose2 other1 at jin
    with dissolve
    voice v3
    c "果然啊~没饭卡你怎么吃饭呢~我带你去办饭卡吧。"
    "突然想起来昨天班主任就告诉过我吃饭要办饭卡。但我给忘了。"
    "救星来了。我除了感激还是感激。"
    scene bg_gohan
    with fade
    play sound "audio/yakamashii.ogg"
    "我跟随班长到了食堂。"
    "办事处排队的人早已排成一条长龙。"
    show zicheng_pose2 at jin
    with dissolve
    voice v5
    c "队伍有点长啊！林洛你饿不饿，你先把我的饭卡拿去用吧要不。记得买两份！"
    "叶梓澄说罢便把饭卡交到我的手里。"
    l "啊~那班长你？"
    hide zicheng_pose2
    show zicheng_pose1 mouth1 at jin
    with dissolve
    voice v3
    c "我去帮你排队。等你买到饭的时候我也帮你把饭卡办好了。"
    hide zicheng_pose1
    with dissolve
    "我看着打饭的队伍，同样也是一条长龙。"
    show zicheng_pose1 mouth1 eyes7 at jin
    with dissolve
    l "啊..."
    "虽然很想说“这么做不太合适吧”，但是说不出口。可恶！我恨我自己的内在人格。"
    voice v3
    c "谁叫我是班长呢！"
    show zicheng_pose1 eyes4 mouth1 at jin
    with dissolve
    voice v3
    c "照顾班员是班长的责任。"
    "叶梓澄补充道。"
    $ persistent.tips11 = True
    "flag就不用立了吧。很怕等会响起{a=showmenu:tips11}{color=#F18D7D}《希望之草》{/color}{/a}。我在心里想着。"
     #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    scene bg_gohan
    with dissolve
    "无法推脱。于是我帮着买饭。看着班长排着队帮我办理饭卡。不由得有一丝心动。"
    $ persistent.tips12 = True
    "不行！怎么能这么{a=showmenu:tips12}{color=#F18D7D}现充{/color}{/a}！"
     #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    "我心里的主人格呵斥道。"
    "排队的途中，我端详着班长的饭卡。"
    show hitagi:
      xcenter 0.2
      ycenter 0.3
    with dissolve
    "双面贴了动漫卡通形象......啊！是！"
    show yotugi:
      xcenter 0.2
      ycenter 0.3
    with dissolve
    $ persistent.tips13 = True
    $ persistent.tips14 = True
    $ persistent.tips15 = True
    "居然是{a=showmenu:tips13}{color=#F18D7D}战场原白仪{/color}{/a}和{a=showmenu:tips14}{color=#F18D7D}斧乃木正弦{/color}{/a}！原来班长也是个{a=showmenu:tips15}{color=#F18D7D}故事{/color}{/a}粉丝吗？"
     #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    "泪目！还以为不会找到同好的！"
    scene bg_gohan3
    with dissolve
    "额这......好不容易到我了。才发现今天的菜里有青椒。而且这个学校的食堂每顿饭固定四个菜不能换。"
    "我不由得面露难色。"
    scene bg_gohan_tukue
    with dissolve
    "买完两份饭以后就找到一个座位坐下了。同时端着两份盘子确实是个技术活，时时刻刻得小心翼翼和集中注意力。不过幸好没出事。"
    show zicheng_pose1 mouth1 at jin
    with dissolve
    voice v1
    c "久等啦！"
    "班长过来了。拿着办好的新饭卡一起。"
    voice v3
    c "这个学校怎么样？有在习惯吗？"
    "额。虽然有各种不满意的地方，但终归还是没有表现出来。不能让班长难堪，"
    l "嗯嗯~挺好的。有在适应了。"
    "保持了相当大的决心才说出这几个字。"
    "说出口就后悔了。有些句子这么说并不合适。完蛋。会不会听完以后对我产生坏印象了。"
    "我在心里祈祷着。"
    hide zicheng_pose1
    show zicheng_pose2 at jin
    with dissolve
    voice v3
    c "这是你的饭卡！要保管好哦！"
    "班长把饭卡递给我。我也同时把她的饭卡还给她。"
    l "那个...用了你饭卡里面的餐费的事..."
    hide zicheng_pose2
    show zicheng_pose1 mouth1 at jin
    with dissolve
    voice v3
    c "啊~没事的！不用还了。今天这顿当我请你的。"
    "还是营业式笑容。"
    scene bg_gohan_tukue2
    $ persistent.cg01_unlocked = True
    with dissolve
    "班长坐下来开始吃饭了。我找不到其他的话题了。只能也先吃饭。"
    "这辈子第一次感觉到吃饭是一件很困难的事。尤其是有女孩子就坐在桌子对面的时候。啊~手开始抖了。"
    "必须留下好印象。我一改平时狼吞虎咽的气势。开始慢慢品尝美味。"
    "这不是最难的。最难的是青椒也必须下咽。额呜~"
    "绅士怎么能挑食呢？心里如此想到。"
    "额，如果不把青椒看作是青椒而是其他什么蔬菜的话。倒也能吃得下去了。"
    "鼓起胆抬头看了一眼班长。正在低头吃着饭。依然是一副面无表情。就像《故事》里的斧乃木正弦一样。"
    "感觉这样不行！得活跃一下气氛才可以。怎么能让别人对我的初印象就止步于此。心中的恶魔在耳旁窃窃私语了。"
    $ persistent.tips16 = True
    l "那个！班长你也是故事{a=showmenu:tips16}{color=#F18D7D}厨{/color}{/a}吗？"
     #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    scene bg_gohan_tukue
    with dissolve
    show zicheng_pose1 eyes7 mouth3 at jin
    with dissolve
    "正在吃饭的班长突然抬起头来。"
    voice v3
    c "难道你也看故事系列吗？"
    "完蛋了。面对对方的反应，我竟一时半会不知道该如何回答。"
    "马上就开始后悔我做的决定了。这附近有没有下水道什么的。能不能让我躲一会~"
    l "嗯~有看过..."
    show zicheng_pose1 mouth1 eyes4 at jin
    with dissolve
    voice v3
    c "太好了！终于遇见同好了！"
    voice v3
    c "我一直以为故事系列是很冷门的动画呢！"
    voice v3
    c "你是我这几年来遇见的第二个故事厨！"
    show zicheng_pose1 mouth1 eyes4 other2 at jin
    with dissolve
    "原本愁眉苦脸的样子瞬间消失了。脸上有了真正的笑容。"
    voice v3
    c "你说你喜欢看动画的时候我就觉得可能是同好。那你喜欢这部动画吗？"
    "提到这个我可就不困了。也不管什么社交礼仪什么自身印象了。"
    l "超级喜欢！每个故事都很有趣，欣赏之余还能感受到里面的哲学色彩。"
    voice v3
    c "哦哦哦！好！好！"
    "她脸上的笑容收不住了。"
    scene bg_none
    with fade
    "就这样我们边吃边聊，唠了十几分钟的动画片。最后赶在午睡之前才踩午睡铃的点回到教室。"
    scene bg_class_naka
    with fade
    show zicheng_pose1 mouth1 at jin
    with dissolve
    l "你还知道班上有哪些故事厨吗？"
    "我顾不上羞耻了。午睡一结束就跑过来问叶梓澄。"
    voice v3
    c "你同桌就是一个哦~"
    "什么？故事厨竟在我身边！"
    scene bg_kinoshita
    show kexi_pose mono at jin
    show noko
    "我的同桌，也就是开学那天放学后找我搭讪的那个女生......"
    "什么搭讪...呸！我太看得起我自己了。这叫质问才对。"
    "开学那天放学以后质问我的那个女生。竟然也是个方厨！！而且就是我的同桌。"
    "我爱新学校！我爱我亲爹！能搬到这个城市来真是太好了！"
    "等等。叫什么名字来着？我同桌的名字......"
    "qin......什么来着？"
    "怎么办！忘记了名字的话该怎么开口找话题......"
    "有办法了。"
    scene bg_class_mae
    with fade
    play sound suzu
    "下课了。我假装来抄课程表。走到了教室前面黑板旁边。"
    "黑板旁边贴的不止有课程表。还有值日人员表。"
    "抄完了。顺便看到了名字："
    scene bg_kexi
    with dissolve
    show bg_syuucyuu
    "覃可汐。"
    "是叫这个名字。毕竟她跟我一样是星期五值日。"
    "不行啊，得赶紧想个办法。"
    scene bg_tukue
    with fade
    "这节课我也没心思去听。得赶紧找个话柄让对方知道我是个故事厨。"
    "能在新的学校发现故事厨，就像挖到了宝藏一样让人兴奋。"
    "昸！"
    "放在桌上的自动铅笔不知道因为我做了什么动作而掉到了地上。"
    "还好巧不巧掉到了覃可汐的脚边。"
    "啊呜~我看了看笔周围，已经不敢继续抬头了。"
    "只能另想办法了。"
    scene bg_tukue2
    with dissolve
    show kexi_pose2 at jin
    with dissolve
    voice v1
    x "你铅笔掉了。"
    "覃可汐帮我捡起了铅笔，并递给我。"
    "笔芯已经摔断了。但是幸好我还有很多备用。"
    "覃可汐似乎瞟见了我正在做的题目。"
    "哇！这道题你都会做！隐藏学霸吗？"
    l "我不是什么都知道，我只知道我知道的。"
    $ persistent.tips20 = True
    nvle "糟糕！不小心把心里想的话说出来了。这算什么？我也没有经历过{a=showmenu:tips20}{color=#F18D7D}再上映{/color}{/a}啊喂！"
    nvl clear
     #词典
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

    show kexi_pose2 mouth3 at jin
    with Dissolve(1)
#词典
    "覃可汐突然把眼睛盯着我看。"
    "我只敢用余光瞥见。"
    "啊呜~可恶。我恨我自己。"
    "但能感觉到对方用一种不一样的眼光看着我了。"
    "等会。她似乎从我坐在她旁边开始就一直有在偷看我。"
    "当然有一种可能就是这只是我自我意识过剩而已。啊~我果然是个潜在变态吗？"
    l "啊谢谢！"
    "为了向对方表达谢意我不得不看向对方的眼睛。"
    "是一双很漂亮的眼睛。仿佛深处点缀着星光。坚定且炯炯有神。"
    "啊可恶！"
    "羞耻心爆棚。只能赶紧拿完铅笔然后作罢。"
    scene bg_tukue
    with fade
    play sound suzu
    "下课了。"
    "有谁在戳我。"
    scene bg_kexi_egao
    $ persistent.cg03_unlocked = True
    with dissolve
    "是覃可汐。拿着合盖的中性笔。在戳我的肩"
    voice v3
    x "我什么都不知道！只有你自己知道"
    $ persistent.tips22 = True
    "啊~这突然{a=showmenu:tips22}{color=#F18D7D}中二{/color}{/a}的台词吓得我差点后仰倒了过去。"
     #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    "故事厨无疑了。"
    "没想到覃可汐是这种外向型的人。反而主动地找我套话了。"
    l "我什么都知道！"
    "我附和着对方说道。"
    "她笑了。很开心地笑了。"
    $ persistent.tips26 = True
    "既不是那种做作的笑，也不是公交上刷{a=showmenu:tips26}{color=#F18D7D}抖乐{/color}{/a}外放的那种猴子笑。而是一种发自内心的，很爽朗轻快的笑声。"
     #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    "我也跟着笑了。"
    scene bg_none
    with fade
    play music richang fadeout 1.0 fadein 1.0
    "坐着放学后的公交。我开始回想今天发生的事。"
    play music "music/home.ogg" fadeout 1.0 fadein 1.0
    "认识了两个同好。班长叶梓澄。以及...同桌覃可汐。"
    "覃可汐跟我是认识没多久的吧。就主动跟我聊这么多。"
    $ persistent.tips27 = True
    "是潜在{a=showmenu:tips27}{color=#F18D7D}腹黑{/color}{/a}吗？"
     #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    "为什么我会有这种罪恶的想法。明明对方可能只是跟我一样。遇到志同道合的人以后话匣子收不住了而已。"
    "今天晚上我睡得依然很香甜。开始期待以后有更好的校园生活了。"
    scene bg_kuruma_matu
    with fade
    "跟往常一样起床打算去学校。"
    "已经逐渐开始习惯新学校的生活了。"
    scene bg_tukue
    with dissolve
    play music school fadeout 1.0 fadein 1.0
    play sound "audio/yakamashii.ogg"
    "今天到的比较早。早自习也还没开始。"
    "班上很热闹。同学们三两成群地在聊天。"
    "覃可汐似乎还没来。"
    "反正无事可做。觉得是时候开始新的冒险了。"
    scene bg_egaku
    with dissolve
    "拿出了平时画画的本子。开始构思创作新的角色和世界观。"
    x "画的啥？"
    scene bg_kexi_egao
    with dissolve
    "啊可恶！画的太入迷了完全没在意周围的环境。回过神来的时候覃可汐的头已经凑了过来。"
    "正打算用肩膀遮挡。"
    "已经来不及了。整个画本被她抽了过去。"
    scene bg_tukue2
    with dissolve
    show kexi_pose2 mono mouth1 at jin
    with dissolve
    $ persistent.tips28 = True
    voice v3
    x "诶？这是你自己构思的{a=showmenu:tips28}{color=#F18D7D}宝可魔{/color}{/a}吗？"
     #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    "只好开始解释了。"
    scene bg_egaku
    with dissolve
    l "这是御三家的水。进化了是这个样子。他还有一个地区形态是这样的......"
    scene bg_kexi_egao
    with dissolve
    voice v1
    x "画的真不错啊！"
    $ persistent.tips29 = True
    l "小孩子不懂事画着玩的。反正{a=showmenu:tips29}{color=#F18D7D}任地堂{/color}{/a}不会看到更不会征求我的建议。"
     #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    l "再加上游戏官方现在，有些老宝可魔根本不做进新作游戏。唉~"
    voice v5
    x "是这样吗？我一直想玩这个游戏但是一直没有设备...唉~不知道下次考试以后我妈会不会给我买。"
    l "其实...我偷偷带过来了。"
    $ persistent.tips30 = True
    l "{a=showmenu:tips30}{color=#F18D7D}witch{/color}{/a}游戏机。"
     #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    "这本该是禁止事项的。但出于对覃可汐的信任。还是告诉了她。"
    "也是今天早上才想到可以带进学校。本来打算午睡时间带去公共卫生间找个隔间爽玩一中午的。"
    l "你要玩吗？"
    "啊！啊！啊！我说出来了。"
    "给刚认识三天的女同学借游戏机玩。"
    "心里已经做好了被羞辱的准备了。对方又要觉得是在搭讪了。"
    "但必须保持镇定。至少外表上要镇定。"
    "我吞了一口口水。"
    "汗珠从额头上滑落。这不是我紧张了。只是快下雨了空气太闷热了而已。"
    "真的吗？我看看！"
    scene bg_kabann
    $ persistent.cg09_unlocked = True
    with dissolve
    "还没等我答应。覃可汐就开始翻我的书包了。仿佛这是她自己的东西一样。"
    "救命！太吓人了！"
    "我被对方没有分寸的行为举止吓得不轻。一时间竟愣在原地。"
    voice v1
    x "哇塞！果然有！"
    scene bg_kabann_2
    with dissolve
    "她在我包里翻出一个黑盒子。用拉链封锁住的。"
    "里面确实是游戏机。"
    l "嘘！小声一点！"
    "我在心里如此说道。"
    "但是覃可汐也很识相地没有拿出来。"
    scene bg_kexi_egao
    with dissolve
    x "说好了哟！借我玩。"
    l "额~好！"
    l "但是在教室里太危险了。到处有监控。会被老师抓的。"
    "比起羞耻心，我还是更关心我游戏机的生命安全。"
    voice v3
    x "那，放学以后借我玩可以吗？"
    scene bg_neko
    $ persistent.cg06_unlocked = True
    with dissolve
    "覃可汐突然摆出来一副小乖猫的样子。"
    "倒也不是不行。反正我主线已经通关了。图鉴也集的差不多了。"
    l "可以的！但是我得给你创一个新的账号。"
    x "那，就拜托你啦！"
    scene bg_tukue
    with dissolve
    "覃可汐满意地回到了自己的位置。"
    "只剩我一个人愣在原地。"
    "可恶！"
    "我在心里想着。"
    "这不明摆着挑逗我拿我取乐吗？"
    "可能觉得我真好逗。"
    "但我承认这是事实。这就是我对同龄女生尽量拒绝交谈的原因。"
    "万一被搭话就不知道该说什么。"
    "覃可汐和叶梓澄是因为我的找动漫同好的本能战胜了我的主人格。"
    "啊！我恨昨天的我。以后我的日子肯定不好过了。"
    "如果覃可汐一直这样戏弄我的话。"
    scene bg_tukue
    with fade
    play sound suzu
    "时间过得好快。到了课间休息的时间了。"
    scene bg_class_naka
    with dissolve
    l "班长！"
    "我走到了班长的座位旁边。"
    l "这个季度的新番你有在看吗？"
    show zicheng_pose2 at jin
    with dissolve
    voice v1
    c "有的。"
    $ persistent.tips31 = True
    $ persistent.tips32 = True
    l "我追了{a=showmenu:tips31}{color=#F18D7D}泥可泥丝{/color}{/a}，还有{a=showmenu:tips32}{color=#F18D7D}蒸汽朋克：边缘行者{/color}{/a}。这两部都很不错。"
         #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    hide zicheng_pose2
    show zicheng_pose1 yingan at jin
    with dissolve
    voice v3
    c "我...我只看了泥可泥丝。最近两周更新的我还没看。"
    "为什么？"
    "我正要开口询问。班主任突然出现在教室门口打断了对话。"
    scene bg_2_3
    with dissolve
    show sensei1_pose eyes2 at jin
    with dissolve
    voice v3
    s "叶梓澄！你来一下办公室。"
    "班主任面色很沉重地说道。"
    scene bg_class_naka
    with dissolve
    show zicheng_pose2 at jin
    with dissolve
    voice v1
    c "哦，好。"
    hide zicheng_pose2
    show zicheng_pose1 eyes5 at jin
    with dissolve
    voice v3
    c "不好意思。等会回来再聊。"
    hide zicheng
    with dissolve
    "说罢便出去了。"
    scene bg_tukue
    with fade
    play sound suzu
    "直到回来时上课铃已经响了。"
    "回来的时候面色更加沉重。仿佛要哭出来了一样。"
    scene bg_none
    with fade
    play music sora fadeout 1.0 fadein 1.0
    "究竟发生了什么。"
    scene bg_sorawomiru
    with fade
    show noko
    "我想起了开学那一天。班长也是独自一人苦恼地看着天空。"
    scene bg_tukue
    with fade
    "我准备下课再问问。"
    scene bg_tukue
    with fade
    play music school fadeout 1.0 fadein 1.0
    play sound suzu
    "下课了。"
    "但是班长却收拾了书包。"
    "准备出教室了。"
    "这是要去哪？回家吗？"
    scene bg_2_3
    with dissolve
    show zicheng_pose1 eyes6 mouth4 at jin
    with dissolve
    l "叶梓澄！你这是......"
    voice v3
    c "抱歉，林洛。我有事必须得回去一趟了。"
    l "哦。是吗？好吧。"
    scene bg_school_soto
    with dissolve
    "看着班长渐渐走出校门。各种不安涌上心头。"
    scene bg_none
    with fade
    "那一整天班长都没有再回来。"
    play sound higurashi loop
    scene bg_schoolmae yubi
    with fade
    play music richang fadeout 1.0 fadein 1.0
    "下午放学后。我和覃可汐约定好在校门口“交货”。"
    show kexi_pose mono mouth1 at jin
    with dissolve
    l "好好照顾它哟！"
    "我如此告诫道。除了家里的电脑以外，这台掌机就是我最珍贵的伙伴了。"
    hide kexi_pose
    show kexi_pose2 mono mouth4 at jin
    with dissolve
    voice v3
    x "嗯！我今晚通宵了明天就还你。"
    scene bg_none
    with fade
    play music school fadeout 1.0 fadein 1.0
    "已经星期四了。班长还没来。"
    scene bg_tukue
    with fade
    play sound suzu
    "伴随着上课铃。覃可汐背着书包匆忙地冲了进来。"
    scene bg_tukue2
    with dissolve
    show kexi_pose mono mouth1 at jin
    play audio odoro
    with vpunch
    voice v3
    x "呼！呼！呼！差一点就迟到了！"
    voice v3
    x "林洛那个.....商量个事呗！"
    l "申请多玩一天对吧！"
    nvle "我如此答道。感觉自己渐渐和其他人的距离变近了。"
    nvle "没有以前那样害怕和别人交谈了。这就是找到朋友的感觉吗？"
    nvl clear
    show kexi_pose mono eyes3 mouth3 at jin
    with dissolve
    voice v5
    x "啊啊啊谢谢！我跟你讲我昨天有个馆主一直打不过。克制我全队的属性。啊啊~"
    show kexi_pose mono eyes5 at jin
    with dissolve
    voice v3
    x "打了几个小时都打不过！身上的钱全都输光啦！"
    voice v3
    x "最后只能抓了只属性克制的精灵一直练级。结果一直没睡！"
    l "我的天！你说的通宵是真的通宵啊！"
    l "你还在上高中啊！你还要上学啊！"
    l "你这么搞，什么时候倒学校里了都不稀奇。"
    hide kexi_pose
    show kexi_pose2 mono mouth3 at jin
    with dissolve
    voice v3
    x "啊哈哈哈~对不起！下次不会了~"
    nvle "通宵只有零次和无数次。覃可汐所说的保证我一个标点符号都不会信。"
    nvl clear
    l "那个！为了我的机子着想，请温柔一点！不要再通宵了！"
    voice v5
    x "啊啊！！嗯嗯！！对不起！！我下次不会了！！明天就还给你！！"
    "我突然想起了什么。"
    l "班长今天怎么没有来，你知道是什么原因吗？"
    hide kexi_pose2
    show kexi_pose mono eyes2 at jin
    with dissolve
    "覃可汐一听。态度突然转变了。"
    "笑脸瞬间收了回去。"
    voice v1
    x "班长跟我发消息说了。"
    voice v1
    x "警察说找到了失踪好几天的。"
    voice v1
    x "她父亲的遗体。"
    voice v1
    x "所以。"
    voice v1
    x "这几天得在家里准备葬礼。"
    show noko
    with dissolve
    $ persistent.music_omou = True
    play music "music/omou.ogg" fadeout 1.0 fadein 1.0
    nvle "怎么会......"
    nvle "我逐渐理解为什么这几天。"
    nvle "叶梓澄一直都是一副忧伤的表情。"
    nvle "我真是个废物。"
    nvle "叶梓澄这几天帮了我这么多忙。我却什么都不知道。甚至连一句安慰她的话都没有说。"
    nvle "甚至在昨天还找她谈论动画片这种娱乐项目。"
    nvle "我对我所做的对叶梓澄的冒犯感到懊悔。"
    nvl clear
    scene bg_tukue
    with fade
    play music school fadeout 1.0 fadein 1.0
    "放学前最后一节课是物理课。"
    $ persistent.tips33 = True
    w "{a=showmenu:tips33}{color=#F18D7D}AADR{/color}{/a},全称America Atom's Digitization Research organization。美国原子数据化研究组织。"
     #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    w "这个组织一直致力于研究原子的数据化转换，传输和还原。在全球各地都有分部。其中最近的分部位于......"
    play sound higurashi loop
    scene bg_schoolmae yubi
    with fade
    play music richang fadeout 1.0 fadein 1.0
    "放学了。"
    show ketai1
    with dissolve
    pause 1
    play sound "audio/ketai.ogg"
    show ketai2
    pause 0.7
    stop sound
    play sound "audio/ketai2.ogg"
    show ketai3
    pause 0.2
    hide ketai2
    show ketai4
    pause 0.2
    hide ketai3
    show ketai5
    pause 0.2
    hide ketai4
    show ketai3
    pause 0.2
    hide ketai5
    show ketai4
    pause 0.2
    hide ketai3
    show ketai5
    pause 0.2
    hide ketai4
    show ketai3
    pause 0.2
    hide ketai5
    show ketai4
    pause 0.2
    hide ketai3
    show ketai5
    pause 0.2
    hide ketai4
    show ketai3
    pause 0.2
    hide ketai5
    show ketai4
    pause 0.2
    hide ketai3
    show ketai5
    pause 0.2
    hide ketai4
    show ketai3
    pause 0.2
    hide ketai5
    show ketai4
    pause 0.2
    hide ketai3
    show ketai5
    pause 0.2
    hide ketai4
    show ketai3
    pause 0.2
    hide ketai5
    show ketai4
    pause 0.2
    hide ketai3
    show ketai5
    pause 0.2
    show ketai6
    "我拨通了叶梓澄的电话。"
    "号码是覃可汐写给我的。"
    stop sound
    play sound "audio/ketai3.ogg"
    "滴~滴~滴~咚！"
    stop sound
    show ketai_zicheng
    play music sora fadeout 1.0 fadein 1.0
    voice v1
    c "你好。"
    l "叶梓澄！请问是叶梓澄吗？"
    voice v3
    c "林洛！？你是林洛吗？"
    voice v3
    c "我就是叶梓澄。怎么了？"
    l "那个......这几天的事.....很抱歉..."
    voice v3
    c "嗯？为什么要给我道歉？"
    voice v3
    c "你又没做什么不好的事？"
    l "我......"
    show noko
    with dissolve
    "一想到叶梓澄失去了她的父亲。而我却心安理得地跟她聊这些生活琐事。我就感到非常后悔。"
    hide noko
    with dissolve
    voice v3
    c "林洛！你不需要给我任何道歉的。你没有做错什么。"
    voice v3
    c "我还要感谢你。这几天来陪我聊天。聊自己喜欢的动漫。"
    voice v5
    c "很感激...但是...我的私人琐事还是我自己一个人处理吧！谢谢你的关心。明天见！"
    scene bg_none
    with fade
    "电话挂断了。"
    "她说的没错。"
    "这是她自家的事情。不需要也不应该让我这个外人来插手。"
    "只能先睡了。"
    scene bg_none
    with fade
    play music "music/omou.ogg" fadeout 1.0 fadein 1.0
    "救命！"
    "救命！有没有人来救我！"
    "救我......"
    "覃可汐？"
    scene bg_mizu
    $ persistent.cg07_unlocked = True
    with fade
    "我身处河岸边缘。覃可汐则在河中向我求救。"
    scene bg_kawa
    with dissolve
    "湍急的河流不断吞噬着覃可汐的身体。但她依旧挣扎着。"
    voice v1
    x "救我！"
    scene bg_kawa:
        xalign 0.0 yalign 0.0
        xzoom 1.0  yzoom 1.0
        linear 1.0 xalign 0.45 xzoom 1.5 yalign 0.3  yzoom 1.5
    $ persistent.cg08_unlocked = True
    voice v1
    x "林......洛................."
    scene bg_home
    with fade
    play music "music/home.ogg" fadeout 1.0 fadein 1.0
    "呼！！！"
    "做了一个噩梦。醒来时还是大早上。"
    scene bg_tv
    with dissolve
    "朝阳才刚刚升过山头。该去上班的父亲也还在客厅里吃着早餐看电视。"
    scene bg_tvnews
    with dissolve
    tv "AADR美国总部今日展示了他们研究团队的最新研究成果。据悉该研究成果将颠覆未来人们的时空观念......"
    scene bg_tv
    with dissolve
    "电视台的新闻这样报道着。"
    "AADR？好像昨天上课也听到过这个组织的名字。"
    scene bg_none
    with fade
    "起得比较早。所以我干脆直接在家里吃了早餐了。"
    scene bg_tukue
    with fade
    play music school fadeout 1.0 fadein 1.0
    "到达学校的时候离正式上课还有很久。"
    "班长也还没来。"
    "不会今天还是请假吧。"
    "不会的。我相信班长。"
    "昨天通话的时候也说过了会来的。"
    scene bg_tukue
    with fade
    "快上课的时候。班长终于来了。紧随其后的是覃可汐。"
    scene bg_tukue2
    with dissolve
    show kexi_pose mono mouth1 at jin
    play audio odoro
    with vpunch
    voice v1
    x "呼~呼~赶上了。"
    l "你又通宵了对吧。"
    voice v3
    x "那个......可不可以......"
    l "再让你玩一天对吧！"
    hide kexi_pose
    show kexi_pose2 mono mouth3 at jin
    with dissolve
    voice v1
    x "谢谢！"
    "果然是这样。"
    hide kexi_pose2
    show kexi_pose at jin
    with dissolve
    $ persistent.tips34 = True
    voice v3
    x "对了。明天的{a=showmenu:tips34}{color=#F18D7D}ChieAnime{/color}{/a}你去不去？"
     #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    l "这是什么？"
    "第一次听到这个称谓。是什么活动的名字吗？"
    show kexi_pose mono eyes3 mouth3 at jin
    with dissolve
    $ persistent.tips35 = True
    voice v5
    x "{a=showmenu:tips35}{color=#F18D7D}漫展{/color}{/a}啦漫展！就在市中心的广场附近那个会展中心那里！"
     #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    hide kexi_pose
    show kexi_pose2 mono mouth4 at jin
    with dissolve
    voice v5
    x "我打算去出cos！你也要来吗？来的话我就顺便把游戏机带了在漫展还给你吧！"
    "在经过了0.01秒艰苦的思想斗争以后。"
    l "来！"
    $ persistent.tips36 = True
    $ persistent.tips37 = True
    "澄清一下。我并不是想去看{a=showmenu:tips36}{color=#F18D7D}cosplay{/color}{/a}的漂亮女{a=showmenu:tips37}{color=#F18D7D}coser{/color}{/a}。只是想拿回我的游戏机而已！"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    show kexi_pose2 mono mouth3 at jin
    voice v3
    x "好！那......星期六我们在校门口集合吧!"
    voice v3
    x "怕你找不到路,迷路了就完蛋啦！"
    l "迷路什么的怎么可能存在呢？"
    "我嘴上这样说着。"
    $ persistent.tips38 = True
    "关于我在转学第一天就迷路了三个小时并被{a=showmenu:tips38}{color=#F18D7D}低德地图{/color}{/a}骗到市郊这件事,我不会跟任何人说。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    l "但是。"
    l "我不知道我可以cos什么。而且明天的话我也来不及准备cos服了吧。"
    show kexi_pose2 mono mouth2 at jin
    voice v3
    x "嗯......这确实是个问题......"
    show kexi_pose2 mono mouth3 at jin
    voice v3
    x "不过没关系！你就来帮我提包.....你就来陪我们一起逛就行！"
    "喂！绝对是说漏嘴了什么对吧！"
    scene bg_tukue
    with fade
    play sound suzu
    "上课了！"
    "但覃可汐明显意犹未尽的样子。"
    l "咿啊！"
    scene bg_kexi_egao
    with dissolve
    "被覃可汐拿笔戳了手臂。"
    "然后覃可汐便递给我一个纸条。上面写着："
    scene bg_kami
    with dissolve
    "一定要来哦！明天来我家见面。拜托了{font=SourceHanSansLite.ttf}( •̀ ω •́ )✧{/font}"
    $ persistent.tips40 = True
    "{a=showmenu:tips40}{color=#F18D7D}颜文字{/color}{/a}是什么鬼！？"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    "虽然还.....挺不错的......"
    scene bg_tukue
    with dissolve
    play sound suzu
    "下课了。"
    scene bg_tukue2
    with dissolve
    show kexi_pose2 mouth3 at jin
    with vpunch
    "覃可汐又凑了过来。"
    voice v3
    x "可以吗？你就当来凑个场嘛~"
    "你家在哪？"
    "不问出见面地点的话很难办。"
    show noko
    with dissolve
    "等会。这算邀请我去她家吗？"
    "这......这怎么可以......"
    "刚认识几天就去人家女孩子的家，被当成流氓变态怎么办......"
    "她父母会怎么看我......"
    "内心开始动摇了。"
    scene bg_kexi_egao
    with dissolve
    "在我犹豫不决的时候覃可汐已经写好了一张新的纸条。递给了我。"
    "然后继续摆出期待的摸样。"
    scene bg_tukue2
    with dissolve
    show kexi_pose mouth1 at jin
    with dissolve
    "沁野市水潭村12号......"
    "原来覃可汐是住农村的吗？"
    "不对，这个地理位置......应该已经算市郊了。"
    "到她家也能公交车直达。"
    voice v1
    x "一定要来哟！"
    voice v3
    x "不认识路的话给我打电话就行了！"
    voice v3
    x "明天早上十点到就可以了。我让我妈妈多做一份早餐！"
    "不太好拒绝。毕竟对方都如此盛却邀请了。"
    l "好！"
    "正在这个时候，我想起来了重要的事情。"
    scene bg_tukue
    with dissolve
    l "班长！"
    scene bg_class_naka
    with dissolve
    "我起身离开座位。"
    "覃可汐也跟在了我身后。似乎也是找班长有事。"
    show zicheng_pose1 eyes6 mouth3 at jin
    with dissolve
    voice v1
    c "林洛......"
    l "你还好吗？"
    show zicheng_pose1 eyes7 mouth3 at jin
    with dissolve
    voice v3
    c "嗯！但是......以后我得和我祖父母住一起了。"
    "？......为什么？"
    "我很疑惑，但是不方便直接问。只能作罢。"
    show kexi_pose at jin:
      xpos 0.8
    with vpunch
    show zicheng1_shadow at jin
    voice v3
    x "没事的班长！打起精神啊！明天我们一起去漫展吧！"
    "覃可汐开口了。"
    hide kexi_pose
    show kexi_pose mouth1 at jin:
        xpos 0.8
    voice v3
    x "我上次给你订做了一套cos服！明天你一定要穿穿看！"
    hide zicheng1_shadow
    show zicheng_pose1 eyes4 mouth3 at jin
    with dissolve
    show kexi1_shadow at jin:
        xpos 0.8
    voice v3
    c "哦......好！谢谢！那......在哪见面。"
    hide kexi1_shadow
    show zicheng1_shadow at jin
    voice v3
    x "我家！你去过很多次的！"
    hide zicheng1_shadow
    show kexi1_shadow at jin:
        xpos 0.8
    voice v1
    c "哦！好！"
    hide kexi1_shadow
    show zicheng1_shadow at jin
    voice v3
    x "对了！林洛明天也会来。这样就有三个人了！"
    hide zicheng1_shadow
    "我不好意思地后退了退。"
    "跟在两个女孩子之后，感觉我格格不入。像个边缘人。"
    "到时候一定很束手束脚吧。"
    "我这样想着。"
    scene bg_tukue
    with fade
    play sound suzu
    "上课了。"
    "我写了一张纸条，递给覃可汐。"
    "内容是：叶梓澄要跟祖父母住一起了，她的母亲呢？"
    scene bg_tukue
    with fade
    "几分钟后收到了“回信”。"
    nvle "叶梓澄的妈妈......"
    nvle "在一个多星期前......"
    nvle "就被人杀害了！！"
    nvl clear
    play music sora fadeout 1.0 fadein 1.0
    "呃！！！"
    "我心头一震。"
    show noko
    with dissolve
    "班长如此命运多舛。却仍然尽好了她作为班长的职责。"
    "看向班长的背影。心里有一种说不出来的辛酸。"
    "生活没有击垮她。她依旧负重前行着。"
    "我不由得肃然起敬。当然是内心里的。"
    scene bg_tukue
    with fade
    play music school fadeout 1.0 fadein 1.0
    "到正午了。"
    "正打算去吃饭的时候覃可汐拉住了我。"
    scene bg_kexi_egao
    with dissolve
    voice v1
    x "林洛！你还记得吧！"
    "啊？记得什么？"
    voice v3
    x "值日啦值日！今天是我们两个负责打扫班级清洁区！"
    l "啊！~"
    "早已被我抛至脑后！"
    l "好！我知道了！"
    voice v3
    x "所以，就拜托你吃饭的时候快一点点啦！12点50在教室见！"
    l "啊好！"
    scene bg_gohan_tukue
    with fade
    "要是失约了，覃可汐会对我失望的！"
    "我一边这样想着一边狼吞虎咽着。生怕错过了约定时间。"
    scene bg_gohan_tukue
    with fade
    "吃完了。"
    "第一次吃这么快。应该还有时间。"
    play sound run
    "我一气呵成地收拾餐具，然后往教学楼飞奔。"
    scene bg_2_3
    with fade
    l "呼~呼~"
    "啊！腹部一阵剧痛。但是我也不清楚为什么每次刚吃完饭再跑步就会很痛。"
    "我扶着教室门框，覃可汐已经拿着两把扫把和一个铲子在讲台上等我了。"
    scene bg_class_naka
    with dissolve
    show kexi_pose mouth1 at jin
    with dissolve
    "看着教师前面黑板上悬挂的钟。指向了12：49。"
    voice v3
    x "守约了呢！真不错！"
    voice v3
    x "扫把和铲子给你！我们走吧！"
    l "需要做什么？"
    "我问道。"
    hide kexi_pose
    show kexi_pose2 mouth1 at jin
    with dissolve
    voice v5
    x "很简单的！把教室正外面的广场打扫一下！然后看看有没有垃圾，清理一下就可以啦！走吧！"
    l "理解了！走吧!"
    show kexi_pose2 mouth4 at jin
    voice v5
    x "要记得一件事哦！必须在午睡之前打扫干净才行。不然检查卫生的干部来了就得扣分了。"
    show kexi_pose2 mouth3 at jin
    voice v3
    x "不过我相信你可以的。"
    "覃可汐微笑着向我打气。"
    "其实不需要做到如此地步的。不就是扫个地。"
    "我心里想着。"
    scene bg_school_hiroba_naka
    #$ persistent.cg11_unlocked = True
    with dissolve
    "广场上人群熙熙攘攘。基本都是刚吃完饭以后回来的。"
    "我打扫着广场左侧。覃可汐则负责右侧。"
    "计划最后在中间会合。也就是把地上的垃圾抖扫到中间以后一次性铲走。"
    "天气还是很闷热。即便天早已黑压压的一片了。"
    "我既便身穿短袖，仍然弄得汗流浃背。"
    "真想快点扫完了回教室吹电扇啊~"
    "我这样想着。打扫着地面。"
    show zicheng_pose2 eyes2 at jin:
        xpos 0.5
    with dissolve
    voice v3
    c "呀！林洛在值日啊！加油！"
    "班长也吃完饭回来了。"
    scene bg_school_hiroba_naka
    #$ persistent.cg12_unlocked = True
    with dissolve
    "我抬起头看着班长叶梓澄。她正在一边和覃可汐交谈，一边慢慢靠近覃可汐。"
    $ persistent.tips44 = True
    "她俩的关系很不错啊~愈发感觉自己是个{a=showmenu:tips44}{color=#F18D7D}橘外人{/color}{/a}了。"
        #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    "开始犹豫明天到底还去不去参加漫展。"
    "覃可汐已经打扫到了楼下了，我还在广场前面。不行了我得加油了！"
    "我心里这样想着。"
    scene bg_none
    with fade
    play sound "audio/hasai.ogg"
    play music omou fadeout 1.0 fadein 1.0
    with vpunch
    nan "嘭！"
    "猛烈的一阵巨响！"
    "发生了什么？我猛地一抬头。"
    scene bg_kexi_shiru at shake:
        zoom 1.1
    with fade2
    show bg_syuucyuu:
        alpha 1.0
        linear 1.0 alpha 0.5
        linear 1.0 alpha 1.0
        repeat
    with dissolve
    $ persistent.cg13_unlocked = True
    c "啊......啊......"
    "叶梓澄叫着。"
    c "覃可汐......"
    c "覃可汐她......"
    nvle "这一切发生的过于突然。"
    nvle "刚刚还生龙活虎的覃可汐..."
    nvl clear
    nvle "头部被一个花盆砸中了。"
    nvle "倒在了地上。"
    nvle "身体开始淌出鲜红的血来......."
    nvl clear
    nvle "我被吓得愣在了原地。"
    nvle "叶梓澄也是，直接呆在了原地。"
    nvle "路过的行人也停住了脚步，朝这边看过来。"
    nvl clear
    nvle "办公室和教学楼里的同学也纷纷探出头来。"
    nvle "时间仿佛凝固了。"
    nvle "凝固了。"
    nvl clear
    nvle "我脸上没有表情。因为我已经吓得不敢做出任何其他动作了。"
    nvle "手中的扫把不知道何时自己倒在了地上。是什么时候松手的也不知道了。"
    nvle "覃可汐...她......"
    nvl clear
    "一个离的最近的男老师穿过围观的人群走了过来。"
    s "大家！不要围观！不要围观！有序回到教室！"
    "然后拿出手机开始拨打急救电话。"
    c "林洛......覃可汐她......"
    nvle "叶梓澄带着哭腔朝着我喊道。"
    nvle "但我还是一动也不敢动。"
    nvle "再次想起来昨晚的梦境。"
    nvl clear
    scene bg_mizu
    show noko
    with fade
    play music "music/omou.ogg" fadeout 1.0 fadein 1.0
    "覃可汐被河流吞噬者，哭喊着让我救她。"
    scene bg_kexi_shiru at shake:
        zoom 1.1
    with fade2
    show bg_syuucyuu:
        alpha 1.0
        linear 1.0 alpha 0.5
        linear 1.0 alpha 1.0
        repeat
    with dissolve
    "是啊。我明明是可以救覃可汐的。"
    "如果我没有准时到教室。是不是就不会这样了。"
    scene bg_none
    with fade2
    play music omou fadeout 1.0 fadein 1.0
    "我这样想着。周围视野逐渐没入黑暗。周围的喧闹声和叶梓澄的哭喊声也逐渐消失在我的脑海。"
    "都是我的错...都是我的错...都是我的错...都是我的错...都是我的错...都是我的错...都是我的错...都是我的错...都是我的错...都是我的错...都是我的错...都是我的错...都是我的错...都是我的错..."
    "都是我的错...都是我的错...都是我的错...都是我的错...都是我的错...都是我的错...都是我的错...都是我的错..."
    "都是我的错...都是我的错...都是我的错..."
    "都是我的错............................................................"
    "........................."
    "啊！！！！！！！！！！！！！！！！！！！！！！！！！！\n！！！！！！"
    "啊！！！啊！！！！！！！！！！！"
    "我再也无法忍受。对着天空大喊了出来。"
    scene bg_tukue
    with fade
    play music sora fadeout 1.0 fadein 1.0
    "不知过了多久。我坐在教室里。"
    scene bg_tukue2
    with dissolve
    "看着我旁边空无一人的座位。现在没有人，以后也不会有了。永远都不会有了。"
    "为什么......为什么刚好......"
    "回想着这一切的一切。"
    scene bg_tukue2
    show kexi_pose mono mouth1 at jin
    show noko
    with fade2
    "今天早上，覃可汐还在用着灿烂的笑容跟我在打招呼。"
    scene bg_tukue2
    show kexi_pose mono mouth1 at jin
    show noko
    with fade2
    "今天早上，覃可汐还在邀请我明天去参加ChieAnime。"
    scene bg_tukue2
    show kexi_pose mono mouth1 at jin
    show noko
    with fade2
    "覃可汐借的游戏机也还没来得及亲手还我......"
    scene bg_mado
    with dissolve
    "看着窗外的走廊。"
    "警察已经拉起了警戒线。覃可汐已经被救护车抬走了。"
    "并不是去抢救。"
    "医生的诊断结果是当场死亡。死于头部重创。"
    "这一切发生的太快了..."
    "太突然了......"
    "我没料到..覃可汐本人也没有..."
    "......"
    "............"
    "..."
    "已经没有心情做任何事情了。"
    scene bg_zicheng_miru
    with dissolve
    "我看向叶梓澄。"
    "坚强如她也依旧在座位上啜泣。"
    "坚强如她也依然被接二连三的重大打击击垮了。"
    scene bg_tukue
    with fade
    play sound suzu
    "放学了。"
    "校园内的空气死一般的寂静。"
    "天气依旧闷热。"
    scene bg_keikoku
    with dissolve
    "我站在警戒线外面，看着地面上的血迹和粉笔画的线条。"
    "不知道看了多久。班长过来了。"
    show zicheng_pose1 mono eyes2 mouth4 at jin
    with dissolve
    voice v3
    c "林洛......回去吧......"
    scene bg_zicheng_te
    with dissolve
    $ persistent.cg14_unlocked = True
    "叶梓澄抓住了我的手，这样说到。"
    "我抬起头，看着叶梓澄湿润的眼角。"
    l "走吧......"
    scene bg_none
    with fade
    play music "music/home.ogg" fadeout 1.0 fadein 1.0
    "回到家以后。我没有心情吃饭。"
    "电视上播放着覃可汐遇害的新闻。"
    "躺在床上，没有丝毫睡意。"
    play music sora fadeout 1.0 fadein 1.0
    "会想起覃可汐的点点滴滴。即便只有几天的回忆。"
    "但还是很难受。"
    "不知道是什么时候睡着了。"
    scene bg_home
    with fade
    play sound "audio/ketaisong.ogg"
    "被电话声吵醒。"
    "是叶梓澄打来的。"
    show ketai_zicheng2
    with dissolve
    stop sound
    play sound "audio/ketai3.ogg"
    c "林洛......"
    c "那个......"
    c "覃可汐的葬礼.....你去吗？"
    "想起来今天是周六，没有课。即便有课，在出了这种安全事故以后也大概率不会上课了。"
    l "葬礼在哪？"
    "我问道。"
    c "覃可汐的家。"
    "想起来，覃可汐昨天给我写了她家的住址。"
    c "你来吗？一起去葬礼上看覃可汐最后一面......"
    "........."
    "是啊...以后再也见不到覃可汐了..."
    l "我来！"
    show noko
    with dissolve
    "毕竟是我的错。如果我当时能小心一点，能看到楼顶飘飘欲坠的花盆就好了......如果我吃饭慢一点......"
    "就能迟一点去打扫卫生......或许就能不被花盆砸到了......"
    "我需要赎罪！"
    hide noko
    with dissolve
    c "好！那在校门口集合可以吗？"
    l "好......"
    hide ketai_zicheng2
    with dissolve
    "叶梓澄挂断了电话。"
    scene bg_home2
    with fade
    play music "music/home.ogg" fadeout 1.0 fadein 1.0
    "我找了一套比较体面的衣服。"
    "顺便抓了一把抽纸。"
    "不为别的，只是想到，到葬礼现场以后肯定眼泪会止不住的流下来。"
    "父母都出门上班去了。"
    "家里只有我一个人。"
    scene bg_kuruma_matu
    with fade
    show screen ame
    with dissolve
    play sound ame loop fadeout 1.0 fadein 1.0
    "我拿着雨伞出了门。"
    "因为一醒来外面就一直下着大雨。"
    "连苍天都对覃可汐的死感到可惜吗......"
    "今天的公交车来的格外的慢。等了差不多半个小时才有车过来。"
    hide screen ame
    scene bg_none
    with fade
    car "{color=#C1394F}尊敬的旅客您好！沁野市高级中学站到了！请各位旅客有序下车！谢谢！{/color}"
    scene bg_schoolmae ame
    with fade
    show screen ame
    with dissolve
    "下车了。"
    show zicheng_2
    with dissolve
    "叶梓澄已经在校门口看起来像等了很久的样子。"
    "手里拿着一把花束。"
    c "走吧~"
    "叶梓澄没有多说什么。只说了这两个字。"
    hide screen ame
    scene bg_none
    with fade
    "我们拦了一辆出租车。目的地就是覃可汐的家。葬礼举办的地方。"
    "即便在路上。叶梓澄也依旧是一滩不发。偏着头坐在副驾驶看着窗外的雨景。"
    "由于晕车的缘故，我摇下了车窗玻璃。任凭冰冷的雨水哗哗地打在我的脸上。"
    "这样或许也能让我冷静一点。"
    "一直在想关于覃可汐的事情。不知道什么时候，车停了。"
    c "到了。"
    "叶梓澄终于开口了。"
    scene bg_kexihome
    with fade
    show screen ame
    with dissolve
    "我右脚踏出车外，目视着周围。"
    "覃可汐的房子是很古朴的红砖平房。这样来看其实家境并不是很好。"
    "可以理解为什么当初覃可汐会抱怨家里人不给她买游戏机了。"
    "大概是因为还是白天，来的人很少。大部分都是中年人和老人。应该都是覃可汐的亲戚。"
    $ persistent.tips43 = True
    "叶梓澄把拿的花束分给了我一半。然后带我到了房子的{a=showmenu:tips43}{color=#F18D7D}堂屋{/color}{/a}。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    hide screen ame
    scene bg_kexi_syashin
    with dissolve
    $ persistent.cg15_unlocked = True
    play music sora fadeout 1.0 fadein 1.0
    "房间正中央放着覃可汐永远安息的地方：棺木。前面则堆满了花束和花圈。"
    "以及......覃可汐的遗像。是她暑假在河边拍摄的照片。"
    "照片上的她穿着白色连衣裙，笑得很灿烂。"
    "只是这笑容永远地定格了。"
    "看到这照片以后叶梓澄最先忍受不住。痛哭了起来。"
    c "对不起......覃可汐......不能和你一块.........毕业了..."
    c "也不能....去同一所....大学了......"
    c "额......呜......"
    c "为什么......"
    c "为什么你要单方面违约......"
    "叶梓澄哭了许久。"
    "我的眼泪也早已挤到眼角。但我的悲痛是绝对不比叶梓澄多的。"
    "覃可汐...对不起了...不能陪你去漫展了......"
    "说罢。我便将花束放在了覃可汐的最后的微笑面前。叶梓澄也紧随其后。花束渐渐没过照片的1/3了。"
    c "林洛...你现在打算在这里继续进行葬礼......还是说......跟我一起回去？"
    l "已经准备走了吗？"
    c "我每在这里多呆一秒，我的悲伤就多一分。"
    "我能感同身受。"
    l "回去吧......"
    scene bg_none
    with fade
    play sound ame loop fadeout 1.0 fadein 1.0
    "我和叶梓澄正打算坐着来的出租车离开。一个中年妇女拦住了我。"
    "林洛？你就是林洛对吧！"
    scene bg_kexihome
    with dissolve
    show screen ame
    with dissolve
    l "啊？"
    "回头一看。"
    show kexihaha_pose at jin
    with dissolve
    play music sora fadeout 1.0 fadein 1.0
    voice v3
    m "我是覃可汐的妈妈。这几天老听女儿提到你的名字。"
    voice v3
    m "不打算多呆一会吗？"
    l "不了......谢谢阿姨..."
    voice v3
    m "哦对了！你等一会。"
    hide kexihaha_pose
    with dissolve
    "说罢覃可汐的母亲便回里屋了。"
    scene bg_kexihome
    with fade
    "过了一分钟以后走了出来。"
    show kexihaha_pose at jin
    with dissolve
    voice v3
    m "这个...是你的对吧！"
    "手里拿着的正是我之前借给覃可汐的游戏机。"
    voice v3
    m "还是感谢您，让我女儿最后享受了一段快乐的时光。这个东西她很早就想要了。"
    hide kexihaha_pose
    show kexihaha_pose eyes2 at jin
    with dissolve
    voice v3
    m "但是因为我嫌贵了一直没买......"
    "一边说着，覃可汐的母亲的眼泪开始止不住了......"
    voice v3
    m "请你......把这个东西拿回去吧！"
    "我接过了游戏机。"
    hide screen ame
    scene bg_none
    with fade
    play sound ame loop fadeout 1.0 fadein 1.0
    "回去的路上，我看着手里拿的游戏机。"
    "这是我和覃可汐最后的回忆了。"
    play music "music/home.ogg" fadeout 1.0 fadein 1.0
    "我和叶梓澄在校门口便分别了。我继续搭乘公交车回家了。"
    "晚上依旧睡不着。"
    "又忘记了是什么时候睡着了的。"
    with vpunch
    play music lanzhu fadeout 1.0 fadein 1.0
    "啪！"
    "睡梦中被什么东西吵醒了！"
    "我迷迷糊糊中睁开眼。"
    scene bg_home
    with fade
    "啊~"
    "闻到一股浓烈的塑料的烧焦味。"
    "呃啊！~"
    scene bg_home3
    with dissolve
    play music lanzhu fadeout 1.0 fadein 1.0
    "不知何时开始，卧室里连接电脑的插座开始擦起了电火花。顺带着的还有隐隐飘起的浓烟。"
    "以及啪啪的响声。"
    "顺带被烧起来的，还有我正在充电的手机。"
    "吓得我赶紧爬起来，拔掉了插头。"
    scene bg_none
    with fade
    play music "music/home.ogg" fadeout 1.0 fadein 1.0
    "好险。差一点就引发火灾了！"
    "不由得流出了一身冷汗。"
    scene bg_home
    with fade
    "再次睁开眼时已是正午。"
    "啊！~"
    "睡了这么久了。"
    "高情商的说法便是："
    "提前体验了一次大学生的生活。"
    scene bg_home2
    with dissolve
    "父母已经出门去了。"
    scene bg_tv2
    with dissolve
    tv "今天早上十点半，挖掘泥沙的施工队在沁野市水潭村河段内挖出了一大块奇特的球状金属物体......"
    "刚打开的电视上这样报道着。"
    scene bg_home2
    with dissolve
    "今天还是什么都不想做。"
    scene bg_none
    with fade
    "把作业做完了就一直等到天黑。然后睡觉了。"
    "即便出了这种事故，明天依旧要照常上课。"
    "大人的世界是浑浊的。"
    scene bg_home
    with fade
    "........."
    "周一了。"
    "刚想看看时间。"
    "但是发现手机已经在半夜被烧毁了，电池都鼓起来了。"
    scene bg_home2
    with dissolve
    "洗漱完以后，来到客厅打开了电视。"
    "额啊！！！已经快上课了！完蛋了！今天必迟到了！"
    "我赶紧关掉电视，收拾物品冲出家门。早餐什么的没必要吃了。朝着公交站牌跑去。"
    scene bg_kuruma_matu
    with dissolve
    play music richang fadeout 1.0 fadein 1.0
    "呼~呼~"
    "好不容易跑到了公交站牌，发现刚好有一辆公交车擦肩而过，已经开走了！"
    "可恶！！我恨！！"
    "我心里想着。血压逐渐升高。"
    scene bg_none
    with fade
    "几分钟后等到了另一辆公交车。"
    "天道好轮回。之前跑掉的那辆车现在已经被追上了。"
    "当然是在十字路口的红绿灯这里。"
    "看起来已经等了很久了。"
    "不过我坐的这辆车一过来就马上绿灯了。"
    "什么嘛，我运气也不是很差嘛~"
    "刚这样想着。"
    stop sound
    play sound "audio/kuruma.ogg"
    play music omou fadeout 1.0 fadein 1.0
    with vpunch
    "嘭！！！！！！！！！！！！"
    "！！！！！！！！！！！！！！！！！！！！！！"
    "?!"
    "发生了什么？"
    "十字路口有一辆大货车像失控了一般横冲直撞了过来！"
    "我前面那辆车直接被撞翻了。被顶偏移了好几米，顺便压倒了另一侧的轿车。"
    "！！！！！！！"
    "我所乘坐的这辆车的司机也明显没做好准备。直接追尾撞了上去。"
    "也撞到了大货车身上。"
    n "司机师傅！！开门啊司机师傅！！"
    "车被撞停以后，车上的乘客开始骚动了。"
    "包括我！！"
    "刚刚的撞击让我的头直接撞到了扶杆上面。头一阵眩晕。"
    "这下真的要吐出来了。"
    "但我还是冷静了下来。取下了车上的消防锤。"
    with vpunch
    "嘭！！！！！！！！！！！！"
    "我破开了车窗。打算跳出去。也示意其他乘客排队跳。"
    "该死！！"
    "发现大货车已经开始漏油了！！"
    "机油顺着车身不断往地上渗漏，流动。"
    "大家！！！！！"
    l "快跳窗！！车要爆炸了！！！"
    "说罢。在我跳窗的一瞬间。"
    with vpunch
    "嘭！！！！！！！！！！！！"
    "撞车产生的电火花点燃了渗漏的汽油。"
    "随着一阵连环的爆炸声。我也渐渐失去了知觉......"
    "........."
    "过了一会，我被救护车的警笛声唤醒。"
    "手还可以动，但是腿脚已经失去了知觉。"
    y "这里！！这里还有生还者！！"
    y "快！抬担架过来！！"
    "太好了.......救助小组发现了我......"
    "可以稍微......休息一会了......"
    ".............."
    "......."
    stop sound
    play music "music/home.ogg" fadeout 1.0 fadein 1.0
    "呼！~"
    scene bg_byouin
    with fade2
    "看着陌生的天花板。再次醒来时发现自己身处医院。"
    c "啊？林洛你醒了！"
    "旁边传来一阵女声。"
    show zicheng_pose1 mono eyes4 mouth1 at jin
    with dissolve
    "是班长。"
    l "班长......我这是......"
    show zicheng_pose1 mono mouth5 at jin
    with dissolve
    voice v3
    c "你先躺下，慢慢来别急。"
    show zicheng_pose1 mono mouth3 at jin
    with dissolve
    voice v3
    c "你出车祸了。我是来看望你的。"
    l "是吗......医生怎么说？"
    hide zicheng_pose1
    show zicheng_pose2 mono mouth1 other2 other1 at jin
    with dissolve
    voice v1
    c "额...那个......"
    "有了不好的预感。"
    "大概已经猜到了。"
    hide zicheng_pose2
    show zicheng_pose1 mono mouth3 eyes3 at jin
    with dissolve
    voice v3
    c "其他一切正常。就是你的腿...可能以后必须坐轮椅了......"
    "果然吗？"
    "为什么？为什么我会这么倒霉！？"
    "不过......至少捡回了一条命不是吗？"
    l "班长...我逐渐理解你了。"
    show zicheng_pose1 mono mouth5 other2 at jin
    play audio odoro
    with vpunch
    c "？"
    l "接二连三的挫折。既然没有打倒我，那我就必须继续走下去，人生的这条道路。"
    l "班长你也是这么想的对吧！"
    hide zicheng_pose1
    show zicheng_pose2 mono eyes2 mouth1 at jin
    with dissolve
    c "嗯..."
    "班长微微点了点头。"
    l "啊！那个...对了！"
    l "我大概躺了多久？"
    hide zicheng_pose2
    show zicheng_pose1 mono eyes5 at jin
    with dissolve
    c "已经两个星期了..."
    show zicheng_pose1 mono mouth3 at jin
    with dissolve
    voice v3
    c "林洛......那个......我有一事相求！"
    l "什么事？"
    "班长对我一直很好，也帮了我很多忙，现在也是时候回报她了。"
    "说罢班长拿出来一份报纸，并示意让我看。"
    "我接过报纸。"
    scene bg_news
    with dissolve
    "头版赫赫用大黑字体写着："
    "AADR组织向各国政府发出通告："
    "本组织已掌握足以控制整个世界的武器。请各国政府首脑在限期内前往本组织在全世界各地成立的分部。"
    "签署归从协定。让出政府的统治权，由AADR接管并实行自治管理。"
    "如果有政府认为我们是在开玩笑，或者在进行虚假的威慑，或者准备采取武力镇压的方式解决，那你们可以试一试。"
    "至于代价：则是向你们国家所处地区投放武器。敬告各国政府：本组织，即AADR组织，现已纳入美国政府保护之下"
    "我们将在一个月后在未签署协定的国家中随机抽取一个国家，进行武器的投放。以进行威慑，并证明武器的威力并不是巧合，而是人为控制的事件结果。"
    "关于武器的威力。可以参考我们组织在沁野市的第一次投放。"
    l "这是？"
    "我大惑不解。"
    l "参考在沁野市的第一次投放是什么意思？"
    scene bg_byouin
    show zicheng_pose1 mono eyes7 at jin
    with dissolve
    play music speak fadeout 1.0 fadein 1.0
    voice v1
    c "字面意思！"
    "班长解释道。"
    hide zicheng_pose1
    show zicheng_pose2 mono eyes2 at jin
    with dissolve
    voice v3
    c "这个所谓的“武器”。会产生一种类似辐射的东西。并不会直接作用于人体。"
    voice v3
    c "而是会作用于环境。"
    "什么意思？我还是听的一头雾水。"
    hide zicheng_pose2
    with dissolve
    "班长似乎也知道很晦涩难懂。又转身从包里拿出来一本被牛皮包裹的笔记本。"
    show zicheng_pose1 mono eyes3 mouth3 at jin
    with dissolve
    show note:
      xcenter 0.2
      ycenter 0.3
    with dissolve
    voice v3
    c "这是我父亲生前记录下来的笔记本。是我在我父亲的研究所里找到的。"
    l "这是？"
    voice v5
    c "我似乎还未曾对你解释过。我的父亲和母亲都是科研学者，在这个城市修建了一所研究所。"
    voice v3
    c "研究项目是原子的数字化转换和传输。"
    l "啊！？"
    nvle "我似乎想起了什么。"
    nvl clear
    l "这不就是......"
    voice v3
    c "没错！这也是AADR的研究目标。"
    hide note
    with dissolve
    voice v5
    c "但是跟AADR不同。我父亲确确实实好几年前就已经成功实现了把物体再构成物质，原子进行拆分重组来构成了一种新的物质粒子，这种新的物质粒子，可以进行存储和还原，并且支持以光速进行运动。"
    $ persistent.tips45 = True
    voice v5
    c "我父亲将物质的原子分解成的这种新创造的物质粒子，命名为“{a=showmenu:tips45}{color=#F18D7D}零子{/color}{/a}”。由于零子的物理性质之一是具有吸收特定波长的能力，所以肉眼可以观测到其是一种黑白相间，呈漂浮碎屑状的物质。"
#词典
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    hide zicheng_pose1
    show zicheng_pose2 mono eyes2 at jin
    with dissolve
    voice v3
    c "零子是一种梦幻般的物质，我父亲如此形容它。这个宇宙上，只要是由原子作为基本物质结构而构造而形成的物质，都能转换成零子。"
    voice v3
    c "我父亲也已经开发出来可以将质量较小的物质再构成为零子，传输到特定地方再还原为原子的集合体，也就是物质最开始面貌的机器。"
    $ persistent.tips53 = True
    voice v3
    c "至于如何负责还原，就需要在物质再构成之前，有一部分外来的零子负责记录和保存物质内原子的空间排布关系，这部分零子被成为：{a=showmenu:tips53}{color=#F18D7D}原子匹配分布表{/color}{/a}！"
#词典
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    $ persistent.tips54 = True
    l "相当于记录的{a=showmenu:tips54}{color=#F18D7D}蓝图{/color}{/a}对吧！"
#词典
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    voice v1
    c "没错！"
    l "这么厉害！！！"
    l "如果公开的话这不妥妥的拿诺奖！！"
    voice v3
    c "但是一直未曾公开。因为——————"
    voice v3
    c "我父亲偶然之中又开发出来了一种新的仪器。可以将零子注入更高维度。"
    $ persistent.tips49 = True
    voice v3
    c "我父亲将它命名为“{a=showmenu:tips49}{color=#F18D7D}时间刻校正仪{/color}{/a}”！"
    #词典
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
    $ persistent.time = 2
    $ time_end1 = True
   #词典
    l "这......这是什么意思？"
    scene bg_umi
    with dissolve
    c "你可以假设宇宙是一片大海。"
    c "我们所处的维度便是海平面。"
    c "海平面之上的天空便是更高的一层维度。"
    c "天空中蓄积的水蒸气越多，云层就会积的越厚。"
    c "最后则会变成降雨，拍打在海平面之上。"
    l "注入到更高维度里的零子就相当于水蒸气对吧。"
    "我若有所思的回答道。"
    c "非常正确！"
    c "更高维度的零子对本维度的干涉可以比喻为蓄积水蒸气引发的降水，对海平面的干涉。"
    l "也就是说，这台时间刻校正仪的功能，就像是在海平面上修筑了一座可以把水蒸气蒸发到天空中的蒸发炉对吧！"
    scene bg_byouin
    show zicheng_pose1 mono eyes3 mouth3 at jin
    with dissolve
    voice v5
    c "实际上这也是我看了父亲的笔记本以后才知道的。父亲秘密制造了这台仪器。但我找不到任何关于制造这台仪器有关的信息。"
    voice v3
    c "也不知道这台机器的注入零子的具体运作原理，恐怕只有我父亲本人才知道了。"
    voice v3
    c "或许是有不得已的原因，父亲从来没有告诉过我。但或许已经告诉过我的母亲。"
    show zicheng_pose1 mono eyes6 mouth4 at jin
    with dissolve
    voice v3
    c "你知道的吧。我父亲出事之前，是我的母亲先被杀害。"
    l "嗯......当然记得！"
    voice v3
    c "极有可能就是AADR所为！"
    l "这......"
    nvle "班长显得非常冷静。这跟我内心深处的班长形象有所不同。"
    nvl clear
    hide zicheng_pose1
    show zicheng_pose2 mono eyes2 at jin
    with dissolve
    voice v3
    c "我怀疑是AADR趁我母亲独自在外的时候杀害了她。不管是意外还是一开始就动手。"
    voice v3
    c "总之AADR得到了我母亲手机内的数据。所以后面采取行动入侵了我父亲的研究所。"
    voice v3
    c "然后杀害了我的父亲。"
    voice v3
    c "杀害方式很可能是....."
    "班长顿了一顿，继续说道。"
    show zicheng_pose2 mono eyes2 mouth1 other2 at jin
    with dissolve
    voice v5
    c "丢入了转换成零子的仪器，然后将我父亲转换成的零子注入了时间刻校正仪。"
    l "也就是将你父亲身体转换成的零子注入了更高维度是吧。"
    "我插话道。"
    show zicheng_pose2 mono eyes2 mouth2 at jin
    with dissolve
    voice v5
    c "嗯！证据就是，我接到警察电话去领我父亲遗体的时候，只看到了一只手臂。手臂断口处残留着零子。"
    l "我记得是找到手臂以后就举办了葬礼了对吧！"
    l "但是为什么只找到手臂就断定你父亲已经遇害了呢？"
    voice v3
    c "是我父亲在留下了的笔记里写的：如果找不到我父亲，或者找到的只是身体的一部分，就默认已经去世了。"
    l "是吗....."
    l "所以注入到更高维度的零子对我们所处纬度的干涉到底是什么？"
    voice v3
    c "我父亲并没有在我找到的这个笔记本里写出。但是我推测是："
    voice v3
    c "会影响本维度物质之间的不稳定性！就像降水拍打海面会激起涟漪，拍出海浪和水花一样。"
    voice v3
    c "因为，沁野市自从我父亲遇害以后。从覃可汐开始，意外事故不断发生。"
    voice v3
    c "覃可汐也好，你也好，都是受了这个影响。"
    show zicheng_pose2 mono eyes2 mouth1 other2 at jin
    with dissolve
    voice v5
    c "实际上在你住院以后两个星期之间，沁野市至少又发生了七起意外事故。涉及到车祸，火灾和楼房坍塌。"
    voice v3
    c "媒体已经将沁野市报道为不幸之城了。"
    voice v3
    c "再加上AADR亲口出面承认沁野市目前的处境是AADR所为。"
    hide zicheng_pose2
    show zicheng_pose1 mono eyes3 mouth3 at jin
    with dissolve
    voice v3
    c "更加坚定了我的说法！"
    l "如果是往更高维度注入零子影响我们所处的维度的话。那为什么只有沁野市受到了影响？不应该是全世界都受影响吗？"
    show zicheng_pose1 mono eyes7 mouth3 at jin
    with dissolve
    voice v3
    c "不是这样的。我推测零子所注入的那层更高维度，平行浮于我们所处的维度之上。"
    hide zicheng_pose1
    show zicheng_pose2 mono eyes2 at jin
    with dissolve
    c "简要解释就是："
    voice v3
    c "在这个维度的哪个地方注入的零子，影响的就是这个维度的哪个地方。"
    voice v5
    c "一片海域所处的天空，引发的降水一般只会拍打到正下方的那一片海域不是吗？"
    voice v3
    c "看AADR的如此狂妄的声明。我推测注入的量越多，影响的范围就越大。"
    voice v3
    c "就像积雨云越大，降水的范围越大一样。"
    hide zicheng_pose2
    show zicheng_pose1 mono eyes4 mouth1 at jin
    with dissolve
    voice v3
    c "不过幸运的是。林洛你所在的这个医院似乎并不在所影响的范围内！"
    l "也就是说我暂时是安全的对吧！"
    "我头已经被说晕了。只能大概听出这个结论。"
    l "所以，到底想拜托我什么事呢？"
    "我尝试将讨论拉回主题。"
    voice v3
    c "陪我一起，拯救我父母，以及，拯救覃可汐，拯救沁野市！！"
    l "啊！！！？？？"
    l "让我捋一捋。"
    l "你的父母已经被杀害了对吧！覃可汐也是，还有如今沁野市的处境。"
    l "所以怎么才能拯救？"
    l "难不成回溯时间？"
    show zicheng_pose1 mono eyes4 at jin
    play audio odoro
    with vpunch
    voice v1
    c "对！"
    "叶梓澄说道。"
    "看她的表情并不像是在开玩笑。"
    l "怎么做？"
    "虽然感到很震惊。但我还是选择相信叶梓澄，以及她父亲的研究成果。"
    hide zicheng_pose1
    show zicheng_pose2 mono at jin
    with dissolve
    voice v3
    c "需要做两件事。"
    voice v3
    c "对抗AADR。以及。"
    show zicheng_pose2 mono other2 at jin
    with dissolve
    voice v3
    c "制造时间机器。"
    l "时间机器？"
    "叶梓澄继续说道。"
    show note:
      xcenter 0.2
      ycenter 0.3
    with dissolve
    show zicheng_pose2 mono eyes2 at jin
    with dissolve
    voice v3
    c "没错！我父亲的这个笔记本里也记载了关于时间机器的构想。"
    l "什么构想？"
    voice v3
    c "我们所处的这个维度之上的，更高维度的时间流逝速度，是比我们所在维度更慢一点的。"
    voice v3
    c "也就是说，如果在现在往时间刻校正仪注入零子，得好一会才会对我们所处的维度产生干涉。"
    voice v3
    c "这也能解释为什么覃可汐的死离我父亲的死相差了三天，又或者更久。"
    voice v3
    c "所以这个时间机器的构想是："
    voice v3
    c "根据爱因斯坦的相对论的结论。速度越快，时间流速越慢。"
    voice v3
    c "移速达到光速，时间流速为零。"
    voice v3
    c "零子这种物质的其中一个性质便是可以附和着普通的电子数据一起进行传输。"
    voice v3
    c "所以让零子达到光速运动是很简单的。"
    voice v3
    c "更高维度的时间流速更慢。也就是说如果在更高维度里注入零子并让其进行光速运动。"
    voice v5
    c "速度越快时间流速越慢。那么如果在原本时间就为零或者原本时间就为负数的维度继续光速运动，时间流速就会继续减慢，也就是会变为负数。"
    voice v3
    c "而更高维度时间的流速相对于我们所处的维度的时间流速而言。是负的。"
    voice v5
    c "所以零子在更高维度光速运动以后，再瞬间将零子抽出回到我们所处的维度。所回到的我们所在的维度，时间就是负的，也就是所谓的回到过去。"
    voice v3
    c "但是整个过程中抽出的操作都必须在更高维度那一侧完成。也就是说要在更高维度内让零子自己抽出自己才行。"
    voice v3
    c "嗯......如果要让我再做一个比喻的话......"
    voice v3
    c "你可以理解成，我们所处纬度是一辆轿车，更高那层维度则是一辆货车..."
    hide zicheng_pose2
    show zicheng_pose1 mono mouth5 other1 at jin
    play audio odoro
    with vpunch
    voice v3
    c "啊对不起......揭起你的伤疤了...我换一个比喻..."
    l "啊没事的......你继续说就行了..."
    hide zicheng_pose1
    show zicheng_pose2 mono mouth3 at jin
    with dissolve
    voice v3
    c "那好吧林洛，我继续了。"
    scene bg_car
    with dissolve
    c "货车和轿车上都分别托运的有一个足球。从同一起点开动的话。轿车的速度就当作我们所处纬度的时间流速。"
    l "货车的速度就相当于更高维度的时间流速对吧！"
    "不自觉地就说出口了。"
    c "厉害！都学会抢答了。"
    scene bg_car2
    with dissolve
    c "所以正常情况下，两辆车同时开动的话，轿车会跑到货车前面。轿车的路辙就相当于流逝的时间。"
    c "车上托运的足球就相当于是在光速运动的零子。"
    c "在跑得慢的货车上将足球丢到轿车的路辙上面。这时候这个足球就到达了轿车流逝的时间上去了。"
    c "足球在被卡车丢进轿车的路辙的那一刻，足球就已经抵达了相对于轿车而言的过去。"
    c "也就是说，我们要开发的可以将自身转换成零子进行光速运动并且可以自己还原成原状的时间机器。从被更高维度丢进我们所处纬度的流逝的时间上的那一刻，时间机器就已经抵达了过去。"
    c "在跑得快的轿车上面将足球丢到货车那条道上面，因为货车还没有移动到这个位置，所以足球会处于未来的时间。"
    l "但是这样的话足球只会处于相对于更高维度而言才是未来的时间啊！"
    l "这样的话将货车这条道上的球不管什么时候重新丢回去，都只会丢在轿车的路辙上面吧！"
    c "是的。因为父亲并没有试验过，也无法验证在更高维度那端抽出零子能不能控制零子抽出的方向。"
    c "也就是不知道能否控制在货车上把足球斜方向丢到轿车的前面去。"
    c "但是只要能回到过去就已经够了。"
    l "既然更高维度时间流速是更慢的。那只需要注入并抽出零子，就可以回到相对而言的过去吧。为什么必须要光速运动呢？"
    c "我看你，完全是不懂呢~！"
    c "确实，哪怕不进行光速运动。只要零子注入更高维度，并在更高维度那一侧自己控制抽出到我们所处的维度。就可以直接回到过去。"
    c "但是这样的可以回到的过去的时间是不可控的。甚至可以说是只能固定回到某个时间段。但是如果进行光速运动的话。"
    c "就能找准时机不断拉开高纬度和我们所处维度的时间差距，然后实现精准地控制时间的回溯位置。"
    scene bg_byouin
    show zicheng_pose2 mono at jin
    with dissolve
    l "但是怎么注入和抽出零子呢？"
    l "只有时间刻校正仪可以做到。但是机器已经被抢走了。"
    voice v1
    c "我当然也考虑到了。"
    voice v3
    c "既然时间刻校正仪是在父亲的研究所创造出来的。"
    voice v3
    c "那总会找到制作数据和原材料的！"
    voice v3
    c "总而言之，我需要制造出能连带着使用者一起被转换成零子注入更高维度。"
    voice v5
    c "经过光速运动以后能够从更高维度抽出，回到我们所在维度的仪器。也就是符合我父亲理论的时间机器。"
    voice v3
    c "前面我所说的对抗AADR并不是在现在对抗，而是回到过去对抗。"
    voice v1
    c "概括而言则是："
    voice v3
    c "阻止AADR拿到关于我父亲的研究数据！"
    hide zicheng_pose2
    show zicheng_pose1 mono eyes2 mouth4 at jin
    with dissolve
    voice v3
    c "我只能想到这个方法了！林洛！你愿意帮我吗？"
    voice v3
    c "即便这个过程可能很漫长！"
    voice v3
    c "即便AADR可能会出面干扰。随时可能失败。"
    voice v1
    c "但是我必须去做！"
    voice v3
    c "现在去对抗AADR是没用的。时间刻校正仪已经不知道被转移到了什么地方。"
    voice v3
    c "而且AADR在全世界都有分部，个人之力想撼动AADR这座大山难如登天！"
    nvle "事到如今，能够拯救覃可汐的方法似乎只有这一个了。"
    nvle "本以为永远陨落的覃可汐的灵魂，如今有了死而复生的机会。"
    nvle "这就当作是我的赎罪吧！"
    nvl clear
    l "我愿意帮你！！不仅是为了覃可汐，也是为了整个沁野市，整个世界的存亡！"
    show zicheng_pose1 mono eyes2 mouth1 at jin
    with dissolve
    voice v1
    c "好！！！"
    scene bg_zicheng_te2
    with dissolve
    $ persistent.cg16_unlocked = True
    "叶梓澄激动地握住了我的手。"
    show noko
    with dissolve
    "自那一天起。我和叶梓澄默默走上了对抗AADR之路。"
    scene bg_none
    with fade2
    play music "music/title2.ogg" fadeout 1.0 fadein 1.0
    "我和叶梓澄离开了沁野市，隐居到了一个没有受到AADR的时间刻校正仪干涉的地方。靠着叶梓澄父亲留下的研究数据和笔记。"
    "开始了漫长的时间机器的研究。"
    scene bg_none
    with fade2
    play music sora fadeout 1.0 fadein 1.0
    "........"
    "........"
    "........"
    "一晃十年过去了。"
    "当年和叶梓澄许下的诺言，如今却趋近于失败的边缘......"
    "还在测试阶段的时间机器的研究，终于是被AADR发现了。"
    "叶梓澄本打算跟我一起乘坐时间机器回到过去的。但是这个愿望无法实现了。"
    "只能用还只能乘坐一个人的时间机器把我送到了过去。叶梓澄用自己的生命为我争取了机器启动的时间。"
    "勉强回到了2022年9月16号。"
    "但是我还不能放弃。即便我只能撑着轮椅。"
    "即便时间机器的能源已经不足以继续使用。"
    "即便时间机器只能单向回到过去。"
    "我不能放弃。"
    "咳！咳！"
    "受半成品的时间机器影响，我开始吐血了。"
    "我......"
    "即便好不容易回到了这里。回到了2022年。"
    "我能活着阻止AADR吗？"
    "对不起......叶梓澄......看来失败了呢......任务....."
    "等等!我想起来什么。"
    "我在时间机器内找了找。"
    $ persistent.tips47 = True
    "找到了！早期测试零子传输功能的手表。可以把大脑中{a=showmenu:tips47}{color=#F18D7D}海马体{/color}{/a}内存储的信息拷贝成零子并进行传输。"
#词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    scene bg_schoolmae
    with fade2
    play music richang fadeout 1.0 fadein 1.0
    "我开始在曾经的学校门口搭建摊位。这是最好的能将手表交给过去的我的方式了。"
    "过去的我一定会来这个地方。到时候我便将手表交还给他......"
    $ persistent.tips48 = True
    "至于{a=showmenu:tips48}{color=#F18D7D}时间悖论{/color}{/a}.......我回到过去的一瞬间，就已经是过去的一部分了。"
#词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    scene bg_schoolmae
    with fade2
    "不知等了多少天......终于等到了！"
    "我看着过去的我，下了公交车，向着我所在的方向走来。"
    show linluo_pose at jin:
        zoom 0.8
    with dissolve
    play music sora fadeout 1.0 fadein 1.0
    "我那个时候真好啊~"
    "年轻中透着稚嫩。充满朝气和光明的未来。"
    "只不过......这光明的未来得由你自己的双手来创造了！"
    play sound run
    show linluo_pose at jin
    with dissolve
    "在他靠近的一刻，我抓住了他的手。"
    "用我仅剩的一点力气......抓住了他的手。"
    show linluo_pose eyes2 mouth1 other1 other2 at jin
    play audio odoro
    with vpunch
    voice v1
    l "{size=50}呃！~~{/size}"
    "意料之中的叫出了声。"
    "但是我不能松手。"
    voice v1
    l "{size=50}呃啊~~{/size}"
    voice v1
    l "你想干什么？"
    show hold_watch:
      xcenter 0.2
      ycenter 0.3
    with dissolve
    "我抬起了另一只手，手里紧紧握着手表。握着凝聚着叶梓澄的血与汗的，对抗AADR的唯一的救命稻草。"
    "这块手表送你了。戴上吧。"
    "用着剩余的力气说道。每一个字都很吃力。"
    "或许我真的命不久矣了。原本就身体残疾，再加上没日没夜开发时间机器，以及半成品时间机器的副作用。"
    "过去的我还在犹豫......"
    show linluo_pose at jin
    with dissolve
    voice v1
    l "谢谢！"
    hide hold_watch
    with dissolve
    hide linluo_pose
    show linluo_pose pose2 mono2 other2 at jin
    with dissolve
    voice v3
    l "老板这表多少钱？"
    "太好了......"
    "不需要钱。只是，希望你能，一直，戴着它。"
    hide linluo_pose
    with dissolve
    play sound "audio/run.ogg"
    "已经准备离开了吗......"
    with vpunch
    "等等！"
    "还不可以！"
    show linluo_pose mono1 eyes2 mouth1 other1 other2 at jin
    play audio odoro
    with vpunch
    "我又上前抓住了他的手。"
    "去找叶梓澄！"
    "这是我最后的提示了。也是我最后能说出口的几个字了。"
    show linluo_pose pose2 mono2 eyes2 mouth1 other2 at jin
    with dissolve
    voice v3
    l "叶梓澄......我认识他吗？"
    "以后你会认识的。"
    "我松开了手。并示意让他快点进学校。"
    hide linluo_pose
    with dissolve
    play music "music/title.ogg" fadeout 1.0 fadein 1.0
    "手表的功能...你以后就会知道的..."
    "检测到心脏停跳以后就会启动程序，把拷贝的记忆的零子，通过我所乘坐的时间机器内的注入功能，传输到过去的自己身上的："
    "回到过去的手表！"
    "对不住了。过去的我自己。"
    "接下来的你可能会面临各种各样的苦难。"
    "但是你一定要坚持下来！"
    "不仅是为了你自己！更是为了打破AADR在未来的残暴统治！"
    "就这样吧。"
    $ config.allow_skipping = False
    "准备收摊了，去哪都无所谓。死了也无所谓。如果过去的我真的改变了时间的轨迹，那我大概率会被再构成掉吧......"
    $ end = 1
    hide screen quick_menu_full
    $ quick_menu = False
    $ quick_menu_full_= False
    play music "music/end.ogg" fadeout 1.0 fadein 1.0
    call disable_shortcut from _call_disable_shortcut_1
    scene bg_none
    show end1
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
    call enable_shortcut from _call_enable_shortcut_1
    $ config.allow_skipping = True
    return