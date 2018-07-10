import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

imagefile='a.jpg'
imag=Image.open(imagefile)

def title():
    title=input('请输入标题')
    titlefont=ImageFont.truetype('AdobeHeitiStd-Regular.otf',24)#这一步用来设置字体
    draw=ImageDraw.Draw(imag)
    x=400
    num=len(title)
    num=int(num)
    x=x-(3*num)
    draw.text((x,10),title,(0,0,0),titlefont)
    draw=ImageDraw.Draw(imag)
    imag.save('ok.jpg')


def time():
    title=input('请输入时间完整格式')#这里修改变量和内容
    titlefont=ImageFont.truetype('AdobeHeitiStd-Regular.otf',14)#这里修改字体大小
    draw=ImageDraw.Draw(imag)
    x=46  #这里填写居中位置
    num=len(title)#这里修改变量
    num=int(num)
    x=x-(1*num)#这里修改算法
    draw.text((x,72),title,(0,0,0),titlefont) #这里修改y轴
    draw=ImageDraw.Draw(imag)
    imag.save('ok.jpg')

def time():
    title=input('请输入时间完整格式')#这里修改变量和内容
    titlefont=ImageFont.truetype('AdobeHeitiStd-Regular.otf',14)#这里修改字体大小
    draw=ImageDraw.Draw(imag)
    x=46  #这里填写居中位置
    num=len(title)#这里修改变量
    num=int(num)
    x=x-(1*num)#这里修改算法
    draw.text((x,72),title,(0,0,0),titlefont) #这里修改y轴
    draw=ImageDraw.Draw(imag)
    imag.save('ok.jpg')

def left1():
    title=input('请输入自定义文字1')#这里修改变量和内容
    titlefont=ImageFont.truetype('AdobeHeitiStd-Regular.otf',14)#这里修改字体大小
    draw=ImageDraw.Draw(imag)
    draw.text((12,128),title,(0,0,0),titlefont) #这里修改y轴
    draw=ImageDraw.Draw(imag)
    imag.save('ok.jpg')
def left2():
    title=input('请输入自定义文字2')#这里修改变量和内容
    titlefont=ImageFont.truetype('AdobeHeitiStd-Regular.otf',14)#这里修改字体大小
    draw=ImageDraw.Draw(imag)
    draw.text((12,179),title,(0,0,0),titlefont) #这里修改y轴
    draw=ImageDraw.Draw(imag)
    imag.save('ok.jpg')
def left3():
    title=input('请输入自定义文字3')#这里修改变量和内容
    titlefont=ImageFont.truetype('AdobeHeitiStd-Regular.otf',14)#这里修改字体大小
    draw=ImageDraw.Draw(imag)
    draw.text((12,230),title,(0,0,0),titlefont) #这里修改y轴
    draw=ImageDraw.Draw(imag)
    imag.save('ok.jpg')
    
def jcfs():
    title=input('基础分数')#这里修改变量和内容
    titlefont=ImageFont.truetype('AdobeHeitiStd-Regular.otf',14)#这里修改字体大小
    draw=ImageDraw.Draw(imag)
    x=740  #这里填写居中位置
    num=len(title)#这里修改变量
    num=int(num)
    x=x-(1*num)#这里修改算法
    draw.text((x,296),title,(0,0,0),titlefont) #这里修改y轴
    draw=ImageDraw.Draw(imag)
    imag.save('ok.jpg')

def xgzyzs():
    title=input('相关专业知识分数')#这里修改变量和内容
    titlefont=ImageFont.truetype('AdobeHeitiStd-Regular.otf',14)#这里修改字体大小
    draw=ImageDraw.Draw(imag)
    x=740  #这里填写居中位置
    num=len(title)#这里修改变量
    num=int(num)
    x=x-(1*num)#这里修改算法
    draw.text((x,326),title,(0,0,0),titlefont) #这里修改y轴
    draw=ImageDraw.Draw(imag)
    imag.save('ok.jpg')

def zyzs():
    title=input('专业知识分数')#这里修改变量和内容
    titlefont=ImageFont.truetype('AdobeHeitiStd-Regular.otf',14)#这里修改字体大小
    draw=ImageDraw.Draw(imag)
    x=740  #这里填写居中位置
    num=len(title)#这里修改变量
    num=int(num)
    x=x-(1*num)#这里修改算法
    draw.text((x,356),title,(0,0,0),titlefont) #这里修改y轴
    draw=ImageDraw.Draw(imag)
    imag.save('ok.jpg')

def zysjnl():
    title=input('专业时间能力分数')#这里修改变量和内容
    titlefont=ImageFont.truetype('AdobeHeitiStd-Regular.otf',14)#这里修改字体大小
    draw=ImageDraw.Draw(imag)
    x=740  #这里填写居中位置
    num=len(title)#这里修改变量
    num=int(num)
    x=x-(1*num)#这里修改算法
    draw.text((x,386),title,(0,0,0),titlefont) #这里修改y轴
    draw=ImageDraw.Draw(imag)
    imag.save('ok.jpg')

def hz():
    title=input('请输入红字标题')#这里修改变量和内容
    titlefont=ImageFont.truetype('AdobeHeitiStd-Regular.otf',14)#这里修改字体大小
    draw=ImageDraw.Draw(imag)
    x=325  #这里填写居中位置
    num=len(title)#这里修改变量
    num=int(num)
    x=x-(1*num)#这里修改算法
    draw.text((325,420),title,(255,0,0),titlefont) #这里修改y轴
    draw=ImageDraw.Draw(imag)
    imag.save('ok.jpg')

def hz1():
    title=input('请输入红字第一行')#这里修改变量和内容
    titlefont=ImageFont.truetype('AdobeHeitiStd-Regular.otf',14)#这里修改字体大小
    draw=ImageDraw.Draw(imag)
    x=325  #这里填写居中位置
    num=len(title)#这里修改变量
    num=int(num)
    x=x-(1*num)#这里修改算法
    draw.text((325,450),title,(255,0,0),titlefont) #这里修改y轴
    draw=ImageDraw.Draw(imag)
    imag.save('ok.jpg')

def hz2():
    title=input('请输入红字第二行')#这里修改变量和内容
    titlefont=ImageFont.truetype('AdobeHeitiStd-Regular.otf',14)#这里修改字体大小
    draw=ImageDraw.Draw(imag)
    x=325  #这里填写居中位置
    num=len(title)#这里修改变量
    num=int(num)
    x=x-(1*num)#这里修改算法
    draw.text((325,480),title,(255,0,0),titlefont) #这里修改y轴
    draw=ImageDraw.Draw(imag)
    imag.save('ok.jpg')

def hz3():
    title=input('请输入红字第三行')#这里修改变量和内容
    titlefont=ImageFont.truetype('AdobeHeitiStd-Regular.otf',14)#这里修改字体大小
    draw=ImageDraw.Draw(imag)
    x=325  #这里填写居中位置
    num=len(title)#这里修改变量
    num=int(num)
    x=x-(1*num)#这里修改算法
    draw.text((325,510),title,(255,0,0),titlefont) #这里修改y轴
    draw=ImageDraw.Draw(imag)
    imag.save('ok.jpg')


def name():
    title=input('输入名字')#这里修改变量和内容
    titlefont=ImageFont.truetype('AdobeHeitiStd-Regular.otf',12)#这里修改字体大小
    draw=ImageDraw.Draw(imag)
    x=650  #这里填写居中位置
    num=len(title)#这里修改变量
    num=int(num)
    x=x-(1*num)#这里修改算法
    draw.text((x,154),title,(0,0,0),titlefont) #这里修改y轴
    draw=ImageDraw.Draw(imag)
    imag.save('ok.png')

def hgzt():
    title=input('输入合格状态')#这里修改变量和内容
    titlefont=ImageFont.truetype('AdobeHeitiStd-Regular.otf',12)#这里修改字体大小
    draw=ImageDraw.Draw(imag)
    x=650  #这里填写居中位置
    num=len(title)#这里修改变量
    num=int(num)
    x=x-(1*num)#这里修改算法
    draw.text((x,182),title,(0,0,0),titlefont) #这里修改y轴
    draw=ImageDraw.Draw(imag)
    imag.save('ok.png')

def sfzh():
    title=input('输入身份证号')#这里修改变量和内容
    titlefont=ImageFont.truetype('AdobeHeitiStd-Regular.otf',12)#这里修改字体大小
    draw=ImageDraw.Draw(imag)
    x=650  #这里填写居中位置
    num=len(title)#这里修改变量
    num=int(num)
    x=x-(2.9*num)#这里修改算法
    draw.text((x,210),title,(0,0,0),titlefont) #这里修改y轴
    draw=ImageDraw.Draw(imag)
    imag.save('ok.png')

def logo():
    def small():
        imagefox=input('请把logo放于根目录下 并且输入logo名称')
        bigimage = Image.open(imagefox)
        smallimage = bigimage.resize((50,50))
        return smallimage
        
        
    base_img=Image.open('ok.png')
    box=(0,0,55,55)
    tmp_image=small()
    tmp_image = tmp_image.resize((box[2] - box[0], box[3] - box[1]))
    base_img.paste(tmp_image, box)
    base_img.show() # 查看合成的图片
    base_img.save('../out.png') #保存图片
    
title()
time()
left1()
left2()
left3()
jcfs()
xgzyzs()
zyzs()
zysjnl()
hz()
hz1()
hz2()
hz3()
name()
hgzt()
sfzh()    
logo()

    

