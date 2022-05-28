from ast import While
from operator import index
from re import T


def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    keep_num = len(sorted_array)    #listの長さ　中央のインデックスを保存する役割 
    first = 0                       # sをリストの最小インデックスと仮定 
    last = keep_num - 1             # lをリストの最大インデックスと仮定 

    for i in range(len(sorted_array)):
        
        # リストの要素数が偶数の場合の分岐
        if keep_num % 2 == 0:
            keep_num = int(keep_num/2 - 1)          # 中央値のインデックスを保存・更新
            M_index = int((first+last)/2 - 0.5)     # 返り値用のリストの中央のインデックス
            M_num = (sorted_array[M_index] + sorted_array[M_index+1])/2  # リストの中央値
            #リストの中央値によって条件分岐
            if M_num == target_number:
                return M_index
            if M_num > target_number:
                last = last + keep_num          # 最大インデックスをずらす
            if M_num < target_number:           
                first = first + keep_num + 1    # 最小インデックスをずらす



        # リストの要素数が奇数の場合の分岐
        if keep_num % 2 == 1:
            keep_num = int(keep_num/2 - 0.5)        # 中央値のインデックスを保存・更新
            M_index = int((first+last)/2)           # 返り値用のリストの中央のインデックス
            M_num = sorted_array[M_index]           # リストの中央値
            #リストの中央値によって条件分岐
            if M_num == target_number:
                return M_index
            if M_num > target_number:
                last = last + keep_num - 1          # 最大インデックスをずらす
            if M_num < target_number:
                first = first + keep_num + 1        # 最小インデックスをずらす

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()