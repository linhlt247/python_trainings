#Pythonchallenge.com
*Tên tài liệu: Tìm hiểu Pythonchallenge*

*Người làm: Hoàng Quốc Cường*

##Mục lục:
- [1.Ý tưởng làm challenge](#challenge)
- [2. re Module](#re)

##Nội dung:

<a name = "challenge" />
###1.Ý tưởng làm challenge:
####Phân tích: 
"One small letter, surrounded by EXACTLY three big bodyguards on each of its sides."Dựa vào đoạn mã trong source web và gợi ý bên, ta có thể đoán rắng kết quả sẽ là một chuỗi chữ cái in thường có nghĩa và mỗi chữ cái cấu thành lên chuỗi đó sẽ được bao bọc bởi chính xác 3 chữ cái in hoa ở trong đoạn mà source web. Giờ vấn đề đặt ra là tìm được các chữ cái thường thỏa điều kiện là nó được bao bọc bởi duy nhất 3 chữ cái in hoa ở mỗi mặt, có nghĩa nó sẽ được bao bọc tổng cộng 6 chữ cái in hoa ở hai bên. Ví dụ: `m-A-I-L-a-A-N-H-e`, trong chuỗi bên, 'a' chính là một thành phần trong chuỗi cần tìm vì đó đáp ứng đủ yêu cầu đề cho.
####Ý tưởng giải:
Ta sẽ dùng vòng lặp và dựa vào chỉ mục của chuỗi. Đầu tiên, ta sẽ cho i chạy từ 0 đến độ dài của chuỗi. Sau đó kiểm tra xem ở vị trí i trong chuỗi là ký tự in hoa hay in thường, nếu in thường thì qua chỉ mục tiếp theo, nếu in HOA, thì ta sẽ kiểm tra xem các điều kiện sau:
```
Vị trí i - 1: là chữ thường
Vị trí i + 1: là chữ in hoa
Vị trí i + 2: là chữ in hoa
Vị trí i + 3: là chữ thường
Vị trí i + 4: là chữ in hoa
Vị trí i + 5: là chữ in hoa
Vị trí i + 6: là chữ in hoa
Vị trí i + 7: là chữ thường
```
Từ các điều kiện trên và kết hợp điều kiện vị trí i là chữ in HOA, ta có thể thấy rằng vị trí i+3 sẽ là một phần tử trong chuỗi cần tìm và ta add vào chuỗi rỗng để cuối cùng là thu được kết quả.

<a name = 're' />
###.2.re Module
*(comming soon)*