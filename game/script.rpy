label disable_shortcut():
    python:
        ## 禁止显示游戏菜单
        ##_game_menu_screen = None
 
        ## 禁止快进
        config.allow_skipping = False
 
        ## 禁止隐藏界面
        _windows_hidden = True
        _game_menu_screen = None
 
    return
## 快捷键恢复
label enable_shortcut():
    python:
        config.allow_skipping = True
        _windows_hidden = False
        _game_menu_screen = 'game_menu'
    return
transform jin:
         xcenter 0.5 
         ycenter 0.74
         zoom 1.1
transform at_tips:
         xpos 0.0 
         ypos 0.2
transform shake:
    xalign 0.5 yalign 0.5
    linear 0.05 xoffset 5 yoffset -5, easein 0.05
    linear 0.05 xoffset -5 yoffset 5, easein 0.05
    linear 0.05 xoffset -5 yoffset -5, easein 0.05
    linear 0.05 xoffset 5 yoffset 5, easein 0.05
    linear 0.05 xoffset 0 yoffset 0
    repeat
define _game_menu_screen = 'game_menu'
define _screenshot_callback = None
image endtext= Text(_("通关"), size=120,outlines = [(3,"#000000",1,1)],color="#ffffff")
define fade2 = Fade(1.5, 0.0, 1.5)
define tipsanime = Dissolve(2.5, alpha=True,time_warp=None)
define l = Character(_("林洛"),voice_tag="linluo",outlines = [(3,"#3C67A8",0,0)],ctc="hito_kotoba",ctc_position="nestled")
define x = Character(_("覃可汐"),voice_tag="kexi",outlines = [(3,"#A83C86",0,0)],ctc="hito_kotoba",ctc_position="nestled")
define c = Character(_("叶梓澄"),voice_tag="zicheng",outlines = [(3,"#A8523C",0,0)],ctc="hito_kotoba",ctc_position="nestled")
define car = Character(_("公交车广播"),outlines = [(3,"#603CA8",0,0)],ctc="hito_kotoba",ctc_position="nestled")
define suzu = Character(_("学校铃声"),outlines = [(3,"#603CA8",0,0)],ctc="hito_kotoba",ctc_position="nestled")
define tv = Character(_("电视"),outlines = [(3,"#603CA8",0,0)],ctc="hito_kotoba",ctc_position="nestled")
define t = Character(_("摊主"),voice_tag="linluo_old",outlines = [(3,"#3C67A8",0,0)],ctc="hito_kotoba",ctc_position="nestled")
define b = Character(_("保安"),outlines = [(3,"#A83C3E",0,0)],ctc="hito_kotoba",ctc_position="nestled")
define n = Character(_("乘客"),outlines = [(3,"#A83C3E",0,0)],ctc="hito_kotoba",ctc_position="nestled")
define y = Character(_("救助小组"),outlines = [(3,"#A83C3E",0,0)],ctc="hito_kotoba",ctc_position="nestled")
define m = Character(_("覃可汐的母亲"),voice_tag="kexihaha",outlines = [(3,"#3CA855",0,0)],ctc="hito_kotoba",ctc_position="nestled")
define s = Character(_("老师"),voice_tag="sensei",outlines = [(3,"#A89C3C",0,0)],ctc="hito_kotoba",ctc_position="nestled")
define w = Character(_("物理老师"),outlines = [(3,"#3CA855",0,0)],ctc="hito_kotoba",ctc_position="nestled")
define nvle = Character("", kind=nvl, ctc="kotoba",ctc_position="nestled")
define nan = Character(_("？？？"),outlines = [(3,"#000000",0,0)],ctc="hito_kotoba",ctc_position="nestled")
define narrator = Character("", ctc="kotoba",ctc_position="nestled")    
# 游戏在此开始。
image end1=At("chapters/end1.webp")
image end2=At("chapters/end2.webp")
label start:
#序章
    $ save_name = "{font=ZiTiQuanWeiJunHei-W3-2.ttf}序章{/font}"
    scene bg_none
    with fade
    play music lanzhu fadein 1.0 fadeout 1.0
    with vpunch
    nan "呜呜~"
    with vpunch
    nan "救.....救..."
    with vpunch
    nan "救救......我....."
    l "呼！呼！"
    play sound run
    "我拼劲全身的力气奔跑到河岸边上。"
    with vpunch
    "刚好赶上！！还有机会！！"
    play sound mizu_help
    "我纵身一跃进河中。"
    "为了面对此时此刻，我已经拼命练习了几个月的游泳了！一切都是为了现在！！"
    nan "救.....救...."
    "我小心翼翼地绕到身后，用手臂托住了她的身体躯干。"
    "另一只手则托住她的下巴，让其露出水面得以呼吸空气。"
    play music sora fadein 1.0 fadeout 1.0
    l "呼......呼....."
    "小心翼翼中......"
    "我成功将她带离了河中央。"
    "先平放在草地上吧。"
    "我回想着自己学习了很久的专业知识，进行着口腔清理和人工呼吸。"
    nan "呜......."
    "她终于逐渐开始有了意识....."
    "慢慢地睁开了眼睛。"
    nan "呜.....你..."
    "这时候，看着远处已经有大人朝这边过来了。"
    "我该走了。她目前应该至少脱离了生命危险。"
    play sound run
    "我起身，不顾她的呼喊，朝着反方向跑开。"
    "............."
    play sound run
    "奔跑了很久很久，确认不会有人注意到我以后，才稍微地坐在地上休息一会。"
    play sound run
    "接着便是继续奔跑。"
    "................."
    "回来了终于..........."
    "这样的话......一切都结束了......"
    "我努力到现在....终于......"
    "时间过的真快啊......回想起我第一次被牵扯进这个事件的时候....."
    "那个注定我永生难忘的九月......"
    call disable_shortcut from _call_disable_shortcut
    $ persistent.chapter1 = True
    $ persistent.chapter=1
    $ persistent.extra_chapter1 = True
    image chapter1 ="chapters/chapter1.webp"
    scene bg_none
    $ quick_menu = False
    show chapter1
    with fade2
    $ renpy.pause(5, hard=False)
    hide chapter2
    with fade2
    scene bg_none
    $ quick_menu = True
    call enable_shortcut from _call_enable_shortcut
    $ persistent.time_end1 = False
    $ persistent.chapter2 = False
    $ persistent.chapter3 = False
#这里开始
    $ save_name = "{font=ZiTiQuanWeiJunHei-W3-2.ttf}章节一：莫比乌斯的始段{/font}"
    scene bg_none
    with fade2
    play music richang fadeout 1.0 fadein 1.0
    $ persistent.music_richang = True
    play sound "audio/car_stop.ogg"
    car "{color=#C1394F}尊敬的旅客您好！沁野市高级中学站到了！请各位旅客有序下车！谢谢！{/color}"
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
    "公交车渐渐走远了，我的眩晕感也慢慢的减弱。我背着包，站在校门附近，四处端详我即将入学的这个新学校。"
    "沁野市高级中学。"
    "由于沁野市地方比较小，人口也不多，所以貌似公立高中就只有这一所。"
    "虽然跟我之前读的那所学校比起来显得很小，但从外面看，篮球场和大屏幕公告板什么的至少还都有。就是不知道有没有游泳馆和室内羽毛球场。"
    "我是昨天才搬到这个城市来。实际上已经开学大概两个多星期了吧。"
    #image ceshi=At("images/测试.png")
    #scene ceshi
    "校门口附近都没有什么人，两个保安也只是在门后的窗口那谈笑风生着。也对，这个点都要到正午了。"
    "门口附近的公路旁边摆的有地摊。但是这个点基本都收摊了，遮阳伞下面什么东西也没摆。"
    "{size=50}等等！{/size}似乎有一个摊位还在营业。"
    play sound run
    show linluo_old_pose other1 at jin
    with dissolve
    "我慢慢走到那个摊位的面前。摊主还坐着轮椅。"
    "是残疾人吗？真不容易啊。我感叹道，并向摊主走去。"
    "摊主慢慢抬起头。左手朝我这边伸了过来。"
    play music lanzhu fadeout 1.0 fadein 1.0
    $ persistent.music_lanzhu = True
    with vpunch
    l "{size=50}呃！~~{/size}"
    "感觉自己的手臂被抓住了。那瞬间施加的力量，让我的手臂不自觉的颤抖起来。我惊恐地叫出了声。"
    "是这个摊主。戴着一个宽大的帽子所以看不清他的脸。没想到他虽然坐着轮椅，但这抓我的手还格外有力气。"
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
    "摊主开口了。很憔悴的中年男性的声音。虽然是第一次听，但是有些熟悉的感觉。"
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
    "接受这表，还是不接受？"
    show noko with dissolve
menu:
     "接受":
      jump havewatch
     "不接受":
      jump nowatch
default havewatch = False
#不拿手表
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
    "又或者是某一天的假日，认识的朋友发给我一张照片或者视频，然后问“这是你”吗，然后点开一看是我在看{a=showmenu:tips02}{color=#F18D7D}工口同人本{/color}{/a}的照片，或者是我其他什么事的私房照。"
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
    b "没见过你啊？哪个班的？"
    l "额？"
    "校门口保安不肯放我进去。最后打电话给我的新班主任确认了好半天以后才同意让我进学校。"
    "对这个学校的好感度-1。我在心里想着。"
    scene bg_school_basketball
    with fade
    "一边欣赏着校内的景色一边寻找我所在班级的教学楼。"
    "穿过篮球场再走过桥应该就是了。"
    play sound suzu
    suzu "咚~咚~"
    "伴随着清脆的铃声一起。我感觉到了地面的震动。但是这时的我刚走过桥。"
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
    "应该是叫广场吧。反正就是教学楼前面到大屏幕告示板之间的一块空地。走廊外面的人工种植的草地也可以直接看见。"
    "大屏幕告示牌后面有一条人工河，通过桥梁连接着对岸的篮球场以及学校大门。"
    "河对岸栽种的几颗桂花树也能看得清楚。只是这个季节已经没有桂花了。估计得明年春天才有的看了。"
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
    scene bg_school_soto
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
    show kexi_pose at jin
    with dissolve
    play music kexi fadeout 1.0 fadein 1.0
    voice v5
    x "那个...我就长话短说了。你，，，或者你的亲属。以前是否来过沁野市。"
    l "没有。"
    show kexi_pose eyes2 mouth3 at jin
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
    show kexi_pose eyes1 mouth1 at jin
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
    show kexi_pose2 mouth1 at jin
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
    scene bg_schoolmae
    with fade
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
    scene bg_gohan2
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
    show kexi_pose at jin
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
    show kexi_pose2 mouth1 at jin
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
    scene bg_schoolmae
    with fade
    play music richang fadeout 1.0 fadein 1.0
    "下午放学后。我和覃可汐约定好在校门口“交货”。"
    show kexi_pose mouth1 at jin
    with dissolve
    l "好好照顾它哟！"
    "我如此告诫道。除了家里的电脑以外，这台掌机就是我最珍贵的伙伴了。"
    hide kexi_pose
    show kexi_pose2 mouth4 at jin
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
    show kexi_pose mouth1 at jin
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
    show kexi_pose eyes3 mouth3 at jin
    with dissolve
    voice v5
    x "啊啊啊谢谢！我跟你讲我昨天有个馆主一直打不过。克制我全队的属性。啊啊~"
    show kexi_pose eyes5 at jin
    with dissolve
    voice v3
    x "打了几个小时都打不过！身上的钱全都输光啦！"
    voice v3
    x "最后只能抓了只属性克制的精灵一直练级。结果一直没睡！"
    l "我的天！你说的通宵是真的通宵啊！"
    l "你还在上高中啊！你还要上学啊！"
    l "你这么搞，什么时候倒学校里了都不稀奇。"
    hide kexi_pose
    show kexi_pose2 mouth3 at jin
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
    show kexi_pose eyes2 at jin
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
    scene bg_schoolmae
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
    show kexi_pose mouth1 at jin
    play audio odoro
    with vpunch
    voice v1
    x "呼~呼~赶上了。"
    l "你又通宵了对吧。"
    voice v3
    x "那个......可不可以......"
    l "再让你玩一天对吧！"
    hide kexi_pose
    show kexi_pose2 mouth3 at jin
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
    show kexi_pose eyes3 mouth3 at jin
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
    show kexi_pose2 mouth4 at jin
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
    show kexi_pose2 mouth3 at jin
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
    show kexi_pose2 mouth2 at jin
    voice v3
    x "嗯......这确实是个问题......"
    show kexi_pose2 mouth3 at jin
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
    voice v3
    x "没事的班长！打起精神啊！明天我们一起去漫展吧！"
    "覃可汐开口了。"
    hide kexi_pose
    show kexi_pose mouth1 at jin:
        xpos 0.8
    voice v3
    x "我上次给你订做了一套cos服！明天你一定要穿穿看！"
    show zicheng_pose1 eyes4 mouth3 at jin
    with dissolve
    voice v3
    c "哦......好！谢谢！那......在哪见面。"
    voice v3
    x "我家！你上次去过的应该还记得路吧！"
    voice v1
    c "哦！好！"
    l "对了！林洛明天也会来。这样就有三个人了！"
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
    scene bg_school_hiroba
    $ persistent.cg11_unlocked = True
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
    scene bg_school_hiroba2
    $ persistent.cg12_unlocked = True
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
    play music "music/dead.ogg" fadeout 1.0 fadein 1.0
    with vpunch
    "嘭！"
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
    "这一切发生的过于突然。"
    "刚刚还生龙活虎的覃可汐..."
    "头部被一个花盆砸中了。"
    "倒在了地上。"
    "身体开始淌出鲜红的血来......."
    "我被吓得愣在了原地。"
    "叶梓澄也是，直接呆在了原地。"
    "路过的行人也停住了脚步，朝这边看过来。"
    "办公室和教学楼里的同学也纷纷探出头来。"
    "时间仿佛凝固了。"
    "凝固了。"
    "我脸上没有表情。因为我已经吓得不敢做出任何其他动作了。"
    "手中的扫把不知道何时自己倒在了地上。是什么时候松手的也不知道了。"
    "覃可汐...她......"
    "一个离的最近的男老师穿过围观的人群走了过来。"
    s "大家！不要围观！不要围观！有序回到教室！"
    "然后拿出手机开始拨打急救电话。"
    c "林洛......覃可汐她......"
    "叶梓澄带着哭腔朝着我喊道。"
    "但我还是一动也不敢动。"
    "再次想起来昨晚的梦境。"
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
    play music "music/dead.ogg" fadeout 1.0 fadein 1.0
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
    show kexi_pose mouth1 at jin
    show noko
    with fade2
    "今天早上，覃可汐还在用着灿烂的笑容跟我在打招呼。"
    scene bg_tukue2
    show kexi_pose mouth1 at jin
    show noko
    with fade2
    "今天早上，覃可汐还在邀请我明天去参加ChieAnime。"
    scene bg_tukue2
    show kexi_pose mouth1 at jin
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
    show zicheng_pose1 eyes2 mouth4 at jin
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
    play sound ame loop fadeout 1.0 fadein 1.0
    "我拿着雨伞出了门。"
    "因为一醒来外面就一直下着大雨。"
    "连苍天都对覃可汐的死感到可惜吗......"
    "今天的公交车来的格外的慢。等了差不多半个小时才有车过来。"
    scene bg_none
    with fade
    car "{color=#C1394F}尊敬的旅客您好！沁野市高级中学站到了！请各位旅客有序下车！谢谢！{/color}"
    scene bg_schoolmae
    with fade
    "下车了。"
    show zicheng_2
    with dissolve
    "叶梓澄已经在校门口看起来像等了很久的样子。"
    "手里拿着一把花束。"
    c "走吧~"
    "叶梓澄没有多说什么。只说了这两个字。"
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
    "我右脚踏出车外，目视着周围。"
    "覃可汐的房子是很古朴的红砖平房。这样来看其实家境并不是很好。"
    "可以理解为什么当初覃可汐会抱怨家里人不给她买游戏机了。"
    "房子里外都很喧闹。来的人很多。大部分都是中年人和老人。应该都是覃可汐的亲戚。"
    "由于还是白天，所以负责敲锣打鼓的仪仗队并没有来。"
    "从二楼阳台拉到对面楼房二楼阳台的遮雨布，构成了一个很大的“帐篷”。"
    "覃可汐的亲属们就是在这个“帐篷”底下布置桌椅，招揽宾客。"
    "几个小孩已经开始等上菜了。"
    "但我和叶梓澄此行目的并不是吃酒。"
    $ persistent.tips43 = True
    "叶梓澄把拿的花束分给了我一半。然后带我到了房子的{a=showmenu:tips43}{color=#F18D7D}堂屋{/color}{/a}。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    scene bg_kexi_syashin
    with dissolve
    $ persistent.cg15_unlocked = True
    play music sora fadeout 1.0 fadein 1.0
    "房间正中央放着一座棺材。棺材前面则堆满了花束和花圈。"
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
    play music "music/dead.ogg" fadeout 1.0 fadein 1.0
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
    play music "music/home.ogg" fadeout 1.0 fadein 1.0
    "呼！~"
    scene bg_byouin
    with fade2
    "看着陌生的天花板。再次醒来时发现自己身处医院。"
    c "啊？林洛你醒了！"
    "旁边传来一阵女声。"
    show zicheng_pose1 eyes4 mouth1 at jin
    with dissolve
    "是班长。"
    l "班长......我这是......"
    show zicheng_pose1 mouth5 at jin
    with dissolve
    voice v3
    c "你先躺下，慢慢来别急。"
    show zicheng_pose1 mouth3 at jin
    with dissolve
    voice v3
    c "你出车祸了。我是来看望你的。"
    l "是吗......医生怎么说？"
    hide zicheng_pose1
    show zicheng_pose2 mouth1 other2 other1 at jin
    with dissolve
    voice v1
    c "额...那个......"
    "有了不好的预感。"
    "大概已经猜到了。"
    hide zicheng_pose2
    show zicheng_pose1 mouth3 eyes3 at jin
    with dissolve
    voice v3
    c "其他一切正常。就是你的腿...可能以后必须坐轮椅了......"
    "果然吗？"
    "为什么？为什么我会这么倒霉！？"
    "不过......至少捡回了一条命不是吗？"
    l "班长...我逐渐理解你了。"
    show zicheng_pose1 mouth5 other2 at jin
    play audio odoro
    with vpunch
    c "？"
    l "接二连三的挫折。既然没有打倒我，那我就必须继续走下去，人生的这条道路。"
    l "班长你也是这么想的对吧！"
    hide zicheng_pose1
    show zicheng_pose2 eyes2 mouth1 at jin
    with dissolve
    c "嗯..."
    "班长微微点了点头。"
    l "啊！那个...对了！"
    l "我大概躺了多久？"
    hide zicheng_pose2
    show zicheng_pose1 eyes5 at jin
    with dissolve
    c "已经两个星期了..."
    show zicheng_pose1 mouth3 at jin
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
    show zicheng_pose1 eyes7 at jin
    with dissolve
    play music speak fadeout 1.0 fadein 1.0
    voice v1
    c "字面意思！"
    "班长解释道。"
    hide zicheng_pose1
    show zicheng_pose2 eyes2 at jin
    with dissolve
    voice v3
    c "这个所谓的“武器”。会产生一种类似辐射的东西。并不会直接作用于人体。"
    voice v3
    c "而是会作用于环境。"
    "什么意思？我还是听的一头雾水。"
    hide zicheng_pose2
    with dissolve
    "班长似乎也知道很晦涩难懂。又转身从包里拿出来一本被牛皮包裹的笔记本。"
    show zicheng_pose1 eyes3 mouth3 at jin
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
    c "但是跟AADR不同。我父亲确确实实好几年前就已经成功实现了把物体的构成物质，原子进行拆分重组来构成了一种新的物质粒子，这种新的物质粒子，可以进行存储和还原，并且支持以光速进行运动。"
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
    show zicheng_pose2 eyes2 at jin
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
    show zicheng_pose1 eyes3 mouth3 at jin
    with dissolve
    voice v5
    c "实际上这也是我看了父亲的笔记本以后才知道的。父亲秘密制造了这台仪器。但我找不到任何关于制造这台仪器有关的信息。"
    voice v3
    c "也不知道这台机器的注入零子的具体运作原理，恐怕只有我父亲本人才知道了。"
    voice v3
    c "或许是有不得已的原因，父亲从来没有告诉过我。但或许已经告诉过我的母亲。"
    show zicheng_pose1 eyes6 mouth4 at jin
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
    show zicheng_pose2 eyes2 at jin
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
    show zicheng_pose2 eyes2 mouth1 other2 at jin
    with dissolve
    voice v5
    c "丢入了转换成零子的仪器，然后将我父亲转换成的零子注入了时间刻校正仪。"
    l "也就是将你父亲身体转换成的零子注入了更高维度是吧。"
    "我插话道。"
    show zicheng_pose2 eyes2 mouth2 at jin
    with dissolve
    voice v5
    c "嗯！证据就是，我接到警察电话去领我父亲遗体的时候，只看到了一只手臂。手臂断口处残留着零子。"
    l "所以注入到更高维度的零子对我们所处纬度的干涉到底是什么？"
    voice v3
    c "我父亲并没有在我找到的这个笔记本里写出。但是我推测是："
    voice v3
    c "会影响本维度物质之间的不稳定性！就像降水拍打海面会激起涟漪，拍出海浪和水花一样。"
    voice v3
    c "因为，沁野市自从我父亲遇害以后。从覃可汐开始，意外事故不断发生。"
    voice v3
    c "覃可汐也好，你也好，都是受了这个影响。"
    show zicheng_pose2 eyes2 mouth1 other2 at jin
    with dissolve
    voice v5
    c "实际上在你住院以后两个星期之间，沁野市至少又发生了七起意外事故。涉及到车祸，火灾和楼房坍塌。"
    voice v3
    c "媒体已经将沁野市报道为不幸之城了。"
    voice v3
    c "再加上AADR亲口出面承认沁野市目前的处境是AADR所为。"
    hide zicheng_pose2
    show zicheng_pose1 eyes3 mouth3 at jin
    with dissolve
    voice v3
    c "更加坚定了我的说法！"
    l "如果是往更高维度注入零子影响我们所处的维度的话。那为什么只有沁野市受到了影响？不应该是全世界都受影响吗？"
    show zicheng_pose1 eyes7 mouth3 at jin
    with dissolve
    voice v3
    c "不是这样的。我推测零子所注入的那层更高维度，平行浮于我们所处的维度之上。"
    hide zicheng_pose1
    show zicheng_pose2 eyes2 at jin
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
    show zicheng_pose1 eyes4 mouth1 at jin
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
    show zicheng_pose1 eyes4 at jin
    play audio odoro
    with vpunch
    voice v1
    c "对！"
    "叶梓澄说道。"
    "看她的表情并不像是在开玩笑。"
    l "怎么做？"
    "虽然感到很震惊。但我还是选择相信叶梓澄，以及她父亲的研究成果。"
    hide zicheng_pose1
    show zicheng_pose2 at jin
    with dissolve
    voice v3
    c "需要做两件事。"
    voice v3
    c "对抗AADR。以及。"
    show zicheng_pose2 other2 at jin
    with dissolve
    voice v3
    c "制造时间机器。"
    l "时间机器？"
    "叶梓澄继续说道。"
    show note:
      xcenter 0.2
      ycenter 0.3
    with dissolve
    show zicheng_pose2 eyes2 at jin
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
    show zicheng_pose1 mouth5 other1 at jin
    play audio odoro
    with vpunch
    voice v3
    c "啊对不起......揭起你的伤疤了...我换一个比喻..."
    l "啊没事的......你继续说就行了..."
    hide zicheng_pose1
    show zicheng_pose2 mouth3 at jin
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
    show zicheng_pose2 at jin
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
    show zicheng_pose1 eyes2 mouth4 at jin
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
    show zicheng_pose1 eyes2 mouth1 at jin
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
    show linluo_pose pose2 other2 at jin
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
    show linluo_pose eyes2 mouth1 other1 other2 at jin
    play audio odoro
    with vpunch
    "我又上前抓住了他的手。"
    "去找叶梓澄！"
    "这是我最后的提示了。也是我最后能说出口的几个字了。"
    show linluo_pose pose2 eyes2 mouth1 other2 at jin
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
    "时间跳跃手表！"
    "对不住了。过去的我自己。"
    "接下来的你可能会面临各种各样的苦难。"
    "但是你一定要坚持下来！"
    "不仅是为了你自己！更是为了打破AADR在未来的残暴统治！"
    "就这样吧。"
    "准备收摊了，去哪都无所谓。死了也无所谓。如果过去的我真的改变了时间的轨迹，那我大概率会被再构成掉吧......"
    $ end = 1
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
    return
#拿手表
label havewatch:
    $ havewatch = True
    hide noko
    hide hold_watch
    with dissolve
    "恶意揣测别人的好意是不对的。我就勉为其难的收下吧。特别是想到进入学校以后我的手机还得上缴。有一块手表也更方便看时间。"
    l "谢谢！"
    show watch_off:
      xcenter 0.2
      ycenter 0.3
    with dissolve
    "我接过了手表。是一块黑色的电子表。"
    show watch_on:
      xcenter 0.2
      ycenter 0.3
    with dissolve
    "开机了。不过貌似仅仅只能显示时间。有点失望，还以为能玩玩俄罗斯方块什么的。虽然长得像个智能手表。但一点也不智能。"
    $ persistent.tips05 = True
    $ persistent.tips06 = True
    "拿这个手表上{a=showmenu:tips05}{color=#F18D7D}cq{/color}{/a}或者看{a=showmenu:tips06}{color=#F18D7D}番剧{/color}{/a}看来是不现实了。"
 #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     
#词典

    hide watch_on
    hide watch_off
    l "老板这表多少钱？"
    "天上没有免费的午餐，有点担心老板是先交货后付款这类强买强卖。我还是试探性地问了问价钱。"
    voice v3
    t "不需要钱。只是，希望你能，一直，戴着它。"
    "摊主用嘶哑的声音说到。"
    "戴上手表以后我就转身准备进校门了。这时那位摊主仿佛突然想起了什么似的。又拉住了我的手臂。"
    play sound odoro
    with vpunch
    voice v1
    t "去找叶梓澄！"
    "叶梓澄是谁？我在脑海中不断搜索着叫这个名字的人。"
    "结果是查无此人。"
    l "叶梓澄......我认识他吗？"
    "我有礼貌地问道。"
    voice v3
    t "以后你会认识的。"
    "说罢便松开了抓着我手臂的手。并示意我快进去。"
    hide storer
    scene bg_school_door
    with fade
    play music richang fadeout 1.0 fadein 1.0
    b "没见过你啊？哪个班的？"
    l "额？"
    "校门口保安不肯放我进去。最后打电话给我的新班主任确认了好半天以后才同意让我进学校。"
    "对这个学校的好感度-1。我在心里想着。"
#手表
    $ years = "2022.9.19"
    $ times = "12:27"
    $ weeks = _("周一")
    #手表
    show screen watch
    with dissolve
    "用刚得到的手表看了看时间。"
    "额啊！都快到午饭时间了。现在不赶紧去教室的话可能会被冲去吃饭的学生给推出来。"
    "暂时还不想做逆行者。虽然不确定这个学校吃午饭用不用赛跑。但是毕竟这方面全国统一。"
    play sound "audio/run.ogg"
    "我加快了脚步，跑了起来。"
    scene bg_school_basketball
    with fade
    $ times = "12:29"
    play sound suzu
    scene bg_2_3
    with fade
    "我刚一跑到教室门口。一阵清脆的铃声就响起了。"
    play sound "audio/yakamashii.ogg"
    "班上的学生都像没看到我就站在门口一样。纷纷从座位上下来往教室门口挤过去。仿佛在参加竞速比赛一样。"
    scene bg_school_humans
    with fade
    $ times = "12:30"
    "我顿时被从从教室里涌出来的人群所淹没。"
    "整个人被人群连带着往教室外面后退了三米多。"
    scene bg_2_3
    with fade
    $ times = "12:31"
    stop sound
    "直到大家都冲出去了。我才能好好地看着即将迎接我的新教室的模样。"
    "班级是三班。所以教室就在一楼。对下课吃饭的人来说简直是绝佳的地理位置。"
    scene bg_school_soto
    with dissolve
    "还有一点比较好，可以透过一楼的窗户直接看到走廊外面的广场。"
    "应该是叫广场吧。反正就是教学楼前面到大屏幕告示板之间的一块空地。走廊外面的人工种植的草地也可以直接看见。"
    "大屏幕告示牌后面有一条人工河，通过桥梁连接着对岸的篮球场以及学校大门。"
    "河对岸栽种的几颗桂花树也能看得清楚。只是这个季节已经没有桂花了。估计得明年春天才有的看了。"
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
    s "林洛是吧？刚刚保安打电话的时候有跟我说过。我是你的班主任，叫我李老师就可以了。"
    s "你先坐那个位置吧！正好那里现在没人！"
    scene bg_class_naka
    with dissolve
    $ times = "12:32"
    "老师伸手指向了一个后排靠窗的座位。"
    scene bg_2_3
    with dissolve
    show sensei1_pose eyes2 at jin
    with dissolve
    $ times = "12:33"
    voice v5
    s "这个点大家都去吃饭去了。你把东西收拾好了也去吃饭吧。食堂就在教学楼左侧，一条路一直走过去就到了。"
    s "中午好好休息顺便准备一下。下午上课的时候你做个自我介绍向大家展示一下自己吧。"
    l "好的老师！"
    "我虽然表面上面无表情。但是心里乐开了花。"
    $ persistent.tips08 = True
    "这可是后排靠窗的位子啊！主角专用座位。我就是{a=showmenu:tips08}{color=#F18D7D}地球online{/color}{/a}的主角！"
     #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    scene bg_tukue
    with fade
    $ times = "14:20"
    play sound suzu
    play music school fadeout 1.0 fadein 1.0
    $ persistent.music_school = True
    "在座位上坐立不安地终于熬到下午了。"
    s "这节课，我们要欢迎一位新同学。"
    scene bg_kyoudan
    with dissolve
    $ times = "14:25"
    "班主任在讲台上说完。便看向了我，示意我上讲台。"
    "虽然很紧张。但还是不得不上去。"
    "只能硬着头皮上了。"
    play sound "audio/yakamashii.ogg"
    scene bg_stand_kyoudan
    with fade
    $ times = "14:26"
    l "大家好...我叫林洛...来自芷柚市...因父母工作变动，搬家来到沁野市..."
    "感觉我全身都在发抖。尤其是班上同学都盯着我的脸看的时候。"
    "但我还是必须强作镇定。一定要给同学们留下好印象。"
    l "爱好是画画还有打游戏......以及...看动画..."
    "听到班上有几个同学在偷笑了。果然又是刻板印象。估计是觉得高中生了还看动画很幼稚。我的评价是看少了。"
    "当然我没有说出来，可不想在开学第一天就结仇。"
    scene bg_ojigi
    with dissolve
    $ times = "14:30"
    l "总之...以后请...多多关照！"
    play sound "audio/hakusyu.ogg"
    "我低头鞠躬。班主任鼓起了掌。同学们也附和着。教室里充满了同学们的掌声。"
    scene bg_stand_kyoudan
    with dissolve
    $ times = "14:31"
    s "大家要多多照顾新同学！新同学你有什么不懂的也尽管找同学们帮忙！这位是班长叶梓澄。有事找她就可以了！"
    scene bg_stand_kyoudan:
        xalign 0.0 yalign 0.0
        xzoom 1.0  yzoom 1.0
        linear 1.0 xalign 0.5 xzoom 1.5 yalign 0.5  yzoom 1.5 
    $ times = "14:33"
    "班主任用手指向坐在第一排的一个女生。"
    "是一个紫色头发的女孩子，梳着单马尾。本来是面无表情的，被老师点名以后看向了我，脸上挤出了一副营业式笑容。"
    "等等？叶梓澄？"
    scene bg_schoolmae
    show storer
    show noko
    with fade
    play music lanzhu fadeout 1.0 fadein 1.0
    "我猛地想起了在校门口遇到的那位摊主的话。"
    t "{cps=5}{size=50}去-找-叶-梓-澄！{/size}{/cps}"
    "叶梓澄跟校门口那位摊主是有什么关系吗？我计划着下课问问。"
    play music school fadeout 1.0 fadein 1.0
    scene bg_tukue
    with fade
    $ times = "15:00"
    "下课了。"
    "我在座位上支支吾吾了半天以后终于还是鼓起勇气走到了班长叶梓澄的座位旁边。"
    scene bg_class_naka
    with dissolve
    show zicheng_pose1 eyes7 mouth1 at jin
    with dissolve
    $ times = "15:03"
    voice v3
    c "啊~是转校生啊。你叫林洛是吧。请多关照。"
    l "我......"
    "话到嘴边却说不出来。因为我还没构思好自己应该怎么提问。"
    l "校门口摊位那里......有个坐轮椅的中年人...你认识吗？"
    show zicheng_pose1 eyes7 mouth3 at jin
    with dissolve
    "叶梓澄一脸疑惑地看着我。"
    voice v3
    c "我不记得校门口有看过坐轮椅的人。是摆摊的人还是路过的路人？"
    l "摆摊的。"
    voice v1
    c "没有。"
    "叶梓澄摇了摇头。"
    "我感到一阵不安。"
    l "真的没有吗？一个戴着帽子的中年人。声音很嘶哑。坐着轮椅。就在出校门到公路旁边，第一个摊位那里。"
    "我努力地提供关键词，希望班长可以想起来什么。"
    l "哦对了。那个摊主给了我一块电子表。"
    hide screen watch
    with dissolve
    show watch_look
    with dissolve
    play music lanzhu fadeout 1.0 fadein 1.0
    "我把手举起来把戴着的电子表展示给她看。"
    hide zicheng_pose1
    show zicheng_pose2 at jin
    with dissolve
    voice v7
    c "第一个摊位吗？我不清楚是不是你说的那个。原本校门口到公路的转角处是没有摊位的。但是从前天开始就不知道是谁在那里搭了一个摊。"
    voice v3
    c "但是那个摊位没有人看守，也没有摆放任何商品。"
    voice v5
    c "说没人看守可能不太严谨。我每天早上七点半上学和每天下午五点半放学的时候没有看到有人在那里。"
    "难道这个摊主专挑学生上下学以外的时间摆摊吗？"
    "但是我路过的时候，摊位上也什么商品都没有。除了那块手表。"
    "我还以为是商品卖光了。都不在上下学高峰期摆摊。怎么可能卖光。"
    "恐惧和不安涌上了心头。只有一个理由说得过去了。"
    "那位摊主可能是在等我出现。"
    "我看着我这块手表。愈发感到害怕。"
    hide watch_look
    with dissolve
    show screen watch
    with dissolve
    l "没事了。谢谢班长。"
    scene bg_tukue
    with fade
    $ times = "15:08"
    play music school fadeout 1.0 fadein 1.0
    "我回到了座位上。虽然摊主告诉过不要摘下手表。但我还是将它摘下来打算检查一下。"
    hide screen watch
    with dissolve
    show watch_miru:
      xcenter 0.2
      ycenter 0.3
    with dissolve
    play sound suzu
    "一直研究到上课都没发现什么端倪。整个手表都没看到可能是针孔摄像头的地方，也没看到可能是麦克风的洞。重量实际上比较轻，但是感觉不到廉价感。"
    hide watch_miru
    with dissolve
    $ times = "15:11"
    show screen watch
    with dissolve
    "最后我还是决定放学后亲自质问。"
    "额...如果叶梓澄所言属实.那我放学后就见不到他了。"
    scene bg_tukue
    with fade
    play sound suzu
    $ times = "17:30"
    "终于放学了。"
    "收拾完作业，拿到手机以后。我就背上书包跑出教室。"
    scene bg_2_3
    with dissolve
    "得去看一下给我手表的摊主还在不在那个地方。"
    $ times = "17:35"
    scene bg_school_soto
    with dissolve
    "嗯？有一个人站在两边种满桂花树的那条路上。" 
    scene bg_sorawomiru
    $ persistent.cg04_unlocked = True
    with fade
    $ persistent.music_sora = True
    play music sora fadeout 1.0 fadein 1.0
    $ times = "17:37"
    "是叶梓澄。"
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
    $ times = "17:39"
    scene bg_xinoyobu:
        xalign 0.0 yalign 0.0
        xzoom 1.0  yzoom 1.0
        linear 1.0 xalign 0.07 xzoom 1.5 yalign 0.5  yzoom 1.5
    $ times = "17:40"
    "朝着声音来源的方向看去。是今天班上我座位旁边坐着的那个女生。也就是我的同桌。"
    "我今天一直在想那个摊主的事，并没有问她的名字。"
    "她靠着校门口附近的一棵桂花树，伸手呼唤我过去。"
    l "怎么了？"
    "支线任务：去见同学。"
    "我心里这么想着。"
    scene bg_kinoshita
    with dissolve
    show kexi_pose at jin
    with dissolve
    play music kexi fadeout 1.0 fadein 1.0
    $ times = "17:41"
    voice v5
    x "那个...我就长话短说了。你，，，或者你的亲属。以前是否来过沁野市。"
    l "没有。"
    show kexi_pose eyes2 mouth3 at jin
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
    show kexi_pose eyes1 mouth1 at jin
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
    show kexi_pose2 mouth1 at jin
    with dissolve
    voice v3
    x "嗯~明天见。真是不好意思占用了你很多时间..."
    scene bg_school_nakato
    with dissolve
    play sound "audio/run.ogg"
    play music school fadeout 1.0 fadein 1.0
    $ times = "17:44"
    "覃可汐一边挥着手一边跑着出了校门。没看到是朝左还是朝右边走的了。"
    "我也紧随其后打算出校门。"
    "突然我想到了什么，朝身后张望了一下。"
    scene bg_sorawomiru2
    $ persistent.cg05_unlocked = True
    with dissolve
    play music sora fadeout 1.0 fadein 1.0
    $ times = "17:45"
    "叶梓澄依然站在道路中间，仰望着天空。"
    scene bg_schoolmae
    with fade
    play music lanzhu fadeout 1.0 fadein 1.0
    $ times = "17:47"
    "出了校门。"
    "摊位不见了。"
    "不是说没人在摊位上。而是整个摊位都被收走了。不管是遮阳伞还是铺在地上的地摊。仿佛这里以前没人搭过摊一样。"
    "我心头一震。"
    "有生以来第一次感到如此害怕。"
    scene bg_none
    with fade
    play music "music/omou.ogg" fadeout 1.0 fadein 1.0
    $ times = "23:07"
    "晚上回到家中以后也睡不着。"
    "辗转反侧，感觉仿佛有人一直在看着我。在床底下，还是衣柜里？"
    scene bg_home
    with fade
    $ persistent.music_home = True
    play music "music/home.ogg" fadeout 1.0 fadein 1.0
    $ years = "2022.9.20"
    $ times = "07:07"
    $ weeks = _("周二")
    "天亮了。昨天晚上不知道什么时候睡着的。"
    "总之很困。得赶紧去学校。因为离得比较远。来不及吃家里的早餐了。"
    scene bg_kuruma_matu
    with fade
    play music richang fadeout 1.0 fadein 1.0
    $ times = "07:15"
    $ persistent.tips10 = True

    "在公交站牌旁边的移动商贩那里买了点{a=showmenu:tip10}{color=#F18D7D}油陷{/color}{/a}。"
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
    $ times = "07:28"
    car "{color=#C1394F}尊敬的旅客您好！沁野市高级中学站到了！请各位旅客有序下车！谢谢！{/color}"
    scene bg_schoolmae
    with fade
    "到学校了。"
    stop sound
    "一路汽车颠簸。我现在已经没有食欲了。"
    l "呕~"
    "喉咙发酸。但还是被我憋回去了。如果学校离得再远一点我可能就控制不住了。"
    "消失的摊位并没有回来。"
    "经历了一晚上以后我的心情逐渐平复了下来。"
    "虽然尚不明白摊主想干什么。但是谜团只能等以后再次遇到他了才能解开了。"
    scene bg_tukue
    with fade
    play music school fadeout 1.0 fadein 1.0
    $ times = "08:02"
    "第一节课是英语课。反正英语老师还不认识我。而且我坐在后排。正好睡一觉。"
    scene bg_none
    with fade
    $ times = "12:33"
    "似乎不小心睡过了头。一觉醒来已经是正午了。"
    scene bg_tukue
    with dissolve
    l "呜~呃~"
    "大家似乎都去吃午饭了。我也打算去食堂。"
    scene bg_tukue2
    with dissolve
    show zicheng_pose1 mouth3 at jin
    with dissolve
    $ times = "12:34"
    "这时班长走了过来。"
    "？班长没去吃饭吗？"
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
    "突然想起来昨天班主任就告诉过我吃饭要办饭卡。但那时候我一直在想别的事就给忘了。"
    "救星来了。我除了感激还是感激。"
    scene bg_gohan
    with fade
    $ times = "12:44"
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
    scene bg_gohan2
    with dissolve
    $ times = "12:47"
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
    $ times = "12:50"
    "额这......好不容易到我了。才发现今天的菜里有青椒。而且这个学校的食堂每顿饭固定四个菜不能换。"
    "我不由得面露难色。"
    scene bg_gohan_tukue
    with dissolve
    $ times = "12:52"
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
    $ times = "12:54"
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
    $ times = "12:57"
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
    "就这样我们边吃边聊，唠了十几分钟的动画片。最后赶在午睡之前才踩点回到教室。"
    scene bg_class_naka
    with fade
    show zicheng_pose1 mouth1 at jin
    with dissolve
    $ times = "14:11"
    l "你还知道班上有哪些故事厨吗？"
    "我顾不上羞耻了。午睡一结束就跑过来问叶梓澄。"
    voice v3
    c "你同桌就是一个哦~"
    "什么？故事厨竟在我身边！"
    scene bg_kinoshita
    show kexi_pose at jin
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
    $ times = "15:02"
    "下课了。我假装来抄课程表。走到了教室前面黑板旁边。"
    "黑板旁边贴的不止有课程表。还有值日人员表。"
    "抄完了。顺便看到了名字："
    scene bg_kexi
    with dissolve
    show bg_syuucyuu
    $ times = "15:03"
    "覃可汐。"
    "是叫这个名字。毕竟她跟我一样是星期五值日。"
    "不行啊，得赶紧想个办法。"
    scene bg_tukue
    with fade
    $ times = "15:21"
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
     
#词典
    show kexi_pose2 mouth3 at jin
    with Dissolve(1)
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
    $ times = "15:51"
    "下课了。"
    "有谁在戳我。"
    scene bg_kexi_egao
    $ persistent.cg03_unlocked = True
    with dissolve
    $ times = "15:52"
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
    hide screen watch
    with dissolve
    scene bg_none
    with fade
    play music richang fadeout 1.0 fadein 1.0
    "坐着放学后的公交。我开始回想今天发生的事。"
    play music "music/home.ogg" fadeout 1.0 fadein 1.0
    "认识了两个同好。班长叶梓澄。以及...同桌覃可汐。"
    "那个摊主依旧没有看到。但我已经慢慢地开始不在意这些事了。"
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
    "今天晚上我睡得很香甜。开始期待以后有更好的校园生活了。"
    scene bg_kuruma_matu
    with fade
    $ years = "2022.9.21"
    $ times = "06:51"
    $ weeks = _("周三")
    show screen watch
    with dissolve
    "跟往常一样起床打算去学校。"
    "已经逐渐开始习惯新学校的生活了。"
    scene bg_tukue
    with dissolve
    $ times = "07:19"
    play music school fadeout 1.0 fadein 1.0
    play sound "audio/yakamashii.ogg"
    "今天到的比较早。早自习也还没开始。"
    "班上很热闹。同学们三两成群地在聊天。"
    "覃可汐似乎还没来。"
    "反正无事可做。觉得是时候开始新的冒险了。"
    scene bg_egaku
    with dissolve
    $ times = "07:21"
    "拿出了平时画画的本子。开始构思创作新的角色和世界观。"
    x "画的啥？"
    scene bg_kexi_egao
    with dissolve
    $ times = "07:24"
    "啊可恶！画的太入迷了完全没在意周围的环境。回过神来的时候覃可汐的头已经凑了过来。"
    "正打算用肩膀遮挡。"
    "已经来不及了。整个画本被她抽了过去。"
    scene bg_tukue2
    with dissolve
    show kexi_pose2 mouth1 at jin
    with dissolve
    $ times = "07:25"
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
    $ times = "07:26"
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
    $ times = "07:27"
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
    $ times = "09:00"
    play sound suzu
    "时间过得好快。到了课间休息的时间了。"
    scene bg_class_naka
    with dissolve
    $ times = "09:01"
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
    $ times = "09:03"
    voice v3
    s "叶梓澄！你来一下办公室。"
    "班主任面色很沉重地说道。"
    scene bg_class_naka
    with dissolve
    show zicheng_pose2 at jin
    with dissolve
    $ times = "09:01"
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
    $ times = "09:10"
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
    $ times = "09:50"
    "下课了。"
    "但是班长却收拾了书包。"
    "准备出教室了。"
    "这是要去哪？回家吗？"
    scene bg_2_3
    with dissolve
    show zicheng_pose1 eyes6 mouth4 at jin
    with dissolve
    $ times = "09:52"
    l "叶梓澄！你这是......"
    voice v3
    c "抱歉，林洛。我有事必须得回去一趟了。"
    l "哦。是吗？好吧。"
    scene bg_school_soto
    with dissolve
    $ times = "09:56"
    "看着班长渐渐走出校门。各种不安涌上心头。"
    scene bg_none
    with fade
    "那一整天班长都没有再回来。"
    scene bg_schoolmae
    with fade
    $ times = "17:41"
    play music richang fadeout 1.0 fadein 1.0
    "下午放学后。我和覃可汐约定好在校门口“交货”。"
    show kexi_pose mouth1 at jin
    with dissolve
    l "好好照顾它哟！"
    "我如此告诫道。除了家里的电脑以外，这台掌机就是我最珍贵的伙伴了。"
    hide kexi_pose
    show kexi_pose2 mouth4 at jin
    with dissolve
    voice v3
    x "嗯！我今晚通宵了明天就还你。"
    scene bg_none
    with fade
    play music school fadeout 1.0 fadein 1.0
    "已经星期四了。班长还没来。"
    scene bg_tukue
    with fade
    $ years = "2022.9.22"
    $ times = "07:30"
    $ weeks = _("周四")
    play sound suzu
    "伴随着上课铃。覃可汐背着书包匆忙地冲了进来。"
    scene bg_tukue2
    with dissolve
    show kexi_pose mouth1 at jin
    play audio odoro
    with vpunch
    $ times = "07:31"
    voice v3
    x "呼！呼！呼！差一点就迟到了！"
    voice v3
    x "林洛那个.....商量个事呗！"
    l "申请多玩一天对吧！"
    nvle "我如此答道。感觉自己渐渐和其他人的距离变近了。"
    nvle "没有以前那样害怕和别人交谈了。这就是找到朋友的感觉吗？"
    nvl clear
    show kexi_pose eyes3 mouth3 at jin
    with dissolve
    voice v5
    x "啊啊啊谢谢！我跟你讲我昨天有个馆主一直打不过。克制我全队的属性。啊啊~"
    show kexi_pose eyes5 at jin
    with dissolve
    voice v3
    x "打了几个小时都打不过！身上的钱全都输光啦！"
    voice v3
    x "最后只能抓了只属性克制的精灵一直练级。结果一直没睡！"
    l "我的天！你说的通宵是真的通宵啊！"
    l "你还在上高中啊！你还要上学啊！"
    l "你这么搞，什么时候倒学校里了都不稀奇。"
    hide kexi_pose
    show kexi_pose2 mouth3 at jin
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
    show kexi_pose eyes2 at jin
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
    $ times = "17:15"
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
    scene bg_schoolmae
    with fade
    $ times = "17:43"
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
    hide screen watch
    with dissolve
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
    $ years = "2022.9.23"
    $ times = "06:30"
    $ weeks = _("周五")
    show screen watch
    with dissolve
    play music "music/home.ogg" fadeout 1.0 fadein 1.0
    "呼！！！"
    "做了一个噩梦。醒来时还是大早上。"
    scene bg_tv
    with dissolve
    $ times = "06:35"
    "朝阳才刚刚升过山头。该去上班的父亲也还在客厅里吃着早餐看电视。"
    scene bg_tvnews
    with dissolve
    tv "AADR美国总部今日展示了他们研究团队的最新研究成果。据悉该研究成果将颠覆未来人们的时空观念......"
    scene bg_tv
    with dissolve
    $ times = "06:39"
    "电视台的新闻这样报道着。"
    "AADR？好像昨天上课也听到过这个组织的名字。"
    scene bg_none
    with fade
    "起得比较早。所以我干脆直接在家里吃了早餐了。"
    scene bg_tukue
    with fade
    $ times = "07:08"
    play music school fadeout 1.0 fadein 1.0
    "到达学校的时候离正式上课还有很久。"
    "班长也还没来。"
    "不会今天还是请假吧。"
    "不会的。我相信班长。"
    "昨天通话的时候也说过了会来的。"
    scene bg_tukue
    with fade
    $ times = "07:28"
    "快上课的时候。班长终于来了。紧随其后的是覃可汐。"
    scene bg_tukue2
    with dissolve
    show kexi_pose mouth1 at jin
    play audio odoro
    with vpunch
    voice v1
    $ times = "07:29"
    x "呼~呼~赶上了。"
    l "你又通宵了对吧。"
    voice v3
    x "那个......可不可以......"
    l "再让你玩一天对吧！"
    hide kexi_pose
    show kexi_pose2 mouth3 at jin
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
    show kexi_pose eyes3 mouth3 at jin
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
    show kexi_pose2 mouth4 at jin
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
    show kexi_pose2 mouth3 at jin
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
    show kexi_pose2 mouth2 at jin
    voice v3
    x "嗯......这确实是个问题......"
    show kexi_pose2 mouth3 at jin
    voice v3
    x "不过没关系！你就来帮我提包.....你就来陪我们一起逛就行！"
    "喂！绝对是说漏嘴了什么对吧！"
    scene bg_tukue
    with fade
    play sound suzu
    $ times = "07:31"
    "上课了！"
    "但覃可汐明显意犹未尽的样子。"
    l "咿啊！"
    scene bg_kexi_egao
    with dissolve
    "被覃可汐拿笔戳了手臂。"
    "然后覃可汐便递给我一个纸条。上面写着："
    scene bg_kami
    with dissolve
    $ times = "07:32"
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
    $ times = "08:10"
    play sound suzu
    "下课了。"
    scene bg_tukue2
    with dissolve
    show kexi_pose2 mouth3 at jin
    with vpunch
    $ times = "08:11"
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
    $ times = "08:13"
    "在我犹豫不决的时候覃可汐已经写好了一张新的纸条。递给了我。"
    "然后继续摆出期待的摸样。"
    scene bg_tukue2
    with dissolve
    show kexi_pose mouth1 at jin
    with dissolve
    $ times = "08:14"
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
    $ times = "08:16"
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
    voice v3
    x "没事的班长！打起精神啊！明天我们一起去漫展吧！"
    "覃可汐开口了。"
    hide kexi_pose
    show kexi_pose mouth1 at jin:
        xpos 0.8
    voice v3
    x "我上次给你订做了一套cos服！明天你一定要穿穿看！"
    show zicheng_pose1 eyes4 mouth3 at jin
    with dissolve
    voice v3
    c "哦......好！谢谢！那......在哪见面。"
    voice v3
    x "我家！你上次去过的应该还记得路吧！"
    voice v1
    c "哦！好！"
    l "对了！林洛明天也会来。这样就有三个人了！"
    "我不好意思地后退了退。"
    "跟在两个女孩子之后，感觉我格格不入。像个边缘人。"
    "到时候一定很束手束脚吧。"
    "我这样想着。"
    scene bg_tukue
    with fade
    play sound suzu
    $ times = "08:20"
    "上课了。"
    "我写了一张纸条，递给覃可汐。"
    "内容是：叶梓澄要跟祖父母住一起了，她的母亲呢？"
    scene bg_tukue
    with fade
    $ times = "08:24"
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
    $ times = "12:30"
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
    $ times = "12:40"
    "要是失约了，覃可汐会对我失望的！"
    "我一边这样想着一边狼吞虎咽着。生怕错过了约定时间。"
    scene bg_gohan_tukue
    with fade
    $ times = "12:45"
    "吃完了。"
    "第一次吃这么快。只花了五分钟。"
    "很好！离约定时间还有五分钟。我一气呵成地收拾餐具，然后往教学楼飞奔。"
    play sound run
    scene bg_2_3
    with fade
    $ times = "12:48"
    l "呼~呼~"
    "啊！腹部一阵剧痛。但是我也不清楚为什么每次刚吃完饭再跑步就会很痛。"
    "我扶着教室门框，覃可汐已经拿着两把扫把和一个铲子在讲台上等我了。"
    scene bg_class_naka
    with dissolve
    show kexi_pose mouth1 at jin
    with dissolve
    $ times = "12:49"
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
    scene bg_school_hiroba
    $ persistent.cg11_unlocked = True
    with dissolve
    $ times = "12:52"
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
    scene bg_school_hiroba2
    $ persistent.cg12_unlocked = True
    with dissolve
    $ times = "12:54"
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
    play music "music/dead.ogg" fadeout 1.0 fadein 1.0
    $ times = "12:56"
    with vpunch
    "嘭！"
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
    voice v3
    c "啊......啊......"
    "叶梓澄叫着。"
    c "覃可汐......"
    c "覃可汐她......"
    "这一切发生的过于突然。"
    "刚刚还生龙活虎的覃可汐..."
    "头部被一个花盆砸中了。"
    "倒在了地上。"
    "身体开始淌出鲜红的血来......."
    "我被吓得愣在了原地。"
    "叶梓澄也是，直接呆在了原地。"
    "路过的行人也停住了脚步，朝这边看过来。"
    "办公室和教学楼里的同学也纷纷探出头来。"
    "时间仿佛凝固了。"
    "凝固了。"
    "我脸上没有表情。因为我已经吓得不敢做出任何其他动作了。"
    "手中的扫把不知道何时自己倒在了地上。是什么时候松手的也不知道了。"
    "覃可汐...她......"
    "一个离的最近的男老师穿过围观的人群走了过来。"
    s "大家！不要围观！不要围观！有序回到教室！"
    "然后拿出手机开始拨打急救电话。"
    c "林洛......覃可汐她......"
    "叶梓澄带着哭腔朝着我喊道。"
    "但我还是一动也不敢动。"
    "再次想起来昨晚的梦境。"
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
    play music "music/dead.ogg" fadeout 1.0 fadein 1.0
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
    $ times = "17:05"
    play music sora fadeout 1.0 fadein 1.0
    "不知过了多久。我坐在教室里。"
    scene bg_tukue2
    with dissolve
    "看着我旁边空无一人的座位。现在没有人，以后也不会有了。永远都不会有了。"
    "为什么......为什么刚好......"
    "回想着这一切的一切。"
    scene bg_tukue2
    show kexi_pose mouth1 at jin
    show noko
    with fade2
    "今天早上，覃可汐还在用着灿烂的笑容跟我在打招呼。"
    scene bg_tukue2
    show kexi_pose mouth1 at jin
    show noko
    with fade2
    "今天早上，覃可汐还在邀请我明天去参加ChieAnime。"
    scene bg_tukue2
    show kexi_pose mouth1 at jin
    show noko
    with fade2
    "覃可汐借的游戏机也还没来得及亲手还我......"
    scene bg_mado
    with dissolve
    $ times = "17:10"
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
    $ times = "17:14"
    "我看向叶梓澄。"
    "坚强如她也依旧在座位上啜泣。"
    "坚强如她也依然被接二连三的重大打击击垮了。"
    scene bg_tukue
    with fade
    $ times = "17:30"
    play sound suzu
    "放学了。"
    "校园内的空气死一般的寂静。"
    "天气依旧闷热。"
    scene bg_keikoku
    with dissolve
    $ times = "17:34"
    "我站在警戒线外面，看着地面上的血迹和粉笔画的线条。"
    "不知道看了多久。班长过来了。"
    show zicheng_pose1 eyes2 mouth4 at jin
    with dissolve
    voice v3
    c "林洛......回去吧......"
    scene bg_zicheng_te
    with dissolve
    $ times = "17:36"
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
    $ years = "2022.9.24"
    $ times = "08:03"
    $ weeks = _("周六")
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
menu:
     "来":
      jump come
     "不来":
      jump nocome
default come = False
#不去参加葬礼
label nocome:
    play music sora fadeout 1.0 fadein 1.0
    l "我还是......算了吧......"
    "事情已经发生了。现在去也只会徒增悲伤而已。"
    c "你真的......不想再看覃可汐最后一次吗？"
    "叶梓澄带着哭腔说道。"
    "我当然想！但是我做不到！"
    "我的腿已经吓软了。比起悲伤，更多的是恐惧。"
    "对死亡的恐惧。"
    l "我就不去了......对不起......班长..."
    l "我刚好有事脱不开身。"
    c "可是..."
    play sound "audio/ketai3.ogg"
    hide ketai_zicheng2
    with dissolve
    "我挂掉了电话。"
    "我逃避了。找了个借口逃避了。"
    "无法鼓起勇气去面对这个事实。"
    "覃可汐已死。"
    "这个事实。"
    "我做不到......"
    "对不起......覃可汐..."
    "永别了...覃可汐......"
    "对不起...叶梓澄......"
    hide screen watch
    with dissolve
    scene bg_home
    with fade
    play sound ame loop fadeout 1.0 fadein 1.0
    "今天我没有出门。一直把自己闷在家里。"
    "外面已经哗啦啦地下起了大雨。"
    "父母出门上班去了。家里只有我一个人。"
    "我试图用各种方法回避注意力。"
    "但无论我做什么都感觉没有意思了。"
    $ persistent.tips42 = True
    "平时最爱玩的{a=showmenu:tips42}{color=#F18D7D}《撒旦的结合》{/color}{/a}，开了游戏也只能对着游戏窗口发呆。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    scene bg_none
    with fade
    play music sora fadeout 1.0 fadein 1.0
    "永别了...覃可汐...以及...我的游戏机..."
    "如果有重来的机会就好了......"
    "已经开始胡思乱想了......"
    "浑浑噩噩地度过了一天......"
    $ persistent.come = False
    jump chapter1_5
#不去参加葬礼
#去参加葬礼
label come:
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
    $ times = "08:12"
    play music "music/home.ogg" fadeout 1.0 fadein 1.0
    "我找了一套比较体面的衣服。"
    "顺便抓了一把抽纸。"
    "不为别的，只是想到，到葬礼现场以后肯定眼泪会止不住的流下来。"
    "父母都出门上班去了。"
    "家里只有我一个人。"
    scene bg_kuruma_matu
    with fade
    play sound ame loop fadeout 1.0 fadein 1.0
    "我拿着雨伞出了门。"
    "因为一醒来外面就一直下着大雨。"
    "连苍天都对覃可汐的死感到可惜吗......"
    "今天的公交车来的格外的慢。等了差不多半个小时才有车过来。"
    scene bg_none
    with fade
    car "{color=#C1394F}尊敬的旅客您好！沁野市高级中学站到了！请各位旅客有序下车！谢谢！{/color}"
    scene bg_schoolmae
    with fade
    $ times = "08:58"
    "下车了。"
    show zicheng_2
    with dissolve
    "叶梓澄已经在校门口看起来像等了很久的样子。"
    "手里拿着一把花束。"
    c "走吧~"
    "叶梓澄没有多说什么。只说了这两个字。"
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
    $ times = "09:26"
    "我右脚踏出车外，目视着周围。"
    "覃可汐的房子是很古朴的红砖平房。这样来看其实家境并不是很好。"
    "可以理解为什么当初覃可汐会抱怨家里人不给她买游戏机了。"
    "房子里外都很喧闹。来的人很多。大部分都是中年人和老人。应该都是覃可汐的亲戚。"
    "由于还是白天，所以负责敲锣打鼓的仪仗队并没有来。"
    "从二楼阳台拉到对面楼房二楼阳台的遮雨布，构成了一个很大的“帐篷”。"
    "覃可汐的亲属们就是在这个“帐篷”底下布置桌椅，招揽宾客。"
    "几个小孩已经开始等上菜了。"
    "但我和叶梓澄此行目的并不是吃酒。"
    $ persistent.tips43 = True
    "叶梓澄把拿的花束分给了我一半。然后带我到了房子的{a=showmenu:tips43}{color=#F18D7D}堂屋{/color}{/a}。"
    #词典
     
    play sound "audio/tips.ogg"
    show screen tips_say
    with dissolve
    hide screen tips_say
    with tipsanime
     

#词典
    scene bg_kexi_syashin
    with dissolve
    $ persistent.cg15_unlocked = True
    play music sora fadeout 1.0 fadein 1.0
    "房间正中央放着一座棺材。棺材前面则堆满了花束和花圈。"
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
    $ times = "09:40"
    play sound ame loop fadeout 1.0 fadein 1.0
    "我和叶梓澄正打算坐着来的出租车离开。一个中年妇女拦住了我。"
    "林洛？你就是林洛对吧！"
    scene bg_kexihome
    with dissolve
    $ times = "09:41"
    l "啊？"
    "回头一看。"
    show kexihaha_pose at jin
    with dissolve
    play music sora fadeout 1.0 fadein 1.0
    voice v3
    m "我是覃可汐的妈妈。这几天老听女儿提到你的名字。"
    m "不打算多呆一会吗？"
    l "不了......谢谢阿姨..."
    m "哦对了！你等一会。"
    hide kexihaha_pose
    with dissolve
    "说罢覃可汐的母亲便回里屋了。"
    scene bg_kexihome
    with fade
    $ times = "09:43"
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
    hide screen watch
    with dissolve
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
    $ persistent.come = True
    jump chapter1_5
label chapter1_5:
    play music lanzhu fadeout 1.0 fadein 1.0
    "啪！"
    "睡梦中被什么东西吵醒了！"
    "我迷迷糊糊中睁开眼。"
    $ years = "2022.9.25"
    $ times = "01:20"
    $ weeks = _("周日")
    show screen watch
    with dissolve
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
    $ times = "12:54"
    "再次睁开眼时已是正午。"
    "啊！~"
    "睡了这么久了。"
    "高情商的说法便是："
    "提前体验了一次大学生的生活。"
    scene bg_home2
    with dissolve
    $ times = "13:10"
    "父母已经出门去了。"
    scene bg_tv2
    with dissolve
    $ times = "13:19"
    tv "今天早上十点半，挖掘泥沙的施工队在沁野市水潭村河段内挖出了一大块奇特的球状金属物体......"
    "刚打开的电视上这样报道着。"
    scene bg_home2
    with dissolve
    $ times = "14:30"
    "今天还是什么都不想做。"
    scene bg_none
    with fade
    "把作业做完了就一直等到天黑。然后睡觉了。"
    "即便出了这种事故，明天依旧要照常上课。"
    "大人的世界是浑浊的。"
    scene bg_home
    with fade
    $ years = "2022.9.26"
    $ times = "07:10"
    $ weeks = _("周一")
    "........."
    "周一了。"
    "额啊！？"
    "看了手表的时间。"
    "马上就要上课了！"
    "顾不得吃早餐和洗漱了！"
    "清水漱了漱口以后我就冲出家门。朝着公交站牌跑去。"
    scene bg_kuruma_matu
    with dissolve
    $ times = "07:16"
    play music richang fadeout 1.0 fadein 1.0
    "呼~呼~"
    "运气还算可以！刚到车站就有一辆车来了。"
    scene bg_none
    with fade
    $ times = "07:20"
    play sound "audio/yakamashii.ogg"
    n "听说了吗？昨天西路那边十字路口出了车祸，骑电动车的那个直接被撞飞几十米了！"
    "车上的人在窃窃私语着。"
    "离上课只有十分钟了。但是在十字路口还遇到了红灯。"
    "真是让人着急！"
    "时间一分一秒地过去了。公交车终于再次发动。"
    stop sound
    play sound "audio/kuruma.ogg"
    play music "music/dead.ogg" fadeout 1.0 fadein 1.0
    with vpunch
    "嘭！！！！！！！！！！！！"
    "！！！！！！！！！！！！！！！！！！！！！！"
    "？！"
    "发生了什么？"
    "随着一阵剧烈的撞击声的响起。我只感觉自己和其他的乘客一起被公交车带着翻转了过来。"
    hide screen watch
    with dissolve
    scene bg_none
    with fade
    "啊~~！"
    "好痛！~~"
    "反应过来时。我已经被车内剧烈的摇晃和冲击波弄得遍体鳞伤。"
    "尝试动了动。但是手和脚已经没有知觉了。"
    play sound "audio/mimi.ogg" fadeout 1.0 fadein 1.0
    "脑内一阵耳鸣......"
    play sound "audio/120.ogg" fadeout 1.0 fadein 1.0
    "只能隐隐约约听到远处传来救护车的警笛......"
    "呼吸越来越困难.............."
    "意识越来越淡薄..........."
    stop sound
    "好困.....好想睡............."
    "......................"
    "......................"
    "..........."
    scene bg_school_basketball
    with fade2
    play music school fadeout 1.0 fadein 1.0
    with vpunch
    "啊！！！！！"
    "我惊醒了过来！！"
    "但是全身的疼痛感仿佛从来没发生过。"
    "并且我好好地站在学校里。"
    scene bg_school_door
    with dissolve
    scene bg_school_basketball
    with dissolve
    "我环视着四周。熟悉的篮球场。校门口熟悉的两位保安。"
    "而我......还挎着书包！"
    "突然想起了什么。"
    $ years = "2022.9.19"
    $ times = "12:27"
    $ weeks = _("周一")
    play music "music/omou.ogg" fadeout 1.0 fadein 1.0
    show screen watch
    with dissolve
    "看了看手表的时间。是："
    "{b}{size=50}{cps=5}2022年9月19日  12：27  星期一！！！{/cps}{/size}{/b}"
    hide screen watch
    with dissolve
    call disable_shortcut from _call_disable_shortcut_2
    $ persistent.chapter2 = True
    $ persistent.chapter=2
    $ persistent.extra_chapter2 = True
    $ persistent.achievement_chapter1 = True
    image chapter2 ="chapters/chapter2.webp"
    scene bg_none
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
    $ save_name = "{font=ZiTiQuanWeiJunHei-W3-2.ttf}章节二：死而又生的起始{/font}"
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
    voice v5
    c "覃可汐并不是你想的这样的！我和林洛是有事情要谈。嗯.......没错！要商量关于校内各种公共设施，以及校规的事情。"
    hide zicheng_pose1
    show zicheng_pose2 mouth3 other1 at jin:
        xcenter 0.3
    with dissolve
    voice v5
    c "毕竟是第一天来我们学校嘛。万一以后违反了什么校规，然后又反过来说是因为我没告诉他，那最后被处罚的可能就有我了。"
    "这口吻，说的我仿佛是个坏学生一样。"
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
    l "时间跳跃机器？"
    $ persistent.tips63 = True

    l "但是它是手表而不是{a=showmenu:tips63}{color=#BFBFFF}电话电磁炉{/color}{/a}。"
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
    c "这一切都是{a=showmenu:tips64}{color=#BFBFFF}斯坦因之窗{/color}{/a}的选择！"
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
    c "但是我觉得，既然AADR能在未来用我父亲的研究成果造福人类。那未来的人怎么会坚持造出时间机器回到现在，并给你一块时间跳跃的手表呢？"
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
    c "因为这都是为了保证未来时间的走向跟你经历过的一致，才能保证还原手表的时间跳跃机能。如果覃可汐没有死，可能会由于各种蝴蝶效应，导致下周一的车祸不会出现。"
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
    l "即便在下次时间跳跃以后，一切都会一笔勾销。"
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
    voice v3
    x "班长？班主任找你出去是有什么事吗？"
    "覃可汐凑了过来。用一副关心的语气问道。"
    "叶梓澄凝视了一会覃可汐。"
    hide zicheng_pose1
    show zicheng_pose1 mouth1 at jin
    with dissolve
    "接着脸上摆出了营业式微笑。"
    voice v3
    c "没事......谢谢你为我担心。"
    hide kexi_pose
    show kexi_pose eyes4 at jin:
        xpos 0.8
    with dissolve
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
    voice v3
    x "那我就不客气咯~加油啊林洛！"
    hide kexi_pose2
    show kexi_pose mouth3 at jin
    with dissolve
    voice v3
    x "如果你不希望我在你回教室之前翻阅你画画的本子的话~"
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
    voice v3
    x "班长？班主任找你出去是有什么事吗？"
    "覃可汐凑了过来。用一副关心的语气问道。"
    "叶梓澄凝视了一会覃可汐。"
    hide zicheng_pose1
    show zicheng_pose1 mouth1 at jin
    with dissolve
    "接着脸上摆出了营业式微笑。"
    voice v3
    c "没事......谢谢你为我担心。"
    hide kexi_pose
    show kexi_pose eyes4 at jin:
        xpos 0.8
    with dissolve
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
    "嘭！！！！！！！！！！！！"
    "在一阵阵连环爆炸声中
    
    。我已经头晕目眩。"
    "果然还是很痛啊！"
    "呃~"
    "呼吸逐渐变得淡薄。"
    "想最后再看一眼我的手表是否正常......但是不仅眼睛睁不开，而且手也使不上劲了，没有了知觉。"
    "就这样吧..........七天前见!"
    "我放弃了抵抗。静静地等待着死神的降临。"
    "...................."
    "............................."
    "..........."
    "...."
    ".................."
    ".........."
    "呼！！！！"
    "呼！！！！呼！！！！呼！！！！！呼！！！！！"
    "全身的疼痛已经没了踪影。"
    "我缓缓睁开眼睛。校内的风光映入了我的眼帘。"
    "呼！！！！！呼！！！！！叶梓澄你看.......成功了！！！！"
    "成功了！！！！真的太好了！！！！！"
    "这意味着，覃可汐又活了过来。"
    "确认一下手表。"
    "现在的时间是："
    "2022年9月19日  12：27  星期一！！！"
    "跟上次一分不差。"
    "庆祝完了。该做正事了。"
    "我努力回想着和叶梓澄讨论过的事情。"
    "虽然跟覃可汐的死无关，但是跟叶梓澄的父亲和沁野市的未来有关系的作战方法。"
    "那天，也就是我上次经历的这个星期一的晚上。"
    "所以，我希望你做的方法是："
    "重演一次，你最开始经历的一周的时间。"
    "然后验证你的手表能否把你送回周一刚进校门的那一刻。"
    "也就是说，你需要准确地见证覃可汐的死去，准确地在下周一搭乘那辆会出车祸的公交车。"
    "直到这一步，我已经成功了。验证了手表的可以把我送回过去的机能是存在并且正确的。"
    "我现在能站在这里就足以证明。"
    "如果成功将你送回过去了。那么，我需要你做的事是："
    "从校门出去，直接找摊主了解详细情况。然后回学校将所有东西和所有经历，告诉给那个时候的我！"
    "叶梓澄和我是这样说的。"
    "从校门出去！"
    "我再次看了看时间。"
    "12点29！！"
    "现在那个摊主一定还在校门外面。也就是说。这是找他了解这一切的最好机会。"
    "但是马上就要下课了。而且我该如何从校门出去？"
    "从我前两次的记忆来看，这个学校的管理很严格。"
    "进去了除非放学时候不然就别想出去了。"
    "赶紧去找老师请假？"
    "不行！哪有刚转学过来第一次遇到老师就说要请假的。"
    "而且等手续批下来的时候，摊主估计早就收摊离开了。"
    "那......翻墙？"
    "我抬头望了望附近的高墙。"
    "不仅高，而且插满了玻璃碎片。到处也都是摄像头。"
    "而且如果因为翻墙被处分了，大概也没有机会找到叶梓澄告知详情了吧。"
    "果然......只有这一步了吗？"
    "虽然在经历了两次轮回以后，我的对外交际能力已经比最开始好得多了。"
    "但是凭空捏造一个理由去让保安放我出去......"
    "上次是叶梓澄也在场。"
    "林洛啊林洛！拿出你的勇气和决心！"
    "嗯！我必须去做。"
    "我转身走到了校门口保安室。与此同时，下课铃声响了起来。"
    "这位同学，你怎么刚进去就往回走了？"
    "那个，我在外面买东西的时候，把钱包落下了。"
    "我得去把找回来。"
    "意外发现我在说谎方面有不错的天赋。一旦正儿八经撒起谎来，就可以做到面不改色。"
    "嗯......"
    "快去找吧！"
    "保安利索地关掉了电子门的护栏。"
    "谢谢！"
    "本来想加个称谓“保安叔叔”的，但还是开不了口。"
    "我快步踏出了校门。寻找着那个摊主的踪影。"
    "让我看看你的庐山真面目吧！"
    "我在校门口附近张望。"
    "找到你了！"
    "摊主果然还在那里！"
    "我大步走上前来。"
    "你是谁？"
    "我低头探进遮阳伞内，质问道。"
    "看来你已经经历过了呢~"
    "时间跳跃！"
    "你果然知道这块手表具有时间跳跃能力。"
    "对。我知道。所以我才将这块手表交给了你。"
    "所以你到底是谁？"
    "我知道你来自未来，未来到底发生了什么事？"
    "我是林洛！来自未来的,,林洛！"
    "说话间，摊主摘掉了遮挡他脸部的帽子，露出了原本的模样。"
    "什么.......这......"
    "这个摊主突然的话，把我大脑搞宕机了。"
    "等等.........你是我？"
    "对！我是你！"
    "......."
    "我看向摊主的脸，一副略显苍白的中年模样。确实和我有几分相似。"
    "我一时不知道该从何下手提问什么了。"
    "你能走到我面前来，就说明你已经经历过了许多磨难，并且已经获取到了很多真相吧。"
    "摊主，不对，是未来的我先开口了。"
    "我来自10年后的未来。回到2022年的目的只有一个。"
    "那就是："
    "改变被AADR实行霸权专制统治的世界这个未来。"
    "果然是AADR吗？"
    "AADR...到底在未来干了什么？"
    "值得你特地回到十年前的现在。"
    "AADR利用他们的研究成果，胁迫全世界的政府成为他们的附庸。并接管了美国政府。建立了人类历史上第一个完全统一的世界帝国。"
    "虽然他们所吹嘘的是建立一个人与人之间没有隔阂，没有等级制度的共同创造劳动成果的世界。"
    "但这只是虚伪的说辞罢了。"
    "表面上看，AADR是通过和平而非战争的方式统一了全世界。"
    "但通过研究的武器胁迫各国政府签署协议，实在称不上是和平统一。"
    "并且AADR在接管世界以后，开始实行类似古代中世纪的等级制度和专制集权。"
    "当然世界各地也是反抗不断。"
    "但是AADR镇压反抗的方式也是通过他们的武器，无差别打击所抗议地区。"
    "这种暴君统治导致十年后的2032年，全世界人口骤减了1/4。"
    "未来的我和叶梓澄侥幸活了下来，并且一直从事着时间机器的研发。只为改变这个未来。"
    "那.......AADR所用来统一世界，以及镇压反抗的武器究竟是什么？"
    "难道是？"
    "时间刻校正仪。"
    "果然吗？"
    "我从叶梓澄父亲的研究笔记里了解到了时间刻校正仪具有把零子输送到+1时间刻维度的能力。"
    "并且+1维度的零子数增加，会对我们所处的0维度产生干涉。"
    "你的进度已经到这里了吗？"
    "嗯！但是研究笔记里并没有说这个干涉到底是什么。"
    "我来告诉你吧。"
    "覃可汐就是死于这个干涉。"
    "什么？"
    "覃可汐.........死于干涉？"
    "死于由时间刻校正仪向+1时间刻维度输送零子导致的干涉？"
    "嗯......"
    "你还是乐观地觉得覃可汐只是死于偶然事故对吧！"
    "但是抱歉，你的幻想被打破了。"
    "覃可汐的死不是偶然。而是时间刻校正仪被AADR夺走之后的必然。"
    "这个所谓的干涉！就是增加我们所处纬度的分子结构之间的不稳定性。"
    "用通俗的话来解释，就是："
    "会导致各种意外事故，包括天灾人祸的产生概率大大增加。增加的频率跟往+1时间刻维度所注入的零子数量有关。"
    "这便是......+1时间刻维度对0时间刻维度的干涉的外在表现。"
    "而第一个受干涉影响的地区.....就是沁野市。"
    "沁野市会在这个星期五，开始受到干涉影响。"
    "你看我现在坐着轮椅。是因为我的腿，就是受干涉影响，变成了残疾。"
    "不过万幸活了下来。才得以在未来开发出时间机器。"
    "所以......这个干涉，并不是作用于全世界？"
    "至少时间刻校正仪刚被夺走的时候，只能作用于使用时间刻校正仪注入过零子的地区。"
    "因为+1时间刻维度其实是平行于我们所处的0时间刻维度之上的，就是一楼和二楼的关系。"
    "但是后来AADR应该是对时间刻校正仪进行了某种改造，使其就算不在哪个地区，也能精准对哪个地区产生干涉了。"
    "你开发的时间机器，也是使用了往+1时间刻维度注入零子的原理吗？"
    "对！理论基础都来自叶梓澄父亲所保留下来的那份研究笔记。"
    "关于你所说的东西，让我先消化理解一下。"
    "AADR利用时间刻校正仪统治了未来的世界。属于是你和未来的叶梓澄开发了时间机器回到现在，目的是为了改变被AADR统治的这个未来？"
    "嗯。"
    "那未来的叶梓澄呢？没跟你一起乘坐时间机器吗？"
    "..........."
    "伴随着未来的我的沉默，我似乎猜到了什么。"
    "死了........."
    "是吗？死因呢？"
    "制造时间机器的计划被AADR发现了。是叶梓澄给我争取了搭乘时间机器的时间。"
    "........"
    "但是没关系的。只要改变了未来，叶梓澄就不会死掉了。"
    "为什么在我所经历的干涉中，我死了，而你虽然残疾但是一直活到了最后？"
    "这就是受蝴蝶效应所导致的。"
    "那.....那为什么....你说覃可汐的死是必然？明明也可以通过蝴蝶效应去阻止覃可汐的死亡对吧！"
    "覃可汐跟其他人的情况不一样！"
    "实际上我和叶梓澄有走访调查等方式了解过覃可汐出事之前的行动轨迹。"
    "很正常，与AADR乃至叶梓澄的父亲都没有交集。"
    "但是。"
    "我们从警察处获取到的关于覃可汐的尸检结果显示，覃可汐的体内存在某种物质。"
    "其在微观下观测，结构和外观很类似用于制造时间机器和时间刻校正仪的核心部件：零之石。"
    "零之石是什么？"
    "这是时间刻校正仪和时间机器的最核心的部分。虽然来源和形成原因是个谜，但是叶梓澄的父亲使用这种物质开发出了时间刻校正仪。"
    "我所乘坐的时间机器的主要机能也靠零之石来实现。"
    "大概说的话就是。零之石具有一种很奇特的性质。会将涂抹在其上面的零子“吞噬”掉。"
    "但实际却是，零子涂抹在零之石的表面以后，会透过零之石，进入到+1时间刻维度。"
    "所以这个所谓“零之石”，是我们所处0时间刻维度与+1时间刻维度之间架设的桥梁一般的存在？"
    "你有玩过NC吗？"
    "等会，你肯定玩过了，毕竟你是过去的我。"
    "你把零之石想象成类似上界传送门和未地传送门之间的传送门方块就好理解了。和传送门不同的则是，零之石只会让零子通过。"
    "所以？不管是时间刻校正仪还是时间机器，它们往更高维度注入零子的机能的实现，都是靠的零之石的桥梁功能吗？"
    "嗯。"
    "那......从覃可汐身体里发现类似零之石的东西.......意味着什么？"
    "虽然我一直都没弄清覃可汐体内的零之石碎屑的来源是什么，但是这种碎屑单体颗粒大小非常小，却零散分布于覃可汐的体内。"
    "或许因为单个零之石碎屑的大小足够小，所以身体并没有产生排异反应。"
    "这些零之石碎屑，就是造成覃可汐遇害的罪魁祸首。"
    "因为一旦让+1时间刻维度对0时间刻维度产生干涉。作为传递干涉的窗口的零之石本身，就会发生共鸣。"
    "这种共鸣的外在表现就是会吸引附近的灾厄，也就是使零之石附近的不稳定因素活跃度迅速增加。。"
    "单个零之石产生的共鸣几乎可以忽略不计。但是覃可汐体内无数的零之石碎屑，每一颗碎屑都相当于一扇传递干涉的窗口。"
    "当这么多的零之石碎屑同时产生共鸣，就会在干涉产生之后吸收大量灾厄。"
    "也就是说，从产生干涉的那一刻起，覃可汐本身就变成了一个招灾体质！会不断吸引灾厄降临自身。"
    "所以......无论怎么做，由AADR导致的干涉产生的共鸣，都会最终杀死覃可汐。"
    "我想，你应该已经通过自己的实际行动证明了吧！不阻止时间刻校正仪的干涉的话，即便阻止了会导致覃可汐死亡的因素，也依然会有新的因素导致覃可汐死去。"
    if persistent.disagree:
       label chapter2_5_1:
            "嗯......"
            "最开始的覃可汐死于高空坠物的花盆。"
            "我就尝试着事先拿掉了花盆......但最后覃可汐还是死了。"
            "死于教室内坠落的吊扇。"
            "果然呢。看来叶梓澄的这方面的推论是正确的！"
            "如果不想办法阻止AADR启动时间刻校正仪对我们所处纬度进行干涉，覃可汐就会死去。"
            jump chapter2_6
    else:
       label chapter2_5_2:
            "........."
            "对不起......很遗憾.....我为了验证我是否能准确地回到过去.......选择了袖手旁观......"
            "你没有错。毕竟随意改变时间的轨迹，可能会导致历史走向另外的一条车辙。"
            "但是如果你说的是对的。那就算我阻止了高空坠落的花盆......覃可汐大概也会死掉吧......"
            "没错。其实这是叶梓澄在搜集了足够的资料和缜密的论证以后得出的关于覃可汐死亡原因的结论。"
            "班长......果然还是一直在意着覃可汐么......"
            jump chapter2_6
label chapter2_6:
    "所以如果想避免覃可汐的死亡......必须阻止AADR夺走叶梓澄父亲的时间刻校正仪......对吗？"
    "没错！"
    "我能做得到吗？"
    "你...不可能！"
    "我也不可能。"
    "AADR是可以为了达到目的不择手段的组织。如果想正面阻止AADR夺走时间刻校正仪，很难。或者说基本不可能。"
    "我带着警察去呢？"
    "最多只能取得暂时的效果。AADR不会放走这块肥肉的。"
    "那.......那该怎么做？"
    "你都专门乘坐时间机器回来了，那你肯定有头绪吧！"
    "嗯......"
    "我需要你收集线索，找到AADR盯上叶梓澄父亲的契机。"
    "你的意思是？通过切断AADR和叶梓澄父亲的联系，从而改变时间刻校正仪被AADR夺走的未来吗？"
    "没错！"
    "你都这么说了！所以我这块手表，是可以设置回溯的时间点的对吧！"
    "是可以的。"
    "但是受机器大小和技术的限制，最多只能把你送回半个月，也就是15天前。"
    "如果调查以后发现AADR在15天以前就知道了叶梓澄父亲的研究项目了呢？"
    "如果是那样的话就没办法了。那就在AADR来之前毁掉时间刻校正仪吧！！！"
    "如果最后是这种情况，这就是计划C！"
    "我明白了！"
    "但是我还想知道更多！ "
    "你问吧！我知道的东西都会告诉你的。"
    "我这个手表是如何实现把我送回过去的？"
    "也跟时间机器的原理一样吗？"
    "原理一样。但是你的手表只是个发送端。会不断将你的大脑内海马体内的记忆存储为数据，保存在手表内。"
    "在检测到佩戴者心跳停跳两分钟，或者检测到手表受到猛烈重击或者高低温损害的一瞬间，将存储的最后的记忆。"
    "发送到我的时间机器内。通过时间机器的机能之一，将接收到的记忆数据转换成零子并送回过去。"
    "被送回过去的记忆会搜寻数值与本人最匹配的大脑并转换成脑电波，存储进搜寻到的大脑。"
    "用简单的话说的话。会在你死的时候把你的记忆复制一份并发送到过去的你的脑子里。"
    "货真价实的时间跳跃机器！"
    "是这样吗？"
    "那当你和我处在同一时空的时候，记忆的传输不会串号吗？在检索到有两个本人的大脑的时候！"
    "人是会变的。"
    "计算机中不是存在一种名为“哈希值”的东西吗？"
    "你的大脑跟我的大脑，内部的记忆虽有共同的地方，但是更多的是不共同的记忆。"
    "我脑中的记忆，是堆积过很多年的，这个过程中也消失过很多记忆。"
    "就跟哈希值一样，最后系统检测出来的还是独一无二的个体。"
    "就跟...忒修斯之船一样吗？"
    "倒也不完全一样，记忆的忒修斯之船，组成部分是记忆数据的不断更换，但其实脑细胞是会一直存活的。"
    "总之不会让记忆进错脑子对吧！"
    "没错！"
    "但是我还有更多疑问。"
    "你问吧，我能回答的话都会回答你的。"
    "为什么你都回到了现在的时代了，还是要让我来完成这个事情，你肯定有准备对抗AADR的武器吧！"
    "因为我能搭乘时间机器就已经够勉强了。我目前的身体状况并不足以支撑我去做这种事。"
    "至于对抗AADR的武器......就是你手上这块手表，没有其他的了。"
    "那，为什么选择了我，而不是这个时代的叶梓澄。不管是知识储备还是应对紧急情况的能力，叶梓澄都要比我强很多吧。"
    "你和她才刚认识这么点时间，就已经看出了叶梓澄的才能吗？"
    "其实，我已经不想再让叶梓澄牵扯进这个事件了。"
    "如果我把手表交给她，这便意味着，叶梓澄将会经受不断地轮回，我已经不想让她再承受这种痛苦了。"
    "而且我相信过去的我，也就是你的能力！"
    "也相信，你有着对抗AADR和拯救覃可汐的决心。"
    "好！我会改变未来的。用我自己的努力！"
    "我还有关于这个手表的机能的问题。"
    "这个手表，传输记忆到过去的时间，是绝对时间还是相对时间？"
    "绝对时间！并且手表所显示的时间会跟我时间机器里面的时间同步。"
    "而我时间机器里的时间又是实时获取所在时间段的各项数据精准地计算出来的。"
    "还有问题。这块手表难道就只能被动触发吗？能不能我主动触发，让记忆发送回过去？"
    "是可以的！"
    "那你为什么一开始不告诉我这些？我已经经历了两次死亡了，很痛苦的！"
    "我脾气起来了。为什么未来的我要这样整我。"
    "这确实是我的问题，但是我是综合考虑到。初次见面的你不太可能听我讲这么多东西。"
    "有些事情，只有亲身经历过一遍，才能理解，不是吗？"
    "已经说了这么多了。"
    "你该出发了。"
    "该回学校了。"
    "我就在这里，等你的关于AADR的动机的调查结果。"
    "你先把手表摘下来一下。"
    "啊？干什么？"
    "摘下来给我就行！"
    "哦...好！"
    "........."
    "............"
    "好了！戴上吧！"
    "现在的时间是12点38！"
    "我把你的手表的记忆送回时间点设置为了今天的12点40！"
    "也就是两分钟以后！"
    "好了！你在这里呆三分钟了再进学校吧！"
    "所以我下次轮回，会直接回到12点40吗？"
    "嗯。"
    "如果想主动触发记忆传送。就在手表的显示屏上面画下手势吧。"
    "........."
    "未来的我给我在空中演示了一遍。"
    "懂了！遇到希望回到过去的时候，只需要手放在手表上画出这个手势，就可以回到过去了对吧！"
    "没错！"
    "大概就这样吧！我在这里等你的好消息！"
    "这对我来说，只需要等两分钟以后，对你来说，则可能是一个星期的时间了！"
    "那~两分钟后再见！！"
    "12点41了，我大步走进了校门。"
    "我手上戴的，不是手表，而是未来！"
    "AADR！我会打碎你们的阴谋的！！"
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
    $ renpy.pause(10, hard=True)
    hide chapter3
    with fade2
    scene bg_none
    $ quick_menu = True
    call enable_shortcut from _call_enable_shortcut_3
    $ save_name = "{font=ZiTiQuanWeiJunHei-W3-2.ttf}章节三：收束迷宫的展露{/font}"
    "我走进教室的时候，里面已经空无一人了。"
    "我只好自己走到我的座位上坐着。"
    "过了一会，班主任来了。"
    "你是？"
    "老师你好，我叫林洛。是新来的转校生。"
    "哦~之前保安打电话跟我说了。"
    "我是你的新班主任，叫我李老师就可以了。"
    "既然你自己选了一个座位的话，那你就坐那里吧！刚好那个位置是空出来的。"
    "好的！谢谢老师！"
    "毕竟这个座位我已经坐了两个礼拜了。已经有肌肉记忆了。"
    "我现在首要的事情，就是继续执行叶梓澄的计划。"
    "计划的上半部分：回到过去。我已经完成了。"
    "接下来是下半部分：将我获得的所有情报告诉给这个时间的叶梓澄。"
    "在漫长的等待中，叶梓澄终于回到了教室。"
    "跟随着一起的，则是覃可汐。"
    "我得找一个合适的时机，告诉叶梓澄这些事情。"
    "诶？这个位置？"
    "你是新来的转校生吗？"
    "嗯。"
    "转校生......你的名字是？"
    "林洛。"
    "林洛......真是个不错的名字呢~那，希望你能融入到我们这个学校的氛围中！"
    "嗯！我会努力的！"
    "嗯......你......好眼熟？"
    "你是从外地转学来的吗？还是说就是沁野市本地人？"
    "出现了！每次初见覃可汐都会听到的提问！"
    "不得不说，这也算一种奇妙的缘分吧！"
    "也许.....有见过吧！"
    "啊嘞！？我都没问是不是见过面！是读心术吗？"
    "不过......既然你都这么说了.....也许是吧......"
    "跟上一次通过手表时间跳跃到过去相比，我自己也感觉到，自己对覃可汐的事情并没有那么关心了。"
    "可能是因为，这次的我，已经有了一个明确的目标吧！"
    "比起上次那个单纯天真的我。现在的我已经明白了。"
    "想要救覃可汐，并不是一件容易的事。"
    "这次的未来也是耗材。毕竟获取了关于AADR了解到叶梓澄父亲研究项目的相关信息以后，就要继续回到过去了。"
    "在这次的时间里，还是不要保留太多感情比较好。这也是为了大局的一部分。"
    "我心里想到。"
    "这......"
    "我似乎想起了什么。"
    "我并没有询问来自未来的我一个很重要的问题。"
    "我每次回到过去的话。"
    "那个被我抛弃的未来，是会被过去的改变的未来所覆盖，还是说？"
    "单独独立出来成为一个分支的平行世界？"
    "怎么样都好，等下次回到过去以后，再询问他吧！"
    "在我思考的时候，午睡铃已经响了。"
    "覃可汐和叶梓澄也都回到了自己的座位上。"
    "到了下午，我依旧是上台做自我介绍。"
    "一下课，我立刻找到叶梓澄。"
    "虽然前几次我确实也是找了。"
    "叶梓澄依旧是满面愁容的样子。至于发愁的原因，我也知道是什么了。"
    "班长......可以出来一趟吗？"
    "啊！是转校生啊！我记得你叫.....林洛？"
    "说吧！有什么是需要我帮忙的吗？"
    "跟我出来吧！"
    "嗯嗯.....行！如果在教室里你不好开口的话！"
    "那走吧！去哪！"
    "走廊上二楼的楼梯转角怎么样？"
    "嗯....好吧！不过新来的转校生就清楚学校的构造，确实让我有点意外呢！"
    "哈哈......"
    "不知道怎么解释就只能尬笑了。"
    "到了转角。"
    "我顿了顿口气。说道："
    "我接下来要说的话，请你务必相信！"
    "嗯...你先说！"
    "你现在最想要的的东西是宝可魔 方/圆的游戏卡带。最希望交换得到的宝可魔是鸡嘴火龙。"
    "你的饭卡正面是巴麻镁，反面是晓美岩。"
    "你父亲是一名科研人员，在沁野市的一座山的半山腰修建了一所私人研究所。"
    "你父亲现在失踪了。并且你怀疑是被AADR所带走。"
    "叶梓澄的营业式笑容凝固了。"
    "脸也不自觉红了起来，将头扭向一旁。"
    "这个场景在我上次经历的时候见过，似乎叶梓澄觉得喜欢魔法少女小方是一件很羞耻的事情。"
    "过了一会才开口。"
    "你......是怎么知道这些信息的？尤其是我的喜好！"
    "我来自未来！通过根据你父亲所提出原理研制的时间机器，回到的这里。"
    "这........."
    "虽然很难信任你！但是谅你绝对不可能知道我想要的东西......"
    "毕竟是未来的你告诉我的！"
    "那...那你回到这个时间点的目的是什么？"
    "目的是执行，未来的你提出的：拯救你父亲的计划！"
    "同时也是，拯救沁野市的计划，拯救全人类的计划！"
    "你...能明白是什么意思吧！？"
    "嗯........."
    "拯救我父亲？所以你知道我父亲现在的下落了吗？"
    "现在的下落我并不了解，但是。"
    "你父亲会在两天后，也就是星期三，被警察找到遗体。"
    "..........."
    "那你是怎么回到这里来的？如果我父亲已经遇害了的话。"
    "又是怎么知道我父亲时间机器的原理的呢？"
    "那是因为.................."
    "........................."
    "我向叶梓澄说明了一切我能说明的东西......"
    "叶梓澄陷入了沉思。"
    "所以......在我父亲的研究所里可以找到，有关研发时间机器的笔记？"
    "未来的你，和未来的我一起，研发出了时间机器，并回到了这个时代。"
    "这样做的目的是改变我父亲死去的未来。因为我父亲的死会导致未来AADR统治全人类。"
    "而你手上这块手表，就是用来将你的记忆送回过去的你身体里的，微型时间机器，吗？"
    "嗯！"
    "虽然很抱歉，我并没有任何关于你的记忆，无论是你说的和你度过的那两次的一星期时间，还是和你一起去我父亲的研究所的事。"
    "毕竟这些事情，已经变成了未发生的状态了。"
    "所以，来自你上次所经历过的未来的我，拜托你将这一切都告诉给现在的我的目的就是。"
    "找出AADR会盯上我父亲的研究的契机对吧！"
    "没错！找出这一切的最根本的原因，然后，由我来避开这个原因。"
    "你这块手表可以将你的记忆，发送给过去的你自己，但是最多只能发送回十五天前，对吧！"
    "没错！所以如果AADR在比15天更早的时间就盯上了你的父亲的话。"
    "那我恐怕就只有毁掉你父亲研发的时间刻校正仪这一条路可走了。至少可以避免AADR对其的滥用。"
    "......"
    "林洛。"
    "已经上课了。"
    "更多的事情，下节课下课继续在这里说吧！"
    "嗯。好！"
    "我跟着叶梓澄回了教室。"
    "我刚一坐到座位上。就感受到一阵异样的目光。"
    "是覃可汐。但是我没空去管覃可汐在想什么了。"
    "虽然很对不起她，但我现在必须要专注于找到线索。"
    "终于等到了下课。"
    "继续之前的话题吧！"
    "AADR是研究原子的数字化转换的，而我父亲成功发现了原子转换成的零子。"
    "你父亲有对外宣传过零子有关的文章或者发言吗？"
    "应该不会的。我父亲亲口跟我说过。零子相关的研究还在继续，父亲希望等关于传输和还原零子相关的研究变得可行和安全之后，再将其发表在论文中。"
    "也就是说，并没有对外界公开！"
    "那......你母亲也是研究人员吗？"
    "嗯。"
    "关于你母亲相关的事情，方便进一步说吗？"
    "嗯..."
    "七天前，也就是9月12号。"
    "我母亲被发现，倒在了一个巷子里。脖子上有手印和指甲抓出来的血痕。"
    "上一次轮回的你跟我说过这件事，嫌疑人并没有被抓到。"
    "没错。"
    "遗体被发现的时候，身上的手机，有在吗？"
    "没有。钱包和手机都不翼而飞了。"
    "林洛......你觉得，是AADR通过我母亲了解到的我父亲的研究项目的吗？"
    "嗯......一般而言的确会这样想。"
    "但是AADR有什么动机去杀害你的母亲呢？"
    "难道还有更早的关于你父亲研究项目的信息？"
    "不知道。"
    "是不是你母亲，在遇害之前跟什么人说过了你父亲的研究项目，然后那个人，又或许是其他人，向AADR告密了......"
    "又或许......那个人就是AADR的人？"
    "这个我也不清楚。毕竟手机没了，想查通话记录也没有办法。"
    "你母亲除了在研究所上班以外，还有其他工作吗？"
    "没有了。跟我父亲不同。我母亲除开研究所以外就只在家里，负责打理家中事务。"
    "那？"
    "你母亲在9月12号那天，出门的动机是什么？"
    "我也不知道，那天是星期一，我在上学。"
    "但是平时那个时候的话，应该是不会出门的。"
    "警察得到的结果，事发时间是下午两点多。"
    "那个时候太阳也是一天中最热的时候。的确就算是一般的家庭主妇都不会选择出门。"
    "好了。现在有了一个新的目标了。"
    "我们现在要了解清楚。"
    "你母亲，在9月12号下午两点之前，出门的目的是什么？以及为什么要经过巷子。"
    "等会。"
    "虽然这样问可能会勾起你的不好回忆，但是。"
    "看着叶梓澄的惆怅的眼神，我又不敢开口询问了。担心再次伤到她的心。"
    "从我告诉她，他的父亲未来会死掉的时候，就已经受到了一次打击了吧。"
    "看得出来，叶梓澄尽量不表现得难过。"
    "没事，你问吧，"
    "叶梓澄看我一直犹豫不决，主动开口了。"
    "好。"
    "你母亲出事的地点，是那个巷子，还是说......是从什么地方把遗体搬进了巷子？"
    "警察现场勘察的时候没有找到地上存在拖拽的血迹什么的，反而是母亲倒下的那个地方的墙上有很多血迹。"
    "巷子里也存在很多打斗的痕迹。"
    "看来...是发生在巷子里的。"
    "那，巷子内外有监控吗？"
    "没有。最近的监控也是出巷子几十米的地方才有一个。"
    "虽然拍到了嫌疑人，但是搜查的时候却找不到任何踪迹了。"
    "那有拍到你母亲什么时候，跟谁一起进的巷子吗？"
    "有。但是只有母亲一个人，背着挎包。"
    "服饰呢？"
    "是平时出门见同学朋友才会穿的一套正装。"
    "正装......"
    "又上课了。"
    "要不，放学后再聊吧！连续的讨论才有助于思维的活跃。"
    "老是被上课打断。"
    "嗯！"
    "我和叶梓澄约定好了。放学以后来到了校门口见面。"
    "这命运的校门口。"
    "久等了，林洛！"
    "嗯。"
    "嗯？"
    "覃可汐为什么也跟了过来。"
    "你们两个，以前认识？"
    "我看你们一下课就跑出去聊天，一直到上课才回来。"
    "是在聊什么啊？"
    "有兴趣跟我分享吗？"
    "嗯？可以吗？可以吗？"
    "叶梓澄抢先拒绝了她。"
    "不行！覃可汐你先回家吧！我和林洛讨论的东西跟你没啥关系的。"
    "没啥关系，这是叶梓澄的谎言。"
    "不嘛！这么遮遮掩掩的，难不成是？"
    "覃可汐露出了邪魅的笑容。"
    "叶梓澄，我看要不？"
    "我靠近叶梓澄的耳边，小声商量着。"
    "要不让覃可汐也一起，帮忙思考和推理一下？"
    "这不行吧！如果让她知道了自己死期将至......"
    "有一种东西，叫角色扮演......"
    ".........."
    "嗯......那好吧！"
    "啊嘞嘞？！已经开始有亲密接触了吗？关系发展真是迅速啊！"
    "难道是？在我之前就发展关系了？叶梓澄！居然对我隐瞒了这么久！"
    "我之前都不知道的！"
    "覃可汐！你听我说！"
    "听你狡辩是吧！好！我要看看你怎么编！"
    "林洛，我和他是今天才认识的。"
    "我之前也一直喜欢看小说，这个你也是清楚的吧！"
    "刚好林洛他现在正在构思一个小说，希望我帮他完善相关剧情。"
    "希望用我丰富的“知识储备”，帮他构思什么的！"
    "所以我说你误会了！"
    "是什么类型的小说？恋爱吗？"
    "不是！"
    "啊！好快的否定！"
    "是悬疑和推理题材的小说。"
    "我帮忙圆场到。"
    "覃可汐，我们现在还是很缺人，你看你有兴趣参与进来吗？"
    "嗯......好啊！我还是玩过不少推理游戏的！"
    "像正转裁判啊，炮丸论破啊什么的。"
    "推理类动画我也没少看哦！"
    "名侦探柯北啊，复活笔记啊，火龙菓啊~"
    "好好好！缺的就是你这种人才！"
    "人材！我在脑海里小声说道。"
    "呐~说吧！大概是什么剧情？"
    "嗯......"
    "我大脑进行着飞速的运算。寻找着一个完美的不会让覃可汐起疑的虚构情节。"
    "嗯。"
    "我顿了顿口气。看着覃可汐期待的眼神。"
    "我创作的小说里的主角，是一名侦探。"
    "他碰到了一件棘手的案子。"
    "一个人遇害了，但是我构思不出凶手的作案过程以及作案动机。"
    "这个受害者，在本该呆在家里的时间段，被发现遇害在了一个巷子里。"
    "然后监控没有拍摄到详细的作案过程，虽然拍到了像是凶手的嫌疑人，但是却搜查不出结果。"
    "这是目前，主角所遇到的难题。"
    "被害人被发现的时候，穿着只有去见关系好的人的时候才会穿在身上的正装，并且身上的金钱和手机都没了。"
    "嗯......"
    "根据你所提供的信息来看。"
    "根本就是没有悬念的事情吧。不是拍到了嫌疑人吗？"
    "嫌疑人，谋财害命，在巷子里杀害了被害人，然后拿走了金钱和手机。"
    "警察抓不到他，可能是因为在案发以后就已经逃离了案发所在地区，脱离了当地警察的管辖范围。"
    "但是你这么设计的话。这个嫌疑人有点蠢啊！"
    "这话怎么说？"
    "拿走金钱可以理解，但是现在这个时代，手机反而是很不利于自己逃离的设备。毕竟现在的手机找回功能，就算设备关机了也能通过定位锁定凶手位置。"
    "那万一是凶手带走手机方便销毁呢？"
    "你的意思是？被害者通过手机录下了对凶手不利的信息？"
    "有这个可能吧！不然不会特地把手机也拿走了。而且现在大多数手机，所有人都会设置密码锁，虽然密码锁可以暴力解开就是了。"
    "你这么说确实。凶手把手机也带走，可能就是为了销毁证据。"
    "好，这样解释就能说得通为什么凶手在杀害受害者以后要这样行动了。"
    "那下一步，我得构思凶手的作案动机是什么。"
    "我觉得作案动机很明显了，就是谋财害命，不然不管是蹲点在小巷里也好，还是拿走受害者的钱财也好，都很难用其他动机来解释。"
    "你觉得，如果凶手带走钱财只是在故意混淆呢？故意隐藏自己真正的作案动机。"
    "例如......凶手真正关心的只是手机内的资料，拿走钱财只是想干扰警察的办案。"
    "这个感觉......怎么来安排作案动机都差不多吧......"
    "我倒是觉得你构思的这个凶手有点大胆。"
    "不是大胆，就是蠢货。"
    "到处都是监控，就算混淆了作案动机，也早晚会被警察抓住然后审讯吧！"
    "但是你说却没被抓住。"
    "对！警察提取了监控内凶手的资料，在全市内顺着监控搜查，都没有结果。"
    "叶梓澄如此说着。"
    "一般凶手被监控所拍到的话，警察应该可以顺着监控挨个追踪凶手的踪迹吧！包括开的什么车，走的哪条路。"
    "怎么会抓不到呢？"
    "还是说？你在构思的时候，希望这个凶手不会被抓到？"
    "我懂了！"
    "覃可汐觉得自己明白了什么，会心一笑。"
    "这个凶手后面还有重要戏份对吧！"
    "是最终反派吗？"
    "还是说？警察无权抓他？"
    "让我猜猜？你构思的故事里也有一套类似生理测量者的，犯罪指数的东西？"
    "然后这个凶手是稀有的免疫检测体质，所以警察不能直接抓他吗？"
    "这样来推断的话。真相大白了！！"
    "这个凶手肯定已经被做成百脑汇了吧！"
    "果然覃可汐的推理已经脱离现实逻辑开始朝着虚幻发展了。"
    "那个......不是......我小说的时代背景就是我们生活的这个时代，不是什么赛博朋克和未来世界，也不存在犯罪系数这东西。"
    "就是一个普普通通的，跟现代一样的一套治安管理体系！"
    "是这样吗？好吧！"
    "我倒是觉得这样写很有趣，不是吗？"
    "那凶手没被抓到的真正原因到底是什么？"
    "监控把凶手跟丢了？"
    "差不多是这样。"
    "警察办案的时候顺着沿路的监控调查。但是发现嫌疑人在跑到一个监控盲区以后就再也没在其他监控里出现过了。"
    "然后警察去查了那个盲区了吗？"
    "当然有查，但是那块地方是一家私人企业的地下车库。"
    "车库里只有向上通往地面的路口。"
    "也就是说，凶手进了这个里面以后，是不可能久留的。"
    "既然是车库，那肯定有很多车辆吧！凶手搭乘里面的车辆跑了呢？"
    "都查过了。包括车库里出入的每一辆车，但是没有收获。"
    "而且这个车库的车流量还算比较大，车辆出入很是频繁。"
    "如果凶手躲进了汽车后备箱等无法被监控拍到的地方呢？"
    "这个也很难查，除非挨个追踪和排查每一辆车辆。"
    "而且万一凶手的同伙，开的不是自己的车就更难查了。"
    "原来是这样跟丢的吗？嗯........."
    "不过地下车库没有监控摄像头已经很奇怪了。"
    "林洛！你这小说已经有很大的潜力了呢！细节方面都构思了这么多！"
    "啊哈哈~有很多东西是叶梓澄帮我想出来的。"
    "不过，凶手费这么大的周折，那被害人肯定很有钱吧！值得凶手不择手段地去杀人。"
    "实际上，被害人的收入很普通，至少绝对算不上有钱。"
    "那......难道说？凶手其实是不小心杀掉了被害人？"
    "嗯？为什么这样说？"
    "当然这只是我个人的通过已知条件推导出来的可能原因。"
    "凶手并不是故意杀掉被害人的。"
    "你还设定了什么东西吗？"
    "例如，监控有没有拍到凶手用的什么凶器，以及，死者的死亡原因是什么？"
    "这个我也不知道了，只能让叶梓澄帮我回答。"
    "没有拍到凶手的作案工具。也不会拍到。"
    "案发现场也没有留下任何凶器。"
    "这是因为："
    "被害人的死亡原因是————————"
    "窒息。"
    "也就是......被掐死了。"
    "啊？这个细节，叶梓澄并没有在之前透露过。"
    "这样的话.........."
    "案件细节大概可以分为两种情况了。"
    "情况一，凶手是为了抢夺财物，但是失手杀死了被害人。"
    "情况二，凶手的真正目的是被害人手机里的东西，为了得到这些东西，不惜杀掉被害人。"
    "关于凶手的资料，既然警察都锁定了是谁，应该拿得到吧！"
    "凶手就是当地的一个无业混混，曾经有过几次因盗窃和拦路抢劫而入刑的犯罪记录，并且在案发前两星期才刚出狱。"
    "这样么？"
    "但是就算是混混，也会有一个住所吧！"
    "你这话说的！警察也不是笨蛋！首先排查的就是住所。"
    "啊哈哈哈哈~也是呢~"
    "所以根据他的案底来看，其实更倾向于情况一吧！"
    "无论是被害者的死法，还有凶手之前的犯案记录。"
    "那什么条件下会出现情况二？"
    "当然有条件。例如："
    "有人需要手机里的东西，所以雇佣凶手去作案。"
    "怎么样？"
    "你想的很好！我会吸纳你的这部分想法的。"
    "还有很多问题！我需要更多线索来辅助我进行思考。"
    "看着覃可汐认真的样子，感觉像是变了一个人一样。"
    "你说过，被害人遇害的时间，在平时的这个时段是应该呆在家里对吧！"
    "身上的正装，表示被害人可能有什么重要的人要见面。"
    "在小巷里遇害，则说明被害人和准备见面，或者是已经见过面的人的见面地点，必须经过这条小巷才能到达。"
    "反正就是有，不得不穿过巷子的原因！"
    "不得不穿过巷子的原因吗？"
    "以及，如果事实是情况二，也就是凶手受雇杀人。那么。"
    "雇佣者或者凶手，一定有一个知道被害人的行动路径。"
    "也就是说，一定知道被害人会穿过巷子吗？"
    "穿过这条没有监控的巷子。"
    "没错。"
    "如果凶手和被害人之间并没有在之前有过关联的话。"
    "就很可能是，雇佣凶手的人，是很熟悉受害人的人，并且很需要受害人手机内的东西，资料啊通话啊什么的。"
    "但是这一点其实有点站不住脚，死者是窒息而死吧。有受雇的杀手会选择掐死被害人吗？"
    "怎么也没有选择一把锋利的刀子，或者一杆枪来的快吧！？"
    "而且被掐死还存在很多不确定性，可能需要跟被害人搏斗，以及可能最后杀不死被害人。"
    "除非......雇佣凶手的人，只需要拿到数据就可以了，被害人是死是活，都无所谓。"
    "这意味着这个雇佣杀手的人，可能背后拥有更强大的力量，从而使其可以不用畏惧被害人的报警。"
    "覃可汐还在头头是道地推理着，但是天色渐渐暗了下来。"
    "要不今天就到这里吧！覃可汐！"
    "啊~我才刚找到推理的感觉~"
    "没错！天色很晚了，也该散伙了。"
    "好吧！"
    "一定要采纳我的话哦！"
    "一定会的！"
    "嗯嗯~那就好~"
    "那我就先回家了，明天继续吧！？"
    "看着覃可汐逐渐走远，叶梓澄长舒了一口气。"
    "林洛，你怎么看待覃可汐的推理？"
    "很有参考价值。我感觉真相就藏在覃可汐的推理里面了。"
    "嗯！那你也回家吧。"
    "我想再去找警察了解一下关于这个案子的更多的信息。"
    "你觉得.....凶手会是我母亲去见面的那个人吗？"
    "有这种可能！"
    "不然常规无法解释为什么你母亲必须经过那个巷子。以及凶手那娴熟的逃跑手法。"
    "那......你知道你母亲那一天去见的谁吗？"
    "不知道。毕竟可以用来调查的手机也被拿走了。"
    "嗯........"
    "你母亲见的最多的朋友是谁？"
    "警察也可以通过你母亲手机号码的通话记录什么的，查到一点蛛丝马迹吧！"
    "如果你母亲见的那个人，其实在为AADR卖命，倒是可以解释的通了。"
    "找你母亲套出关于零子的研究的话以后，邀请你母亲出去见面，再雇佣杀手去杀掉她，封口并且获得手机的的更多资料。"
    "然后AADR总部获得了资料以后，就派人去研究所抢夺仪器和资料，绑架你父亲。"
    "如果真的是这种情况的话......就得找那个你母亲见面的人对质了呢~"
    "嗯！我去找警察问问详细的后续调查资料。"
    "林洛......"
    "嗯？"
    "虽然我不知道......你穿越时间之前遇到的我......是怎么看你的......"
    "但是对现在的我来说......你真的帮了我很多......"
    "我本以为母亲的死，和父亲的失踪......都将成为永别......"
    "是你给了我希望......"
    "已经......不知道该怎么感谢你了！"
    "看着叶梓澄这副情形，我深感不妙。"
    "叶梓澄似乎觉得自己欠了我一个人情。"
    "干嘛感谢我。"
    "我能有今天，还是多亏了你啊！"
    "这是事实。"
    "我这块能传输记忆到过去的手表，是你发明的。"
    "未来的我之所以能把这块手表交到我手里，也是多亏了你，发明了时间机器。"
    "所以要说的话，是我欠你一个人情才对。"
    "没有你的帮助，我也没想到自己可以有这么大的用。"
    "我啊，从小就很孤独，没有什么朋友，学习也很平庸。"
    "只能看动画片和打游戏，因为在现实中没有人愿意跟我一起玩耍。"
    "在第一次遇到你之后，我才感受到。"
    "朋友的温暖。"
    "原来拥有朋友，是这种感觉吗？"
    "拥有知心的人，可以互相讨论兴趣爱好，互相倾诉自己的不快和压力。"
    "是你，以及覃可汐，让我找到了我人生中新的意义。"
    "所以在覃可汐突然出现意外以后，我才会那么痛苦，那也是我第一次体会到知心的友人跟我永别的痛苦。"
    "老实说，当我知道我还能拯救覃可汐的时候，我第一次感觉到，我并不是对社会毫无用处的人。"
    "现在的我，也可以通过自己的努力，去拯救周围的人。我终于是有用的了。"
    "而这一切，还是多亏了你！叶梓澄......"
    "叶梓澄......你有在听.....吗？"
    "比较抱歉，跟你说了这么多跟解决问题无关的话。"
    "没......我也是第一次收到别人的倾诉......第一次了解到别人对我的看法......"
    "那.....林洛......一起加油吧~！"
    "不管是为了你自己，还是为了覃可汐，还是为了.........."
    "为了........"
    "我..."
    "总之！一起努力吧！！"
    "啊~嗯！好！"
    "我会坚持下去的！"
    "叶梓澄似乎说了什么不得了的话。"
    "但是已经无所谓了。"
    "我现在得假装没听到她说的什么，不然也太难堪了。"
    "和叶梓澄分别以后。我回到了家。"
    "用电脑在网上查阅着关于叶梓澄父母的相关信息。"
    "因为还存在着一种可能。就是叶梓澄的父母可能在网上主动或被动，将研究项目泄露给了AADR。"
    "不管是直接通过搜索引擎还是翻阅各大学术网站，关键词检索都没有什么有用的信息。"
    "叶梓澄父亲也只能查到显示是一名大学在职老师。"
    "叶梓澄母亲更是什么基本信息都查不到。用着叶梓澄告诉我的名字输进去，检索结果一个都没有。"
    "关于叶梓澄母亲遇害的相关报道，被害人姓名也都是使用的化名。"
    "凶手仍在逃中。"
    "凶手的大头照和名字倒是查得到。"
    "那AADR是如何提前知道叶梓澄父母的研究项目的呢？"
    "而且.......照着AADR这蛮横的做事风格。"
    "如果知道了叶梓澄父母的研究项目，也不会拐弯抹角的先杀掉叶梓澄母亲，再袭击研究所吧~"
    "难道说？"
    "是叶梓澄母亲在跟与她见面的那个人那里泄露了信息？"
    "这样才能解释的通，为什么先杀了叶梓澄母亲，再袭击研究所。"
    "但是........."
    "既然叶梓澄母亲已经将信息泄露给了这个人，那为什么还要选择杀掉叶梓澄母亲？是有什么非做不可的理由吗？"
    "毕竟自己作为和叶梓澄母亲最后约定见面的人，如果叶梓澄母亲出了事，嫌疑最大的肯定是自己。"
    "必须拿到手机里的信息？"
    "还是想不通，叶梓澄母亲手机里可以有的信息，直接去研究所肯定得到的更多。"
    "那就是？"
    "叶梓澄母亲和朋友的有关泄露消息的内容，被那位朋友的周围有人获得了？"
    "存在这个可能。"
    "不管结果如何，我觉得都必须去亲自拜访一下那位叶梓澄母亲生前最后见面的那位朋友了。"
    "嗯......好吧！我会去跟班主任请假的！"
    "嗯！"
    "挂断了和叶梓澄的电话。"
    "我拜托叶梓澄明天跟我去亲自找到那位叶梓澄母亲的朋友。所以让她去申请明天请假一天。"
    "我和她都请假。"
    "额......后知后觉。班上会不会又传出不好的传言。"
    "天气很晴朗。我也早早地感到了校门口附近。"
    "总不能在家里集合，跟我爸妈不太好解释为什么没去上学，不如就装成去上学的样子。"
    "我和叶梓澄也是约好了在校门口见面。"
    "林洛！！"
    "朝着声音来源的方向看去。"
    "是公交车站的方向，叶梓澄一下公交车就喊着我的名字，小跑了过来。"
    "我已经请好假了。"
    "对了！"
    "我昨天去找了警察要到了更多的资料。"
    "包括我母亲最后见面的人。"
    "以及最先发现我母亲遇害的人。"
    "最后见面的是谁？"
    "是我母亲的大学同学，丁唯。"
    "警察调取了我母亲手机号码最后的通话记录，是我母亲和丁唯的通话。"
    "通话日期是我母亲遇害当天的早上。"
    "通话内容是什么？"
    "这个查不到，通信公司也没有记录通话录音。"
    "但是，大概是这个丁唯让你母亲出门的吗？"
    "走吧！"
    "你拿到这个丁唯的所在地方了吗？"
    "嗯！"
    "我跟随叶梓澄，搭上了一辆出租车。"
    "到地方了。"
    "额？"
    "面前是一个小巷。"
    "这里难道是......？"
    "是我母亲遇害的那个巷子。"
    "巷子内部昏暗潮湿，两侧墙上的涂刷也掉落了不少，露出了红色的砖体。"
    "并没有看到血迹，或者说看不到可以证明这里是案发现场的东西。"
    "大概是案发后被清理过了吧。"
    "所以你把我带到在这里来，是希望我调查一下现场吗？"
    "可以哟！"
    "可以......？"
    "但主要目的还是见我母亲的大学同学。"
    "准确的说，是穿过这个巷子以后就能走到她的家。"
    "额！！！！？"
    "走吧！"
    "我跟随叶梓澄，慢慢走出了小巷。"
    "跟着她，来到了一栋房子面前。"
    "昸！昸！昸！"
    "门上没有门铃，所以叶梓澄用手敲打着紧闭着的门。"
    "在吗？阿姨？"
    "几秒钟后，门开了。"
    "啊？你就是......白椎音的女儿...叶梓澄？"
    "白锥音正是叶梓澄母亲的名字。"
    "看来找对地方了。"
    "这个时候，你不应该去上学了吗？"
    "丁阿姨好。我有一些关于我母亲的事情，希望详细了解一下。"
    "哦？是吗？这几天警察天天往我这里跑，我也说了足够多的情报了，唉。"
    "不过，既然你想了解更多，那就行吧！毕竟，你是白椎音的女儿。"
    "这位是？"
    "这是我的朋友，他也想了解一些事情。"
    "朋友啊......我懂了，哈哈~那进来坐吧！"
    "她最好真的是懂了，我看着她那眼神，心里想到。"
    "那我就开始问了。"
    "我从警察那里了解到，您......在我母亲出事的那挺天上午，和我母亲约好了见面？"
    "对！唉~现在想起来......依旧很后悔......如果那天我没有给她打电话......"
    "或许就不会......碰到这种事情了......还是在快到我家的地方....."
    "见面的目的,是相约一起去打麻将对吧？"
    "对.......你母亲经常会趁你和你父亲都不在家的时候，和我约好去打麻将。"
    "出事的那天也是如此。"
    "那打麻将的地点是你家吗？"
    "不是，是我家附近的一家麻将馆。"
    "所以每次都是约好了在你家会合吗？"
    "对！"
    "那....我母亲有在会合，或者打麻将的途中，说过什么关于科研项目的事情吗？"
    "科研项目？每次打麻将都跟我聊的是你的学习怎么怎么样，以及看的电视剧是什么，晚上打算给你做什么吃。"
    "什么科研项目什么的，没有聊过，或许吧。"
    "或许？"
    "嗯。因为这种东西，在打麻将的时候，无法集中精神听啊，就算听到了可能回头就会忘掉了。"
    "嗯........."
    "我母亲出事当天，您有在家里听到附近的相关的声响吗？"
    "对不起......抱歉......那天的那个时候，我还在客厅沙发上刷手机......开的外放.....所以......"
    "论短视频外放的危害。我在心里如此想到。"
    "还有什么，你都问吧！我知道的东西都会回答的。"
    "不过，我有一个请求，希望你们能答应。"
    "是什么？"
    "相信我...你母亲不是我杀的，杀她的人也跟我没关系。"
    "如果说我的罪过的话......就是直接导致她遇到了凶手，在巷子里。"
    "我相信您！阿姨！"
    "你放心！我一开始就没把您当作嫌疑人！"
    "是吗？"
    "我查过我母亲大学期间的记录。您和我母亲是室友。而且....从我母亲电脑里翻到的照片，也能看出，您们是很好的朋友。"
    "所以我相信！您是不会这样做的！"
    "好......谢谢你......为了给白椎音一个公正的结果......我会全力配合你的提问的！"
    "您是否知道？我母亲有没有，仇人？"
    "就是...看我目前不爽的人，或者，因为我母亲而受到挫折的人？"
    "据我所知的话......没有......"
    "你母亲在大学期间就经常帮助别人。"
    "如果像她这类人都会结仇的话，那可能每个人都有很多仇人了。"
    "阿姨，您丈夫，是做什么工作的？"
    "我丈夫的话，现在在本地一家公司做销售的职务。"
    "平时有出差吗？"
    "偶尔会有，不过也基本是出差到邻近的城市。"
    "......"
    "阿姨！就这样吧！谢谢您告诉我这么多信息！"
    "已经要走了吗？"
    "要不在我这里吃完午饭了再走？"
    "不用了阿姨！谢谢您的好心，但是我们得去其他地方调查了。"
    "而且调查完以后还要回学校呢！所以抱歉啦~"
    "好吧！慢走啊！"
    "等会。"
    "丁唯走进了里面一间房间。"
    "过了一会，走了出来，手里拿了一件大衣。"
    "啊？这是......"
    "是以前一天，你母亲来我这打麻将，当时天气比较闷热，就给脱了。"
    "然后就忘记带走了。我也是今天才想起来。"
    "你带回去吧。"
    "嗯!"
    "我和叶梓澄从丁唯家里以后。叶梓澄和我继续商讨接下来的行动。"
    "临近正午的太阳，依旧刺眼和炎热。"
    "我也叶梓澄坐在一楼的台阶处乘着凉。"
    "顺便讨论着事项。"
    "怎么样？这个丁唯，有可能是杀害你母亲的幕后黑手吗？"
    "缺少作案动机，又或者说。"
    "我认为她缺少作案动机。"
    "丁唯...是你母亲的大学同学，以及好朋友吧。"
    "再加上还经常一起约着玩，确实不像会杀害你母亲。"
    "再加上，丁唯的丈夫也是从事着跟我父亲的研究项目基本上搭不上边的工作。"
    "那......还有谁有可能？"
    "最简单的办法当然是直接找凶手问了。但是连警察都抓不到凶手......"
    "找找其他突破口吧~"
    "你说......你了解到了最先发现你母亲遗体的人？"
    "目击者的话不太可能吧......"
    "但是你不觉得很奇怪吗？"
    "目击者目击到了凶手作案，凶手采取的措施是扭头就跑，而不是灭口。"
    "等等......所以这个目击者是直接看到了作案过程吗？"
    "还是说？"
    "只是发现了遗体。"
    "至少从监控上来看，是目击者先走进巷子里，凶手才从巷子里跑出来。"
    "如果是这样的话。"
    "假设凶手只是为了劫财不小心杀掉了人，那看见目击者会逃跑可以理解。"
    "没有心理准备嘛毕竟。"
    "但在另一种可能，也就是凶手受雇的情况下，一样说得通。"
    "雇主的要求只是杀掉你母亲，拿走手机，自然只需要这样做就行了。"
    "这个雇主，肯定早就安排好了凶手事后离开案发现场的相关事务。"
    "自然就算不杀掉目击者，也能安身离开了。"
    "反而第一种假设有点奇怪，林洛。"
    "叶梓澄抬起头，说到。"
    "如果凶手是不小心杀了人，那逃跑以后是如何把自己藏起来的呢？"
    "藏到以至于警察的力量都找不到踪影。"
    "所以依旧还是第二种情况比较合理对吧！？"
    "至少根据目前得到的线索来看，是如此。"
    "说了这么多，所以目击者是谁？"
    "是你认识的人。"
    "？我认识？"
    "我们都认识。"
    "所以......是？"
    "我们的班主任，李老师。"
    "？啊！！？"
    "但是案发时间是周一下午啊！"
    "她是怎么路过学校外面的那个巷子并目击到案发现场的？"
    "案发现场距离学校，大概也有半个小时的车程吧~"
    "这就是我们接下来要调查的地方了。"
    "那现在回学校去吧！？"
    "虽然我内心是很不愿意回去的。"
    "但是继续呆在外面也无法获得新的线索了。"
    "林洛！！"
    "再聊会天吧~"
    "现在时间也还够。"
    "但是......"
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
    image chapter3 ="chapters/chapter4.webp"
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
    $ save_name = "{font=ZiTiQuanWeiJunHei-W3-2.ttf}章节四：命运枷锁的挣脱{/font}"
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
    "臭流氓闪开！本来想给你点面子的！"
    "你如果不放我走，那我报警了！"
    "叶梓澄母亲打算伸手掏手机。"
    "不许报警！！！"
    "却被对方用手勒住脖子。"
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