#参考
#https://dev.classmethod.jp/articles/export-text-data-from-image-using-python/
#https://tech.mof-mof.co.jp/blog/tesseract-ocr/


from PIL import Image,ImageEnhance
import sys
import pyocr
import pyocr.builders
import pdf2image

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'libtesseract'


img = pdf2image.convert_from_path("./T1-H.pdf", dpi=350, fmt='jpg')


# lang = 'eng'
lang = 'jpn+eng'
# 画像オブジェクトからテキストに
f = open('myfile.txt', 'w')
for image in img:
    # img_g=image.crop((0, 200, 2300, 3300))
    img_g = image.convert('L') #Gray変換
    enhancer= ImageEnhance.Contrast(img_g) #コントラストを上げる
    img_con = enhancer.enhance(2.0) #コントラストを上げる
    # img_con.open()
    # cv2.imshow("Image", img_con)
    # img_con.save("a.jpg")
    # a=Image.open("a.jpg")
    # a.show()
    # exit()
    txt = tool.image_to_string(
        img_con,
        lang=lang,
        builder=pyocr.builders.TextBuilder()
    )
    txt=txt.replace(" ","")
    txt=txt.replace("   ","")
    txt=txt.replace("　","") 
    txt=txt.replace(",","、")
    txt=txt.replace("`","「")
    txt=txt.replace("①","1")
    txt=txt.replace("②","2")
    txt=txt.replace("③","3")
    txt=txt.replace("④","4")
    txt=txt.replace("⑤","5")
    txt=txt.replace("⑥","6")
    txt=txt.replace("⑦","7")
    txt=txt.replace("⑧","8")
    txt=txt.replace("⑨","9")
    txt=txt.replace("⑩","10")

    

    # print(txt)
    
    f.write(txt)
f.close()