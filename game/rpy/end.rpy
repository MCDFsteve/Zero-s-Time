transform end:
         xcenter 0.5
         ypos 0.0
         linear 189.0 ypos -6000
image black = "#000"
screen game_end():
       add "black"
       #zorder 102
       vbox:
        ypos 0.0
        spacing 5
        if end == 1:
          add "title/title1.webp":
            at end
          add "chapters/end1.webp":
            at end
        elif end == 2:
          add "title/title2.webp":
            at end
          add "chapters/end2.webp":
            at end
        elif end == 0:
          add "title/title2.webp":
            at end
          add "chapters/nise_end.webp":
            at end
        vbox:
          xcenter 0.5
          spacing 50
          text _("总企划：\n{u}{a=https://space.bilibili.com/381681555/}戴夫邻居史蒂夫DFsteve{/a}{/u}") size 70 :
            at end
          text _("剧本：\n{u}{a=https://space.bilibili.com/381681555/}戴夫邻居史蒂夫DFsteve{/a}{/u}") size 70 color "#ffffff":
            at end
          text _("剧本协力：\n箫蓝") size 70 color "#ffffff":
            at end
          text _("程序设计：\n{u}{a=https://space.bilibili.com/381681555/}戴夫邻居史蒂夫DFsteve{/a}{/u}") size 70 color "#ffffff":
            at end
          text _("道具设计：\n{u}{a=https://space.bilibili.com/381681555/}戴夫邻居史蒂夫DFsteve{/a}{/u}") size 70 color "#ffffff":
            at end
          text _("程序帮助：\n随意.") size 70 color "#ffffff":
            at end
          text _("美术设计：\n{u}{a=https://space.bilibili.com/32947315/}猫嗝嗝嗝嗝颖{/a}{/u}") size 70 color "#ffffff":
            at end
          text _("立绘：\n{u}{a=https://space.bilibili.com/32947315/}猫嗝嗝嗝嗝颖{/a}{/u}") size 70 color "#ffffff":
            at end
          text _("角色设计：\n{u}{a=https://space.bilibili.com/381681555/}戴夫邻居史蒂夫DFsteve{/a}{/u}\n{u}{a=https://space.bilibili.com/32947315/}猫嗝嗝嗝嗝颖{/a}{/u}") size 70 color "#ffffff":
            at end
          text _("音乐：\n陈次犬") size 70 color "#ffffff":
            at end
          text _("游戏测试：\n{u}{a=https://space.bilibili.com/381681555/}戴夫邻居史蒂夫DFsteve{/a}\n{a=https://space.bilibili.com/32947315/}猫嗝嗝嗝嗝颖{/a}{/u}\n陈次犬\n箫蓝") size 70 color "#ffffff":
            at end
          text _("制作人：\n{u}{a=https://space.bilibili.com/381681555/}戴夫邻居史蒂夫DFsteve{/a}{/u}") size 70 :
            at end
          text _("游戏版本：\n[config.version]") size 70 color "#ffffff":
            at end
          text _("游戏引擎：\n{u}{color=#000000}{a=https://www.renpy.org/}Ren'Py{/a}{/color}{/u}") size 70 color "#ffffff":
            at end
          text "             " size 100 color "#ffffff":
            at end
          text "             " size 100 color "#ffffff":
            at end
          text "             " size 100 color "#ffffff":
            at end
          text "             " size 100 color "#ffffff":
            at end
          text _("感谢游玩！！！") size 100 color "#ffffff":
            at end