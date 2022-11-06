from my_funcs.file_workers import read_from_file


def create_test_data(test_data):
    with open("/Users/romankashlev/PycharmProjects/pythonProject/tests/test_file_workers/testfile.txt", "a") as f_o:
        f_o.writelines(test_data)

def test_read_from_file_0():
    test_data = ['porsche_911\n', 'ferrari_f40\n', 'lamborghini_miura\n', 'alfa_romeo_33\n', 'toyota_2000gt\n',
                 'honda_nsx']
    create_test_data(test_data)
    assert test_data == read_from_file("/Users/romankashlev/PycharmProjects/pythonProject/tests/test_file_workers/testfile.txt")

def test_read_from_file_1():
    test_data = ['porsche_911\n', 'ferrari_f40\n', 'lamborghini_miura\n', 'alfa_romeo_33\n', 'toyota_2000gt\n',
                 'honda_nsx\n', 'lada_priora']
    create_test_data(test_data)
    assert test_data == read_from_file("/Users/romankashlev/PycharmProjects/pythonProject/tests/test_file_workers/testfile.txt")
