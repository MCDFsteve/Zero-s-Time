define config.version  = "beta-v1.2.4.3"
define endsay  = _("{color=#ffffff}用于鉴赏立绘、音乐和结局、章节的Extra板块\n已解锁。请在游戏主菜单内查看。{/color}")
define audio.v1 = "voice/v1.ogg"
define audio.v3 = "voice/v3.ogg"
define audio.v5 = "voice/v5.ogg"
define audio.v7 = "voice/v7.ogg"
define audio.v9 = "voice/v9.ogg"
define audio.v11 = "voice/v11.ogg"
define config.steam_appid = 2520710
define audio.school = "music/school.ogg"
define audio.sora = "music/sora.ogg"
define audio.speak = "music/speak.ogg"
define audio.kexi = "music/kexi.ogg"
define audio.richang = "music/richang.ogg"
define audio.lanzhu = "music/lanzhu.ogg"
define audio.ruins = "music/ruins.ogg"
define audio.title2 = "music/title2.ogg"
define audio.home = "music/home.ogg"
define audio.title = "music/title.ogg"
define audio.title2 = "music/title2.ogg"
define audio.dead = "music/dead.ogg"
define audio.omou = "music/omou.ogg"

define audio.suzu = "audio/school_suzu.ogg"
define audio.ketaisong = "audio/ketaisong.ogg"
define audio.ketai3 = "audio/ketai3.ogg"
define audio.odoro = "audio/odoro.ogg"
define audio.ochiru = "audio/ochiru.ogg"
define audio.higurashi = "audio/higurashi.ogg"
define audio.ame = "audio/ame.ogg"
define audio.yabu = "audio/yabu.ogg"
define audio.book = "audio/book.ogg"
define audio.desk = "audio/desk.ogg"
define audio.souji = "audio/souji.ogg"
define audio.fan = "audio/fan.ogg"
define audio.with1 = "audio/with.ogg"
define audio.car_stop = "audio/car_stop.ogg"
define audio.mizu_help = "audio/mizu_help.ogg"
define audio.yousuru = "audio/yousuru.ogg"
define audio.saku = "audio/saku.ogg"
define audio.key = "audio/key.ogg"
define audio.door = "audio/door.ogg"
define audio.utusu = "audio/utusu.ogg"
define audio.opendoor = "audio/opendoor.ogg"
define audio.watch = "audio/watch.ogg"
define audio.loop_bgm = "audio/loop_bgm.ogg"
define audio.bilibili = "audio/bilibili.ogg"
define audio.phone_ochiru = "audio/phone_ochiru.ogg"
define audio.tatakai = "audio/tatakai.ogg"
define audio.kamera = "audio/kamera.ogg"
define audio.enter = "audio/enter.ogg"
define audio.shindou = "audio/shindou.ogg"
define audio.run_kai = "audio/run_kai.ogg"
define audio.opendoor2 = "audio/opendoor2.ogg"
define audio.hakusyu = "audio/hakusyu.ogg"
define audio.umineko = "audio/umineko.ogg"
define audio.umi = "audio/umi.ogg"
define audio.kawa = "audio/kawa.ogg"
define audio.yowa = "audio/yowa.ogg"
define audio.tips = "audio/tips.ogg"
image zicheng1_shadow:
    "images/shadows/zicheng1_shadow.webp"
image zicheng2_shadow:
    "images/shadows/zicheng2_shadow.webp"
image kexi1_shadow:
    "images/shadows/kexi1_shadow.webp"
image kexi2_shadow:
    "images/shadows/kexi2_shadow.webp"
image sensei1_shadow:
    "images/shadows/sensei1_shadow.webp"

image quickmenu_roll2= Text(_("回退"),font="Huayuan.Gothic.Bold.ttf", size=40,color="#000000",outlines = [(2,"#ffffff",1,1)])
layeredimage ui_quickmenu_roll_on:
        always:
            "gui/quickmenu/roll2.webp" zoom 1.2 xpos 0.005 ypos 0.005
        group pose:
            attribute title default:
                "quickmenu_roll2" xpos 0.025
image quickmenu_roll= Text(_("回退"),font="Huayuan.Gothic.Bold.ttf", size=40,color="#ffffff",outlines = [(2,"#000000",1,1)])
layeredimage ui_quickmenu_roll:
        always:
            "gui/quickmenu/roll.webp" zoom 1.2 xpos 0.005 ypos 0.005
        group pose:
            attribute title default:
                "quickmenu_roll" xpos 0.025

image quickmenu_history2= Text(_("历史"),font="Huayuan.Gothic.Bold.ttf", size=40,color="#000000",outlines = [(2,"#ffffff",1,1)])
layeredimage ui_quickmenu_history_on:
        always:
            "gui/quickmenu/history2.webp" zoom 1.2 xpos 0.005 ypos 0.005
        group pose:
            attribute title default:
                "quickmenu_history2" xpos 0.025
image quickmenu_history= Text(_("历史"),font="Huayuan.Gothic.Bold.ttf", size=40,color="#ffffff",outlines = [(2,"#000000",1,1)])
layeredimage ui_quickmenu_history:
        always:
            "gui/quickmenu/history.webp" zoom 1.2 xpos 0.005 ypos 0.005
        group pose:
            attribute title default:
                "quickmenu_history" xpos 0.025

image quickmenu_tips2= Text(_("提示"),font="Huayuan.Gothic.Bold.ttf", size=40,color="#000000",outlines = [(2,"#ffffff",1,1)])
layeredimage ui_quickmenu_tips_on:
        always:
            "gui/quickmenu/tips2.webp" zoom 1.2 xpos 0.005 ypos 0.005
        group pose:
            attribute title default:
                "quickmenu_tips2" xpos 0.025
image quickmenu_tips= Text(_("提示"),font="Huayuan.Gothic.Bold.ttf", size=40,color="#ffffff",outlines = [(2,"#000000",1,1)])
layeredimage ui_quickmenu_tips:
        always:
            "gui/quickmenu/tips.webp" zoom 1.2 xpos 0.005 ypos 0.005
        group pose:
            attribute title default:
                "quickmenu_tips" xpos 0.025

image quickmenu_quicksave2= Text(_("快存"),font="Huayuan.Gothic.Bold.ttf", size=40,color="#000000",outlines = [(2,"#ffffff",1,1)])
layeredimage ui_quickmenu_quicksave_on:
        always:
            "gui/quickmenu/quicksave2.webp" zoom 1.2 xpos 0.005 ypos 0.005
        group pose:
            attribute title default:
                "quickmenu_quicksave2" xpos 0.025
image quickmenu_quicksave= Text(_("快存"),font="Huayuan.Gothic.Bold.ttf", size=40,color="#ffffff",outlines = [(2,"#000000",1,1)])
layeredimage ui_quickmenu_quicksave:
        always:
            "gui/quickmenu/quicksave.webp" zoom 1.2 xpos 0.005 ypos 0.005
        group pose:
            attribute title default:
                "quickmenu_quicksave" xpos 0.025

image quickmenu_quick2= Text(_("快进"),font="Huayuan.Gothic.Bold.ttf", size=40,color="#000000",outlines = [(2,"#ffffff",1,1)])
layeredimage ui_quickmenu_quick_on:
        always:
            "gui/quickmenu/quick2.webp" zoom 1.2 xpos 0.005 ypos 0.005
        group pose:
            attribute title default:
                "quickmenu_quick2" xpos 0.025
image quickmenu_quick= Text(_("快进"),font="Huayuan.Gothic.Bold.ttf", size=40,color="#ffffff",outlines = [(2,"#000000",1,1)])
layeredimage ui_quickmenu_quick:
        always:
            "gui/quickmenu/quick.webp" zoom 1.2 xpos 0.005 ypos 0.005
        group pose:
            attribute title default:
                "quickmenu_quick" xpos 0.025

image quickmenu_auto2= Text(_("自动"),font="Huayuan.Gothic.Bold.ttf", size=40,color="#000000",outlines = [(2,"#ffffff",1,1)])
layeredimage ui_quickmenu_auto_on:
        always:
            "gui/quickmenu/auto2.webp" zoom 1.2 xpos 0.005 ypos 0.005
        group pose:
            attribute title default:
                "quickmenu_auto2" xpos 0.025
image quickmenu_auto= Text(_("自动"),font="Huayuan.Gothic.Bold.ttf", size=40,color="#ffffff",outlines = [(2,"#000000",1,1)])
layeredimage ui_quickmenu_auto:
        always:
            "gui/quickmenu/auto.webp" zoom 1.2 xpos 0.005 ypos 0.005
        group pose:
            attribute title default:
                "quickmenu_auto" xpos 0.025

image quickmenu_load2= Text(_("读取"),font="Huayuan.Gothic.Bold.ttf", size=40,color="#000000",outlines = [(2,"#ffffff",1,1)])
layeredimage ui_quickmenu_load_on:
        always:
            "gui/quickmenu/load2.webp" zoom 1.2 xpos 0.005 ypos 0.005
        group pose:
            attribute title default:
                "quickmenu_load2" xpos 0.025
image quickmenu_load= Text(_("读取"),font="Huayuan.Gothic.Bold.ttf", size=40,color="#ffffff",outlines = [(2,"#000000",1,1)])
layeredimage ui_quickmenu_load:
        always:
            "gui/quickmenu/load.webp" zoom 1.2 xpos 0.005 ypos 0.005
        group pose:
            attribute title default:
                "quickmenu_load" xpos 0.025

image quickmenu_quickload2= Text(_("快读"),font="Huayuan.Gothic.Bold.ttf", size=40,color="#000000",outlines = [(2,"#ffffff",1,1)])
layeredimage ui_quickmenu_quickload_on:
        always:
            "gui/quickmenu/quickload2.webp" zoom 1.2 xpos 0.005 ypos 0.005
        group pose:
            attribute title default:
                "quickmenu_quickload2" xpos 0.025
image quickmenu_quickload= Text(_("快读"),font="Huayuan.Gothic.Bold.ttf", size=40,color="#ffffff",outlines = [(2,"#000000",1,1)])
layeredimage ui_quickmenu_quickload:
        always:
            "gui/quickmenu/quickload.webp" zoom 1.2 xpos 0.005 ypos 0.005
        group pose:
            attribute title default:
                "quickmenu_quickload" xpos 0.025

image quickmenu_menu2= Text(_("菜单"),font="Huayuan.Gothic.Bold.ttf", size=40,color="#000000",outlines = [(2,"#ffffff",1,1)])
layeredimage ui_quickmenu_menu_on:
        always:
            "gui/quickmenu/menu2.webp" zoom 1.2 xpos 0.005 ypos 0.005
        group pose:
            attribute title default:
                "quickmenu_menu2" xpos 0.025
image quickmenu_menu= Text(_("菜单"),font="Huayuan.Gothic.Bold.ttf", size=40,color="#ffffff",outlines = [(2,"#000000",1,1)])
layeredimage ui_quickmenu_menu:
        always:
            "gui/quickmenu/menu.webp" zoom 1.2 xpos 0.005 ypos 0.005
        group pose:
            attribute title default:
                "quickmenu_menu" xpos 0.025

image quickmenu_save2= Text(_("保存"),font="Huayuan.Gothic.Bold.ttf", size=40,color="#000000",outlines = [(2,"#ffffff",1,1)])
layeredimage ui_quickmenu_save_on:
        always:
            "gui/quickmenu/save2.webp" zoom 1.2 xpos 0.005 ypos 0.005
        group pose:
            attribute title default:
                "quickmenu_save2" xpos 0.025
image quickmenu_save= Text(_("保存"),font="Huayuan.Gothic.Bold.ttf", size=40,color="#ffffff",outlines = [(2,"#000000",1,1)])
layeredimage ui_quickmenu_save:
        always:
            "gui/quickmenu/save.webp" zoom 1.2 xpos 0.005 ypos 0.005
        group pose:
            attribute title default:
                "quickmenu_save" xpos 0.025

image logo= At("title/logo.webp")
image warning= Text(_("{b}本故事纯属虚构。\n与现实生活中任何个人或组织均无关联。\n游戏内包含的所有内容。\n均无存在影射任何现实事物的含义\n请勿主观带入。若由此带来不良后果，\n本游戏不承担任何连带责任。{/b}"),font="Cubic-11-1.000-R-2.ttf", size=45,color="#ffffff")
image play= Text(_("{b}本游戏推荐外设设备：鼠标。\n使用鼠标游玩以获得最佳效果。{/b}"),font="Cubic-11-1.000-R-2.ttf", size=45,color="#ffffff")
image start= Text("{b}START{/b}", size=45,color="#000000")
image hito_kotoba= Text("{font=Cubic-11-1.000-R-2.ttf}』{/font}{image=kotoba}{alt}kotoba{/alt}", size=45,color="#ffffff")
image kotoba:
        "gui/ctc/ctc_full.webp"
        0.6
        "gui/ctc/ctc_down1.webp"
        0.1
        "gui/ctc/ctc_down2.webp"
        0.1
        "gui/ctc/ctc_top3.webp"
        0.6
        "gui/ctc/ctc_down2.webp"
        0.1
        "gui/ctc/ctc_down1.webp"
        0.1
        "gui/ctc/ctc_full.webp"
        0.6
        "gui/ctc/ctc_top1.webp"
        0.1
        "gui/ctc/ctc_top2.webp"
        0.1
        "gui/ctc/ctc_down3.webp"
        0.6
        "gui/ctc/ctc_top2.webp"
        0.1
        "gui/ctc/ctc_top1.webp"
        0.1
        repeat
image eye:
        "anime/eye/01.webp"
        0.9
        "anime/eye/02.webp"
        0.1
        "anime/eye/03.webp"
        0.5
        "anime/eye/02.webp"
        0.1
        "anime/eye/01.webp"
        0.7
        "anime/eye/02.webp"
        0.1
        "anime/eye/03.webp"
        0.1
        "anime/eye/04.webp"
        2.0
##
layeredimage unlocked:
        always:
            "gui/locked.webp"
        group pose:
            attribute title default:
                "gui/nvl.webp"
layeredimage unlocked_on:
        always:
            "gui/locked.webp"
        group pose:
            attribute title default:
                "gui/locked.webp"
##
##
layeredimage cg_1:
        always:
            "images/bg_gohan_tukue2.webp"
        group pose:
            attribute title default:
                "gui/nvl.webp"
layeredimage cg_1_on:
        always:
            "gui/nvl.webp"
        group pose:
            attribute title default:
                "images/bg_gohan_tukue2.webp"
##
##
layeredimage cg_2:
        always:
            "images/bg_kexi_momo.webp"
        group pose:
            attribute title default:
                "gui/nvl.webp"
layeredimage cg_2_on:
        always:
            "gui/nvl.webp"
        group pose:
            attribute title default:
                "images/bg_kexi_momo.webp"
##
##
layeredimage cg_3:
        always:
            "images/bg_kexi_egao.webp"
        group pose:
            attribute title default:
                "gui/nvl.webp"
layeredimage cg_3_on:
        always:
            "gui/nvl.webp"
        group pose:
            attribute title default:
                "images/bg_kexi_egao.webp"
##
##
layeredimage cg_4:
        always:
            "images/bg_sorawomiru.webp"
        group pose:
            attribute title default:
                "gui/nvl.webp"
layeredimage cg_4_on:
        always:
            "gui/nvl.webp"
        group pose:
            attribute title default:
                "images/bg_sorawomiru.webp"
##
##
layeredimage cg_5:
        always:
            "images/bg_sorawomiru2.webp"
        group pose:
            attribute title default:
                "gui/nvl.webp"
layeredimage cg_5_on:
        always:
            "gui/nvl.webp"
        group pose:
            attribute title default:
                "images/bg_sorawomiru2.webp"
##
##
layeredimage cg_6:
        always:
            "images/bg_neko.webp"
        group pose:
            attribute title default:
                "gui/nvl.webp"
layeredimage cg_6_on:
        always:
            "gui/nvl.webp"
        group pose:
            attribute title default:
                "images/bg_neko.webp"
##
##
layeredimage cg_7:
        always:
            "images/bg_mizu.webp"
        group pose:
            attribute title default:
                "gui/nvl.webp"
layeredimage cg_7_on:
        always:
            "gui/nvl.webp"
        group pose:
            attribute title default:
                "images/bg_mizu.webp"
##
##
layeredimage cg_8:
        always:
            "images/bg_kawa.webp"
        group pose:
            attribute title default:
                "gui/nvl.webp"
layeredimage cg_8_on:
        always:
            "gui/nvl.webp"
        group pose:
            attribute title default:
                "images/bg_kawa.webp"
##
##
layeredimage cg_9:
        always:
            "images/bg_kabann.webp"
        group pose:
            attribute title default:
                "gui/nvl.webp"
layeredimage cg_9_on:
        always:
            "gui/nvl.webp"
        group pose:
            attribute title default:
                "images/bg_kabann.webp"
##
##
layeredimage cg_10:
        always:
            "images/bg_kexi_miru.webp"
        group pose:
            attribute title default:
                "gui/nvl.webp"
layeredimage cg_10_on:
        always:
            "gui/nvl.webp"
        group pose:
            attribute title default:
                "images/bg_kexi_miru.webp"
##
##
layeredimage cg_11:
        always:
            "images/bg_school_hiroba.webp"
        group pose:
            attribute title default:
                "gui/nvl.webp"
layeredimage cg_11_on:
        always:
            "gui/nvl.webp"
        group pose:
            attribute title default:
                "images/bg_school_hiroba.webp"
##
##
layeredimage cg_12:
        always:
            "images/bg_school_hiroba2.webp"
        group pose:
            attribute title default:
                "gui/nvl.webp"
layeredimage cg_12_on:
        always:
            "gui/nvl.webp"
        group pose:
            attribute title default:
                "images/bg_school_hiroba2.webp"
##
layeredimage cg_13:
        always:
            "images/bg_kexi_shiru.webp"
        group pose:
            attribute title default:
                "gui/nvl.webp"
layeredimage cg_13_on:
        always:
            "gui/nvl.webp"
        group pose:
            attribute title default:
                "images/bg_kexi_shiru.webp"
##
##
layeredimage cg_14:
        always:
            "images/bg_zicheng_te.webp"
        group pose:
            attribute title default:
                "gui/nvl.webp"
layeredimage cg_14_on:
        always:
            "gui/nvl.webp"
        group pose:
            attribute title default:
                "images/bg_zicheng_te.webp"
##
##
layeredimage cg_15:
        always:
            "images/bg_kexi_syashin.webp"
        group pose:
            attribute title default:
                "gui/nvl.webp"
layeredimage cg_15_on:
        always:
            "gui/nvl.webp"
        group pose:
            attribute title default:
                "images/bg_kexi_syashin.webp"
##
##
layeredimage cg_16:
        always:
            "images/bg_zicheng_te2.webp"
        group pose:
            attribute title default:
                "gui/nvl.webp"
layeredimage cg_16_on:
        always:
            "gui/nvl.webp"
        group pose:
            attribute title default:
                "images/bg_zicheng_te2.webp"
##
layeredimage end_locked_on:
        always:
            "gui/locked.webp"
        group pose:
            attribute title default:
                "end_lockedtext" xcenter 0.5 ycenter 1.18
image end_lockedtext= Text("???",font="Aldrich-Regular.ttf", size=180,color="#ffffff",outlines = [(3,"#000000",1,1)])
image end_lockedtext2= Text("???",font="Aldrich-Regular.ttf", size=180,color="#000000",outlines = [(3,"#ffffff",1,1)])
layeredimage end_locked:
        always:
            "gui/locked.webp"
        group pose:
            attribute title default:
                "end_lockedtext2" xcenter 0.5 ycenter 1.18
##
layeredimage extraend1:
        always:
            "chapters/end1.webp"
        group pose:
            attribute title default:
                "chapters/end1.webp"
        group end:
            attribute title default:
                "end1_text" xcenter 0.5 ycenter 1.16
layeredimage extraend1_on:
        always:
            "chapters/end1_menu.webp"
        group pose:
            attribute title default:
                "end1_f" zoom 0.5 ycenter 0.5 xpos 0.5
        group end:
            attribute title default:
                "end1_text2" xcenter 0.5 ycenter 1.16
image end1_f=im.MatrixColor("chapters/end1.webp", im.matrix.colorize("#FFFFFF", "#000000"))
image end1_text= Text(_("结局一：无限命运的重叠"),font="Huayuan.Gothic.Bold.ttf", size=150,color="#ffffff",outlines = [(3,"#000000",1,1)])
image end1_text2= Text(_("结局一：无限命运的重叠"),font="Huayuan.Gothic.Bold.ttf", size=150,color="#000000",outlines = [(3,"#ffffff",1,1)])
##
layeredimage extraend2:
        always:
            "chapters/end2.webp"
        group pose:
            attribute title default:
                "chapters/end2.webp"
        group end:
            attribute title default:
                "end2_text" xcenter 0.5 ycenter 1.16
##
##
layeredimage extraend2_on:
        always:
            "chapters/end2_menu.webp"
        group pose:
            attribute title default:
                "end2_f" zoom 0.5 ycenter 0.5 xpos 0.5
        group end:
            attribute title default:
                "end2_text2" xcenter 0.5 ycenter 1.16
##
image end2_f=im.MatrixColor("chapters/end2.webp", im.matrix.colorize("#FFFFFF", "#000000"))
image end2_text= Text(_("结局二：逃避延拖的恶终"),font="Huayuan.Gothic.Bold.ttf", size=150,color="#ffffff",outlines = [(3,"#000000",1,1)])
image end2_text2= Text(_("结局二：逃避延拖的恶终"),font="Huayuan.Gothic.Bold.ttf", size=150,color="#000000",outlines = [(3,"#ffffff",1,1)])
##
layeredimage extraend3:
        always:
            "chapters/end3.webp"
        group pose:
            attribute title default:
                "chapters/end3.webp"
        group end:
            attribute title default:
                "end3_text" xcenter 0.5 ycenter 1.16
##
##
layeredimage extraend3_on:
        always:
            "chapters/end3.webp"
        group pose:
            attribute title default:
                "chapters/end3.webp"
        group end:
            attribute title default:
                "end3_text2" xcenter 0.5 ycenter 1.16
##
image end3_text= Text(_("结局三：明了曲折的抱憾"),font="Huayuan.Gothic.Bold.ttf", size=150,color="#ffffff",outlines = [(3,"#000000",1,1)])
image end3_text2= Text(_("结局三：明了曲折的抱憾"),font="Huayuan.Gothic.Bold.ttf", size=150,color="#000000",outlines = [(3,"#ffffff",1,1)])
##
layeredimage extraend4:
        always:
            "chapters/end4.webp"
        group pose:
            attribute title default:
                "chapters/end4.webp"
        group end:
            attribute title default:
                "end4_text" xcenter 0.5 ycenter 1.16
##
image end4_f=im.MatrixColor("chapters/end4.webp", im.matrix.colorize("#FFFFFF", "#000000"))
image end4_text= Text(_("结局四：志存高远的破釜"),font="Huayuan.Gothic.Bold.ttf", size=150,color="#ffffff",outlines = [(3,"#000000",1,1)])
image end4_text2= Text(_("结局四：志存高远的破釜"),font="Huayuan.Gothic.Bold.ttf", size=150,color="#000000",outlines = [(3,"#ffffff",1,1)])
##
##
layeredimage extraend4_on:
        always:
            "chapters/end4_menu.webp"
        group pose:
            attribute title default:
                "end4_f" zoom 0.5 ycenter 0.5 xpos 0.5
        group end:
            attribute title default:
                "end4_text2" xcenter 0.5 ycenter 1.16
##
layeredimage extraend5:
        always:
            "chapters/end5.webp"
        group pose:
            attribute title default:
                "chapters/end5.webp"
        group end:
            attribute title default:
                "end5_text" xcenter 0.5 ycenter 1.16
##
image end5_f=im.MatrixColor("chapters/end5.webp", im.matrix.colorize("#FFFFFF", "#000000"))
image end5_text= Text(_("结局五：取义断念的决绝"),font="Huayuan.Gothic.Bold.ttf", size=150,color="#ffffff",outlines = [(3,"#000000",1,1)])
image end5_text2= Text(_("结局五：取义断念的决绝"),font="Huayuan.Gothic.Bold.ttf", size=150,color="#000000",outlines = [(3,"#ffffff",1,1)])
##
layeredimage extraend5_on:
        always:
            "chapters/end5_menu.webp"
        group pose:
            attribute title default:
                "end5_f" zoom 0.5 ycenter 0.5 xpos 0.5
        group end:
            attribute title default:
                "end5_text2" xcenter 0.5 ycenter 1.16
##
##
layeredimage extraend6:
        always:
            "chapters/end6.webp"
        group pose:
            attribute title default:
                "chapters/end6.webp"
        group end:
            attribute title default:
                "end6_text" xcenter 0.5 ycenter 1.16
##
##
layeredimage extraend6_on:
        always:
            "chapters/end6_menu.webp"
        group pose:
            attribute title default:
                "end6_f" zoom 0.5 ycenter 0.5 xpos 0.5
        group end:
            attribute title default:
                "end6_text2" xcenter 0.5 ycenter 1.16
##
image end6_f=im.MatrixColor("chapters/end6.webp", im.matrix.colorize("#FFFFFF", "#000000"))
image end6_text= Text(_("结局六：时间刻环的补缺"),font="Huayuan.Gothic.Bold.ttf", size=150,color="#ffffff",outlines = [(3,"#000000",1,1)])
image end6_text2= Text(_("结局六：时间刻环的补缺"),font="Huayuan.Gothic.Bold.ttf", size=150,color="#000000",outlines = [(3,"#ffffff",1,1)])
##
layeredimage extrachapter1:
        always:
            "chapters/chapter1.webp"
        group chapter:
            attribute title default:
                "chapter1_text" xcenter 0.5 ycenter 1.16
##
##
layeredimage extrachapter1_on:
        always:
            "chapter1_f"
        group end:
            attribute title default:
                "chapter1_text2" xcenter 0.5 ycenter 1.16
##
image chapter1_f=im.MatrixColor("chapters/chapter1.webp", im.matrix.colorize("#FFFFFF", "#000000"))
image chapter1_text= Text(_("章节一：莫比乌斯的始段"),font="Huayuan.Gothic.Bold.ttf", size=150,color="#ffffff",outlines = [(3,"#000000",1,1)])
image chapter1_text2= Text(_("章节一：莫比乌斯的始段"),font="Huayuan.Gothic.Bold.ttf", size=150,color="#000000",outlines = [(3,"#ffffff",1,1)])
##
##
layeredimage extrachapter2:
        always:
            "chapters/chapter2.webp"
        group chapter:
            attribute title default:
                "chapter2_text" xcenter 0.5 ycenter 1.16
##
##
layeredimage extrachapter2_on:
        always:
            "chapter2_f"
        group end:
            attribute title default:
                "chapter2_text2" xcenter 0.5 ycenter 1.16
##
image chapter2_f=im.MatrixColor("chapters/chapter2.webp", im.matrix.colorize("#FFFFFF", "#000000"))
image chapter2_text= Text(_("章节二：死而又生的起始"),font="Huayuan.Gothic.Bold.ttf", size=150,color="#ffffff",outlines = [(3,"#000000",1,1)])
image chapter2_text2= Text(_("章节二：死而又生的起始"),font="Huayuan.Gothic.Bold.ttf", size=150,color="#000000",outlines = [(3,"#ffffff",1,1)])
##
##
layeredimage extrachapter3:
        always:
            "chapters/chapter3.webp"
        group chapter:
            attribute title default:
                "chapter3_text" xcenter 0.5 ycenter 1.16
##
##
layeredimage extrachapter3_on:
        always:
            "chapter3_f"
        group end:
            attribute title default:
                "chapter3_text2" xcenter 0.5 ycenter 1.16
##
image chapter3_f=im.MatrixColor("chapters/chapter3.webp", im.matrix.colorize("#FFFFFF", "#000000"))
image chapter3_text= Text(_("章节三：收束迷宫的展露"),font="Huayuan.Gothic.Bold.ttf", size=150,color="#ffffff",outlines = [(3,"#000000",1,1)])
image chapter3_text2= Text(_("章节三：收束迷宫的展露"),font="Huayuan.Gothic.Bold.ttf", size=150,color="#000000",outlines = [(3,"#ffffff",1,1)])
##
##
layeredimage extrachapter4:
        always:
            "chapters/chapter4.webp"
        group chapter:
            attribute title default:
                "chapter4_text" xcenter 0.5 ycenter 1.16
##
##
layeredimage extrachapter4_on:
        always:
            "chapter4_f"
        group end:
            attribute title default:
                "chapter4_text2" xcenter 0.5 ycenter 1.16
##
image chapter4_f=im.MatrixColor("chapters/chapter4.webp", im.matrix.colorize("#FFFFFF", "#000000"))
image chapter4_text= Text(_("章节四：博弈棋盘的翻转"),font="Huayuan.Gothic.Bold.ttf", size=150,color="#ffffff",outlines = [(3,"#000000",1,1)])
image chapter4_text2= Text(_("章节四：博弈棋盘的翻转"),font="Huayuan.Gothic.Bold.ttf", size=150,color="#000000",outlines = [(3,"#ffffff",1,1)])
##
##
layeredimage extrachapter5:
        always:
            "chapters/chapter5.webp"
        group chapter:
            attribute title default:
                "chapter5_text" xcenter 0.5 ycenter 1.16
##
##
layeredimage extrachapter5_on:
        always:
            "chapter5_f"
        group end:
            attribute title default:
                "chapter5_text2" xcenter 0.5 ycenter 1.16
##
image chapter5_f=im.MatrixColor("chapters/chapter5.webp", im.matrix.colorize("#FFFFFF", "#000000"))
image chapter5_text= Text(_("章节五：真正终点的寻觅"),font="Huayuan.Gothic.Bold.ttf", size=150,color="#ffffff",outlines = [(3,"#000000",1,1)])
image chapter5_text2= Text(_("章节五：真正终点的寻觅"),font="Huayuan.Gothic.Bold.ttf", size=150,color="#000000",outlines = [(3,"#ffffff",1,1)])
##
##
layeredimage extrachapter6:
        always:
            "chapters/chapter6.webp"
        group chapter:
            attribute title default:
                "chapter6_text" xcenter 0.5 ycenter 1.16
##
##
layeredimage extrachapter6_on:
        always:
            "chapter6_f"
        group end:
            attribute title default:
                "chapter6_text2" xcenter 0.5 ycenter 1.16
##
image chapter6_f=im.MatrixColor("chapters/chapter6.webp", im.matrix.colorize("#FFFFFF", "#000000"))
image chapter6_text= Text(_("章节六：衔尾蛇缠的终末"),font="Huayuan.Gothic.Bold.ttf", size=150,color="#ffffff",outlines = [(3,"#000000",1,1)])
image chapter6_text2= Text(_("章节六：衔尾蛇缠的终末"),font="Huayuan.Gothic.Bold.ttf", size=150,color="#000000",outlines = [(3,"#ffffff",1,1)])
##
layeredimage ui_page1_on:
        always:
                "title_page1_2"
layeredimage ui_page1:
        always:
                "title_page1"
image title_page1= Text("1",font="Aldrich-Regular.ttf", size=60,color="#ffffff",outlines = [(3,"#000000",1,1)])
image title_page1_2= Text("1",font="Aldrich-Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
##
##
layeredimage ui_page2_on:
        always:
                "title_page2_2"
layeredimage ui_page2:
        always:
                "title_page2"
image title_page2= Text("2",font="Aldrich-Regular.ttf", size=60,color="#ffffff",outlines = [(3,"#000000",1,1)])
image title_page2_2= Text("2",font="Aldrich-Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
##
##
layeredimage ui_page3_on:
        always:
                "title_page3_2"
layeredimage ui_page3:
        always:
                "title_page3"
image title_page3= Text("3",font="Aldrich-Regular.ttf", size=60,color="#ffffff",outlines = [(3,"#000000",1,1)])
image title_page3_2= Text("3",font="Aldrich-Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
##
##
layeredimage ui_page4_on:
        always:
                "title_page4_2"
layeredimage ui_page4:
        always:
                "title_page4"
image title_page4= Text("4",font="Aldrich-Regular.ttf", size=60,color="#ffffff",outlines = [(3,"#000000",1,1)])
image title_page4_2= Text("4",font="Aldrich-Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
##
##
layeredimage ui_page5_on:
        always:
                "title_page5_2"
layeredimage ui_page5:
        always:
                "title_page5"
image title_page5= Text("5",font="Aldrich-Regular.ttf", size=60,color="#ffffff",outlines = [(3,"#000000",1,1)])
image title_page5_2= Text("5",font="Aldrich-Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
##
image title_page= Text("PAGE",font="Aldrich-Regular.ttf", size=120,color="#ffffff",outlines = [(3,"#000000",1,1)])
layeredimage ui_page:
        always:
            "gui/ui_black.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_page"
##
##
layeredimage ui_page6_on:
        always:
                "title_page6_2"
layeredimage ui_page6:
        always:
                "title_page6"
image title_page6= Text("6",font="Aldrich-Regular.ttf", size=60,color="#ffffff",outlines = [(3,"#000000",1,1)])
image title_page6_2= Text("6",font="Aldrich-Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
##
##
layeredimage ui_page7_on:
        always:
                "title_page7_2"
layeredimage ui_page7:
        always:
                "title_page7"
image title_page7= Text("7",font="Aldrich-Regular.ttf", size=60,color="#ffffff",outlines = [(3,"#000000",1,1)])
image title_page7_2= Text("7",font="Aldrich-Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
##
##
layeredimage ui_page8_on:
        always:
                "title_page8_2"
layeredimage ui_page8:
        always:
                "title_page8"
image title_page8= Text("8",font="Aldrich-Regular.ttf", size=60,color="#ffffff",outlines = [(3,"#000000",1,1)])
image title_page8_2= Text("8",font="Aldrich-Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
##
##
layeredimage ui_page9_on:
        always:
                "title_page9_2"
layeredimage ui_page9:
        always:
                "title_page9"
image title_page9= Text("9",font="Aldrich-Regular.ttf", size=60,color="#ffffff",outlines = [(3,"#000000",1,1)])
image title_page9_2= Text("9",font="Aldrich-Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])

##
##
layeredimage ui_page10_on:
        always:
                "title_page10_2"
layeredimage ui_page10:
        always:
                "title_page10"
image title_page10= Text("10",font="Aldrich-Regular.ttf", size=60,color="#ffffff",outlines = [(3,"#000000",1,1)])
image title_page10_2= Text("10",font="Aldrich-Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])

##
##
layeredimage ui_pageauto_on:
        always:
                "title_pageauto_2"
layeredimage ui_pageauto:
        always:
                "title_pageauto"
image title_pageauto= Text("A",font="Aldrich-Regular.ttf", size=60,color="#ffffff",outlines = [(3,"#000000",1,1)])
image title_pageauto_2= Text("A",font="Aldrich-Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])

##
##
layeredimage ui_pagequick_on:
        always:
                "title_pagequick_2"
layeredimage ui_pagequick:
        always:
                "title_pagequick"
image title_pagequick= Text("Q",font="Aldrich-Regular.ttf", size=60,color="#ffffff",outlines = [(3,"#000000",1,1)])
image title_pagequick_2= Text("Q",font="Aldrich-Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])

##
image title_page= Text("PAGE",font="Aldrich-Regular.ttf", size=120,color="#ffffff",outlines = [(3,"#000000",1,1)])
layeredimage ui_page:
        always:
            "gui/ui_black.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_page"
##
##
image title_other= Text("OTHER",font="Aldrich-Regular.ttf", size=120,color="#ffffff",outlines = [(3,"#000000",1,1)])
image title_other_zhcn= Text(_("其他"),font="Huayuan.Gothic.Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
layeredimage ui_other:
        always:
            "gui/ui_white.webp" ypos 0.06 xpos 0.0
        group pose:
            attribute title default:
                "title_other" xpos -0.01
            attribute title default:
                "title_other_zhcn" ypos 0.026 xpos 0.213
##
##
image title_display= Text("DISPLAY",font="Aldrich-Regular.ttf", size=120,color="#ffffff",outlines = [(3,"#000000",1,1)])
image title_display_zhcn= Text(_("显示"),font="Huayuan.Gothic.Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
layeredimage ui_display:
        always:
            "gui/ui_white.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_display" xpos -0.006
            attribute title default:
                "title_display_zhcn" ypos 0.026 xpos 0.26
##
##
image title_skip= Text("SKIP",font="Aldrich-Regular.ttf", size=120,color="#ffffff",outlines = [(3,"#000000",1,1)])
image title_skip_zhcn= Text(_("快进"),font="Huayuan.Gothic.Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
layeredimage ui_skip:
        always:
            "gui/ui_white.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_skip" xpos -0.006
            attribute title default:
                "title_skip_zhcn" ypos 0.026 xpos 0.145
##
image title_start2= Text("START",font="Aldrich-Regular.ttf", size=120,color="#000000",outlines = [(3,"#ffffff",1,1)])
image title_start_zhcn= Text(_("新游戏"),font="Huayuan.Gothic.Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
layeredimage ui_start_on:
        always:
            "gui/ui_white.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_start2"
        group lang:
            attribute title default:
                "title_start_zhcn" ypos 0.026 xpos 0.213
image title_start= Text("START",font="Aldrich-Regular.ttf", size=120,color="#ffffff",outlines = [(3,"#000000",1,1)])
layeredimage ui_start:
        always:
            "gui/ui_black.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_start"
##
##
image title_quick2= Text("QUICK",font="Aldrich-Regular.ttf", size=120,color="#000000",outlines = [(3,"#ffffff",1,1)])
image title_quick_zhcn= Text(_("快速读取"),font="Huayuan.Gothic.Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
layeredimage ui_quick_on:
        always:
            "gui/ui_white.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_quick2"
        group lang:
            attribute title default:
                "title_quick_zhcn" ypos 0.026 xpos 0.215
image title_quick= Text("QUICK",font="Aldrich-Regular.ttf", size=120,color="#ffffff",outlines = [(3,"#000000",1,1)])
layeredimage ui_quick:
        always:
            "gui/ui_black.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_quick"
##
##
image title_tips2= Text("TIPS",font="Aldrich-Regular.ttf", size=120,color="#000000",outlines = [(3,"#ffffff",1,1)])
image title_tips_zhcn= Text(_("提示"),font="Huayuan.Gothic.Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
layeredimage ui_tips_on:
        always:
            "gui/ui_white.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_tips2"
        group lang:
            attribute title default:
                "title_tips_zhcn" ypos 0.026 xpos 0.150
image title_tips= Text("TIPS",font="Aldrich-Regular.ttf", size=120,color="#ffffff",outlines = [(3,"#000000",1,1)])
layeredimage ui_tips:
        always:
            "gui/ui_black.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_tips"
##
image title_save2= Text("SAVE",font="Aldrich-Regular.ttf", size=120,color="#000000",outlines = [(3,"#ffffff",1,1)])
image title_save_zhcn= Text(_("保存"),font="Huayuan.Gothic.Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
layeredimage ui_save_on:
        always:
            "gui/ui_white.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_save2"
        group lang:
            attribute title default:
                "title_save_zhcn" ypos 0.026 xpos 0.172
image title_save= Text("SAVE",font="Aldrich-Regular.ttf", size=120,color="#ffffff",outlines = [(3,"#000000",1,1)])
layeredimage ui_save:
        always:
            "gui/ui_black.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_save"
image title_load2= Text("LOAD",font="Aldrich-Regular.ttf", size=120,color="#000000",outlines = [(3,"#ffffff",1,1)])
image title_load_zhcn= Text(_("读取"),font="Huayuan.Gothic.Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
layeredimage ui_load_on:
        always:
            "gui/ui_white.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_load2"
        group lang:
            attribute title default:
                "title_load_zhcn" ypos 0.026 xpos 0.181
image title_load= Text("LOAD",font="Aldrich-Regular.ttf", size=120,color="#ffffff",outlines = [(3,"#000000",1,1)])
layeredimage ui_load:
        always:
            "gui/ui_black.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_load"
image title_help2= Text("HELP",font="Aldrich-Regular.ttf", size=120,color="#000000",outlines = [(3,"#ffffff",1,1)])
image title_help_zhcn= Text(_("帮助"),font="Huayuan.Gothic.Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
layeredimage ui_help_on:
        always:
            "gui/ui_white.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_help2"
        group lang:
            attribute title default:
                "title_help_zhcn" ypos 0.026 xpos 0.173
image title_help= Text("HELP",font="Aldrich-Regular.ttf", size=120,color="#ffffff",outlines = [(3,"#000000",1,1)])
layeredimage ui_help:
        always:
            "gui/ui_black.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_help"
image title_about2= Text("ABOUT",font="Aldrich-Regular.ttf", size=120,color="#000000",outlines = [(3,"#ffffff",1,1)])
image title_about_zhcn= Text(_("关于"),font="Huayuan.Gothic.Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
layeredimage ui_about_on:
        always:
            "gui/ui_white.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_about2"
        group lang:
            attribute title default:
                "title_about_zhcn" ypos 0.026 xpos 0.23
image title_about= Text("ABOUT",font="Aldrich-Regular.ttf", size=120,color="#ffffff",outlines = [(3,"#000000",1,1)])
layeredimage ui_about:
        always:
            "gui/ui_black.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_about"
image title_title2= Text("TITLE",font="Aldrich-Regular.ttf", size=120,color="#000000",outlines = [(3,"#ffffff",1,1)])
image title_title_zhcn= Text(_("主菜单"),font="Huayuan.Gothic.Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
layeredimage ui_title_on:
        always:
            "gui/ui_white.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_title2"
        group lang:
            attribute title default:
                "title_title_zhcn" ypos 0.026 xpos 0.177
image title_title= Text("TITLE",font="Aldrich-Regular.ttf", size=120,color="#ffffff",outlines = [(3,"#000000",1,1)])
layeredimage ui_title:
        always:
            "gui/ui_black.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_title"
image title_exit2= Text("EXIT",font="Aldrich-Regular.ttf", size=120,color="#000000",outlines = [(3,"#ffffff",1,1)])
image title_exit_zhcn= Text(_("退出"),font="Huayuan.Gothic.Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
layeredimage ui_exit_on:
        always:
            "gui/ui_white.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_exit2"
        group lang:
            attribute title default:
                "title_exit_zhcn" ypos 0.026 xpos 0.145
image title_exit= Text("EXIT",font="Aldrich-Regular.ttf", size=120,color="#ffffff",outlines = [(3,"#000000",1,1)])
layeredimage ui_exit:
        always:
            "gui/ui_black.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_exit"
image title_return2= Text("RETURN",font="Aldrich-Regular.ttf", size=120,color="#000000",outlines = [(3,"#ffffff",1,1)])
image title_return_zhcn= Text(_("返回"),font="Huayuan.Gothic.Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
layeredimage ui_return_on:
        always:
            "gui/ui_white.webp" ypos 0.06 xpos -0.06
        group pose:
            attribute title default:
                "title_return2" xpos 0.096
        group lang:
            attribute title default:
                "title_return_zhcn" ypos 0.026 xpos 0.034
image title_return= Text("RETURN",font="Aldrich-Regular.ttf", size=120,color="#ffffff",outlines = [(3,"#000000",1,1)])
layeredimage ui_return:
        always:
            "gui/ui_black.webp" ypos 0.06 xpos 0.02
        group pose:
            attribute title default:
                "title_return" xpos 0.096
image title_option2= Text("OPTIONS",font="Aldrich-Regular.ttf", size=120,color="#000000",outlines = [(3,"#ffffff",1,1)])
image title_option_zhcn= Text(_("选项"),font="Huayuan.Gothic.Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
layeredimage ui_option_on:
        always:
            "gui/ui_white.webp" ypos 0.06 xpos -0.04
        group pose:
            attribute title default:
                "title_option2" xpos 0.096
        group lang:
            attribute title default:
                "title_option_zhcn" ypos 0.026 xpos 0.034
image title_option= Text("OPTIONS",font="Aldrich-Regular.ttf", size=120,color="#ffffff",outlines = [(3,"#000000",1,1)])
layeredimage ui_option:
        always:
            "gui/ui_black.webp" ypos 0.06 xpos 0.02
        group pose:
            attribute title default:
                "title_option" xpos 0.096
##
image title_extra2= Text("EXTRA",font="Aldrich-Regular.ttf", size=120,color="#000000",outlines = [(3,"#ffffff",1,1)])
image title_extra_zhcn= Text(_("鉴赏"),font="Huayuan.Gothic.Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
layeredimage ui_extra_on:
        always:
            "gui/ui_white.webp" ypos 0.06 xpos -0.06
        group pose:
            attribute title default:
                "title_extra2" xpos 0.096+0.053
        group lang:
            attribute title default:
                "title_extra_zhcn" ypos 0.026 xpos 0.034+0.053
image title_extra= Text("EXTRA",font="Aldrich-Regular.ttf", size=120,color="#ffffff",outlines = [(3,"#000000",1,1)])
layeredimage ui_extra:
        always:
            "gui/ui_black.webp" ypos 0.06 xpos 0.02
        group pose:
            attribute title default:
                "title_extra" xpos 0.096+0.053
###
image title_cg2= Text("CG-ROOM",font="Aldrich-Regular.ttf", size=120,color="#000000",outlines = [(3,"#ffffff",1,1)])
image title_cg_zhcn= Text(_("立绘鉴赏"),font="Huayuan.Gothic.Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
layeredimage ui_cg_on:
        always:
            "gui/ui_white.webp" ypos 0.06 xpos 0.01 xzoom 2.2
        group pose:
            attribute title default:
                "title_cg2"
        group lang:
            attribute title default:
                "title_cg_zhcn" ypos 0.026 xpos 0.323
image title_cg= Text("CG-ROOM",font="Aldrich-Regular.ttf", size=120,color="#ffffff",outlines = [(3,"#000000",1,1)])
layeredimage ui_cg:
        always:
            "gui/ui_black.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_cg"
###
###
image title_music2= Text("MUSIC-ROOM",font="Aldrich-Regular.ttf", size=120,color="#000000",outlines = [(3,"#ffffff",1,1)])
image title_music_zhcn= Text(_("音乐鉴赏"),font="Huayuan.Gothic.Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
layeredimage ui_music_on:
        always:
            "gui/ui_white.webp" ypos 0.06 xpos 0.01 xzoom 2.2
        group pose:
            attribute title default:
                "title_music2"
        group lang:
            attribute title default:
                "title_music_zhcn" ypos 0.026 xpos 0.445
image title_music= Text("MUSIC-ROOM",font="Aldrich-Regular.ttf", size=120,color="#ffffff",outlines = [(3,"#000000",1,1)])
layeredimage ui_music:
        always:
            "gui/ui_black.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_music"
###
###
image title_end2= Text("END-UNLOCKED",font="Aldrich-Regular.ttf", size=120,color="#000000",outlines = [(3,"#ffffff",1,1)])
image title_end_zhcn= Text(_("已解锁结局"),font="Huayuan.Gothic.Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
layeredimage ui_end_on:
        always:
            "gui/ui_white.webp" ypos 0.06 xpos 0.01 xzoom 2.2
        group pose:
            attribute title default:
                "title_end2"
        group lang:
            attribute title default:
                "title_end_zhcn" ypos 0.026 xpos 0.527
image title_end= Text("END-UNLOCKED",font="Aldrich-Regular.ttf", size=120,color="#ffffff",outlines = [(3,"#000000",1,1)])
layeredimage ui_end:
        always:
            "gui/ui_black.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_end"
###
###
image title_chapter2= Text("CHAPTER-UNLOCKED",font="Aldrich-Regular.ttf", size=120,color="#000000",outlines = [(3,"#ffffff",1,1)])
image title_chapter_zhcn= Text(_("已解锁章节"),font="Huayuan.Gothic.Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
layeredimage ui_chapter_on:
        always:
            "gui/ui_white.webp" ypos 0.06 xpos 0.01 xzoom 2.2
        group pose:
            attribute title default:
                "title_chapter2"
        group lang:
            attribute title default:
                "title_chapter_zhcn" ypos 0.026 xpos 0.695
image title_chapter= Text("CHAPTER-UNLOCKED",font="Aldrich-Regular.ttf", size=120,color="#ffffff",outlines = [(3,"#000000",1,1)])
layeredimage ui_chapter:
        always:
            "gui/ui_black.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_chapter"
###
###
image title_keyboard2= Text("KEYBOARD",font="Aldrich-Regular.ttf", size=120,color="#000000",outlines = [(3,"#ffffff",1,1)])
image title_keyboard_zhcn= Text(_("键鼠"),font="Huayuan.Gothic.Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
layeredimage ui_keyboard_on:
        always:
            "gui/ui_white.webp" ypos 0.06 xpos 0.01 xzoom 1.2
        group pose:
            attribute title default:
                "title_keyboard2"
        group lang:
            attribute title default:
                "title_keyboard_zhcn" ypos 0.026 xpos 0.359
image title_keyboard= Text("KEYBOARD",font="Aldrich-Regular.ttf", size=120,color="#ffffff",outlines = [(3,"#000000",1,1)])
layeredimage ui_keyboard:
        always:
            "gui/ui_black.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_keyboard"
###
###
image title_gamepad2= Text("GAMEPAD",font="Aldrich-Regular.ttf", size=120,color="#000000",outlines = [(3,"#ffffff",1,1)])
image title_gamepad_zhcn= Text(_("手柄"),font="Huayuan.Gothic.Regular.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
layeredimage ui_gamepad_on:
        always:
            "gui/ui_white.webp" ypos 0.06 xpos 0.01 xzoom 1.2
        group pose:
            attribute title default:
                "title_gamepad2"
        group lang:
            attribute title default:
                "title_gamepad_zhcn" ypos 0.026 xpos 0.325
image title_gamepad= Text("GAMEPAD",font="Aldrich-Regular.ttf", size=120,color="#ffffff",outlines = [(3,"#000000",1,1)])
layeredimage ui_gamepad:
        always:
            "gui/ui_black.webp" ypos 0.06 xpos 0.01
        group pose:
            attribute title default:
                "title_gamepad"
###
image suduxian_:
        "anime/suduxian/1.webp"
        0.1
        "anime/suduxian/2.webp"
        0.1
        "anime/suduxian/3.webp"
        0.1
        "anime/suduxian/4.webp"
        0.1
        repeat
screen suduxian:
    add "suduxian_"
image ame_:
        "anime/ame/1.webp"
        0.05
        "anime/ame/2.webp"
        0.05
        "anime/ame/3.webp"
        0.05
        "anime/ame/4.webp"
        0.05
        "anime/ame/5.webp"
        0.05
        repeat
screen ame:
    add "ame_" alpha 0.4
image logo2=At("gui/logowhite_bg.webp")
label splashscreen:
    show logo2
    with fade
    $ renpy.pause(2, hard=False)
    hide logo2 with dissolve
    show logo:
      xcenter 0.5
      ycenter 0.5
    with fade
    $ renpy.pause(2, hard=False)
    hide logo with dissolve
    show warning:
      xcenter 0.5
      ycenter 0.5
    with dissolve
    $ renpy.pause(4, hard=False)
    hide warning with dissolve
    with fade
    return
## 用户可读的游戏名称。此命令用来设置默认窗口标题，并且会在界面和错误报告中出
## 现。
##
## 带有 _() 的字符串表示其可被翻译。
init python:
    define.move_transitions("move", 0.3)
define config.name = _("彼零之时")
define gui.interface_text_outlines = [(4,"#707070",1,1)]
define gui.input_text_outlines = [(4,"#000000",0,0)]
define gui.input_prompt_text_outlines = [(4,"#000000",0,0)]
define gui.label_text_outlines = [(4,"#000000",0,0)]
define gui.prompt_text_outlines = [(4,"#000000",0,0)]
define gui.dialogue_text_outlines = [(2,"#000000",1,1)]
define gui.notify_text_outlines = [(4,"#000000",0,0)]
##define gui.name_text_outlines = [(2,"#ffffff",0,0)]
#define config.mouse = { }
define config.mouse = {}
define config.mouse['default'] = [("gui/mouse/white.webp", 0, 0)]
define config.nvl_adv_transition = Dissolve(1)
define config.adv_nvl_transition = Dissolve(1)
## 决定上面给出的标题是否显示在标题界面屏幕。设置为 False 来隐藏标题。

define gui.show_name = False



## 放置在游戏内“关于”屏幕上的文本。将文本放在三个引号之间，并在段落之间留出空
## 行。
define gui.about = _p("""作者：戴夫邻居史蒂夫DFsteve\n个人博客：{a=https://www.dfsteve.top}www.dfsteve.top{/a}""")



## 在构建的发布版中，可执行文件和目录所使用的短名称。此处仅限使用 ASCII 字符，并
## 且不能包含空格、冒号或分号。

define build.name = "Zero_no_toki"


## 音效和音乐 #######################################################################

## 这三个变量控制哪些内置的混音器会默认显示给用户。将其中一个设置为 False 将隐藏
## 对应的混音器。

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## 为了让用户在音效或语音轨道上播放测试音频，请取消对下面一行的注释并设置播放的
## 样本声音。

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## 将以下语句取消注释就可以设置标题界面播放的背景音乐文件。此文件将在整个游戏中
## 持续播放，直至音乐停止或其他文件开始播放。



## 转场 ##########################################################################
##
## 这些变量用来控制某些事件发生时的转场。每一个变量都应设置成一个转场，或者是
## None 来表示无转场。

## 进入或退出游戏菜单。

define config.enter_transition = Pixellate(.5,5)
define config.exit_transition = Pixellate(.5,5)


## 各个游戏菜单之间的转场。

define config.intra_transition = dissolve
define config.end_splash_transition = dissolve

## 载入游戏后使用的转场。

define config.after_load_transition = Pixellate(.5,5)


## 在游戏结束之后进入主菜单时使用的转场。

define config.end_game_transition = dissolve


## 用于控制在游戏开始标签不存在时转场的变量。作为替代，在显示初始化场景后使用
## with 语句。


## 窗口管理 ########################################################################
##
## 此命令控制对话框窗口何时显示。若为 show，对话框将总是显示。若为 hide，对话框
## 仅在对话出现时显示。若为 auto，对话框会在 scene 语句前隐藏，并在有新对话时重
## 新显示。
##
## 在游戏开始后，可以用 window show、window hide 和 window auto 语句来改变其状
## 态。

define config.window = "hide"


## 用于显示和隐藏对话框窗口的转场

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## 默认设置 ########################################################################

## 控制默认的文字显示速度。默认的 0 为瞬间，而其他数字则是每秒显示出的字符数。

default preferences.text_cps = 20


## 默认的自动前进延迟。数字越大，等待时间越长，有效范围为 0 - 30。

default preferences.afm_time = 8


## 存档目录 ########################################################################
##
## 控制 Ren'Py 放置游戏存档的特定操作系统目录。存档文件将放置在：
##
## Windows：%APPDATA\RenPy\<config.save_directory>
##
## Macintosh：$HOME/Library/RenPy/<config.save_directory>
##
## Linux：$HOME/.renpy/<config.save_directory>
##
## 该语句通常不应变更，若要变更，应为有效字符串而不是表达式。

define config.save_directory = "Zero_no_toki"


## 图标 ##########################################################################
##
## 在任务栏或 Dock 上显示的图标。

define config.window_icon = "gui/window_icon.png"


## 构建配置 ########################################################################
##
## 此部分控制 Ren'Py 如何将您的项目转变为发行版文件。

init python:

    ## 以下函数接受文件模式。文件模式不区分大小写，并与基础目录的相对路径相匹
    ## 配，包括或不包括 /。如果多个模式匹配，则使用第一个模式。
    ##
    ## 在一个模式中：
    ##
    ## / 是目录分隔符。
    ##
    ## * 匹配所有字符，目录分隔符除外。
    ##
    ## ** 匹配所有字符，包括目录分隔符。
    ##
    ## 例如，“*.txt”匹配基础目录中的 txt 文件，“game/**.ogg”匹配游戏目录或任何子
    ## 目录中的 ogg 文件，“**.psd”匹配项目中任何位置的 psd 文件。

    ## 将文件列为 None 来使其从构建的发行版中排除。

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.save', None)
    build.classify('saves/**.save', None)
    build.classify('**.txt', None)
    build.classify('**.md', None)
    build.classify('saves/persistent', None)

    ## 若要封装文件，需将其列为“archive”。打包，使其无法被玩家更改

    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.rpyc', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.wav', 'archive')
    build.classify('game/**.ttf', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.webp', 'archive')

    ## 匹配为文档模式的文件会在 Mac 应用程序构建中被复制，因此它们同时出现在 APP
    ## 和 ZIP 文件中。

    build.documentation('*.html')
    build.documentation('*.txt')


## 下载扩展文件和执行应用内购需要一个 Google Play 许可密钥。许可密钥可以在
## Google Play 开发者控制台的“服务和 API”页面找到。

# define build.google_play_key = "..."


## 与 itch.io 项目相关的用户名和项目名，以 / 分隔。

# define build.itch_project = "renpytom/test-project"