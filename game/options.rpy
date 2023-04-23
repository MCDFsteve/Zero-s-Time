define config.version  = "alpha-v1.0.12"
define audio.v1 = "voice/v1.ogg"
define audio.v3 = "voice/v3.ogg"
define audio.v5 = "voice/v5.ogg"
define audio.v7 = "voice/v7.ogg"
define audio.v9 = "voice/v9.ogg"
define audio.v11 = "voice/v11.ogg"
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
define audio.car_stop = "audio/car_stop.ogg"
define audio.mizu_help = "audio/mizu_help.ogg"
define audio.yousuru = "audio/yousuru.ogg"
image logo= At("title/logo.webp")
image warning= Text("{b}本故事纯属虚构。\n与现实生活中任何人和组织无关。\n存在的所有东西。\n都没有存在影射显示事物的含义\n请勿主观带入。{/b}",font="Cubic-11-1.000-R-2.ttf", size=45,color="#ffffff")
image play= Text("{b}本游戏推荐外设设备：鼠标。\n使用鼠标游玩以获得最佳效果。{/b}",font="Cubic-11-1.000-R-2.ttf", size=45,color="#ffffff")
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
image title_other_zhcn= Text("其他",font="ZiTiQuanWeiJunHei-W1-2.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
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
image title_display_zhcn= Text("显示",font="ZiTiQuanWeiJunHei-W1-2.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
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
image title_skip_zhcn= Text("快进",font="ZiTiQuanWeiJunHei-W1-2.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
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
image title_start_zhcn= Text("新游戏",font="ZiTiQuanWeiJunHei-W1-2.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
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
image title_quick_zhcn= Text("快速读取",font="ZiTiQuanWeiJunHei-W1-2.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
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
image title_tips_zhcn= Text("提示",font="ZiTiQuanWeiJunHei-W1-2.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
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
image title_save_zhcn= Text("保存",font="ZiTiQuanWeiJunHei-W1-2.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
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
image title_load_zhcn= Text("读取",font="ZiTiQuanWeiJunHei-W1-2.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
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
image title_help_zhcn= Text("帮助",font="ZiTiQuanWeiJunHei-W1-2.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
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
image title_about_zhcn= Text("关于",font="ZiTiQuanWeiJunHei-W1-2.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
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
image title_title_zhcn= Text("主菜单",font="ZiTiQuanWeiJunHei-W1-2.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
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
image title_exit_zhcn= Text("退出",font="ZiTiQuanWeiJunHei-W1-2.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
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
image title_return_zhcn= Text("返回",font="ZiTiQuanWeiJunHei-W1-2.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
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
image title_option_zhcn= Text("选项",font="ZiTiQuanWeiJunHei-W1-2.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
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
image title_extra_zhcn= Text("鉴赏",font="ZiTiQuanWeiJunHei-W1-2.ttf", size=60,color="#000000",outlines = [(3,"#ffffff",1,1)])
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
label splashscreen:
    if persistent.chapter==1:
       $ config.main_menu_music = "music/title.ogg"
    elif persistent.chapter==5:
       $ config.main_menu_music = "music/title2.ogg"
    elif persistent.chapter==6:
       $ config.main_menu_music = "music/title.ogg"
    else:
       $ config.main_menu_music = "music/title.ogg"
    scene bg_none 
    with fade
    show logo:
      xcenter 0.5
      ycenter 0.5
    with dissolve
    $ renpy.pause(2, hard=False)
    hide logo with dissolve
    show warning:
      xcenter 0.5
      ycenter 0.5
    with dissolve
    $ renpy.pause(3, hard=False)
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
    build.classify('**.txt', None)
    build.classify('**.md', None)

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