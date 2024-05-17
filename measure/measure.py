# -*- coding: utf-8 -*-
import os
from PySide2 import QtWidgets
from PySide2.QtUiTools import QUiLoader
from maya import cmds
import pymel.core as pm
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin

# designer.exeで作ったUIファイルを取得する
CURRENT_FILE = os.path.normpath(__file__)
path, ext = os.path.splitext(CURRENT_FILE)
UI_FILE = path + ".ui"

class MeasureWindow(MayaQWidgetBaseMixin, QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MeasureWindow, self).__init__(*args, **kwargs)

        # 作ったUIファイルをロードして変数に入れる
        self.widget = QUiLoader().load(UI_FILE)
        self.setWindowTitle(self.widget.windowTitle())

        # QMainWindowの中央のウィジェットに入れる
        self.setCentralWidget(self.widget)

        # ボタンとのコネクションを作る
        self.widget.v_dm.clicked.connect(self.clicked_get_distance_between_selected_vertices) #頂点
        self.widget.v_dm_2.clicked.connect(self.clicked_get_distance_between_selected_vertices_2) #頂点
        self.widget.v_dm_3.clicked.connect(self.clicked_get_distance_between_selected_vertices_3) #頂点減算
        self.widget.e_dm.clicked.connect(self.clicked_measure_selected_edges_length) #エッジ
        self.widget.e_dm_2.clicked.connect(self.clicked_measure_selected_edges_length_2) #エッジ
        self.widget.e_dm_3.clicked.connect(self.clicked_measure_selected_edges_length_3) #エッジ減算
        self.widget.e_v_c.clicked.connect(self.clicked_bust_cup_measurement) #バスト測定
        self.widget.v_cl.clicked.connect(self.clicked_cl) #クリアー

    def clicked_get_distance_between_selected_vertices(self):

    # 選択された頂点を取得
        selected_vertices = pm.filterExpand(sm=31)  # sm=31は頂点選択モード
        if not selected_vertices or len(selected_vertices) != 2:
            Warning_text = ("2つの頂点を選択してください。")
            self.widget.v_t.setPlainText(Warning_text)
            return

    # 頂点の位置を取得
        pos1 = pm.pointPosition(selected_vertices[0], world=True)
        pos2 = pm.pointPosition(selected_vertices[1], world=True)

        # 距離を計算
        distance = pm.dt.Vector(pos1).distanceTo(pos2)

            # 結果をテキストに出力
        result_text = format(distance)
        self.widget.v_t.setPlainText(result_text)


    # その2
    def clicked_get_distance_between_selected_vertices_2(self):

    # 選択された頂点を取得
        selected_vertices = pm.filterExpand(sm=31)  # sm=31は頂点選択モード
        if not selected_vertices or len(selected_vertices) != 2:
            Warning_text = ("2つの頂点を選択してください。")
            self.widget.v_t_2.setPlainText(Warning_text)
            return

    # 頂点の位置を取得
        pos1 = pm.pointPosition(selected_vertices[0], world=True)
        pos2 = pm.pointPosition(selected_vertices[1], world=True)

        # 距離を計算
        distance = pm.dt.Vector(pos1).distanceTo(pos2)

            # 結果をテキストに出力
        result_text = format(distance)
        self.widget.v_t_2.setPlainText(result_text)

    # 頂点減算スプリクト
    def clicked_get_distance_between_selected_vertices_3(self):

        # v_tとv_t_2のテキストを取得
        text1 = self.widget.v_t.toPlainText()
        text2 = self.widget.v_t_2.toPlainText()

        try:
            # テキストを数値に変換
            value1 = float(text1)
            value2 = float(text2)

            # 数値を引き算
            result_value = value1 - value2

            result_text = format(result_value)
        except ValueError:
        # 数値変換に失敗した場合、エラーメッセージを出力
            result_text = "数値変換に失敗しました。"

        # 結果をv_t_3テキストに出力
        self.widget.v_t_3.setPlainText(result_text)



    #エッジ版その1
    def clicked_measure_selected_edges_length(self):
        # 選択されたエッジを取得
        selected_edges = pm.filterExpand(selectionMask=32)  # selectionMask=32 はエッジ選択モード
        if not selected_edges:
            Warning_text = ("エッジを選択してください。")
            self.widget.v_e.setPlainText(Warning_text)
            return

        # 全てのエッジの長さの合計を保持する変数
        total_length = 0.0

        # 各エッジの長さを測定
        for edge in selected_edges:
            # エッジの頂点を取得
            vertices = pm.polyListComponentConversion(edge, fromEdge=True, toVertex=True)
            vertices = pm.ls(vertices, flatten=True)

            if len(vertices) != 2:
                Warning_text_2 = ("エッジを選択してください。")
                self.widget.v_e.setPlainText(Warning_text_2)
                continue

            # 頂点の位置を取得
            pos1 = pm.pointPosition(vertices[0], world=True)
            pos2 = pm.pointPosition(vertices[1], world=True)

            # 距離を計算
            distance = pm.dt.Vector(pos1).distanceTo(pos2)

            # 距離を合計に追加
            total_length += distance

            self.widget.v_e.setPlainText("{:.4f}".format(total_length))


    def clicked_measure_selected_edges_length_2(self):
        # 選択されたエッジを取得
        selected_edges = pm.filterExpand(selectionMask=32)  # selectionMask=32 はエッジ選択モード
        if not selected_edges:
            Warning_text = ("エッジを選択してください。")
            self.widget.v_e_2.setPlainText(Warning_text)
            return

        # 全てのエッジの長さの合計を保持する変数
        total_length = 0.0

        # 各エッジの長さを測定
        for edge in selected_edges:
            # エッジの頂点を取得
            vertices = pm.polyListComponentConversion(edge, fromEdge=True, toVertex=True)
            vertices = pm.ls(vertices, flatten=True)

            if len(vertices) != 2:
                Warning_text_2 = ("エッジを選択してください。")
                self.widget.v_e.setPlainText(Warning_text_2)
                continue

            # 頂点の位置を取得
            pos1 = pm.pointPosition(vertices[0], world=True)
            pos2 = pm.pointPosition(vertices[1], world=True)

            # 距離を計算
            distance = pm.dt.Vector(pos1).distanceTo(pos2)

            # 距離を合計に追加
            total_length += distance

            self.widget.v_e_2.setPlainText("{:.4f}".format(total_length))

    #エッジ減算スプリクト
    def clicked_measure_selected_edges_length_3(self):

        # v_tとv_t_2のテキストを取得
        text1 = self.widget.v_e.toPlainText()
        text2 = self.widget.v_e_2.toPlainText()

        try:
            # テキストを数値に変換
            value1 = float(text1)
            value2 = float(text2)

            # 数値を引き算
            result_value = value1 - value2

            result_text = format(result_value)
        except ValueError:
        # 数値変換に失敗した場合、エラーメッセージを出力
            result_text = "数値変換に失敗しました。"

        # 結果をv_e_3テキストに出力
        self.widget.v_e_3.setPlainText(result_text)


    def clicked_bust_cup_measurement(self):

        # v_e_cpのテキストを取得
        text1 = self.widget.v_e_3.toPlainText()

        try:
            # テキストを数値に変換
            top_under = float(text1)

            # カップサイズの差分と対応するカップ
            cup_sizes = [
                (5.0, "AAA"),
                (7.5, "AA"),
                (10.0, "A"),
                (12.5, "B"),
                (15.0, "C"),
                (17.5, "D"),
                (20.0, "E"),
                (22.5, "F"),
                (25.0, "G"),
                (27.5, "H"),
                (30.0, "I"),
                (32.5, "J"),
            ]

            # カップサイズを決定
            cup_size = "J以上"
            for size in cup_sizes:
                if top_under <= size[0]:
                    cup_size = size[1]
                    break

            # 結果をv_e_cpテキストに出力
            self.widget.v_e_cp.setPlainText(cup_size)

        except ValueError:
            self.widget.v_e_cp.setPlainText("入力が不正です。数値を入力してください。")




    #テキスト削除
    def clicked_cl(self):

        # テキスト削除
        self.widget.v_t.setPlainText("")
        self.widget.v_t_2.setPlainText("")
        self.widget.v_t_3.setPlainText("")

        self.widget.v_e.setPlainText("")
        self.widget.v_e_2.setPlainText("")
        self.widget.v_e_3.setPlainText("")
        self.widget.v_e_cp.setPlainText("")

# 問題が発生したら使用する
#win = MeasureWindow()
#win.show()
