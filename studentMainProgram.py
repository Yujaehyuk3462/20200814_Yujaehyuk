import sys
import csv
import os
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QTableView, QVBoxLayout
from PySide6.QtGui import QStandardItem, QStandardItemModel
from studentProgramMainWindow_ui import Ui_MainWindow
from selectionSortingWindow_ui import Ui_selectionSortingWindow
from selectionSortingByAgeWindow_ui import Ui_selectionSortingByAgeWindow
from selectionSortingByGradeWindow_ui import Ui_selectionSortingByGradeWindow
from selectionSortingByNameWindow_ui import Ui_selectionSortingByNameWindow
from insertionSortingWindow_ui import Ui_insertionSortingWindow
from insertionSortingByNameWindow_ui import Ui_insertionSortingByNameWindow
from insertionSortingByAgeWindow_ui import Ui_insertionSortingByAgeWindow
from insertionSortingByGradeWindow_ui import Ui_insertionSortingByGradeWindow
from quickSortingWindow_ui import Ui_quickSortingWindow
from quickSortingByNameWindow_ui import Ui_quickSortingByNameWindow
from quickSortingByAgeWindow_ui import Ui_quickSortingByAgeWindow
from quickSortingByGradeWindow_ui import Ui_quickSortingByGradeWindow
from radixSortingWindow_ui import Ui_radixSortingWindow

class mainWindowClass(QMainWindow, Ui_MainWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.pushButton_selectionSort.clicked.connect(self.selectionSort_clicked)
        self.pushButton_insertionSort.clicked.connect(self.insertionSort_clicked)
        self.pushButton_quickSort.clicked.connect(self.quickSort_clicked)
        self.pushButton_3.clicked.connect(self.radixSort_clicked)
        self.pushButton.clicked.connect(app.quit)

        self.dialog = None

    def selectionSort_clicked(self) :
        if self.dialog is not None :
            self.dialog.close()
        self.dialog = selectionSortingWindowClass()
        self.dialog.show()

    def insertionSort_clicked(self) :
        if self.dialog is not None :
            self.dialog.close()
        self.dialog = insertionSortingWindowClass()
        self.dialog.show()

    def quickSort_clicked(self) :
        if self.dialog is not None :
            self.dialog.close()
        self.dialog = quickSortingWindowClass()
        self.dialog.show()

    def radixSort_clicked(self) :
        if self.dialog is not None :
            self.dialog.close()
        self.dialog = radixSortingWindowClass()
        self.dialog.show()

class selectionSortingWindowClass(QWidget, Ui_selectionSortingWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.pushButton_sortingName.clicked.connect(self.selectionSortingByName)
        self.pushButton_sortingGrade.clicked.connect(self.selectionSortingByGrade)
        self.pushButton_sortingAge.clicked.connect(self.selectionSortingByAge)

        self.dialog = None

    def selectionSortingByName(self) :
        if self.dialog is not None :
            self.dialog.close()
        self.dialog = selectionSortingByNameWindowClass()
        self.dialog.show()

    def selectionSortingByGrade(self) :
        if self.dialog is not None :
            self.dialog.close()
        self.dialog = selectionSortingByGradeWindowClass()
        self.dialog.show()

    def selectionSortingByAge(self) :
        if self.dialog is not None :
            self.dialog.close()
        self.dialog = selectionSortingByAgeWindowClass()
        self.dialog.show()

class selectionSortingByNameWindowClass(QWidget, Ui_selectionSortingByNameWindow) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.model = QStandardItemModel()
        self.tableView.setModel(self.model)

        # 헤더 설정
        self.model.setHorizontalHeaderLabels(["이름", "나이", "성적"])

        # 정렬된 데이터 추가
        self.sorted_data_byName = selection_sort_dict(data, "이름")
        self.add_items(self.sorted_data_byName)

        self.pushButton.clicked.connect(self.sort_descending)

    def add_items(self, data):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(["이름", "나이", "성적"])

        # 데이터 추가
        for item in data:
            if isinstance(item, dict):
                name_item = QStandardItem(item.get("이름"))
                age_item = QStandardItem(str(item.get("나이")))
                grade_item = QStandardItem(str(item.get("성적")))

                # 한 행에 아이템 추가
                self.model.appendRow([name_item, age_item, grade_item])

    def sort_descending(self):
        # 내림차순 정렬
        self.sorted_data_byName.sort(key=lambda x: x["이름"], reverse=True)
        self.add_items(self.sorted_data_byName)

class selectionSortingByAgeWindowClass(QWidget, Ui_selectionSortingByAgeWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.model = QStandardItemModel()
        self.tableView.setModel(self.model)

        # 헤더 설정
        self.model.setHorizontalHeaderLabels(["이름", "나이", "성적"])

        # 정렬된 데이터 추가
        self.sorted_data_byAge = selection_sort_dict(data, "나이")
        self.add_items(self.sorted_data_byAge)

        self.pushButton.clicked.connect(self.sort_descending)

    def add_items(self, data):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(["이름", "나이", "성적"])
        # 데이터 추가
        for item in data:
            if isinstance(item, dict):
                name_item = QStandardItem(item.get("이름"))
                age_item = QStandardItem(str(item.get("나이")))
                grade_item = QStandardItem(str(item.get("성적")))

                # 한 행에 아이템 추가
                self.model.appendRow([name_item, age_item, grade_item])

    def sort_descending(self):
        # 내림차순 정렬
        self.sorted_data_byAge.sort(key=lambda x: x["나이"], reverse=True)
        self.add_items(self.sorted_data_byAge)

class selectionSortingByGradeWindowClass(QWidget, Ui_selectionSortingByGradeWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.model = QStandardItemModel()
        self.tableView.setModel(self.model)

        # 헤더 설정
        self.model.setHorizontalHeaderLabels(["이름", "나이", "성적"])

        # 정렬된 데이터 추가
        self.sorted_data_byGrade = selection_sort_dict(data, "성적")
        self.add_items(self.sorted_data_byGrade)

        self.pushButton.clicked.connect(self.sort_descending)

    def add_items(self, data):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(["이름", "나이", "성적"])
        # 데이터 추가
        for item in data:
            if isinstance(item, dict):
                name_item = QStandardItem(item.get("이름"))
                age_item = QStandardItem(str(item.get("나이")))
                grade_item = QStandardItem(str(item.get("성적")))

                # 한 행에 아이템 추가
                self.model.appendRow([name_item, age_item, grade_item])

    def sort_descending(self):
        # 내림차순 정렬
        self.sorted_data_byGrade.sort(key=lambda x: x["성적"], reverse=True)
        self.add_items(self.sorted_data_byGrade)

class insertionSortingWindowClass(QWidget, Ui_insertionSortingWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.pushButton_sortingName.clicked.connect(self.insertionSortingByName)
        self.pushButton_sortingAge.clicked.connect(self.insertionSortingByAge)
        self.pushButton_sortingGrade.clicked.connect(self.insertionSortingByGrade)

        self.dialog = None

    def insertionSortingByName(self) :
        if self.dialog is not None :
            self.dialog.close()

        self.dialog = insertionSortingByNameWindowClass()
        self.dialog.show()

    def insertionSortingByAge(self) :
        if self.dialog is not None :
            self.dialog.close()

        self.dialog = insertionSortingByAgeWindowClass()
        self.dialog.show()

    def insertionSortingByGrade(self) :
        if self.dialog is not None :
            self.dialog.close()
        
        self.dialog = insertionSortingByGradeWindowClass()
        self.dialog.show()

class insertionSortingByNameWindowClass(QWidget, Ui_insertionSortingByNameWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.model = QStandardItemModel()
        self.tableView.setModel(self.model)

        # 헤더 설정
        self.model.setHorizontalHeaderLabels(["이름", "나이", "성적"])

        # 정렬된 데이터 추가
        self.sorted_data_byName = insertion_sort_dict(data, "이름")
        self.add_items(self.sorted_data_byName)

        self.pushButton.clicked.connect(self.sort_descending)

    def add_items(self, data):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(["이름", "나이", "성적"])
        # 데이터 추가
        for item in data:
            if isinstance(item, dict):
                name_item = QStandardItem(item.get("이름"))
                age_item = QStandardItem(str(item.get("나이")))
                grade_item = QStandardItem(str(item.get("성적")))

                # 한 행에 아이템 추가
                self.model.appendRow([name_item, age_item, grade_item])

    def sort_descending(self):
        # 내림차순 정렬
        self.sorted_data_byName.sort(key=lambda x: x["이름"], reverse=True)
        self.add_items(self.sorted_data_byName)

class insertionSortingByAgeWindowClass(QWidget, Ui_insertionSortingByAgeWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.model = QStandardItemModel()
        self.tableView.setModel(self.model)

        # 헤더 설정
        self.model.setHorizontalHeaderLabels(["이름", "나이", "성적"])

        # 정렬된 데이터 추가
        self.sorted_data_byAge = insertion_sort_dict(data, "나이")
        self.add_items(self.sorted_data_byAge)

        self.pushButton.clicked.connect(self.sort_descending)

    def add_items(self, data):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(["이름", "나이", "성적"])
        # 데이터 추가
        for item in data:
            if isinstance(item, dict):
                name_item = QStandardItem(item.get("이름"))
                age_item = QStandardItem(str(item.get("나이")))
                grade_item = QStandardItem(str(item.get("성적")))

                # 한 행에 아이템 추가
                self.model.appendRow([name_item, age_item, grade_item])

    def sort_descending(self):
        # 내림차순 정렬
        self.sorted_data_byAge.sort(key=lambda x: x["나이"], reverse=True)
        self.add_items(self.sorted_data_byAge)

class insertionSortingByGradeWindowClass(QWidget, Ui_insertionSortingByGradeWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.model = QStandardItemModel()
        self.tableView.setModel(self.model)

        # 헤더 설정
        self.model.setHorizontalHeaderLabels(["이름", "나이", "성적"])

        # 정렬된 데이터 추가
        self.sorted_data_byGrade = insertion_sort_dict(data, "성적")
        self.add_items(self.sorted_data_byGrade)

        self.pushButton.clicked.connect(self.sort_descending)

    def add_items(self, data):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(["이름", "나이", "성적"])
        # 데이터 추가
        for item in data:
            if isinstance(item, dict):
                name_item = QStandardItem(item.get("이름"))
                age_item = QStandardItem(str(item.get("나이")))
                grade_item = QStandardItem(str(item.get("성적")))

                # 한 행에 아이템 추가
                self.model.appendRow([name_item, age_item, grade_item])

    def sort_descending(self):
        # 내림차순 정렬
        self.sorted_data_byGrade.sort(key=lambda x: x["성적"], reverse=True)
        self.add_items(self.sorted_data_byGrade)

class quickSortingWindowClass(QWidget, Ui_quickSortingWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.pushButton_sortingName.clicked.connect(self.quickSortingByName)
        self.pushButton_sortingAge.clicked.connect(self.quickSortingByAge)
        self.pushButton_sortingGrade.clicked.connect(self.quickSortingByGrade)
        
        self.dialog = None

    def quickSortingByName(self) :
        if self.dialog is not None :
            self.dialog.close()
        self.dialog = quickSortingByNameWindowClass()
        self.dialog.show()

    def quickSortingByAge(self) :
        if self.dialog is not None :
            self.dialog.close()
        self.dialog = quickSortingByAgeWindowClass()
        self.dialog.show()

    def quickSortingByGrade(self) :
        if self.dialog is not None :
            self.dialog.close()
        self.dialog = quickSortingByGradeWindowClass()
        self.dialog.show()

class quickSortingByNameWindowClass(QWidget, Ui_quickSortingByNameWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.model = QStandardItemModel()
        self.tableView.setModel(self.model)

        # 헤더 설정
        self.model.setHorizontalHeaderLabels(["이름", "나이", "성적"])

        # 정렬된 데이터 추가
        self.sorted_data_byName = quick_sort_dict(data, "이름")
        self.add_items(self.sorted_data_byName)

        self.pushButton.clicked.connect(self.sort_descending)

    def add_items(self, data):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(["이름", "나이", "성적"])
        # 데이터 추가
        for item in data:
            if isinstance(item, dict):
                name_item = QStandardItem(item.get("이름"))
                age_item = QStandardItem(str(item.get("나이")))
                grade_item = QStandardItem(str(item.get("성적")))

                # 한 행에 아이템 추가
                self.model.appendRow([name_item, age_item, grade_item])

    def sort_descending(self):
        # 내림차순 정렬
        self.sorted_data_byName.sort(key=lambda x: x["이름"], reverse=True)
        self.add_items(self.sorted_data_byName)

class quickSortingByAgeWindowClass(QWidget, Ui_quickSortingByAgeWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.model = QStandardItemModel()
        self.tableView.setModel(self.model)

        # 헤더 설정
        self.model.setHorizontalHeaderLabels(["이름", "나이", "성적"])

        # 정렬된 데이터 추가
        self.sorted_data_byAge = quick_sort_dict(data, "나이")
        self.add_items(self.sorted_data_byAge)

        self.pushButton.clicked.connect(self.sort_descending)

    def add_items(self, data):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(["이름", "나이", "성적"])
        # 데이터 추가
        for item in data:
            if isinstance(item, dict):
                name_item = QStandardItem(item.get("이름"))
                age_item = QStandardItem(str(item.get("나이")))
                grade_item = QStandardItem(str(item.get("성적")))

                # 한 행에 아이템 추가
                self.model.appendRow([name_item, age_item, grade_item])

    def sort_descending(self):
        # 내림차순 정렬
        self.sorted_data_byAge.sort(key=lambda x: x["나이"], reverse=True)
        self.add_items(self.sorted_data_byAge)

class quickSortingByGradeWindowClass(QWidget, Ui_quickSortingByGradeWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.model = QStandardItemModel()
        self.tableView.setModel(self.model)

        # 헤더 설정
        self.model.setHorizontalHeaderLabels(["이름", "나이", "성적"])

        # 정렬된 데이터 추가
        self.sorted_data_byGrade = quick_sort_dict(data, "성적")
        self.add_items(self.sorted_data_byGrade)

        self.pushButton.clicked.connect(self.sort_descending)

    def add_items(self, data):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(["이름", "나이", "성적"])
        # 데이터 추가
        for item in data:
            if isinstance(item, dict):
                name_item = QStandardItem(item.get("이름"))
                age_item = QStandardItem(str(item.get("나이")))
                grade_item = QStandardItem(str(item.get("성적")))

                # 한 행에 아이템 추가
                self.model.appendRow([name_item, age_item, grade_item])

    def sort_descending(self):
        # 내림차순 정렬
        self.sorted_data_byGrade.sort(key=lambda x: x["성적"], reverse=True)
        self.add_items(self.sorted_data_byGrade)


class radixSortingWindowClass(QWidget, Ui_radixSortingWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.model = QStandardItemModel()
        self.tableView.setModel(self.model)

        # 헤더 설정
        self.model.setHorizontalHeaderLabels(["이름", "나이", "성적"])

        # 정렬된 데이터 추가
        self.sorted_data_byGrade = radix_sort_dict(data, "성적")
        self.add_items(self.sorted_data_byGrade)

        self.pushButton.clicked.connect(self.sort_descending)

    def add_items(self, data):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(["이름", "나이", "성적"])
        # 데이터 추가
        for item in data:
            if isinstance(item, dict):
                name_item = QStandardItem(item.get("이름"))
                age_item = QStandardItem(str(item.get("나이")))
                grade_item = QStandardItem(str(item.get("성적")))

                # 한 행에 아이템 추가
                self.model.appendRow([name_item, age_item, grade_item])

    def sort_descending(self):
        # 내림차순 정렬
        self.sorted_data_byGrade.sort(key=lambda x: x["성적"], reverse=True)
        self.add_items(self.sorted_data_byGrade)

# 선택 정렬 알고리즘
def selection_sort_dict(data, key):
    n = len(data)
    for i in range(n - 1):
        # 최소값의 인덱스를 찾기
        min_index = i
        for j in range(i + 1, n):
            if data[j][key] < data[min_index][key]:
                min_index = j
        # 현재 위치와 최소값 위치의 데이터 교환
        data[i], data[min_index] = data[min_index], data[i]
    return data

# 삽입 정렬 알고리즘
def insertion_sort_dict(data, sort_key) :
    n = len(data)
    for i in range(1, n) :
        current = data[i]  # 현재 삽입할 데이터
        j = i - 1

        # sort_key 기준으로 값 비교
        while j >= 0 and data[j][sort_key] > current[sort_key]:
            data[j + 1] = data[j]  # 한 칸씩 뒤로 밀기
            j -= 1

        data[j + 1] = current  # 올바른 위치에 삽입

    return data

# 퀵 정렬 알고리즘
def quick_sort_dict(data, key):
    if len(data) <= 1:  # 리스트 크기가 1 이하인 경우
        return data

    # 기준값 선택: 첫 번째 요소
    pivot = data[0]

    # 분할
    less = [item for item in data[1:] if item[key] <= pivot[key]]  # 기준값 이하
    greater = [item for item in data[1:] if item[key] > pivot[key]]  # 기준값 초과

    # 재귀적으로 정렬 후 합치기
    return quick_sort_dict(less, key) + [pivot] + quick_sort_dict(greater, key)

# 기수정렬 알고리즘(계수정렬)
def counting_sort_for_dict(arr, key, exp):
    n = len(arr)
    output = [None] * n
    count = [0] * 10  # 0~9 자리수 카운트 배열

    # 현재 자리수를 기준으로 카운트
    for item in arr:
        index = (item[key] // exp) % 10
        count[index] += 1

    # 누적 합 계산
    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i][key] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # 원본 배열 갱신
    for i in range(n):
        arr[i] = output[i]

def radix_sort_dict(arr, key):
    # 가장 큰 수의 자리수 계산
    max_val = max(item[key] for item in arr)
    exp = 1  # 1의 자리부터 시작

    # 자리수별로 정렬 수행
    while max_val // exp > 0:
        counting_sort_for_dict(arr, key, exp)
        exp *= 10

    return arr

# csv파일 불러오기
def load_from_csv(filepath):
    data = []
    with open(filepath, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['나이'] = int(row['나이'])
            row['성적'] = int(row['성적'])
            data.append(row)
    return data

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "nameList.csv")
data = load_from_csv(file_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindowClass()
    window.show()
    sys.exit(app.exec())