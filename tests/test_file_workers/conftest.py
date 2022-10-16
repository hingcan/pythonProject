import pytest

cnt = 0


@pytest.fixture(autouse=True)
def testfile_preparation():
    global cnt
    with open("testfile.txt", "w"):
        pass
    print(cnt)
    cnt += 1
