#-*- coding: utf-8 -*-
import zipfile,re
def find_result():
	source = zipfile.ZipFile('channel.zip') # mở file zip
	number = '90052' #file readme.txt gợi ý mở file 90052.txt
	text = 'Next nothing is (\d+)' #thông điệp trong file
	comments = "" 
	while True:
		try:
			txt = source.read(number + '.txt') #đọc nội dung trong file number.txt
			number = re.search(text,txt).group(1) #tìm trong nội dung file và number là số hiệu của file tiếp theo
		except:
			print txt #in ra kết quả cuối cùng :Collect the comments
			break
		comments = comments + source.getinfo(number + '.txt').comment #thu thập comments
	print comments

if __name__ == '__main__':
	find_result()