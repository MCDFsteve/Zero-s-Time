#覃可汐
init -1 python:
    def kexi1_kaixin_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="kexi":
            return ("kexi_shuohua_kaixin", .1)#播放口型动画1
        else:
            return ("kexi_bizui_kaixin", .1)
    def kexi1_nanguo_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="kexi":
            return ("kexi_shuohua_nanguo", .1)#播放口型动画1
        else:
            return ("kexi_bizui_nanguo", .1)
    def kexi1_duqi_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="kexi":
            return ("kexi_shuohua_duqi", .1)#播放口型动画1
        else:
            return ("kexi_bizui_duqi", .1)
    #def zicheng_talk2(st, at):
        #if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="zicheng":
            #return ("zicheng_talk_img1", .1)#播放口型动画2
        #else:
            #return ("zicheng_stoptalk", .1)
init -1:
#定义口型动画1
    image kexi_shuohua_kaixin:
        "images/hito/kexi/cengdie/zishi1/zui-banzhang.webp"
        0.1
        "images/hito/kexi/cengdie/zishi1/zui-zhangkai.webp"
        0.1
        "images/hito/kexi/cengdie/zishi1/zui-banzhang.webp"
        0.1
        "images/hito/kexi/cengdie/zishi1/zui-weixiao.webp"
        0.1
        repeat
    image kexi_shuohua_nanguo:
        "images/hito/kexi/cengdie/zishi1/zui-banzhang.webp"
        0.1
        "images/hito/kexi/cengdie/zishi1/zui-zhangkai.webp"
        0.1
        "images/hito/kexi/cengdie/zishi1/zui-banzhang.webp"
        0.1
        "images/hito/kexi/cengdie/zishi1/zui-nanguo.webp"
        0.1
        repeat
    image kexi_shuohua_duqi:
        "images/hito/kexi/cengdie/zishi1/zui-banzhang.webp"
        0.1
        "images/hito/kexi/cengdie/zishi1/zui-zhangkai.webp"
        0.1
        "images/hito/kexi/cengdie/zishi1/zui-banzhang.webp"
        0.1
        "images/hito/kexi/cengdie/zishi1/zui-duqi.webp"
        0.1
        repeat
    image kexi_bizui_kaixin:
        "images/hito/kexi/cengdie/zishi1/zui-weixiao.webp"
        0.2
        repeat
    image kexi_bizui_nanguo:
        "images/hito/kexi/cengdie/zishi1/zui-nanguo.webp"
        0.2
        repeat
    image kexi_bizui_duqi:
        "images/hito/kexi/cengdie/zishi1/zui-duqi.webp"
        0.2
        repeat
    
    image kexi1_kaixin = DynamicDisplayable(kexi1_kaixin_)
    image kexi1_nanguo = DynamicDisplayable(kexi1_nanguo_)
    image kexi1_duqi = DynamicDisplayable(kexi1_duqi_)
    #image zicheng_talk2_rtn = DynamicDisplayable(zicheng_talk2)
#yan睛正常
    image kexi1_moren_bi:
        "images/hito/kexi/cengdie/zishi1/yan-biyan.webp"
    image kexi1_moren_zhang:
        "images/hito/kexi/cengdie/zishi1//yan-zhengkai.webp"
    image kexi1_moren_banzhang:
        "images/hito/kexi/cengdie/zishi1//yan-banzhang.webp"

    image kexi1_moren:
        "kexi1_moren_zhang"
        choice 5:
            5.0
        choice 4:
            3.0
        choice 1:
            1.0
        "kexi1_moren_banzhang"
        0.1
        "kexi1_moren_bi"
        0.2
        "kexi1_moren_banzhang"
        0.1
        repeat
#yan睛正常
#yan睛heihua
    image kexi1_heihua_bi:
        "images/hito/kexi/cengdie/zishi1/yan-biyan-heihua.webp"
    image kexi1_heihua_zhang:
        "images/hito/kexi/cengdie/zishi1//yan-zhengkai-heihua.webp"
    image kexi1_heihua_banzhang:
        "images/hito/kexi/cengdie/zishi1//yan-banzhang-heihua.webp"
    image kexi1_heihua:
        "kexi1_heihua_zhang"
        choice 5:
            5.0
        choice 4:
            3.0
        choice 1:
            1.0
        "kexi1_heihua_banzhang"
        0.1
        "kexi1_heihua_bi"
        0.2
        "kexi1_heihua_banzhang"
        0.1
        repeat
#yan睛heihua
#yan睛heihualiuhan
    image kexi1_heihua2_bi:
        "images/hito/kexi/cengdie/zishi1/yan-biyan-heihua-liuhan.webp"
    image kexi1_heihua2_zhang:
        "images/hito/kexi/cengdie/zishi1//yan-zhengkai-heihua-liuhan.webp"
    image kexi1_heihua2_banzhang:
        "images/hito/kexi/cengdie/zishi1//yan-banzhang-heihua-liuhan.webp"
    image kexi1_heihua2:
        "kexi1_heihua2_zhang"
        choice 5:
            5.0
        choice 4:
            3.0
        choice 1:
            1.0
        "kexi1_heihua2_banzhang"
        0.1
        "kexi1_heihua2_bi"
        0.2
        "kexi1_heihua2_banzhang"
        0.1
        repeat
#yan睛heihualiuhan
#yan睛yihuo
    image kexi1_yihuo_bi:
        "images/hito/kexi/cengdie/zishi1/yan-biyan.webp"
    image kexi1_yihuo_zhang:
        "images/hito/kexi/cengdie/zishi1//yan-zhengkai-yihuo.webp"
    image kexi1_yihuo_banzhang:
        "images/hito/kexi/cengdie/zishi1//yan-banzhang-yihuo.webp"
    image kexi1_yihuo:
        "kexi1_yihuo_zhang"
        choice 5:
            5.0
        choice 4:
            3.0
        choice 1:
            1.0
        "kexi1_yihuo_banzhang"
        0.1
        "kexi1_yihuo_bi"
        0.2
        "kexi1_yihuo_banzhang"
        0.1
        repeat
#yan睛yihuo
#yan睛流泪
    image kexi1_leishui_bi:
        "images/hito/kexi/cengdie/zishi1/yan-biyan-leishui.webp"
    image kexi1_leishui_zhang:
        "images/hito/kexi/cengdie/zishi1//yan-zhengkai-leishui.webp"
    image kexi1_leishui_banzhang:
        "images/hito/kexi/cengdie/zishi1//yan-banzhang-leishui.webp"
    image kexi1_leishui:
        "kexi1_leishui_zhang"
        choice 5:
            5.0
        choice 4:
            3.0
        choice 1:
            1.0
        "kexi1_leishui_banzhang"
        0.1
        "kexi1_leishui_bi"
        0.2
        "kexi1_leishui_banzhang"
        0.1
        repeat
#yan睛流泪
    image kexi_pose_def:
        "images/hito/kexi/cengdie/zishi1/zhuqugan.webp"
    #image zicheng_face_asm:
    #    "images/hito/zicheng/zicheng_kuchi1.webp"
        
    layeredimage kexi_pose:
        always:
            "images/hito/kexi/cengdie/zishi1/zhuqugan.webp"
        group pose:
            attribute pose1 default:
                "kexi_pose_def"
                
        #group face:
        #    #pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
        #    attribute hajimaru default:
        #        "zicheng_face_asm"
                
        group eyes:
            #pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute eyes1 default:
                "kexi1_moren"
            attribute eyes2:
                "kexi1_heihua"
            attribute eyes3:
                "kexi1_heihua2"
            attribute eyes4:
                "kexi1_yihuo"
            attribute eyes5:
                "kexi1_leishui"
                
        group mouth:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute mouth1:
                "kexi1_kaixin"
            attribute mouth2 default:
                "kexi1_nanguo"
            attribute mouth3:
                "kexi1_duqi"#动态显示组件
            #attribute mouse2 default:
                #"zicheng_talk2_rtn"#动态显示组件2
#################################################
init -1 python:
    def kexi2_kaixin_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="kexi":
            return ("kexi2_shuohua_kaixin", .1)#播放口型动画1
        else:
            return ("kexi2_bizui_kaixin", .1)
    def kexi2_nanguo_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="kexi":
            return ("kexi2_shuohua_nanguo", .1)#播放口型动画1
        else:
            return ("kexi2_bizui_nanguo", .1)
    def kexi2_maozui_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="kexi":
            return ("kexi2_shuohua_maozui", .1)#播放口型动画1
        else:
            return ("kexi2_bizui_maozui", .1)
    def kexi2_xiaomao_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="kexi":
            return ("kexi2_shuohua_xiaomao", .1)#播放口型动画1
        else:
            return ("kexi2_bizui_xiaomao", .1)
    #def zicheng_talk2(st, at):
        #if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="zicheng":
            #return ("zicheng_talk_img1", .1)#播放口型动画2
        #else:
            #return ("zicheng_stoptalk", .1)
init -1:
#定义口型动画1
    image kexi2_shuohua_kaixin:
        "images/hito/kexi/cengdie/zishi2/zui-banzhang.webp"
        0.1
        "images/hito/kexi/cengdie/zishi2/zui-zhangkai.webp"
        0.1
        "images/hito/kexi/cengdie/zishi2/zui-banzhang.webp"
        0.1
        "images/hito/kexi/cengdie/zishi2/zui-weixiao.webp"
        0.1
        repeat
    image kexi2_shuohua_nanguo:
        "images/hito/kexi/cengdie/zishi2/zui-banzhang.webp"
        0.1
        "images/hito/kexi/cengdie/zishi2/zui-zhangkai.webp"
        0.1
        "images/hito/kexi/cengdie/zishi2/zui-banzhang.webp"
        0.1
        "images/hito/kexi/cengdie/zishi2/zui-nanguo.webp"
        0.1
        repeat
    image kexi2_shuohua_maozui:
        "images/hito/kexi/cengdie/zishi2/zui-banzhang.webp"
        0.1
        "images/hito/kexi/cengdie/zishi2/zui-zhangkai.webp"
        0.1
        "images/hito/kexi/cengdie/zishi2/zui-banzhang.webp"
        0.1
        "images/hito/kexi/cengdie/zishi2/zui-maozui.webp"
        0.1
        repeat
    image kexi2_shuohua_xiaomao:
        "images/hito/kexi/cengdie/zishi2/zui-banzhang.webp"
        0.1
        "images/hito/kexi/cengdie/zishi2/zui-zhangkai.webp"
        0.1
        "images/hito/kexi/cengdie/zishi2/zui-banzhang.webp"
        0.1
        "images/hito/kexi/cengdie/zishi2/zui-xiaomao.webp"
        0.1
        repeat
    image kexi2_bizui_kaixin:
        "images/hito/kexi/cengdie/zishi2/zui-weixiao.webp"
        0.2
        repeat
    image kexi2_bizui_nanguo:
        "images/hito/kexi/cengdie/zishi2/zui-nanguo.webp"
        0.2
        repeat
    image kexi2_bizui_maozui:
        "images/hito/kexi/cengdie/zishi2/zui-maozui.webp"
        0.2
        repeat
    image kexi2_bizui_xiaomao:
        "images/hito/kexi/cengdie/zishi2/zui-xiaomao.webp"
        0.2
        repeat
    
    image kexi2_kaixin = DynamicDisplayable(kexi2_kaixin_)
    image kexi2_nanguo = DynamicDisplayable(kexi2_nanguo_)
    image kexi2_maozui = DynamicDisplayable(kexi2_maozui_)
    image kexi2_xiaomao = DynamicDisplayable(kexi2_xiaomao_)
    #image zicheng_talk2_rtn = DynamicDisplayable(zicheng_talk2)
#yan睛正常
    image kexi2_moren_bi:
        "images/hito/kexi/cengdie/zishi2/yan-biyan.webp"
    image kexi2_moren_zhang:
        "images/hito/kexi/cengdie/zishi2//yan-zhengkai.webp"
    image kexi2_moren_banzhang:
        "images/hito/kexi/cengdie/zishi2//yan-banzhang.webp"

    image kexi2_moren:
        "kexi2_moren_zhang"
        choice 5:
            5.0
        choice 4:
            3.0
        choice 1:
            1.0
        "kexi2_moren_banzhang"
        0.1
        "kexi2_moren_bi"
        0.2
        "kexi2_moren_banzhang"
        0.1
        repeat
#yan睛正常
    image kexi2_pose_def:
        "images/hito/kexi/cengdie/zishi2/zhuqugan.webp"
    #image zicheng_face_asm:
    #    "images/hito/zicheng/zicheng_kuchi1.webp"
        
    layeredimage kexi_pose2:
        always:
            "images/hito/kexi/cengdie/zishi2/zhuqugan.webp"
        group pose:
            attribute pose1 default:
                "kexi2_pose_def"
                
        #group face:
        #    #pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
        #    attribute hajimaru default:
        #        "zicheng_face_asm"
                
        group eyes:
            #pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute eyes1 default:
                "kexi2_moren"
        group mouth:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute mouth1:
                "kexi2_kaixin"
            attribute mouth2 default:
                "kexi2_nanguo"
            attribute mouth3:
                "kexi2_maozui"
            attribute mouth4:
                "kexi2_xiaomao"
#覃可汐
######################################################################
#叶梓澄
init -1 python:
    def zicheng1_weixiao_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="zicheng":
            return ("zicheng1_shuohua_weixiao", .1)#播放口型动画1
        else:
            return ("zicheng1_bizui_weixiao", .1)
    def zicheng1_nanguo_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="zicheng":
            return ("zicheng1_shuohua_nanguo", .1)#播放口型动画1
        else:
            return ("zicheng1_bizui_nanguo", .1)
    def zicheng1_wukou_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="zicheng":
            return ("zicheng1_shuohua_wukou", .1)#播放口型动画1
        else:
            return ("zicheng1_bizui_wukou", .1)
    def zicheng1_wunai_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="zicheng":
            return ("zicheng1_shuohua_wunai", .1)#播放口型动画1
        else:
            return ("zicheng1_bizui_wunai", .1)
    def zicheng1_xianqi_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="zicheng":
            return ("zicheng1_shuohua_xianqi", .1)#播放口型动画1
        else:
            return ("zicheng1_bizui_xianqi", .1)
    #def zicheng_talk2(st, at):
        #if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="zicheng":
            #return ("zicheng_talk_img1", .1)#播放口型动画2
        #else:
            #return ("zicheng_stoptalk", .1)
init -1:
#定义口型动画1
    image zicheng1_shuohua_weixiao:
        "images/hito/zicheng/cengdie/zishi1/zui-banzhang.webp"
        0.1
        "images/hito/zicheng/cengdie/zishi1/zui-zhangkai.webp"
        0.1
        "images/hito/zicheng/cengdie/zishi1/zui-banzhang.webp"
        0.1
        "images/hito/zicheng/cengdie/zishi1/zui-weixiao.webp"
        0.1
        repeat
    image zicheng1_shuohua_nanguo:
        "images/hito/zicheng/cengdie/zishi1/zui-banzhang.webp"
        0.1
        "images/hito/zicheng/cengdie/zishi1/zui-zhangkai.webp"
        0.1
        "images/hito/zicheng/cengdie/zishi1/zui-banzhang.webp"
        0.1
        "images/hito/zicheng/cengdie/zishi1/zui-nanguo.webp"
        0.1
        repeat
    image zicheng1_shuohua_wukou:
        "images/hito/zicheng/cengdie/zishi1/zui-banzhang.webp"
        0.1
        "images/hito/zicheng/cengdie/zishi1/zui-zhangkai.webp"
        0.1
        "images/hito/zicheng/cengdie/zishi1/zui-banzhang.webp"
        0.1
        "images/hito/zicheng/cengdie/zishi1/zui-wukou.webp"
        0.1
        repeat
    image zicheng1_shuohua_wunai:
        "images/hito/zicheng/cengdie/zishi1/zui-banzhang.webp"
        0.1
        "images/hito/zicheng/cengdie/zishi1/zui-zhangkai.webp"
        0.1
        "images/hito/zicheng/cengdie/zishi1/zui-banzhang.webp"
        0.1
        "images/hito/zicheng/cengdie/zishi1/zui-wunai.webp"
        0.1
        repeat
    image zicheng1_shuohua_xianqi:
        "images/hito/zicheng/cengdie/zishi1/zui-banzhang.webp"
        0.1
        "images/hito/zicheng/cengdie/zishi1/zui-zhangkai.webp"
        0.1
        "images/hito/zicheng/cengdie/zishi1/zui-banzhang.webp"
        0.1
        "images/hito/zicheng/cengdie/zishi1/zui-nanguo.webp"
        0.1
        repeat
    image zicheng1_bizui_weixiao:
        "images/hito/zicheng/cengdie/zishi1/zui-weixiao.webp"
        0.2
        repeat
    image zicheng1_bizui_nanguo:
        "images/hito/zicheng/cengdie/zishi1/zui-nanguo.webp"
        0.2
        repeat
    image zicheng1_bizui_wukou:
        "images/hito/zicheng/cengdie/zishi1/zui-wukou.webp"
        0.2
        repeat
    image zicheng1_bizui_wunai:
        "images/hito/zicheng/cengdie/zishi1/zui-wunai.webp"
        0.2
        repeat
    image zicheng1_bizui_xianqi:
        "images/hito/zicheng/cengdie/zishi1/zui-xianqi.webp"
        0.2
        repeat
    
    image zicheng1_weixiao = DynamicDisplayable(zicheng1_weixiao_)
    image zicheng1_nanguo = DynamicDisplayable(zicheng1_nanguo_)
    image zicheng1_wukou = DynamicDisplayable(zicheng1_wukou_)
    image zicheng1_wunai = DynamicDisplayable(zicheng1_wunai_)
    image zicheng1_xianqi = DynamicDisplayable(zicheng1_xianqi_)
#yan睛流泪
    image zicheng1_yan_liulei_bi:
        "images/hito/zicheng/cengdie/zishi1/yan-liulei-bi.webp"
    image zicheng1_yan_liulei_zhengkai:
        "images/hito/zicheng/cengdie/zishi1/yan-liulei-zhengkai.webp"
    image zicheng1_yan_liulei_banzhang:
        "images/hito/zicheng/cengdie/zishi1/yan-liulei-banzhang.webp"
    image zicheng1_liulei:
        "zicheng1_yan_liulei_zhengkai"
        choice 5:
            5.0
        choice 4:
            3.0
        choice 1:
            1.0
        "zicheng1_yan_liulei_banzhang"
        0.1
        "zicheng1_yan_liulei_bi"
        0.2
        "zicheng1_yan_liulei_banzhang"
        0.1
        repeat
#yan睛流泪
#yan睛正常
    image zicheng1_yan_zhengchang_bi:
        "images/hito/zicheng/cengdie/zishi1/yan-zhengchang-bi.webp"
    image zicheng1_yan_zhengchang_zhengkai:
        "images/hito/zicheng/cengdie/zishi1/yan-zhengchang-zhengkai.webp"
    image zicheng1_yan_zhengchang_banzhang:
        "images/hito/zicheng/cengdie/zishi1/yan-zhengchang-banzhang.webp"
    image zicheng1_zhengchang:
        "zicheng1_yan_zhengchang_zhengkai"
        choice 5:
            5.0
        choice 4:
            3.0
        choice 1:
            1.0
        "zicheng1_yan_zhengchang_banzhang"
        0.1
        "zicheng1_yan_zhengchang_bi"
        0.2
        "zicheng1_yan_zhengchang_banzhang"
        0.1
        repeat
#yan睛正常
#yan睛阴暗
    image zicheng1_yan_yingan_bi:
        "images/hito/zicheng/cengdie/zishi1/yan-yingan-bi.webp"
    image zicheng1_yan_yingan_zhengkai:
        "images/hito/zicheng/cengdie/zishi1/yan-yingan-zhengkai.webp"
    image zicheng1_yan_yingan_banzhang:
        "images/hito/zicheng/cengdie/zishi1/yan-yingan-banzhang.webp"
    image zicheng1_yingan:
        "zicheng1_yan_yingan_zhengkai"
        choice 5:
            5.0
        choice 4:
            3.0
        choice 1:
            1.0
        "zicheng1_yan_yingan_banzhang"
        0.1
        "zicheng1_yan_yingan_bi"
        0.2
        "zicheng1_yan_yingan_banzhang"
        0.1
        repeat
#yan睛阴暗
#yan睛黑化
    image zicheng1_yan_heihua_yingan_zhengkai:
        "images/hito/zicheng/cengdie/zishi1/yan-heihua-yingan-zhengkai.webp"
    image zicheng1_heihua_yingan:
        "zicheng1_yan_heihua_yingan_zhengkai"
        choice 5:
            5.0
        choice 4:
            3.0
        choice 1:
            1.0
        "zicheng1_yan_yingan_banzhang"
        0.1
        "zicheng1_yan_yingan_bi"
        0.2
        "zicheng1_yan_yingan_banzhang"
        0.1
        repeat
#yan睛黑化
#yan睛高光
    image zicheng1_yan_gaoguang_zhengkai:
        "images/hito/zicheng/cengdie/zishi1/yan-gaoguang-zhengkai.webp"
    image zicheng1_gaoguang:
        "zicheng1_yan_gaoguang_zhengkai"
        choice 5:
            5.0
        choice 4:
            3.0
        choice 1:
            1.0
        "zicheng1_yan_zhengchang_banzhang"
        0.1
        "zicheng1_yan_zhengchang_bi"
        0.2
        "zicheng1_yan_zhengchang_banzhang"
        0.1
        repeat
#yan睛高光
    image zicheng1_heihua:
        "images/hito/zicheng/cengdie/zishi1/yan-heihua-zhengkai.webp"
#yan睛皱眉
    image zicheng1_zhoumei:
        "zicheng1_yan_zhengchang_banzhang"
        choice 5:
            5.0
        choice 4:
            3.0
        choice 1:
            1.0
        "zicheng1_yan_zhengchang_bi"
        0.2
        repeat
#yan睛皱眉
    image zicheng1_pose_def:
        "images/hito/zicheng/cengdie/zishi1/zhuqugan.webp"
    image zicheng1_han:
        "images/hito/zicheng/cengdie/zishi1/lingjian-hanshui.webp"
    image zicheng1_lianhong:
        "images/hito/zicheng/cengdie/zishi1/lingjian-lianhong.webp"
    #image zicheng_face_asm:
    #    "images/hito/zicheng/zicheng_kuchi1.webp"
        
    layeredimage zicheng_pose1:
        always:
            "images/hito/zicheng/cengdie/zishi1/zhuqugan.webp"
        group pose:
            attribute pose1 default:
                "zicheng1_pose_def"
                
        #group face:
        #    #pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
        #    attribute hajimaru default:
        #        "zicheng_face_asm"
                
        group eyes:
            #pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute eyes1 default:
                "zicheng1_zhengchang"
            attribute eyes2:
                "zicheng1_liulei"
            attribute eyes3:
                "zicheng1_yingan"
            attribute eyes4:
                "zicheng1_gaoguang"
            attribute eyes5:
                "zicheng1_heihua"
            attribute eyes6:
                "zicheng1_heihua_yingan"
            attribute eyes7:
                "zicheng1_zhoumei"
        group other1:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute other1:
                "zicheng1_han"
        group other2:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute other2:
                "zicheng1_lianhong"
        group mouth:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute mouth1:
                "zicheng1_weixiao"
            attribute mouth2 default:
                "zicheng1_nanguo"
            attribute mouth3:
                "zicheng1_wukou"
            attribute mouth4:
                "zicheng1_wunai"
            attribute mouth5:
                "zicheng1_xianqi"
#叶梓澄
init -1 python:
    def zicheng2_nanguo_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="zicheng":
            return ("zicheng2_shuohua_nanguo", .1)#播放口型动画1
        else:
            return ("zicheng2_bizui_nanguo", .1)
    def zicheng2_wukou_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="zicheng":
            return ("zicheng2_shuohua_wukou", .1)#播放口型动画1
        else:
            return ("zicheng2_bizui_wukou", .1)
    def zicheng2_xianqi_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="zicheng":
            return ("zicheng2_shuohua_xianqi", .1)#播放口型动画1
        else:
            return ("zicheng2_bizui_xianqi", .1)
init -1:
#定义口型动画1
    image zicheng2_shuohua_nanguo:
        "images/hito/zicheng/cengdie/zishi2/zui-banzhang.webp"
        0.1
        "images/hito/zicheng/cengdie/zishi2/zui-zhangkai.webp"
        0.1
        "images/hito/zicheng/cengdie/zishi2/zui-banzhang.webp"
        0.1
        "images/hito/zicheng/cengdie/zishi2/zui-nanguo.webp"
        0.1
        repeat
    image zicheng2_shuohua_wukou:
        "images/hito/zicheng/cengdie/zishi2/zui-banzhang.webp"
        0.1
        "images/hito/zicheng/cengdie/zishi2/zui-zhangkai.webp"
        0.1
        "images/hito/zicheng/cengdie/zishi2/zui-banzhang.webp"
        0.1
        "images/hito/zicheng/cengdie/zishi2/zui-wukou.webp"
        0.1
        repeat
    image zicheng2_shuohua_xianqi:
        "images/hito/zicheng/cengdie/zishi2/zui-banzhang.webp"
        0.1
        "images/hito/zicheng/cengdie/zishi2/zui-zhangkai.webp"
        0.1
        "images/hito/zicheng/cengdie/zishi2/zui-banzhang.webp"
        0.1
        "images/hito/zicheng/cengdie/zishi2/zui-nanguo.webp"
        0.1
        repeat
    image zicheng2_bizui_nanguo:
        "images/hito/zicheng/cengdie/zishi2/zui-nanguo.webp"
        0.2
        repeat
    image zicheng2_bizui_wukou:
        "images/hito/zicheng/cengdie/zishi2/zui-wukou.webp"
        0.2
        repeat
    image zicheng2_bizui_xianqi:
        "images/hito/zicheng/cengdie/zishi2/zui-xianqi.webp"
        0.2
        repeat
    
    image zicheng2_nanguo = DynamicDisplayable(zicheng2_nanguo_)
    image zicheng2_wukou = DynamicDisplayable(zicheng2_wukou_)
    image zicheng2_xianqi = DynamicDisplayable(zicheng2_xianqi_)
#yan睛正常
    image zicheng2_yan_zhengchang_bi:
        "images/hito/zicheng/cengdie/zishi2/yan-biyan.webp"
    image zicheng2_yan_zhengchang_zhengkai:
        "images/hito/zicheng/cengdie/zishi2/yan-zhengkai.webp"
    image zicheng2_yan_zhengchang_banzhang:
        "images/hito/zicheng/cengdie/zishi2/yan-banzhang.webp"
    image zicheng2_zhengchang:
        "zicheng2_yan_zhengchang_zhengkai"
        choice 5:
            5.0
        choice 4:
            3.0
        choice 1:
            1.0
        "zicheng2_yan_zhengchang_banzhang"
        0.1
        "zicheng2_yan_zhengchang_bi"
        0.2
        "zicheng2_yan_zhengchang_banzhang"
        0.1
        repeat
#yan睛正常
#yan睛黑化
    image zicheng2_yan_wushen:
        "images/hito/zicheng/cengdie/zishi2/yan-zhengkai-wushen.webp"
    image zicheng2_han:
        "images/hito/zicheng/cengdie/zishi2/lingjian-liuhan.webp"
    image zicheng2_heihua:
        "images/hito/zicheng/cengdie/zishi2/lingjian-heihua.webp"
    image zicheng2_wushen:
        "zicheng2_yan_wushen"
        choice 5:
            5.0
        choice 4:
            3.0
        choice 1:
            1.0
        "zicheng2_yan_zhengchang_banzhang"
        0.1
        "zicheng2_yan_zhengchang_bi"
        0.2
        "zicheng2_yan_zhengchang_banzhang"
        0.1
        repeat
#yan睛黑化
    layeredimage zicheng_pose2:
        always:
            "images/hito/zicheng/cengdie/zishi2/zhuqugan.webp"
        group pose:
            attribute pose1 default:
                "zicheng2_pose_def"
                
        #group face:
        #    #pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
        #    attribute hajimaru default:
        #        "zicheng_face_asm"
                
        group eyes:
            #pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute eyes1 default:
                "zicheng2_zhengchang"
            attribute eyes2:
                "zicheng2_wushen"
        group other1:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute other1:
                "zicheng2_han"
        group other2:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute other2:
                "zicheng2_heihua"
        group mouth:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute mouth1:
                "zicheng2_nanguo"
            attribute mouth2 default:
                "zicheng2_wukou"
            attribute mouth3:
                "zicheng2_xianqi"
#林洛
init -1 python:
    def linluo_wukou_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="linluo":
            return ("linluo_shuohua_wukou", .1)#播放口型动画1
        else:
            return ("linluo_bizui_wukou", .1)
    def linluo_liezui_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="linluo":
            return ("linluo_shuohua_liezui", .1)#播放口型动画1
        else:
            return ("linluo_bizui_liezui", .1)
init -1:
#定义口型动画1
    image linluo_shuohua_wukou:
        "images/hito/linluo/cengdie/zui_banzhang.webp"
        0.1
        "images/hito/linluo/cengdie/zui_zhangkai.webp"
        0.1
        "images/hito/linluo/cengdie/zui_banzhang.webp"
        0.1
        "images/hito/linluo/cengdie/zui_bi.webp"
        0.1
        repeat
    image linluo_shuohua_liezui:
        "images/hito/linluo/cengdie/zui_banzhang.webp"
        0.1
        "images/hito/linluo/cengdie/zui_zhangkai.webp"
        0.1
        "images/hito/linluo/cengdie/zui_banzhang.webp"
        0.1
        "images/hito/linluo/cengdie/zui_bi.webp"
        0.1
        repeat
    image linluo_bizui_wukou:
        "images/hito/linluo/cengdie/zui_bi.webp"
        0.2
        repeat
    image linluo_bizui_liezui:
        "images/hito/linluo/cengdie/zui_liezui.webp"
        0.2
        repeat
    image linluo_wukou = DynamicDisplayable(linluo_wukou_)
    image linluo_liezui = DynamicDisplayable(linluo_liezui_)
#yan睛正常
    image linluo_bi:
        "images/hito/linluo/cengdie/yan_bi.webp"
    image linluo_zhang:
        "images/hito/linluo/cengdie/yan_zhengkai.webp"
    image linluo_banzhang:
        "images/hito/linluo/cengdie/yan_banzhang.webp"

    image linluo_moren:
        "linluo_zhang"
        choice 5:
            5.0
        choice 4:
            3.0
        choice 1:
            1.0
        "linluo_banzhang"
        0.1
        "linluo_bi"
        0.2
        "linluo_banzhang"
        0.1
        repeat
#yan睛正常
#yan睛正常
    image linluo_dengyan:
        "images/hito/linluo/cengdie/yan_dengyan.webp"
    image linluo_dayan:
        "linluo_dengyan"
        choice 5:
            5.0
        choice 4:
            3.0
        choice 1:
            1.0
        "linluo_banzhang"
        0.1
        "linluo_bi"
        0.2
        "linluo_banzhang"
        0.1
        repeat
#yan睛正常
    image linluo_yinan:
        "images/hito/linluo/cengdie/lingjian_yinan.webp"
    image linluo_liuhan:
        "images/hito/linluo/cengdie/lingjian_liuhan.webp"
    image linluo_pose_def:
        "images/hito/linluo/cengdie/zhuqugan.webp"
    image linluo_pose2_def:
        "images/hito/linluo/cengdie/zhuqugan2.webp"
    layeredimage linluo_pose:

        group pose:
            attribute pose1 default:
                "linluo_pose_def"
            attribute pose2:
                "linluo_pose2_def"
        #group face:
        #    #pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
        #    attribute hajimaru default:
        #        "zicheng_face_asm"
                
        group eyes:
            #pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute eyes1 default:
                "linluo_moren"
            attribute eyes2:
                "linluo_dayan"
        group other1:
            attribute other1:
                "linluo_yinan"
        group other2:
            attribute other2:
                "linluo_liuhan"
        group mouth:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute mouth1:
                "linluo_liezui"
            attribute mouth2 default:
                "linluo_wukou"
#林洛老
init -1 python:
    def linluo_old_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="linluo_old":
            return ("linluo_old_shuohua", .1)#播放口型动画1
        else:
            return ("linluo_old_bizui", .1)
init -1:
#定义口型动画1
    image linluo_old_shuohua:
        "images/hito/linluo_old/cengdie/zui_banzhang.webp"
        0.1
        "images/hito/linluo_old/cengdie/zui_zhangkai.webp"
        0.1
        "images/hito/linluo_old/cengdie/zui_banzhang.webp"
        0.1
        "images/hito/linluo_old/cengdie/zui_bi.webp"
        0.1
        repeat
    image linluo_old_bizui:
        "images/hito/linluo_old/cengdie/zui_bi.webp"
        0.2
        repeat
    image linluo_old = DynamicDisplayable(linluo_old_)
#yan睛正常
    image linluo_old_bi:
        "images/hito/linluo_old/cengdie/yan_bi.webp"
    image linluo_old_zhang:
        "images/hito/linluo_old/cengdie/yan_zhangkai.webp"
    image linluo_old_banzhang:
        "images/hito/linluo_old/cengdie/yan_banzhang.webp"

    image linluo_old_yan:
        "linluo_old_zhang"
        choice 5:
            5.0
        choice 4:
            3.0
        choice 1:
            1.0
        "linluo_old_banzhang"
        0.1
        "linluo_old_bi"
        0.2
        "linluo_old_banzhang"
        0.1
        repeat
#yan睛正常
    image linluo_old_hat:
        "images/hito/linluo_old/cengdie/lingjian_hat.webp"
    image linluo_old_pose_def:
        "images/hito/linluo_old/cengdie/zhuqugan.webp"
    layeredimage linluo_old_pose:

        group pose:
            attribute pose1 default:
                "linluo_old_pose_def"
        #group face:
        #    #pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
        #    attribute hajimaru default:
        #        "zicheng_face_asm"
                
        group eyes:
            #pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute eyes1 default:
                "linluo_old_yan"
        group other1:
            attribute other1:
                "linluo_old_hat"
        group mouth:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute mouth1 default:
                "linluo_old"
#女老师
init -1 python:
    def sensei1_zui_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="sensei":
            return ("sensei1_zui_shuohua", .1)#播放口型动画1
        else:
            return ("sensei1_zui_bizui", .1)
init -1:
#定义口型动画1
    image sensei1_zui_shuohua:
        "images/hito/sensei1/cengdie/zui_banzhang.webp"
        0.1
        "images/hito/sensei1/cengdie/zui_zhangkai.webp"
        0.1
        "images/hito/sensei1/cengdie/zui_banzhang.webp"
        0.1
        "images/hito/sensei1/cengdie/zui_bi.webp"
        0.1
        repeat
    image sensei1_zui_bizui:
        "images/hito/sensei1/cengdie/zui_bi.webp"
        0.2
        repeat
    image sensei1_zui = DynamicDisplayable(sensei1_zui_)
#yan睛正常
    image sensei1_yan_bi:
        "images/hito/sensei1/cengdie/yan_bi.webp"
    image sensei1_yan_zhang:
        "images/hito/sensei1/cengdie/yan_zhangkai.webp"
    image sensei1_yan_banzhang:
        "images/hito/sensei1/cengdie/yan_banzhang.webp"

    image sensei1_yan:
        "sensei1_yan_zhang"
        choice 5:
            5.0
        choice 4:
            3.0
        choice 1:
            1.0
        "sensei1_yan_banzhang"
        0.1
        "sensei1_yan_bi"
        0.2
        "sensei1_yan_banzhang"
        0.1
        repeat
    image sensei1_yan2:
        "sensei1_yan_banzhang"
        choice 5:
            5.0
        choice 4:
            3.0
        choice 1:
            1.0
        "sensei1_yan_banzhang"
        0.1
        "sensei1_yan_bi"
        0.2
        "sensei1_yan_banzhang"
        0.1
        repeat
#yan睛正常
    image sensei1_pose_def:
        "images/hito/sensei1/cengdie/zhuqugan.webp"
    layeredimage sensei1_pose:

        group pose:
            attribute pose1 default:
                "sensei1_pose_def"
        #group face:
        #    #pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
        #    attribute hajimaru default:
        #        "zicheng_face_asm"
                
        group eyes:
            #pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute eyes1 default:
                "sensei1_yan"
            attribute eyes2 :
                "sensei1_yan2"
        group mouth:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute mouth1 default:
                "sensei1_zui"
#可汐妈
init -1 python:
    def kexihaha_zui_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="kexihaha":
            return ("kexihaha_zui_shuohua", .1)#播放口型动画1
        else:
            return ("kexihaha_zui_bi", .1)
init -1:
#定义口型动画1
    image kexihaha_zui_shuohua:
        "images/hito/kexi_haha/cengdie/zui_banzhang.webp"
        0.1
        "images/hito/kexi_haha/cengdie/zui_zhangkai.webp"
        0.1
        "images/hito/kexi_haha/cengdie/zui_banzhang.webp"
        0.1
        "images/hito/kexi_haha/cengdie/zui_bi.webp"
        0.1
        repeat
    image kexihaha_zui_bi:
        "images/hito/kexi_haha/cengdie/zui_bi.webp"
        0.2
        repeat
    image kexihaha_zui = DynamicDisplayable(kexihaha_zui_)
#yan睛正常
    image kexihaha_yan_bi:
        "images/hito/kexi_haha/cengdie/yan_bi.webp"
    image kexihaha_yan_zhang:
        "images/hito/kexi_haha/cengdie/yan_zhangkai.webp"
    image kexihaha_yan_banzhang:
        "images/hito/kexi_haha/cengdie/yan_banzhang.webp"

    image kexihaha_yan:
        "kexihaha_yan_zhang"
        choice 5:
            5.0
        choice 4:
            3.0
        choice 1:
            1.0
        "kexihaha_yan_banzhang"
        0.1
        "kexihaha_yan_bi"
        0.2
        "kexihaha_yan_banzhang"
        0.1
        repeat
    image kexihaha_yan_liulei_zhang:
        "images/hito/kexi_haha/cengdie/yan_zhangkai_leishui.webp"
    image kexihaha_yan_liulei_banzhang:
        "images/hito/kexi_haha/cengdie/yan_banzhang_leishui.webp"
    image kexihaha_yan2:
        "kexihaha_yan_liulei_zhang"
        choice 5:
            5.0
        choice 4:
            3.0
        choice 1:
            1.0
        "kexihaha_yan_liulei_banzhang"
        0.1
        "kexihaha_yan_bi"
        0.2
        "kexihaha_yan_liulei_banzhang"
        0.1
        repeat
#yan睛正常
    image kexihaha_pose_def:
        "images/hito/kexi_haha/cengdie/zhuqugan.webp"
    layeredimage kexihaha_pose:

        group pose:
            attribute pose1 default:
                "kexihaha_pose_def"
        #group face:
        #    #pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
        #    attribute hajimaru default:
        #        "zicheng_face_asm"
                
        group eyes:
            #pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute eyes1 default:
                "kexihaha_yan"
            attribute eyes2 :
                "kexihaha_yan2"
        group mouth:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute mouth1 default:
                "kexihaha_zui"