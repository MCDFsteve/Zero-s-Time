label loop1_false:
    stop sound
    hide screen watch_loop1
    show screen watch
    with vpunch
    "果然还是不行！"
    $ times = "12:54"
    "让我主动，抹除这几天的珍贵时光，我反而做不到了。"
    "而且这次需要做的事情的风险...一旦我失误了......"
    "可能会再也没有翻身的机会了......"
    voice v3
    c "林洛？你把记忆发送回过去了吗已经？"
    $ times = "12:55"
    l "嗯，发送了。"
    nvle "但是这是我的谎言。"
    nvl clear
    voice v3
    c "那这个世界，似乎并没有发生变化。"
    hide zicheng_pose2
    show zicheng_pose1 eyes7 at jin
    with dissolve
    voice v3
    c "难道确确实实，是平行世界吗？"
    l "是吧。"
    nvle "撒谎也无所谓了，经过这几次的不断重复时间，我也累了。"
    nvle "会有其他的拯救覃可汐的办法的。"
    nvl clear
    scene bg_zicheng_naku
    with dissolve
    "叶梓澄终于忍受不住，跪地痛哭了起来。"
    c "呜呜呜~"
    c "所以.....我们所做的一切,都是徒劳的吗?"
    c "不会对我们现在这个世界产生任何影响......"
    nvle "我觉得我得说点什么。"
    nvl clear
    l "叶梓澄......"
    l "会有其他办法的......最坏的那个未来，现在还没有发生不是吗？"
    l "至少我觉得，我们还可以拯救覃可汐。"
    scene bg_2_3
    with dissolve
    show zicheng_pose1 eyes2 mouth5 at jin
    with dissolve
    voice v1
    c "怎么救？"
    l "..............."
    l "................"
    l "带着覃可汐，离开沁野市吧！"
    $ times = "12:57"
    hide zicheng_pose1
    show zicheng_pose1 eyes6 mouth3 at jin
    with dissolve
    c "........."
    hide zicheng_pose1
    show zicheng_pose1 eyes7 mouth3 at jin
    with dissolve
    voice v3
    c "在目前的处境，能做的确实只有这件事了。"
    voice v3
    c "那，带覃可汐去哪呢？"
    l "去一个，没有纷争，远离喧嚣的地方吧~至少这个地方不会被AADR注意到！"
    l "对这个城市的其他人来说，还存在应对灾难的机会。但是对覃可汐来说，+1时间刻维度的干涉一旦产生，就会因为干涉而死去。"
    l "所以优先保障覃可汐的安全吧！"
    hide screen watch
    with dissolve
    scene bg_none
    with fade
    "就这样，我和叶梓澄约好了，和她放学后在校门口会合。带着覃可汐一起。"
    $ times = "17:41"
    show screen watch
    with dissolve
    play music kexi fadein 1.0 fadeout 1.0
    scene bg_schoolmae yubi
    with fade
    "下午到了。"
    show zicheng_pose2 mono eyes2 mouth1 other2 at jin:
        xcenter 0.3
    with dissolve
    show zicheng2_shadow at jin:
        xcenter 0.3
    show kexi_pose2 mono mouth1 at jin:
        xcenter 0.6
    with dissolve
    $ times = "17:43"
    voice v3
    x "喂！叶梓澄！林洛！把我叫出来，是继续讨论小说的构思和剧本吗？"
    with vpunch
    l "覃可汐你听我说！"
    play sound odoro
    scene bg_kexi_hazukashii
    with vpunch
    "我搭上了覃可汐的肩，用郑重的口气说道。"
    play music lanzhu fadein 1.0 fadeout 1.0
    with vpunch
    x "啊！~"
    "覃可汐被我突如其来的的举动吓得不轻。"
    x "林洛...这.....不合适吧...其他学生在看着呢..."
    play sound odoro
    with vpunch
    l "跟我一起离开沁野市吧！"
    play sound odoro
    with vpunch
    x "啊！！！"
    play sound odoro
    with vpunch
    x "啊？？？"
    x "你......你是认真的？"
    x "这算是表白吗？"
    x "班长.....这是怎么回事？"
    c "覃可汐，跟我们离开吧，详细的事情我们以后再告诉你。"
    x "嗯.....我是不是得先问问我爸妈?"
    c "我觉得你父母不会同意的!所以!现在走吧!"
    x "嗯.....额......"
    play music kexi fadein 1.0 fadeout 1.0
    scene bg_schoolmae yubi 
    with dissolve
    show kexi_pose mono eyes4 mouth3 at jin:
        xcenter 0.6
    with dissolve
    show zicheng_pose2 mono at jin:
        xcenter 0.3
    with dissolve
    show zicheng2_shadow at jin:
        xcenter 0.3
    voice v3
    x "既然叶梓澄也在的话......那我就先听你们的吧......"
    hide kexi_pose
    show kexi_pose mono eyes4 mouth1 at jin:
        xcenter 0.6
    with dissolve
    voice v3
    x "但是叶梓澄...林洛...你们脸色都不是很好啊......果然是出了什么事吗？"
    voice v3
    x "或许我可以帮忙解决呢？嗯？"
    $ times = "17:45"
    voice v3
    x "说出来吧！藏在心里也很不好过吧~"
    show kexi1_shadow at jin:
        xcenter 0.6
    hide zicheng2_shadow
    hide zicheng_pose2
    show zicheng_pose1 mono eyes4 mouth4 at jin:
        xcenter 0.3
    with dissolve
    show kexi1_shadow at jin:
        xcenter 0.6
    voice v3
    c "对不起.....覃可汐......"
    voice v3
    c "如果继续呆在沁野市的话......你会死掉的！"
    hide kexi1_shadow
    show zicheng1_shadow at jin:
        xcenter 0.3
    hide kexi_pose
    show kexi_pose mono at jin:
        xcenter 0.6
    play sound odoro
    with vpunch
    voice v3
    x "啊？"
    voice v3
    x "我会死掉吗......"
    hide kexi_pose
    show kexi_pose mono eyes4 mouth3 at jin:
        xcenter 0.6
    with dissolve
    voice v3
    x "今天是愚人节吗？"
    x "................"
    x "...................."
    x "................."
    hide kexi_pose
    show kexi_pose mono mouth1 at jin:
        xcenter 0.6
    with dissolve
    play music sora fadein 1.0 fadeout 1.0
    voice v3
    x "但是我相信你的话哟！叶梓澄！"
    voice v3
    x "毕竟你是叶梓澄嘛！"
    hide zicheng1_shadow
    show kexi1_shadow at jin:
        xcenter 0.6
    hide zicheng_pose1
    show zicheng_pose1 mono eyes4 mouth1 at jin:
        xcenter 0.3
    with dissolve
    voice v3
    c "所以跟我们一起离开吧！"
    hide zicheng_pose1
    show zicheng_pose1 mono eyes3 mouth1 at jin:
        xcenter 0.3
    with dissolve
    voice v3
    c "到一个，你不会死掉的地方去！"
    hide kexi1_shadow
    show zicheng1_shadow at jin:
        xcenter 0.3
    voice v3
    x "好吧......但是详细的事情一定要跟我讲清楚哦！叶梓澄！"
    voice v3
    x "因为我相信你！不会做对不起我的事的！"
    voice v3
    x "所以......不要再哭了好吗？"
    hide zicheng1_shadow
    show kexi1_shadow at jin:
        xcenter 0.6
    hide zicheng_pose1
    show zicheng_pose1 mono eyes4 mouth1 at jin:
        xcenter 0.3
    with dissolve
    voice v1
    c "嗯........"
    play music title2 fadein 1.0 fadeout 1.0
    voice v3
    c "林洛！选好目的地了吗？"
    l "还没，第一步先出沁野市吧！"
    voice v3
    c "那我去拿我父亲的研究笔记？"
    $ times = "17:47"
    l "不用了....吧......."
    l "有什么意义呢？"
    voice v3
    c "也对.........."
    l "但是现在距离星期五....还有段时间。"
    l "先回家各自收拾东西吧！"
    voice v1
    c "嗯......"
    play music kexi fadein 1.0 fadeout 1.0
    hide kexi1_shadow
    show zicheng1_shadow at jin:
        xcenter 0.3
    hide kexi_pose
    show kexi_pose mono mouth1 at jin:
        xcenter 0.6
    play sound odoro
    with vpunch
    voice v3
    x "啊？收拾东西...么？"
    hide kexi_pose
    show kexi_pose2 mono mouth4 at jin:
        xcenter 0.6
    with dissolve
    voice v3
    x "那我会尽量偷偷收拾的......"
    x "......................"
    hide kexi_pose2
    show kexi_pose mono eyes4 at jin:
        xcenter 0.6
    with dissolve
    voice v3
    x "那我们什么时候再回来？"
    hide zicheng1_shadow
    show kexi1_shadow at jin:
        xcenter 0.6
    hide zicheng_pose1
    show zicheng_pose1 mono eyes3 at jin:
        xcenter 0.3
    with dissolve
    voice v3
    c "覃可汐......"
    voice v3
    c "我们不会再回来了......"
    hide kexi1_shadow
    show zicheng1_shadow at jin:
        xcenter 0.3
    hide kexi_pose
    play sound odoro
    show kexi_pose mono at jin:
        xcenter 0.6
        yoffset 0
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset -50
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset 0
    with vpunch
    voice v1
    x "啊？"
    play music sora fadein 1.0 fadeout 1.0
    hide kexi_pose
    show kexi_pose mono eyes3 at jin:
        xcenter 0.6
    with dissolve
    "覃可汐的脸黑了下来，露出了沮丧的神情。"
    voice v3
    x "果然我还是......舍不得我爸妈......"
    hide kexi_pose
    show kexi_pose mono eyes5 at jin:
        xcenter 0.6
    with dissolve
    voice v1
    x "我......"
    hide zicheng1_shadow
    show kexi1_shadow at jin:
        xcenter 0.6
    hide zicheng_pose1
    show zicheng_pose1 mono eyes4 mouth1 at jin:
        xcenter 0.3
    with dissolve
    voice v3
    c "今天先回家吧！"
    $ times = "17:49"
    voice v3
    c "覃可汐！以后还会回来的！真的！"
    hide zicheng_pose1
    show zicheng_pose1 mono eyes4 mouth3 at jin:
        xcenter 0.3
    with dissolve
    voice v1
    c "很快的！"
    hide kexi1_shadow
    show zicheng1_shadow at jin:
        xcenter 0.3
    voice v1
    x "嗯......"
    hide screen watch
    with dissolve
    scene bg_none
    with fade2
    ".................."
    "分别覃可汐和叶梓澄以后，我乘上了回家的公交车。"
    nvle "对不起了.......叶梓澄.......请允许我任性一次......"
    nvle"15天......手表传送记忆的期限是15天......"
    nvle"15天之后,我就会继续我的任务。"
    nvl clear
    nvle"所以请允许我，在这十五天内得到短暂的休息吧。"
    nvl clear
    $ times = "18:02"
    show screen watch
    with dissolve
    play sound car_stop
    play music kexi fadein 1.0 fadeout 1.0
    scene bg_kuruma_matu
    with fade
    "到站了。"
    stop sound
    with vpunch
    l "呜~~~！"
    play music lanzhu fadein 1.0 fadeout 1.0
    with vpunch
    "是什么！！"
    nvle "公交车刚刚走远，就感觉有人勒住了我的脖子。"
    nvle "从我的背后。"
    nvl clear
    with vpunch
    l "是谁！！"
    nvle "我本来打算呼喊，但是嘴里被一块布堵住了。"
    scene bg_none
    with fade
    nvle "身体也变得昏昏沉沉......眼睛也快睁不开了......"
    nvle "糟了............"
    nvl clear
    hide screen watch
    with dissolve
    nvle "........."
    nvl clear
    play music home fadein 1.0 fadeout 1.0
    scene bg_none
    with fade2
    with vpunch
    "额....."
    with vpunch
    "啊!这是哪儿？"
    scene bg_kousoku
    show eye
    $ renpy.pause(2.7, hard=True)
    hide eye
    with dissolve
    "我睁开双眼，仔细端详着周围的一切。"
    "发现自己被关在了牢笼里。"
    play sound odoro
    with vpunch
    l "额！"
    "不止是我，叶梓澄和覃可汐也......"
    "她们还昏迷着。"
    scene bg_kousoku2
    with fade2
    "过了十几分钟，叶梓澄和覃可汐醒过来了。"
    "在这之前我确实有想过手动叫醒她们，但是我身体却不愿意这样做。"
    c "嗯.......嗯？"
    c "这是？"
    x "这是？"
    show zicheng_pose1 eyes7 at jin:
        xcenter 0.3
    with dissolve
    show kexi_pose eyes4 at jin:
        xcenter 0.6
    with dissolve
    l "醒了吗？我们好像被什么人给囚禁起来了。"
    show zicheng1_shadow at jin:
        xcenter 0.3
    hide kexi_pose
    play sound odoro
    show kexi_pose eyes3 mouth3 at jin:
        xcenter 0.6
        yoffset 0
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset -50
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset 0
    with vpunch
    voice v3
    x "啊......这是什么play？"
    l "我说的是正经事！"
    play music speak fadein 1.0 fadeout 1.0
    l "我也和你们一样，被什么人给弄晕了，醒来之后就到了这里。"
    hide zicheng1_shadow
    show kexi1_shadow at jin:
        xcenter 0.6
    hide zicheng_pose1
    show zicheng_pose2 at jin:
        xcenter 0.3
    with dissolve
    voice v3
    c "这么说我也是，我还走在路上，突然就....."
    hide kexi1_shadow
    show zicheng2_shadow at jin:
        xcenter 0.3
    hide kexi_pose
    show kexi_pose eyes5 mouth3 at jin:
        xcenter 0.6
    with dissolve
    voice v3
    x "我也是。当时想着完蛋了，遇到尾随痴汉了。"
    hide zicheng2_shadow
    show kexi1_shadow at jin:
        xcenter 0.6
    hide zicheng_pose2
    show zicheng_pose2 eyes2 mouth1 other1 at jin:
        xcenter 0.3
    with dissolve
    voice v3
    c "所以是谁，为什么要这么做？"
    play music ruins fadein 1.0 fadeout 1.0
    scene bg_kousoku2
    with dissolve
    "铁栅栏外面是昏暗的走道，尽头慢慢没入黑暗，什么都看不到。"
    show zicheng_pose2 at jin
    with dissolve
    voice v3
    c "现在几点了？"
    l "不清楚！"
    l "我身上的手机，还有我手上戴的手表，全都不见了。"
    hide zicheng_pose2
    play sound odoro
    show zicheng_pose2 eyes2 mouth3 other1 at jin
    with vpunch
    voice v3
    c "啊！我的手机也不见了！"
    hide zicheng_pose2
    show zicheng_pose2 mouth3 at jin:
        xcenter 0.3
    with dissolve
    show zicheng2_shadow at jin:
        xcenter 0.3
    play sound odoro
    show kexi_pose2 at jin:
        xcenter 0.6
        yoffset 0
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset -50
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset 0
    with vpunch
    voice v1
    x "我也是！"
    nvle "这是一个非常糟糕的消息。我的手表被拿走了。"
    nvle "呃啊！开始后悔之前没有早点做出决策。"
    nvl clear
    scene bg_kousoku2
    with fade2
    play sound run
    "过了一会，外面有人走了过来。"
    show npc1
    with dissolve
    nan "叶梓澄！还有，两位关系人。"
    nan "林.....洛......还有....覃可汐..."
    hide npc1
    with dissolve
    play music lanzhu fadein 1.0 fadeout 1.0
    show zicheng_pose2 mouth1 other2 at jin
    with dissolve
    voice v3
    c "你是谁？为什么把我们关在这里？"
    hide zicheng_pose2
    with dissolve
    show npc1
    with dissolve
    nan "这也是没有办法的事情。"
    nan "谁让你继续调查你父母的事情的！已经快触及我们的红线了。"
    hide npc1
    with dissolve
    show zicheng_pose2 mouth1 other2 at jin
    with dissolve
    voice v3
    c "果然是AADR吗？"
    hide zicheng_pose2
    with dissolve
    play sound odoro
    show kexi_pose eyes4 at jin
    with vpunch
    voice v3
    x "啊？什么AADR？你们在说什么？"
    nvle "只有覃可汐还在一头雾水。"
    nvl clear
    hide kexi_pose
    with dissolve
    show zicheng_pose2 mouth1 other2 at jin
    with vpunch
    voice v3
    c "为什么把林洛和覃可汐卷进来？"
    hide zicheng_pose2
    with dissolve
    show npc1
    with dissolve
    nan "因为你让他们也知道了不该知道的事情！"
    nan "本来组织里为了减少社会舆论，低调行动，是不打算处理掉你的！"
    nan "毕竟多亏了你父亲，我们得到了最想得到的东西。"
    nan "但现在我们不得不这样做了！"
    hide npc1
    with dissolve
    show zicheng_pose2 mouth1 other2 at jin
    with dissolve
    voice v3
    c "把我们关在这里对你们有什么好处吗？"
    hide zicheng_pose2
    with dissolve
    play sound odoro
    show npc1
    with vpunch
    nan "哈哈哈哈哈哈~"
    play sound odoro
    with vpunch
    nan "好处......放任你们留在外面就是对我们的坏处！"
    nan "虽然你们的行动根本不会对我们产生一分一毫的影响。"
    nan "但是上头说了，尽量防患于未然，所以必须处理掉你们。"
    nan "你们放心吧！我们会把你们伪装成失踪的！"
    hide npc1
    with dissolve
    play sound odoro
    show zicheng_pose2 eyes2 mouth1 other2 at jin:
        yoffset 0
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset -50
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset 0
    with vpunch
    voice v3
    c "你们把我父亲怎么了？"
    hide zicheng_pose2
    with dissolve
    play sound odoro
    show npc1
    with vpunch
    nan "你的父亲？已经变成了他自己的研究的实验品了！"
    play sound odoro
    with vpunch
    nan "不过你们也马上要步后尘了。"
    nan "我的话就只有这么多了。明天早上会把你们遣送到仪器所在的地方，乖乖成为实验品吧！"
    hide npc1
    with dissolve
    play sound odoro
    play music sora fadein 1.0 fadeout 1.0
    show zicheng_pose1 eyes2 mouth4 at jin:
        yoffset 0
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset -50
        linear 0.05 xoffset 0 yoffset -25
        linear 0.05 xoffset 0 yoffset 0
    with vpunch
    voice v3
    c "等等！覃可汐是无辜的！她什么都不知道！请放过她！"
    hide zicheng_pose1
    with dissolve
    show npc1
    with vpunch
    nan "啊？"
    play sound odoro
    with vpunch
    nan "开什么玩笑？放过她，然后出去以后好报警？"
    nan "虽然警察的事根本不算什么，但是只会给我们徒增麻烦。"
    play sound run
    hide npc1
    with dissolve
    nvle "看着这人离去的背影，我陷入了深深的自责。"
    nvle "我真的没想到，事情会发展成这样。"
    nvle "我只是打算......只是打算.......能多十几天和朋友在一起的时光啊！"
    nvl clear
    nvle "到底是哪里出了差错？"
    nvl clear
    play music ruins fadein 1.0 fadeout 1.0
    show zicheng_pose2 at jin
    with dissolve
    "叶梓澄还在缜密思考。"
    hide zicheng_pose2
    with dissolve
    show kexi_pose at jin:
        xcenter 0.6
    with dissolve
    voice v3
    x "这不是真的吧！？"
    hide kexi_pose
    show kexi_pose eyes3 at jin:
        xcenter 0.6
    with dissolve
    voice v3
    x "叶梓澄？林洛？现在可以告诉我了吗？"
    show zicheng_pose2 eyes2 mouth1 other2 at jin:
        xcenter 0.3
    with dissolve
    show kexi1_shadow at jin:
        xcenter 0.6
    play sound odoro
    with vpunch
    voice v3
    c "覃可汐你听我说，我们现在摊上麻烦了！"
    play sound odoro
    with vpunch
    voice v3
    c "这个AADR组织，是杀害我母亲和绑架我父亲的幕后黑手，更是会在未来杀掉你的杀人凶手！"
    hide kexi1_shadow
    show zicheng2_shadow at jin:
        xcenter 0.3
    hide kexi_pose
    show kexi_pose eyes5 at jin:
        xcenter 0.6
    with dissolve
    voice v3
    x "果然.....我会死掉的事情.....是真的呢......"
    voice v3
    x "所以是跟叶叔叔的事情有关吗？"
    l "叶叔叔？"
    voice v3
    x "就是叶梓澄的爸爸.......在我和叶梓澄还上小学的时候，叶叔叔就经常带我们出去玩......"
    voice v3
    x "虽然不知道你们是怎么知道的这么多的.....但是那我们现在该怎么办？"
    hide zicheng2_shadow
    show kexi1_shadow at jin:
        xcenter 0.6
    hide zicheng_pose2
    show zicheng_pose2 eyes2 at jin:
        xcenter 0.3
    with dissolve
    play music speak fadein 1.0 fadeout 1.0
    voice v3
    c "林洛！你觉得AADR为什么会打算对我们下手？"
    voice v3
    c "从你之前所经历的时间来看，AADR并没有干预我们的行动对吧！"
    with vpunch
    l "对！"
    voice v3
    c "那一定就是在这次的时间，我们做了什么引起AADR对我们提高警惕的事情。"
    voice v3
    c "如果那个人说的是真的，因为我们在调查我母亲的事情。"
    voice v3
    c "那是怎么泄露出去的呢？"
    voice v3
    c "AADR是怎么知道我在查呢？"
    voice v3
    c "难道说一直就在监视我的行动？"
    l "我觉得应该不是，如果一直在监控你的话！你怎么在未来造的出时间机器呢？"
    voice v3
    c "对！那可能是我们所走访过的人中有人通风报信？"
    voice v3
    c "还是说在课间我们讨论的时候......被AADR的人听到了？"
    hide kexi1_shadow
    show zicheng2_shadow at  jin:
        xcenter 0.3
    hide kexi_pose
    show kexi_pose2 at jin:
        xcenter 0.6
    with dissolve
    voice v3
    x "所以......林洛的构思的推理小说......都是真的？"
    hide zicheng2_shadow
    show kexi2_shadow at jin:
        xcenter 0.6
    hide zicheng_pose2
    show zicheng_pose2 other2 at jin:
        xcenter 0.3
    with dissolve
    voice v3
    c "是真的.......我们希望你可以帮忙寻找我母亲去世有关的线索。"
    voice v3
    c "但我怕直说的话你会对我有负罪感。"
    hide kexi2_shadow
    show zicheng2_shadow at jin:
        xcenter 0.3
    hide kexi_pose2
    show kexi_pose eyes5 at jin:
        xcenter 0.6
    voice v3
    x "叶梓澄.....我......"
    voice v3
    x "善意的谎言吗......"
    hide zicheng2_shadow
    show kexi1_shadow at jin:
        xcenter 0.6
    hide zicheng_pose2
    show zicheng_pose2 at jin:
        xcenter 0.3
    with dissolve
    voice v3
    c "我们走访过的人......"
    l "你去的警察局,还有我们一起去的,丁唯家,以及......"
    play sound odoro
    with vpunch
    play music title2 fadein 1.0 fadeout 1.0
    l "班主任的办公室!"
    l "喂!AADR的研究方向,是物理学科的吧!"
    voice v1
    c "嗯。"
    l "我们的班主任......是第一个发现案发现场并且目睹了行凶过程的人，并且......是物理老师！"
    l "在我最开始所经历过的时间里，还依稀记得在一节她的物理课上，她专门给我们介绍了AADR这个组织........."
    voice v3
    c "但是李老师她......"
    l "最近的AADR分部在芷柚市，班主任也亲口说过她是从芷柚市调过来的........."
    l "种种迹象似乎都指向对班主任不利的地位。"
    l "一起努力吧！想办法离开这里！"
    l "然后......"
    l "亲自对质！"
    scene bg_none
    with fade2
    stop music
    "............"
    "然而这一天并没有到来。"
    play music sora fadein 1.0 fadeout 1.0
    "没有逃跑的机会，就被注射药物，押送到了。"
    "将物质转换成零子的，零子转换机旁边！"
    "我在昏迷前听到的最后的声音，仿佛是我班主任发出来的。"
    s "我已经在学校方面给这三个学生汇报了失踪了。"
    s "还是老样子，至少得留点东西下来，就跟昨天处理叶付的结果差不多就行，留条胳膊什么的。"
    s "这样还能让家属死心。从而减少未来的阻碍。"
    play music omou fadein 1.0 fadeout 1.0
    "所以......是我和叶梓澄去她办公室的时候.......就把事情泄露给了AADR了......"
    "..............."
    play sound bilibili loop fadein 1.0 fadeout 1.0 
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
    stop sound
    "......................................................................................"
    $ end = 2
    $ quick_menu = False
    $ quick_menu_full_= False
    hide screen quick_menu_full
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
    $ quick_menu = True
    $ quick_menu_full_= True
    call enable_shortcut from _call_enable_shortcut_4
    return