
# image t = DynamicDisplayable(timeBacker.t_back)
# image d = DynamicDisplayable(timeBacker.d_back)
# image w = DynamicDisplayable(timeBacker.w_back)


init 1 python:
    c_TimeBacker( "loop", [   9, 20,  12,  52,  2,
                                    9, 19, 12, 40, 1, ])
    c_TimeBacker( "loop2", [   9, 19,  12,  42,  1,
                                    9, 9, 12, 42, 2, ])
    c_TimeBacker( "loop3", [   9, 19,  12,  32,  1,
                                    9, 9, 12, 32, 2, ])

init python:
    import math

    def c_TimeBacker(name: str, list):
        ## 构造器
        str_name = name
        name = TimeBacker(*list)
        renpy.image('{}_t'.format(str_name), DynamicDisplayable(name.t_back))
        renpy.image('{}_d'.format(str_name), DynamicDisplayable(name.d_back))
        renpy.image('{}_w'.format(str_name), DynamicDisplayable(name.w_back))
     
    class TimeBacker:
        ## 定义一个包含天日时分周的待迭函数类(24h制)，至少大于1小时，周为对应1~7数字，月为对应1~12数字，不支持跨年(跨年不如从天数开始倒计时)
        
        month = {   '1': 31,  '2': 28,  '3': 31,  '4': 30, 
                    '5': 31,  '6': 30,  '7': 31,   '8': 31, 
                    '9': 30, '10': 31, '11': 30, '12': 31, }

        week = {    '1': '周一', 
                    '2': '周二', 
                    '3': '周三', 
                    '4': '周四', 
                    '5': '周五', 
                    '6': '周六', 
                    '7': '周日', }

        def __init__(self, nowm, nowd, nowt_h, nowt_m, noww, oldm, oldd, oldt_h, oldt_m, oldw, speed=1):
            ## 月份，日期，时， 分，周
            self.nm = nowm
            self.nd = nowd
            self.nth = nowt_h
            self.ntm = nowt_m
            self.nw = noww

            self.om = oldm
            self.od = oldd
            self.oth = oldt_h
            self.otm = oldt_m
            self.ow = oldw

            self.speed = speed

            # ## 补足偏差
            self.ntm = nowt_m + 3

            ## 分钟间隔
            if self.om == self.nm:
                self.dmin = (self.nd - self.od)*1440 + (self.nth - self.oth)*60 + (self.ntm - self.otm)
            else:
                self.dmin = (TimeBacker.month[str(self.om)]-self.od+self.nd)*1440 + (self.nth - self.oth)*60 + (self.ntm - self.otm)
            
            for i in range(self.om+1, self.nm):
                for k, v in TimeBacker.month.items():
                    if k == str(i):
                        self.dmin += v*1440

            self.dt = -2
            self.x = 1

        def sp(self):
            ## 划分五个对称阶段速度，按分钟数，慢，快，高速，快，慢
            
            # if self.x != 0:
            if self.dt < 4:
                # self.x = 1
                self.speed = 1

            elif self.dt < (self.dmin - 8)/6 + 6:
                self.x = 4
                self.speed = 1/(14400 - 8)*6*4

            elif self.dt < (self.dmin - 8)/6*5 + 6:
                if self.dt + 12 > self.dmin -16:
                    self.x = self.dmin - self.dt - 16
                    self.speed = 1.5/(14400 - 8)*6*4
                else:
                    self.x = 12
                    self.speed = 2.5/(14400 - 8)*3/2*12

            elif self.dt < self.dmin - 4:
                if self.dt + 4 > self.dmin - 4:
                    self.x = self.dmin - self.dt -4
                    self.speed = 0.5
                else:
                    self.x = 4
                    self.speed = 1.5/(14400 - 8)*6*4

            elif self.dt < self.dmin:
                self.x = 1
                self.speed = 0.5
            

            self.dt += self.x
            
            # if self.dt == 0:
            #     self.x = 1

        def t_back(self, st, at):             
            ## 初始化
            self.sp()

            ## 分倒退
            self.ntm -= self.x

            ## 分时周日临界
            if self.ntm < 0:
                self.ntm = (self.ntm - 1)%60 + 1
                self.nth = (self.nth - 1)%24

                if self.nth == 23:
                    self.nd -= 1
                    self.nw = (self.nw + 5)%7 + 1

                    if self.nd == 0:
                        self.nm = (self.nm - 2)%12 + 1
                        self.nd = TimeBacker.month[str(self.nm)]

            if self.nd == self.od and self.dt >= self.dmin and self.om == self.nm:
                ## 日期相等，分钟间隔为0时，
                d = Text("{:0>2.0f}:{:0>2.0f}".format(self.oth, self.otm),bold=True, size=340,font="Cubic-11-1.000-R-2.ttf",color="#ffffff")
                return d, None

            else:
                if self.dt > self.dmin - 2:
                    self.nth = self.oth
                    self.ntm = self.otm
                d = Text("{:0>2.0f}:{:0>2.0f}".format(self.nth, self.ntm),bold=True, size=340,font="Cubic-11-1.000-R-2.ttf",color="#ffffff")
                return d, self.speed

        def d_back(self, st, at):
            ## 日期倒退
            if self.nd == self.od and self.dt >= self.dmin and self.om == self.nm:
                d = Text("2022.{:0>2.0f}.{:0>2.0f}".format(self.om, self.od), size=160,font="Cubic-11-1.000-R-2.ttf", color="#ffffff")
                return d, None
            else:
                d = Text("2022.{:0>2.0f}.{:0>2.0f}".format(self.nm, self.nd), size=160,font="Cubic-11-1.000-R-2.ttf", color="#ffffff")
                return d, self.speed

        def w_back(self, st, at):
            ## 周倒退
            if self.nw == self.ow and self.dt >= self.dmin and self.om == self.nm:
                d = Text(_("{}".format(TimeBacker.week[str(self.ow)])),size=240, font="Cubic-11-1.000-R-2.ttf",color="#ffffff")
                return d, None
            else:
                d = Text(_("{}".format(TimeBacker.week[str(self.nw)])),size=240, font="Cubic-11-1.000-R-2.ttf",color="#ffffff")
                return d, self.speed

    

# init -1 python:
#     # import time
#     dbegin = 16
#     dend = 7
#     month = 2
#     # hours = 12
#     min = 14400
#     speedt = 1
#     dt = 0
#     def timer_back(st, at):
#         global min, dbegin, dend, speedt

        
#         f = min mod 60

#         if f <= 0:
#             min = 60
#             h -= 1


#         if h <= 0 and min <= 0 and dbegin != dend:
#             h = 24
#             min = 0
#             dbegin -= 1
        
#         if dbegin == dend and min <= 0:
#             d = Text("{:0>2.0f}:{:0>2.0f}".format(h, f), color="#ff0000")
#             return d, None
#         elif speedt == 1:
#             d = Text("{:0>2.0f}:{:0>2.0f}".format(h, f), color="#ff0000")
#             return d, speedt 
#         else:
#             d = Text("{:0>2.0f}:{:0>2.0f}".format(h, f), color="#ff0000")
#             return d, speedt


#     def dater_back(st, at):
#         global dbegin, dend, month, speedt
        
#         if dbegin == dend and min <= 0:
#             d = Text("2022.{:0>2.0f}.{:0>2.0f}".format(month, dend), color="#ff0000")
#             return d, None
#         else:
#             d = Text("2022.{:0>2.0f}.{:0>2.0f}".format(month, dbegin), color="#ff0000")
#             return d, speedt
