
import xlsxwriter

def load():
    with open('phones.txt', 'r') as f:
        # f.write(str(name))

        lines = f.readlines()
    lines=lines[0]
    # print(lines)
    # print(len(lines))
    # x=Convert(lines)
    # print(x[0])
    replace(lines)


def replace(lines):

    x=lines.replace("['",'-')
    lines=x.replace("']",'-')
    # print('xxxxxxxxxx',lines[0])
    convert_to_list(lines)


def convert_to_list(lines):
    phone=''
    phone_book=[]
    for char in lines:
        if char!='+':
            phone+=char
        else:
            phone_book.append(phone)
            phone=''
    print(phone_book[0:10])
    replace_2(phone_book)

def replace_2(phone_book):
    print('phone_book[i]',phone_book[0])
    for i in range(1,len(phone_book)):
        print('phone_book[i]',phone_book[i])
        phone_book[i] = phone_book[i].replace(" ",'')
        phone_book[i] = phone_book[i].replace("-",'')
        phone_book[i] = '+'+phone_book[i]
    print(len(phone_book))
    
    delete_same(phone_book)

def delete_same(phone_book):
    res = []
    [res.append(x) for x in phone_book if x not in res]
    phone_book=res
    print(len(res))
    save_excel(phone_book)

def save_excel(list):
    with xlsxwriter.Workbook('phone_book.xlsx') as workbook:
        worksheet = workbook.add_worksheet()

        # for row_num, data in enumerate(list):
        #     worksheet.write_row(row_num, 0, data)
        for row in range(len(list)):
            worksheet.write(row, 0, list[row])


load()