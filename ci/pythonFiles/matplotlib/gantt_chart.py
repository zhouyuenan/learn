# ------------------------------------------------
# Project:
#       This project is used to draw a gantt chart
# History:
#       2023/08/12 周月南 First release
# ------------------------------------------------
import matplotlib.pyplot as plt


def build_data():
    data = {
        'task1': {
            'task_name': 'ID01 AKS Version Update of DEV Environment',
            'start_time': "2023/08/10",
            'sustained_time': 1
        },

        'task2': {
            'task_name': 'GO02 AKS Version Update of DEV Environment',
            'start_time': "2023/08/11",
            'sustained_time': 1
        }
    }


def build_draw():
    data = {
        'task1': {
            'task_name': 'ID01 AKS Version Update of DEV Environment',
            'start_time': "2023/08/10",
            'sustained_time': 1
        },

        'task2': {
            'task_name': 'GO02 AKS Version Update of DEV Environment',
            'start_time': "2023/08/11",
            'sustained_time': 1
        }
    }
    x = ['ID01 AKS Version Update of DEV Environment', 'GO02 AKS Version Update of DEV Environment']
    y = [1, 1]
    start_time = [1, 2]
    fix, ax = plt.subplots(1, figsize=(16, 6))
    ax.barh(x, y, left=start_time)
    plt.show()


def build_main():
    build_draw()


build_main()