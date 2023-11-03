label chapter5:
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
    $ renpy.pause(66, hard=True)
    $ quick_menu = True
    $ quick_menu_full_= True
    call enable_shortcut from _call_enable_shortcut_6
    play sound odoro
    with vpunch
    $ renpy.pause(5, hard=True)
    play sound odoro
    with vpunch
    $ renpy.pause(5, hard=True)
    play sound odoro
    with vpunch
    $ renpy.pause(5, hard=True)
    play sound odoro
    with vpunch
    $ renpy.pause(16, hard=True)
    $ persistent.chapter=5
    scene bg_none
    hide screen game_end
    $ quick_menu = False
    image chapter5 ="chapters/chapter5.webp"
    show chapter5
    with fade2
    $ renpy.pause(5, hard=False)
    hide chapter5
    with fade2
    scene bg_none
    $ quick_menu = True
    $ persistent.chapter5 = True
    $ persistent.extra_chapter5 = True
    $ save_name = "{font=Huayuan.Gothic.Bold.ttf}章节五：真正终点的寻觅{/font}"
    play music title2 fadein 1.0 fadeout 1.0
    scene bg_schoolmae yubi
    with fade2
    hide screen game_end
    with dissolve
    "！！！！"
    $ config.allow_skipping = True
    nvle "我现在除了惊讶还是惊讶。"
    nvl clear
    show zicheng_mirai_pose1 yubi at jin
    with dissolve
    nvle "面前这位穿着白大褂，顶着一头蓬松短发的中年女性，自称自己是来自十年后的叶梓澄。"
    nvle "但是有未来的自己的前车之鉴，我内心倒是深信不疑的。"
    nvle "但是既然又有未来人来到了现在，也就意味着未来......"
    nvl clear
    l "你........你真的是叶梓澄？"
    play sound odoro
    with vpunch
    voice v1
    c "没错！"
    l "那你.....你是回来.......救覃可汐的吗？"
    play sound odoro
    with vpunch
    voice v1
    c "没错！"
    nvle "我脸上的忧伤顿时没了踪迹，只觉得有一种劫后余生的高兴。"
    nvl clear
    "覃可汐并不是被神抛弃的孩子，而是被神眷顾的孩子才对。"
    play music speak fadein 1.0 fadeout 1.0
    l "又是AADR统治了世界吗？"
    hide zicheng_mirai_pose1
    show zicheng_mirai_pose1 eyes2 yubi at jin
    with dissolve
    voice v3
    c "没错！AADR的人在十年前，也就是今年，通过卧底调查的方式，获取到了我父母的研究项目，然后派人掠夺了我父母的研究成果。"
    voice v3
    c "还绑走了我的父母，强迫着给AADR干活。"
    voice v3
    c "不过我父亲在这一切发生之前，将改变这一切的办法写在了他的笔记本里面。"
    voice v3
    c "所以我和未来的你，一起通过我父亲的技术，制造出来了时间机器，为了改变过去。"
    l "跟我所经历过的过去，很相似......"
    voice v3
    c "未来的你告诉过我，这次的胜算是远大于，你所见过的更早的，未来的你自己的。"
    voice v1
    c "原因是："
    voice v3
    c "你在小巷里阻止了我母亲遇害，未来发生了改变。"
    l "既然未来发生了改变，那为什么.......为什么覃可汐还是会死.......？"
    voice v3
    c "因为一直有AADR的人在调查我父母的事情，AADR一开始就怀疑到了我父母，只不过是一直在找实际证据。"
    voice v3
    c "证明我父母研究项目为零子相关的证据。"
    l "卧底......是我现在的班主任吗？她一直在调查着你父母？"
    play sound odoro
    with vpunch
    l "是她！！"
    l "那回到过去阻止她不就好了？"
    play sound odoro
    with vpunch
    voice v5
    c "没有用的！这只会让AADR更加怀疑，即便抹除了她跟AADR的关系，AADR也只会派一个新的人过来，说到底她就不是整起事件的关键诱因。"
    l "................"
    l "也就是说，AADR夺走你父亲的研究成果和时间刻校正仪.......只是早晚的事吗？"
    voice v1
    c "没错........."
    l "所以覃可汐.....也是早晚会受到时间刻校正仪的干涉而死去......"
    l "那我之前所做的.....甚至包括那个半身不遂的未来的我和已经死去的你.......所做的都是徒劳的吗？"
    l "一开始就弄错了目标......"
    l "就算弄对了目标，又有什么作用呢？靠半成品时间机器？"
    play sound odoro
    with vpunch
    voice v5
    c "不是徒劳的！至少给未来的我和你争取到了足够的时间做出新的时间机器，而且我父母也没有因此死去，只是被囚禁了而已！！"
    l "是吗？"
    l "不过你都回到现在了.......肯定有对付AADR的新的办法吧！"
    play sound odoro
    with vpunch
    voice v1
    c "当然！！"
    voice v1
    c "我们这次需要："
    voice v3
    c "毁掉时间刻校正仪！！"
    l "？？？！！！"
    play music title2 fadein 1.0 fadeout 1.0
    voice v3
    c "时间刻校正仪就是未来一切不幸的开始。"
    voice v3
    c "没有了这个罪恶的仪器，未来AADR就不可能会统治的了人类了....."
    l "但是时间刻校正仪.....应该算是AADR掠夺研究所的意外发现吧......如果毁掉了时间刻校正仪......AADR会放过你父亲吗？"
    voice v3
    c "大概率不会....但是这个结果也比AADR使用时间刻校正仪奴役全人类.....要好得多！"
    l "这次又只有你一个人吗？也就是说....未来的我........已经......"
    play sound odoro
    with vpunch
    voice v3
    c "并不是！！未来的你也在！"
    l "在哪？"
    voice v3
    c "跟我去时间机器那里就知道了！"
    l "也就是说，这次的时间机器研究的很成功吗？"
    play sound odoro
    with vpunch
    voice v1
    c "没错。"
    l "不过既然是毁掉时间刻校正仪，有你们两个人就足够了吧！！为什么要带上我呢？"
    voice v3
    c "这其实是未来的你的主意。多一个帮手总归更好。不过决定权在你手里！"
    voice v3
    c "你可以选择去，也可以选择继续留在这里。"
    play music sora fadein 1.0 fadeout 1.0
    l "如果我不去的话，你们成功破坏时间刻校正仪以后，我会怎么样？"
    voice v3
    c "会被再构成掉，你所经历过的有关覃可汐的死，和你所拯救覃可汐的记忆，都会就此消失。"
    voice v3
    c "但是你会变成一个无忧无虑享受和平生活的，普普通通的高中生。"
    nvle "........................"
    nvl clear
    l "让我忘掉这一切.........怎么可能做的到........"
    l "即便我经历的事件里，又苦涩又悲痛，但是也有令人珍惜的......只有我一个人还记得过的，美好回忆......"
    play sound odoro
    with vpunch
    l "我跟你一起去！！！"
    play sound odoro
    with vpunch
    l "最后再为这个世界.......以及为阻止覃可汐的死亡........阻止叶梓澄的悲伤..............再努力一次！！！"
    play music title2 fadein 1.0 fadeout 1.0 
    play sound odoro
    with vpunch
    voice v3
    c "好！！！就等你这句话！！！"
    play sound odoro
    with vpunch
    voice v1
    c "走吧！！！"
    play music speak fadein 1.0 fadeout 1.0
    l "但是.........如果成功毁掉了时间刻校正仪.....那你和未来的我.....会怎么样？"
    voice v3
    c "到时候再看情况吧........"
    play music kexi fadein 1.0 fadeout 1.0
    voice v3
    c "可能是留在这个时代，作为不同于原本的我们，作为新的身份生活下去。"
    voice v3
    c "也可能乘坐时间机器回到属于我们的时代，只不过那时候，未来应该已经大变样了。"
    voice v5
    c "你说，我们破坏了时间刻校正仪以后再回到未来，因为未来没有时间刻校正仪相关的技术，所以没有造出时间机器，那我们所乘坐的时间机器。"
    voice v3
    c "是算未来人的科技呢？还是算过去人的科技呢？"
    l "啊！头大了，很难给出一个结论.......要长脑子了......"
    voice v5
    c "哈哈！只是随便说说而已！毕竟未来什么样，得等到未来才知道不是嘛！比起时刻关心未来的事情，不如好好抉择自己的现在，如何行动才会让自己到达自己想要的未来不是吗？"
    with vpunch
    l "非常同意。"
    play sound odoro
    with vpunch
    voice v3
    c "那.....走吧！！"
    l "步行吗？"
    voice v3
    c "真是抱歉......没有这个时代的货币，所以打不了车......"
    l "难道未来AADR把货币也换掉了吗？"
    voice v3
    c "嗯......全球统一一种货币。"
    scene bg_none
    with fade2
    nvle ".................."
    nvl clear
    scene bg_taimumashin
    with fade2
    play music kexi fadein 1.0 fadeout 1.0
    play sound higurashi loop
    l "呼！呼~"
    "不知道走了多久。终于到了目的地。"
    c "到了！"
    "没想到时间机器是停放在一座山的半山腰的树林里的。"
    "而且恰好这山还是叶梓澄父亲研究所的那座，离研究所也不远。"
    "只见树林之中砸入着一个巨大的铁球，铁球正前方展开了一个阶梯，通向球体内部的空间。"
    "见我们来了，铁球里有人伸出了头。"
    play sound odoro
    with vpunch
    "是未来的我！"
    with vpunch
    l "额！！"
    nvle "虽然面相很熟悉，但是这气色还有精气神，跟我最开始所见的未来的我，完全不一样。"
    nvle "这也是多亏了我改变了未来吗？"
    nvl clear
    play sound run
    "未来的我看着我，从铁球里走了出来。"
    show linluo_mirai
    with dissolve
    voice v3
    l "果然是来了吗？不过这也是我意料之中的事情。毕竟我自己是最懂我自己的嘛！"
    l "你好！未来的我！"
    voice v3
    l "你好！过去的我！"
    l "你真的是来自十年后的我自己吗？"
    play music speak fadein 1.0 fadeout 1.0
    voice v3
    l "真的不能在真了。"
    voice v5
    l "我！是！你不断循环时间试图救出覃可汐，到救了叶梓澄母亲以后，到发现覃可汐还是会死掉的这个事实，然后决心造出时间机器改变这一切的，十年后的你！！"
    voice v3
    l "也就是说，我拥有从你在校门口见到未来的叶梓澄之前的全部的记忆！"
    voice v3
    l "如果说你之前见到的坐着轮椅的，是过去的未来的你的话，那我就是："
    play sound odoro
    with vpunch
    voice v3
    l "现在的未来的你！是你本人的未来！！"
    voice v3
    l "说了这么多，来步入正题吧！"
    voice v3
    l "这就是时间机器！"
    hide linluo_mirai
    with dissolve
    show bg_taimumashin:
        xzoom 1.0  yzoom 1.0
        linear 1.0 xcenter 0.5 ycenter 0.65 xzoom 1.5 yzoom 1.5 
    nvle "我抬头看着，一个巨大的铁球，当然材料不一定是铁。内部是各种显示屏和操作按钮。"
    nvl clear
    l "这个时间机器的原理，也是叶梓澄父亲说过的那个吗？"
    scene bg_taimumashin
    with dissolve
    show linluo_mirai
    with dissolve
    voice v3
    l "对！跟时间刻校正仪的原理相同。或者不如说，这就是一个大号的可以穿越时间的时间刻校正仪。"
    l "那为什么AADR不把时间刻校正仪改造成时间机器呢？"
    voice v5
    l "因为叶梓澄父亲只把有关时间机器的理论写在了笔记本里，除此之外没有告诉任何人。AADR是不知道往+1时间刻维度注入的零子进行光速运动是可以回到过去的时间点的。"
    l "不过有个担忧。就算现在毁掉了时间刻校正仪，未来的AADR不会再造出一个时间刻校正仪吗？只要绑走了叶梓澄的父母的话....."
    voice v3
    l "这有考虑过，所以我们也准备了一些武器在机器里面。"
    play sound odoro
    with vpunch
    l "但是治标不治本吧！"
    hide linluo_mirai
    with dissolve
    show linluo_mirai:
        xcenter 0.6
    with dissolve
    show zicheng_mirai_pose1 at jin:
        xcenter 0.3
    with dissolve
    voice v3
    c "其实我们最开始想到的就是这个。"
    voice v3
    c "与其毁掉时间刻校正仪，不如回到时间刻校正仪被发明之前，去阻止机器的发明。"
    voice v3
    c "根据我父亲留下的笔记本，并没有说明时间刻校正仪是何时被发明的。"
    voice v3
    c "所以在找到你之前，我们已经推测性地使用时间机器去过三年前了。"
    l "结果呢？"
    voice v3
    l "不行。叶梓澄的父亲完全不清楚跟时间刻校正仪有关的东西，甚至没有一点往这个方向去研究的势头。"
    l "这难道说，时间刻校正仪其实是在三年内被发明出来的吗？"
    play sound odoro
    with vpunch
    voice v3
    l "没错！所以这次的具体任务是："
    voice v3
    l "计划先回到一年前，如果叶梓澄的父亲已经发明了时间刻校正仪，就毁掉它，如果没有发明，就阻止其诞生！"
    voice v5
    l "不过我们在回到三年前的时候已经告诫过叶梓澄父亲，不要抱有研究时间刻校正仪的念头了，但是看未来的变化.....似乎告诫没有被听进去呢......."
    voice v3
    c "我父亲就是在研究的问题上特别较真，不肯做让步。"
    l "任务完成后需要怎么做？"
    voice v3
    l "把你送回现在的时间点，然后我们返回未来.....或许会这样，又或许不会......"
    voice v3
    l "总之，出发吧！"
    l "好！"
    play music title2 fadein 1.0 fadeout 1.0
    play sound odoro
    with vpunch
    "AADR！虽然我从来没有正面与你们进行过对决，但是你们的恶行，就由我来......进行最终的终结！"
    scene bg_none
    with fade
    nvle "............................."
    nvl clear
    nvle "随着铁球大门的紧闭，我正式踏上了最终之战的路途。"
    nvle "没有硝烟的.......最后的战斗！"
    nvl clear
    play music home fadein 1.0 fadeout 1.0 
    scene bg_taimumashin_naka
    with fade2
    nvle "..................."
    nvl clear
    nvle "机器内比较挤，只能勉强容下三个人。"
    nvle "来自未来的叶梓澄在细细地操作着键盘和按钮，屏幕上的数据和图像也不断变换着。"
    nvle "见叶梓澄在屏幕的聊天框里打入了“将我们送到一年前的这个时间段和这个相对坐标点位置。”。"
    nvl clear
    l "十年后的科技都这么高级了吗？我以为需要操作很复杂的指令。"
    $ persistent.tips110 = True
    c "这就是未来的{a=showmenu:tips110}{color=#F18D7D}AI{/color}{/a}技术的力量，你可以通过对话的方式让AI帮你处理很复杂的工作。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    "我也想体验到这种东西，所以必须更努力地为了未来而战了！"
    nvle "随着指令输入几秒钟后，显示屏上出现了几个窗口，里面有各种图表和数据。"
    nvle "心里很激动，实打实地坐进了来自未来的时间机器里，体验到了未来的科技。虽然之前的手表也是时间机器的一种，但是完全没什么实感。"
    nvl clear
    play sound enter
    scene bg_taimumashin_naka at furu
    "随着叶梓澄按下回车键，舱内开始震动。"
    play sound odoro
    with vpunch
    c "要出发了！"
    scene bg_taimumashin_naka at shake
    "震动越来越剧烈。"
    play music omou fadein 1.0 fadeout 1.0
    
    with dissolve
    "同时感觉自己的身体仿佛在慢慢被剥离。"
    hide bg_syuucyuu
    show bg_taimumashin_naka_2 at shake:
        alpha 1.0
        linear 1.0 alpha 0.5
        linear 1.0 alpha 1.0
        repeat
    show bg_syuucyuu:
        alpha 1.0
        linear 1.0 alpha 0.5
        linear 1.0 alpha 1.0
        repeat
    nvle "这是一种从未体验到的感觉。周围的视野越来越模糊，感觉像在深海里慢慢下沉一般。"
    nvl clear
    scene bg_none
    with fade2
    nvle "也不知道什么时候，慢慢就失去了意识............."
    nvl clear
    nvle "...................."
    nvl clear
    nvle "...................."
    nvl clear
    nvle "...................."
    nvl clear
    nvle "...................."
    nvl clear
    stop music
    play sound odoro
    with vpunch
    nan "到了！！"
    l "............"
    l "...........................!!!"
    play sound odoro
    with vpunch
    l "额！！！"
    nvle "不知道什么时候消失的意识，也不知道什么时候回来的意识，就像在很困的状态下睡着，在很困的状态下醒来一样。"
    nvl clear
    play music home fadein 1.0 fadeout 1.0
    l "已经......到了？"
    scene bg_taimumashin_naka
    show eye
    $ renpy.pause(2.7, hard=True)
    hide eye
    with dissolve
    "大脑慢慢变得清醒。"
    l "跟我想象中的以及电影里看到的时间机器有点不太一样........."
    c "毕竟我们的时间机器的原理是把整个时间机器包括里面的人都拆解转换成零子，进入+1时间刻维度光速运动以后再从+1时间刻维度抽出回到0时间刻维度，再把零子通过原子匹配分布表还原成......."
    l "已经够了....."
    "这个原理我已经在叶梓澄父亲的笔记本里品鉴过了。"
    scene bg_taimumashin_naka
    with fade2
    nvle "在喘息了一会以后，感觉自己逐渐能行动了。"
    nvl clear
    c "那，行动开始！"
    play sound shindou
    scene bg_taimumashin_naka at furu
    $ renpy.pause(2.0, hard=True)
    scene bg_taimumashin_naka_sun
    with dissolve
    "随着舱门缓缓打开，刺眼的阳光逐渐映照进来。"
    stop sound
    play music speak fadein 1.0 fadeout 1.0
    l "不过我还是存在一个疑问。"
    l "如何确定是否真正回到了某个时间点呢？"
    c "方法很多。"
    c "一般直接的办法就是查看时间机器内通过计算宇宙中物质浓度的值来显示绝对时间的系统。"
    c "但再精密的系统也总有出错的那一天。"
    c "所以也会用到那些科幻作品里经常出现的方法。看报刊或者询问路人什么的。"
    l "果然是吗？"
    "艺术毕竟来源于生活嘛......"
    "但是我感觉这个场景应该说是“生活来源于艺术”可能更恰当......"
    play music home fadein 1.0 fadeout 1.0
    scene bg_none
    with fade
    nvle "............."
    nvl clear
    play sound run_kai
    scene white
    with dissolve
    "缓缓地走出了舱门。"
    play music kexi fadein 1.0 fadeout 1.0
    scene bg_taimumashin
    with dissolve
    "外面的场景....跟乘坐时间机器之前并没有什么变化。唯一的变化就是从傍晚变成了正午，应该是正午吧，这晃人的太阳光。"
    "也算正常，首先是荒郊野外，人迹罕至的树林，其次是一年时间还是太短了。"
    l "等会要怎么进行交涉呢？"
    show zicheng_mirai_pose1 at jin:
        xcenter 0.3
    with dissolve
    show linluo_mirai:
        xcenter 0.6
    with dissolve
    voice v3
    c "时间机器显示现在的时间是2021年10月21日，星期四。"
    voice v3
    c "这个时间点的我还在上学，不出意外的话研究所里只有我父亲一个人还在。"
    voice v3
    c "不过在三年前我们就乘坐时间机器去拜访过他了。"
    voice v3
    c "在现在再去的话肯定还是记得我们的！"
    voice v3
    c "交涉起来应该容易许多吧！"
    play music title2 fadein 1.0 fadeout 1.0
    voice v3
    c "再强调一下此次行动的目的："
    voice v3
    c "在AADR发现存在时间刻校正仪这一装置之前，将其从这个世界上抹消掉！"
    voice v3
    c "此行动是真正的，阻止人类未来走向被AADR统治的，决定性的行动！"
    play sound odoro
    with vpunch
    voice v1
    c "走吧！！"
    play music kexi fadein 1.0 fadeout 1.0
    scene bg_none
    with fade2
    play sound yabu loop
    nvle "我跟随着未来的我和叶梓澄，缓缓地穿过树林。"
    nvle "树叶的沙沙声不断围绕在耳边。"
    nvle "这种自然的气息是我很喜欢的。"
    nvl clear
    nvle "也多亏了这种声音，我的心态也逐渐放平了。"
    nvl clear
    nvle "............."
    nvl clear
    scene bg_kennkyuujya hare
    with fade
    stop sound
    nvle "随着最后一片树丛逐渐褪至身后，视野立刻变得宽广了起来。"
    nvle "有棱有角的建筑物显现了出来。"
    nvl clear
    "到了。这存在于我记忆中的...........叶梓澄父亲的研究所。"
    "与记忆中不同的地方是，门是正常关闭着的，地上也没有杂乱的痕迹。"
    show zicheng_mirai_pose1 at jin:
        xcenter 0.3
    with dissolve
    show linluo_mirai:
        xcenter 0.6
    with dissolve
    l "没人吗？大门是紧闭的。"
    voice v3
    c "应该是有人的。"
    scene bg_kennkyuujya hare:
        xzoom 1.0  yzoom 1.0
        linear 1.0 xcenter 0.65 ycenter 0.11 xzoom 1.9 yzoom 1.9
    with dissolve
    "未来的叶梓澄走上门前，敲了敲门。"
    play sound door
    with vpunch
    mono "咚咚咚！"
    c "在吗？"
    play sound door
    with vpunch
    mono "咚咚咚！"
    c "有人吗？"
    stop sound
    scene bg_kennkyuujya hare
    with dissolve
    show zicheng_mirai_pose1 at jin:
        xcenter 0.3
    with dissolve
    show linluo_mirai:
        xcenter 0.6
    with dissolve
    l "果然是不在研究所吗？"
    voice v3
    c "也许是他不清楚我们是好人坏人，而不选择应答呢？"
    scene bg_kennkyuujya hare:
        xzoom 1.0  yzoom 1.0
        linear 1.0 xcenter 0.65 ycenter 0.11 xzoom 1.9 yzoom 1.9
    with dissolve
    "叶梓澄又再次走上门前。"
    play sound door
    with vpunch
    mono "咚咚咚！"
    stop sound
    c "父亲？我是从未来乘坐时间机器回来的叶梓澄！两年前我们见过面的！"
    "............."
    "........"
    "................."
    scene bg_kennkyuujya hare
    with dissolve
    show zicheng_mirai_pose1 at jin:
        xcenter 0.3
    with dissolve
    show linluo_mirai:
        xcenter 0.6
    with dissolve
    voice v3
    c "还是无应答。"
    l "那怎么办？"
    l "如果主动打开大门呢？"
    play sound odoro
    with vpunch
    voice v3
    c "对！在我的记忆里，父亲会把研究所大门的钥匙藏在............"
    scene bg_zicheng_te_gi2
    with dissolve
    play sound yabu loop
    "说罢，叶梓澄走到研究所旁边的灌木丛那里，进行着摸索。"
    play music sora fadein 1.0 fadeout 1.0
    nvle "这一场景我曾经见过！只不过现在的人物从高中生模样的叶梓澄，变成了更加成熟的叶梓澄了......"
    nvle "我看向旁边的未来的我，他也跟我一样，眼里闪烁着高光。"
    nvle "毕竟他拥有我几乎全部的记忆，自然他的记忆深处也有这段回忆。"
    nvl clear
    stop sound
    play music kexi fadein 1.0 fadeout 1.0
    play sound odoro
    with vpunch
    c "找到了！"
    scene bg_kennkyuujya hare
    with dissolve
    show zicheng_mirai_pose1 at jin
    with dissolve
    show key:
        xcenter 0.2
        ycenter 0.3
    with dissolve
    "叶梓澄从灌木丛里摸出一个透明塑料袋，里面是一把钥匙。"
    voice v1
    c "那开门吧！"
    voice v3
    c "如果我父亲在里面，就把事情说清楚。"
    voice v3
    c "如果里面确实没人。"
    voice v3
    c "就在研究所里等待父亲回来！"
    scene white
    with dissolve
    play sound opendoor2
    "伴随着“咯哒咯哒”的声响，门开了。"
    play music home fadein 1.0 fadeout 1.0
    scene bg_kennkyuujya_naka2
    with dissolve
    "走进了熟悉的研究所，和记忆中的不同是，到处都是完好的。"
    play sound run
    "正在我们四处观察的时候，一阵脚步声响起。同时传来一声深沉的男声。"
    play sound odoro
    with vpunch
    nan "你们是谁？"
    "应该就是叶梓澄的父亲了。"
    show zicheng_chichi
    with dissolve
    c "我们是............."
    nvle "看来情况跟未来的我说的不一样啊。"
    nvle "叶梓澄的父亲并没有认出未来的我和叶梓澄，即便在这个时间点的两年前曾经有见过面。"
    nvl clear
    c "父亲！我是来自十一年后的.......未来的.....叶梓澄！未来的您的女儿！！"
    nvle "不应该是十年后吗？哦！想起来回到一年前了。"
    nvl clear
    c "难道您忘记了吗？在两年前曾经搭乘时间机器来找过您........"
    nvle "此情此景，不禁让我后背一凉。"
    nvle "因为我想到了那个可能存在但不愿意去确认的东西："
    nvle "平行世界的存在！"
    nvl clear
    nvle "难道时间机器所回到的过去......真的是分支的一条平行世界吗？"
    nvl clear
    play sound odoro
    with vpunch
    voice v3
    cb "时间机器？未来已经成功发明出时间机器了吗？"
    c "嗯！！用您的理论制造出来的！"
    c "您的..........时间刻数值理论和零子理论............"
    voice v3
    cb "我的理论吗？看来果然是可行的........"
    voice v1
    cb "但是..............."
    voice v3
    cb "你们从未来回到这个时代是为了什么呢？"
    voice v3
    cb "给我一个相信你们的理由.........."
    c "果然您忘光了吗......."
    play music speak fadein 1.0 fadeout 1.0
    nvle "未来的叶梓澄和我一五一十地将AADR在未来会做的事情，以及第一次乘坐时间机器去到过去寻找叶梓澄父亲时所发生的事情告诉给了现在的叶梓澄父亲。"
    nvl clear
    play music home fadein 1.0 fadeout 1.0
    scene bg_none
    with fade2
    nvle "........................."
    nvl clear
    scene bg_kennkyuujya_naka2
    with fade2
    show zicheng_chichi
    with dissolve
    voice v1
    cb "实际上................"
    voice v3
    cb "我不存在这段记忆....."
    play music lanzhu fadein 1.0 fadeout 1.0
    play sound odoro
    with vpunch
    l "这...........什么意思？"
    hide zicheng_chichi
    with dissolve
    show zicheng_mirai_pose1 at jin:
        xcenter 0.3
    with dissolve
    show linluo_mirai:
        xcenter 0.6
    with dissolve
    "未来的叶梓澄和未来的我都露出了极为惊讶的表情。"
    play sound odoro
    with vpunch
    voice v3
    c "难道父亲您理论里面的时间机器..........只能去往平行世界？"
    "未来的叶梓澄也意识到了这个问题。"
    scene bg_kennkyuujya_naka2
    with dissolve
    show zicheng_chichi
    with dissolve
    voice v1
    cb "不是这样的........."
    play music speak fadein 1.0 fadeout 1.0
    voice v3
    cb "本来我是打算把这份秘密带进棺材里面的......看来得在今天告诉给其他人了.........."
    c "您说的秘密............是？"
    voice v3
    cb "关于我和时间刻校正仪的往事。"
    voice v3
    cb "这件事得从.........十年前说起了............."
    scene bg_none
    with dissolve
    cbnvl "我在十年前搬家到了这个城市，沁野市。"
    cbnvl "从事零子相关的研究。"
    cbnvl "研究很顺利，在一年内就取得了很大的成果，我原本是打算将研究成果写成论文发表的。"
    nvl clear
    cbnvl "但是..........."
    cbnvl "在我准备发表前不久，就出现了意外事件。"
    cnvl "意外事件是指？"
    nvl clear
    cbnvl "我女儿的同班同学，同时也是她的好朋友.....覃可汐....遭遇了溺水..........."
    cbnvl "在沁野市水潭村河段.........."
    cnvl "这个！我到现在还依旧印象深刻！"
    nvl clear
    cnvl "毕竟很惊险.....我差一点.......童年里就会永远失去覃可汐了............"
    cnvl "那个事件的最后,覃可汐被不认识的人给救了出来对吧！"
    cbnvl "在你的记忆里确实是这样，但现实是："
    nvl clear
    cbnvl "覃可汐被搜救人员在河里打捞了几天几夜才找到遗骸。"
    play sound odoro
    with vpunch
    cnvl "！！！！！！！！怎么可能？！"
    cnvl "然后呢？"
    nvl clear
    nvle "未来的我拦住了未来的叶梓澄，让叶梓澄父亲继续说下去。"
    nvle "我有点难以置信。"
    nvle "和我以及叶梓澄有过那么多美好回忆的覃可汐......"
    nvl clear
    nvle "早在十年前就已经......死掉了！？"
    nvl clear
    cbnvl "当时伴随着遗骸一块被挖掘机挖出来的，还有河里的一块巨大的铁疙瘩。"
    cbnvl "被金属包裹的生锈球体。"
    cbnvl "由于外壳氧化严重了，所以挖掘机一下就挖开了外壳，露出了内部。"
    nvl clear
    cbnvl "里面是已经无法辨认的各种电子元件一样的残骸。"
    cbnvl "不过最主要的是............在球状金属物体的内部核心位置以及内部下侧被掩盖住的位置。"
    cbnvl "发现了一种很特殊的物质。"
    nvl clear
    cbnvl "像石头一样的硬度，但表面上闪烁着奇异的微光。"
    cbnvl "当地的施工队第一时间找到我也是为了这个，毕竟知道我有一间研究所。"
    cnvl "莫非这就是？"
    nvl clear
    cbnvl "没错，这是我第一次发现零之石的存在。"
    cbnvl "零之石就是我给这种物质的命名。"
    cbnvl "我在研究所内对零之石进行了很多的研究与尝试，但真正让我搁置了零子相关研究成果的论文的发表的原因是："
    nvl clear
    cbnvl "我尝试将零子涂抹到零之石上面的时候，被涂抹的零子消失了。不是转换成其他物质，而是直接消失掉了。"
    cbnvl "我当时怀疑的是，零之石可能具有吞噬零子或者什么其他物质的能力。"
    cbnvl "经过我五年的不断研究和尝试，终于得知了零之石的大概作用。"
    nvl clear
    cbnvl "也根据实验结果进行了大胆的猜测："
    cbnvl "有一个其他的维度平行与我们所处维度之上，并且这层维度和我们维度的关系不能靠科学界传统的多维宇宙论来解释。"
    cbnvl "并不是多了一维还是什么的关系，就是单纯是一个新的维度而已。"
    nvl clear
    cbnvl "并且往这层维度注入零子，会造成我们所处世界的变化。"
    cbnvl "这是我靠往零之石注入零子以后通过观测得知的结论。"
    cnvl "这些结论......在父亲您的笔记本里有记载。我们能成功造出时间机器也是依靠过这个理论。"
    nvl clear
    cbnvl "你们通过实践验证了我的猜测是正确的....真是太好了。"
    cbnvl "不知道零之石会随着时间慢慢生长的特性，我是否有在笔记本中写到。"
    cnvl "这个没有。"
    nvl clear
    $ persistent.tips111 = True
    cbnvl "零之石会像水晶一样“{a=showmenu:tips111}{color=#F18D7D}出芽{/color}{/a}”，慢慢地长出细小的零之石，不过生长的极为缓慢。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    $ persistent.tips112 = True
    cbnvl "从发现的金属球体的物质的{a=showmenu:tips112}{color=#F18D7D}衰变{/color}{/a}计算出的时间来看，金属球体至少在河底埋藏了五十万年以上。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    cbnvl "也就是说零之石的存在时间也至少在这个数字之上。"
    nvl clear
    cbnvl "这么长的时间，零之石表面也只是长出了几厘米的长度。"
    cnvl "五十万年........几乎已经比人类出现时间还要更早了。"
    cnvl "那这个金属球体以及里面的零之石是哪里来的呢？"
    nvl clear
    cbnvl "这就不得而知了。"
    cbnvl "而且构成零之石的物质，即便非常微小，也依旧能产生作用。"
    cbnvl "这是我将零之石在水中浸泡以后测量得出的结论，水中含有的极微量的零之石也依旧会收到往更高维度注入零子的影响。"
    nvl clear
    cbnvl "不过接下来我要说的东西，很可能是只有我才知道的东西了，我没有也不会将它在未来记录在任何位置。"
    cbnvl "关于我们所处世界的本源问题！！"
    cbnvl "在后续的研究中，我发现不止是可以注入零子，而且可以抽出零子。"
    nvl clear
    cbnvl "注入抽出零子的数量不同，对我们所处世界的干涉也都不一样。"
    $ persistent.time = 5
    cbnvl "在两年前我根据所研究的成果，造出了一个简单的装置：{a=showmenu:tips49}{color=#BFBFFF}时间刻校正仪{/color}{/a}！"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say2
    with dissolve
    hide screen tips_say2
    with tipsanime
#词典
    cbnvl "本体就是一个电路板上带着零之石以及负责注入和抽出的通道，和一个观测注入抽出值的显示数字的表盘。"
    nvl clear
    cbnvl "我将注入到更高维度的零子量用数字来表示，例如+1，+2，+3................."
    cbnvl "每一个整数代表所注入的一定量的零子。"
    cbnvl "我把这些数字叫做时间刻。"
    nvl clear
    cbnvl "因为我也无法观测到具体有多少个维度平行于我们所处维度之上，所以我采取的叫法是统一叫做+1时间刻维度，后面的+2  +3什么的，则作为+1时间刻维度的参数了。"
    cbnvl "相对的，我们所处世界就叫做0时间刻维度了，这个名称仅是相对于+1时间刻维度而言。"
    cbnvl "但是如果将注入的零子完全抽干以后，再尝试抽出会发生什么？"
    nvl clear
    cnvl "抽不出来了吧！完全干瘪的牙膏，无论再怎么挤也是挤不出来的！"
    cbnvl  "大部分人可能会这样想。但事实是："
    cbnvl "还能继续抽出，只不过在抽出的过程中我明显感觉到我周围的世界产生了不自然的颤动。"
    nvl clear
    cbnvl "这项实验是我在几个月之前完成的。"
    cbnvl "在我对时间刻校正仪。"
    cbnvl "抽出了1时间刻的量的零子以后，时间刻校正仪表盘上的数字从0变成了-1。"
    nvl clear
    cnvl "-1了............会怎么样？"
    cbnvl "我也在抽出的过程中感到阵阵眩晕。本来计划抽出1时间刻的量的零子以后就停止的。但是已经无法停止了。"
    cbnvl "时间刻校正仪周围五米半径的空间内的物体，包括我和我放在旁边的笔记本，都一切正常，除了时间刻校正仪那停留在-1的表盘。"
    nvl clear
    cbnvl "但是5米以外的其他空间.......完全变了！！"
    cbnvl "最开始我并没有察觉到世界发生了改变。"
    cbnvl "直到——————"
    nvl clear
    cbnvl "我从研究所回到家中的时候，见到了覃可汐............那个在我记忆中已经去世多年的覃可汐........."
    cbnvl "不仅生龙活虎地长成了十几岁的样子，而且还跟我女儿关系很好。"
    cbnvl "我这才彻彻底底地意识到，世界被改变了！"
    nvl clear
    cnvl "所以时间刻校正仪具有跳跃平行世界的功能？"
    cbnvl "比起说是跳跃了平行世界，不如说是整个世界........被再构成了！！"
    cbnvl "那个+1时间刻维度，不仅可以干涉我们所处的世界，而且可以直接对我们所处世界进行再构成.........简直就像计算机里的管理员权限一样......我则像卡出了管理员权限bug的普通用户一样....."
    nvl clear
    cnvl "所以现在这个世界的一切，是在几个月前才构成的吗？"
    cnvl "但是如果当作平行世界来看的话，更能解释为什么我们乘坐时间机器去两年前寻找您的记忆，现在的您并不知情吧！！"
    cnvl "因为您......来自其他平行世界........"
    nvl clear
    cbnvl "我也没办法论证这些东西，只能凭我启动时间刻校正仪时的直觉告诉我，这是世界在再构成，而不是说穿越到了平行世界，因为时间刻校正仪的简易构造，凭机器本身很难想象具有这种机能。"
    cbnvl "但是再构成世界这种机能不是更难想象吗？"
    $ persistent.tips113 = True
    cbnvl "如果将时间刻校正仪看作一个{a=showmenu:tips113}{color=#F18D7D}客户端{/color}{/a}，+1时间刻维度看作一个服务器的话就不难解释了，再构成世界的工作是在+1时间刻维度执行的，时间刻校正仪只是负责发送指令而已。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    nvl clear
    lnvl "所以.........我们所处的这个世界.........处在被更高层的世界的管辖之下？"
    nvle "脑中莫名想到了各种神创世学说。"
    cbnvl "这本是我接下来即将要研究的方向。"
    nvl clear
    cbnvl "不过你们说的属实的话，明年我会被AADR这个机构抓走，导致这项研究会被永远搁置吧..............."
    cnvl "但是！！既然您使用时间刻校正仪到了这个所谓的-1时间刻维度，请允许我把这称为-1时间刻维度吧，虽然可能根本算不上是一个新的维度，这只是借用了一下命名法则。"
    cnvl "为什么不通过重新注入零子的方式回到0时间刻维度呢？从我们现在的-1时间刻维度.........."
    nvl clear
    cnvl "难道是单向车票吗？无法再注入回去了？"
    cnvl "而且既然现在是-1时间刻维度，那为什么再往时间刻校正仪注入零子不是回到0时间刻维度而是继续变成+1，+2，+3，继续对这个世界进行着干涉？"
    cbnvl "因为表盘以0为界，+和-所代表的含义已经完全不是一个东西了。从0时间刻维度抽出到-1时间刻维度的零子，跟正常的零子性质又不一样！！"
    nvl clear
    cbnvl "首先零子是原子再构成的物质，携带有原子本身的信息，但是从0时间刻维度抽出的零子，携带的信息无法直接解读，也无法复制，就像加密了一样。"
    cbnvl "必须重新注入之前抽出的零子才能回到0时间刻维度，普通的零子是不行的。"
    cnvl "加密技术.........."
    nvl clear
    cbnvl "不过我有将抽出的零子妥善保管，如果想回到0时间刻维度，只需要将其注入进时间刻校正仪就可以了。"
    cbnvl "所以必须用我抽出的零子，才能再构成世界回到0时间刻维度，其他的零子只能让+1时间刻维度对0时间刻维度产生干涉。"
    nvl clear
    scene bg_umi2
    with fade
    cbnvl "如果以大海举例的话，海平面是0时间刻维度，天空就是+1时间刻维度了，大气层的从下往上又可以把+1时间刻维度分为+2，+3，+4..............."
    cbnvl "海平面往下的深度则可以分为-1，-2，-3..............."
    show bg_umi3
    with dissolve
    cbnvl "0时间刻维度抽出的零子，就相当于把-1层的海洋翻转到了海平面，海是同一片海，不是其他的海，但是位于海平面的海水，却发生了改变，大概就是这种类似的东西了。"
    nvl clear
    $ persistent.tips114 = True
    cbnvl "为表区分，就把我最开始的世界叫做{a=showmenu:tips114}{color=#F18D7D}原初时间刻{/color}{/a}吧，跟现在所处的-1时间刻区分。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    nvl clear
    scene bg_kennkyuujya_naka2
    with fade
    show zicheng_mirai_pose1 at jin:
        xcenter 0.3
    with dissolve
    show linluo_mirai:
        xcenter 0.6
    with dissolve
    voice v3
    c "说了这么多，不过为什么在发现自己处于-1时间刻维度以后，没有重新回到原初时间刻维度呢？难道是因为？"
    scene bg_kennkyuujya_naka2
    with dissolve
    show zicheng_chichi
    with dissolve
    play sound odoro
    with vpunch
    voice v1
    cb "因为你！"
    play music sora fadein 1.0 fadeout 1.0
    voice v5
    cb "我的女儿！我第一次看到你和覃可汐那无忧无虑的神情的时候，我就已经打消了回去的想法。现在的世界.....也挺好的不是吗？"
    voice v3
    cb "至少你不是永远孤身一人，没有朋友......."
    voice v3
    cb "也没有让你悔恨一生的童年阴影......"
    play sound odoro
    with vpunch
    c "所以因为我，您选择让这个世界永远保持在-1时间刻吗？"
    voice v1
    cb "没错..............."
    voice v3
    cb "不过现在来看........是我走错了一步............."
    voice v3
    cb "因为我原来所处的世界，是不存在AADR这个组织的！！"
    play music lanzhu fadein 1.0 fadeout 1.0
    scene bg_kennkyuujya_naka2
    with dissolve
    show zicheng_mirai_pose1 at jin:
        xcenter 0.3
    with dissolve
    show linluo_mirai:
        xcenter 0.6
    with dissolve
    play sound odoro
    with vpunch
    c "？？？？？！！！！"
    play sound odoro
    with vpunch
    l "！！！！？？？"
    play sound odoro
    with vpunch
    l "什么？不存在？"
    nvle "在场的众人，包括我在内，都发出了惊诧的声音。"
    nvl clear
    voice v3
    c "也就是说.....AADR这个组织.....是仅存在于-1时间刻维度的组织吗？"
    scene bg_kennkyuujya_naka2
    with dissolve
    show zicheng_chichi
    with dissolve
    with vpunch
    voice v1
    cb "没错！"
    play music speak fadein 1.0 fadeout 1.0
    voice v3
    cb "但是作为代价的是，覃可汐会在九年前就死去！"
    voice v3
    cb "也就是说现在这个世界，虽然时间刻校正仪显示的默认依然是0，但是实际数值却是....-1。"
    voice v3
    cb "之所以表盘的数字变化了，是因为我到-1时间刻维度以后手动注入了一些新的零子进去，让表盘的数据变成这样的。"
    nvle "我的脑袋也快要爆炸了，完全不能理解。"
    nvl clear
    voice v3
    cb "所以你们来这个时代的目的......"
    voice v3
    cb "是为了毁掉时间刻校正仪对吧！"
    voice v3
    cb "但是单纯直接毁掉这个机器.....真的能阻止AADR在未来的统治吗？"
    c "我觉得可以。AADR失去了时间刻校正仪，就无法利用这台仪器随意更改+1时间刻维度对我们所处世界的干涉了！"
    voice v3
    cb "如你们所说......AADR一直在默默调查着我,想拿到我的研究成果。"
    voice v3
    cb "就算时间刻校正仪被摧毁了......AADR靠着我的研究成果，复刻另外一台时间刻校正仪也不是什么难事吧！？"
    voice v5
    cb "就像你们根据我的研究成果造出时间机器一样！时间机器的核心不就是一台更大号的时间刻校正仪！你们都能做到的事情.....有着几千位科学家的AADR做不到？"
    scene bg_kennkyuujya_naka2
    with dissolve
    show zicheng_mirai_pose1 at jin:
        xcenter 0.3
    with dissolve
    show linluo_mirai:
        xcenter 0.6
    with dissolve
    play music sora fadein 1.0 fadeout 1.0
    c "............."
    voice v3
    c "看来我们还是太天真了呢..............."
    voice v3
    c "一边潜心研究者时间机器，一边在心中告诉自己，时间机器做好了就好了.....回到过去就好了......只要回到过去.....就什么都好了......"
    voice v3
    c "但更深层的内容....却没有细究......"
    nvle "............."
    nvl clear
    nvle ".................."
    nvl clear
    "我得想个办法打破僵局.........."
    scene bg_kennkyuujya_naka2
    with dissolve
    show zicheng_chichi
    with dissolve
    play music speak fadein 1.0 fadeout 1.0
    l "您不是说您最开始的0时间刻维度是不存在AADR这个组织的吗？"
    l "那把最开始从时间刻校正仪抽出来的“加密”零子，重新注入回+1时间刻维度，让世界回归到最开始的状态...能实现吗？"
    l "从一开始就抹除掉AADR的存在........问题就解决了吧！！！"
    voice v3
    cb "确实是这样.......但是相关的代价是："
    voice v3
    cb "覃可汐会死于九年前的夏天！！"
    voice v3
    cb "不想接受被AADR所奴役，所统治的未来，那么现在摆在我们面前的就是这两条选择了.........."
    l "如果覃可汐会死于九年前的夏天.....那乘坐时间机器回到那个时间把覃可汐救下来呢？"
    scene bg_kennkyuujya_naka2
    with dissolve
    show zicheng_mirai_pose1 at jin:
        xcenter 0.3
    with dissolve
    show linluo_mirai:
        xcenter 0.6
    with dissolve
    voice v3
    c "其实...........时间机器内的能源供给已经不够了......"
    l "能源供给......不够是什么意思？"
    voice v3
    c "这次时间旅行以后我发现时间机器的能源储备已经不够了。"
    voice v3
    c "明明只是回到一年前的时间点....."
    voice v3
    c "但是能源的消耗......却比回到三年前还要多......"
    l "所以............时间机器现在用不了了吗？"
    voice v3
    c "能用.....但是可能无法成功送到准确的时间点了........."
    l "能源供应是什么？有办法解决吗？"
    voice v3
    c "是通过零子相关技术改良后的高压缩率充电电池.....但是这个时代的技术无法做到给电池充电.........."
    l ".................."
    "我苦笑着。"
    voice v1
    c "所以。"
    voice v3
    c "未来还是可以被改变的.........只不过两种方法都带有相对应的代价。"
    voice v3
    c "第一种方法，就是启动时间刻校正仪的机能，将这个世界所属的时间刻从-1恢复成最开始的原初时间刻。"
    voice v1
    c "代价是..."
    voice v3
    c "覃可汐的...不可逆的凋亡....."
    play music sora fadein 1.0 fadeout 1.0
    with vpunch
    nvle "够了.............说实话我受够了..............."
    nvle "为什么.........为什么会死的永远是覃可汐.........."
    nvle "这么多次时间的重复..........唯一的共同点就是.........覃可汐会死。"
    nvl clear
    nvle "无论会发生什么，覃可汐都会死。"
    nvle "无论我做出了哪些努力..........覃可汐都会死。"
    nvle "覃可汐像是被死神的枷锁牢牢束缚着一样。无论怎样........都一定会死..........."
    nvl clear
    nvle "既然覃可汐是命中注定的会死掉，那我不管怎么和命运去做斗争，都改变不了这个事实吧！"
    nvle "我已经快失去了耐心，处在接近放弃的边缘。"
    nvle "即使救活覃可汐是我能走到今天的，一开始的出发点。"
    nvl clear
    scene bg_linluo_mirai_te
    with dissolve
    l "过去的我。我能理解你的心情。"
    "未来的我找我搭话了。"
    l "即便过了这么多年，我对覃可汐的印象已经接近模糊。"
    l "但是我仍然清晰地记得一件事！那就是："
    l "支撑我和叶梓澄走到现在的信念，都来自覃可汐！！！"
    l "而且并不是绝路！即便现在的技术无法给时间机器提供能源。"
    l "但是往后呢？在新的未来里呢？"
    nvle "我恍然大悟！"
    nvl clear
    l "不过还是让你来选择吧！"
    l "至少拯救人类的未来....也还有救！！"
    play music title2 fadein 1.0 fadeout 1.0
    l "方法一就是：启动时间刻
    校正仪的机能，将这个世界所属的时间刻从-1恢复成最开始的原初时间刻。"
    l "方法二则是：将叶梓澄父亲所有有关零子和时间刻校正仪的资料，以及时间刻校正仪本体一起，丢进时间机器.........."
    l "然后......将时间机器送到一个AADR无法接触到的时间点！"
    play sound odoro
    with vpunch
    "！！！！！？？？？？"
    "是未曾设想过的方法！"
    scene bg_kennkyuujya_naka2
    with dissolve
    show zicheng_mirai_pose1 at jin:
        xcenter 0.3
    with dissolve
    show linluo_mirai:
        xcenter 0.6
    with dissolve
    l "方法二的话，的确可以彻底断绝AADR想统治人类的技术上的道路。"
    l "但是零子相关的技术.....也会因此从世界上消失吧！"
    l "而且叶梓澄父亲真的愿意......这样做吗？终止自己研究了多年的技术........."
    scene bg_kennkyuujya_naka2
    with dissolve
    show zicheng_chichi
    with dissolve
    play sound odoro
    with vpunch
    voice v3
    cb "我愿意！未来已经证明了.......我的研究或许一开始就是错的！"
    voice v3
    cb "没有给人来带来技术的便利，反而让人类因为我的发明陷入了水深火热。"
    voice v3
    cb "让我把我所有有关零子和时间刻校正仪的数据和研究成果都销毁....也挺好的.....就当它们从未存在于世上。"
    voice v3
    cb "不过这样做以后，我的研究所也可以宣布关门了。"
    voice v3
    cb "回去老老实实做老本行，当大学老师吧......."
    scene bg_kennkyuujya_naka2
    with dissolve
    show zicheng_mirai_pose1 at jin:
        xcenter 0.3
    with dissolve
    show linluo_mirai:
        xcenter 0.6
    with dissolve
    voice v1
    c "父亲..........."
    play music speak fadein 1.0 fadeout 1.0
    l "方法二的代价，就只有掐断零子相关的.....人类的科技树这一种代价吗？"
    l "跟方法一比起来简直是上帝的馈赠了。"
    l "不过时间机器不能在无人的状态下启动吧.....要怎么把装有研究成果和时间刻校正仪的时间机器送到其他时间呢？"
    l "而且如果送的时间点太近了.....AADR还是接触到了里面的内容怎么办呢？"
    voice v3
    c "可以通过AI自动设定时间机器的倒计时启动。"
    voice v3
    c "至于送的时间，虽然无法保证稳定送到某个时间点.......但是我会尽量让其送到更遥远的时间的。"
    voice v3
    c "至于是过去还是未来......就变成一个悬念吧！"
    voice v3
    c "但是我还是想将决定权交给你！"
    voice v3
    c "你愿意选择哪种方法呢？"
    l "让我来选择？真的好吗？"
    voice v3
    c "也对，毕竟我曾经也让你做过选择了......"
    play sound odoro
    with vpunch
    l "啊！？你有过这段记忆？"
    play music title fadein 1.0 fadeout 1.0
    voice v3
    c "这是未来的你告诉我的.....不过我也似乎...印象中做过类似的梦........"
    voice v3
    c "毕竟我们已经在AADR的统治下生活了十年多，可能很难保持最好的判断力了。"
    l ".................."
    l "让我考虑一下吧.........."
    stop music fadeout 1.0
    scene bg_none
    with fade
    nvle "..........."
    nvle "................"
    nvle "........................"
    nvl clear
    nvle "..........................."
    nvl clear
    scene white
    with dissolve
    play music kexi fadein 1.0 fadeout 1.0
    scene bg_kennkyuujya_gate2
    "我走出了研究所。顺便呼吸一下新鲜空气。"
    "如果我会吸烟的话，这个时候我应该是掏出一根烟然后开始抽吧。"
    "这似曾相识的场景。"
    "上一次的我，也是在这个门口，也是在做影响未来的走向的选择。"
    "如此重大的负担，却都压在我的身上。"
    "虽然我早已适应了这种压力。"
    "同样的地点，同样做出抉择。不同的只有时间。"
    "过去的我在未来做选择，未来的我，却在过去......."
    scene bg_sora
    with dissolve
    "看着晴朗的天空。"
    "云彩在缓缓的飘动。"
    "不管我这次的选择是什么......世界也依旧会照常运转下去........"
    "世界本身的运行规律不会有任何干涉.........."
    scene bg_none
    with fade
    nvle ".................."
    nvl clear
    play music home fadein 1.0 fadeout 1.0
    scene bg_kennkyuujya_naka2
    with fade2
    "思考了很久以后,我走回了研究所。"
    "未来的我和叶梓澄正在书架上翻阅资料。"
    "叶梓澄的父亲则坐在一旁沉思。"
    play sound run
    "见我进来了，未来的叶梓澄和我放下了手边的资料，往我这边过来了。"
    show zicheng_mirai_pose1 at jin:
        xcenter 0.3
    with dissolve
    show linluo_mirai:
        xcenter 0.6
    with dissolve
    voice v3
    c "怎么样？有选择了吗？"
    voice v3
    c "先说结论，这两个选择我们都是能接受的，因为都能改变那个最差的未来。"
    voice v3
    c "如果一开始就置身谷底，那么怎么走都是向上。"
    play sound odoro
    with vpunch
    l "我决定！"
    l "采用："
menu:
     "方案一：用时间刻校正仪将-1时间刻变为原初时间刻":
      jump chapter5_end3
     "方案二：将所有有关的研究成果通过时间机器送到遥远的过去或未来":
      jump chapter5_end4
