import pytest

cnt = 0


@pytest.fixture(autouse=True)
def testfile_preparation():
    global cnt
    with open("/Users/romankashlev/PycharmProjects/pythonProject/tests/test_file_workers/testfile.txt", "w"):
        pass
    print(cnt)
    cnt += 1
