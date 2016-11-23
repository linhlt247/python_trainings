#-*- coding:utf-8 -*-
import Image,re
def imo():
	S = []
	R = ""
	result = ""
	image = Image.open('oxygen.png') #Mở file ảnh
	for x in range(1,629,7): #Chiều dài của ảnh là 628 pixel, khi cho chạy từ 1 đến 628, thì ta thấy mỗi một màu là 7 pixel, nên ta chạy từ 1 đến 628 với bước nhảy là 7
		var2 = image.getpixel((x,47)) #Chiều rộng của hình là 94 pixel, vùng xám trên hình nằm ở giữa, nên ta lấy 94/2 = 47
		S.append(var2[0]) #lấy giá trị đầu tiên trong tuple, tại một vị trí pixel, ta có tuple = [R,G,B,A], giá trị R,G,B giống nhau nên ta lấy giá trị đầu tiên
	for i in S:
		R = R + chr(i) #đối số thanh ký tự theo bảng mã ascii, ta được : smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]njb
	number = re.findall("[0-9]+",R) #lấy đoạn tuple trong chuỗi trên
	for j in number:
		result = result + chr(int(j)) #chuyển các con số thu được thành ký tự ascii, ta thu được kết quả
	print result
if __name__ == '__main__':
	imo()