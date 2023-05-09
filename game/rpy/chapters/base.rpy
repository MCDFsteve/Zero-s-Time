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
define d = Character(_("丁唯"),voice_tag="dingwei",outlines = [(3,"#a86a37",0,0)],ctc="hito_kotoba",ctc_position="nestled")
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
define mono = Character((""),ctc="hito_kotoba",ctc_position="nestled")
define nvle = Character("", kind=nvl, ctc="kotoba",ctc_position="nestled")
define nan = Character(_("？？？"),outlines = [(3,"#000000",0,0)],ctc="hito_kotoba",ctc_position="nestled")
define narrator = Character("", ctc="kotoba",ctc_position="nestled")    
# 游戏在此开始。
image end1=At("chapters/end1.webp")
image end2=At("chapters/end2.webp")