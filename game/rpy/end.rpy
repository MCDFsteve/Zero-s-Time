
transform end_nise:
  xcenter 0.5
  ypos 0.0
  linear 90.0 ypos -4286
  linear 5 ypos 300

transform end:
  xcenter 0.5
  ypos 0.0
  linear 189.0 ypos -9000

  

image black = "#000"
transform wenzi:
  alpha 1.0
  xpos 0.4 ypos 0.5
  yoffset 0
  #linear 5.0 yoffset -160 alpha 0.0
    
image title3_anime:
    contains:
        time 96.0
        "title/title3.webp"
        xcenter 0.5
        ypos 300
        alpha 0.0
        linear 1.0 alpha 1.0
image dialogue2_imag:
  contains:
      time 70.0
      Text("？？？：{cps=15}你是林洛对吧！！{/cps}",size=80,slow=150) 
      wenzi
      
      time 75.0
      Text("林洛：{cps=15}你是？{/cps}", size=80,slow=150) 
      wenzi
      
      time 80.0
      Text("{size=80}？？？：{/size}{cps=10}{size=90}叶梓澄！\n{/size}{size=80}来自十年后的，{/size}{size=90}叶梓澄！{/size}{/cps}",slow=150) 
      wenzi

      time 85.0
      Text("林洛：{cps=15}！！！！！！\n！！！！{/cps}", size=90,slow=150) 
      wenzi

      time 90.0
      Null()

screen game_end():
  add "black"
  zorder 102
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
    elif end == 3:
      add "title/title3.webp":
        at end
      add "chapters/end3.webp":
        at end
    elif end == 4:
      add "title/title3.webp":
        at end
      add "chapters/end4.webp":
        at end
    elif end == 0:
      if nise_end:
        add "title/title2.webp":
          at end_nise
        add "chapters/nise_end.webp":
          at end_nise
      else:
        add "title/title2.webp":
          at end
        add "chapters/nise_end.webp":
          at end
    vbox:
      xpos 0.0
      spacing 50
      
      if nise_end:
        add "end_img1" at end_nise
        add "end_img2" at end_nise
        add "end_img3" at end_nise
      else:
        add "end_img1" at end
        add "end_img2" at end
        add "end_img3" at end
        
  if nise_end:
    add "dialogue2_imag" 
  if nise_end:
    add "title3_anime"

image end_img1:
  Text (_("{size=90}总企划——{/size}\n\n{a=https://space.bilibili.com/381681555/}{size=70}戴夫邻居史蒂夫DFsteve{/size}{/a} \n\n\n\n"))

image end_img2:
  Text (_("""{size=90}剧本——{/size}\n\n{a=https://space.bilibili.com/381681555/}{size=70}戴夫邻居史蒂夫DFsteve{/size}{/a} \n\n\n\n

          {size=90}程序设计——{/size}\n\n{a=https://space.bilibili.com/381681555/}{size=70}戴夫邻居史蒂夫DFsteve{/size}{/a} \n\n\n\n

          {size=90}程序帮助——{/size}\n\n{a=https://space.bilibili.com/438665392/}{size=70}sui_yiii{/size}{/a} \n\n\n\n

          {size=90}美术设计——{/size}\n\n{a=https://space.bilibili.com/32947315/}{size=70}猫嗝嗝嗝嗝颖{/size}{/a} \n\n\n\n

          {size=90}立绘——{/size}\n\n{a=https://space.bilibili.com/32947315/}{size=70}猫嗝嗝嗝嗝颖{/size}{/a} \n\n\n\n

          {size=90}角色设计——{/size}\n\n{a=https://space.bilibili.com/381681555/}{size=70}戴夫邻居史蒂夫DFsteve{/size}{/a} \n\n{a=https://space.bilibili.com/32947315/}{size=70}猫嗝嗝嗝嗝颖{/size}{/a} \n\n\n\n

          {size=90}背景拍摄——{/size}\n\n{a=https://space.bilibili.com/381681555/}{size=70}戴夫邻居史蒂夫DFsteve{/size}{/a} \n\n\n\n

          {size=90}背景绘制——{/size}\n\n{a=https://space.bilibili.com/32947315/}{size=70}猫嗝嗝嗝嗝颖{/size}{/a} \n\n\n\n

          {size=90}音乐——{/size}\n\n{size=70}陈次犬{/size}\n\n\n\n

          {size=90}游戏测试——{/size}\n\n{a=https://space.bilibili.com/381681555/}{size=70}戴夫邻居史蒂夫DFsteve{/size}{/a}\n\n{a=https://space.bilibili.com/32947315/}{size=70}猫嗝嗝嗝嗝颖{/size}{/a} \n\n{size=70}陈次犬{/size}\n\n{size=70}箫蓝{/size}\n\n\n\n

          {size=90}Tips支持——{/size}\n\n{a=https://chat.openai.com/}{size=70}ChatGPT{/size}{/a} \n\n\n\n

          {size=90}设定援助——{/size}\n\n{a=https://chat.openai.com/}{size=70}ChatGPT{/size}{/a} \n\n\n\n

          {size=90}游戏版本——{/size}\n\n{size=70}[config.version]{/size}\n\n\n\n

          {size=90}游戏引擎——{/size}\n\n{color=#000000}{a=https://www.renpy.org/}{size=70}Ren'Py{/size}{/a}{/color}\n\n\n\n\n\n\n\n\n\n """.replace(" ", "")), color="#ffffff")

image end_img3:
  Text (_("感谢游玩！！！"),size=120, color="#ffffff")