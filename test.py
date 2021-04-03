from my_parser import parse

for i in range(1, 4):
    with open(f'test{i}.mylang', 'r', encoding='utf-8') as file_:
        test_dict = lambda x : None
        test_dict.variables = {}
        print(f'Проверяем файл test{i}.mylang:')
        parse(file_.read()).eval(test_dict)