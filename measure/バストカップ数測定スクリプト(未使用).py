import pymel.core as pm

def calc_bra_size(height, bust, waist, is_first_option_checked):
    # 表示用配列
    type_ = [
        "AAAカップ未満(無乳)", "AAAカップ(微乳)", "AAカップ(微乳)", "Aカップ(微乳)",
        "Bカップ(普乳)", "Cカップ(普乳)", "Dカップ(適乳)", "Eカップ(巨乳)", "Fカップ(巨乳)",
        "Gカップ(爆乳)", "Hカップ(爆乳)", "Iカップ(爆乳)", "Jカップ(魔乳)", "Kカップ(魔乳)",
        "Lカップ(魔乳)", "Mカップ(魔乳)", "Nカップ(超乳)", "Oカップ(超乳)", "Pカップ(超乳)",
        "Pカップ以上(神乳)", "身長が未入力、または不正な値です", "バストが未入力、または不正な値です", "ウエストが未入力、または不正な値です"
    ]
    type2 = [
        "AAA未満", "AAA", "AA", "Ａ", "Ｂ", "Ｃ", "Ｄ", "Ｅ", "Ｆ", "Ｇ", "Ｈ", "Ｉ", "Ｊ",
        "Ｋ", "Ｌ", "Ｍ", "Ｎ", "Ｏ", "Ｐ", "Ｐ以上"
    ]
    
    # 初期化
    difference = risou_bust = risou_waist = risou_hip = num = u_bust = advice = result_num = 0
    
    # バストサイズ計算中
    if is_first_option_checked:
        difference = (bust - (height * 0.54)) + (((height * 0.38) - waist) * 0.73) + ((height - 158.8) * 0.1087)
    else:
        difference = (bust - (height * 0.54)) + (((height * 0.38) - waist) * 0.73) + ((height - 158.8) * 0.3261)
    
    risou_bust = (height * 0.54), (bust - height * 0.54)
    risou_waist = (height * 0.38), (waist - height * 0.38)
    risou_hip = height * 0.54
    
    if height <= 0.0:
        num = 20
    elif bust <= 0.0:
        num = 21
    elif waist <= 0.0:
        num = 22
    elif difference < -13.75:
        num = 0
    elif difference < -11.25:
        num = 1
    elif difference < -8.75:
        num = 2
    elif difference < -6.25:
        num = 3
    elif difference < -3.75:
        num = 4
    elif difference < -1.25:
        num = 5
    elif difference < 1.25:
        num = 6
    elif difference < 3.75:
        num = 7
    elif difference < 6.25:
        num = 8
    elif difference < 8.75:
        num = 9
    elif difference < 11.25:
        num = 10
    elif difference < 13.75:
        num = 11
    elif difference < 16.25:
        num = 12
    elif difference < 18.75:
        num = 13
    elif difference < 21.25:
        num = 14
    elif difference < 23.75:
        num = 15
    elif difference < 26.25:
        num = 16
    elif difference < 28.75:
        num = 17
    elif difference < 31.25:
        num = 18
    else:
        num = 19
    
    # アンダーバストの値を計算
    if num < 20:
        u_bust = bust - (difference + 17.5)
    else:
        u_bust = ""
    
    # アドバイスのテキスト作成
    if num < 6:
        j = (-difference - 1.25) % 2.5
    elif num == 6 and difference < 0:
        j = -difference + 1.25
    elif num == 6 and difference > 0:
        j = 1.25 - difference
    else:
        j = 2.5 - ((difference - 1.25) % 2.5)
    
    if num < 19:
        advice = "{}になるためには、あとバストをプラス{:.2f}cm またはウェストをマイナス{:.2f}cm".format(type_[num + 1], j, j / 0.73)
    else:
        advice = ""
    
    # 市販用ブラ計測
    buy_cup = "ゆったりしたのが好みならば……{}({}), きつくてもバストを大きくみせたいならば……{}({})".format(
        type2[calc2(u_bust + (5 - (u_bust % 5)) / 2)], u_bust + (5 - (u_bust % 5)),
        type2[calc2(u_bust - ((u_bust % 5) / 2))], u_bust - (u_bust % 5)
    )
    
    ii = [0] * 6
    jj = [""] * 6
    
    ii[0] = ((5 - (u_bust % 5)) / 2) + abs(bust - ((u_bust + (5 - (u_bust % 5)) / 2) + 2.5 + (calc2(u_bust + (5 - (u_bust % 5)) / 2) * 2.5)))
    jj[0] = "{}({})".format(type2[calc2(u_bust + (5 - (u_bust % 5)) / 2)], u_bust + (5 - (u_bust % 5)))
    ii[1] = ((5 - (u_bust % 5)) / 2) + abs(bust - ((u_bust + (5 - (u_bust % 5)) / 2) + 2.5 + ((calc2(u_bust + (5 - (u_bust % 5)) / 2) + 1) * 2.5)))
    jj[1] = "{}({})".format(type2[calc2(u_bust + (5 - (u_bust % 5)) / 2) + 1], u_bust + (5 - (u_bust % 5)))
    ii[2] = ((5 - (u_bust % 5)) / 2) + abs(bust - ((u_bust + (5 - (u_bust % 5)) / 2) + 2.5 + ((calc2(u_bust + (5 - (u_bust % 5)) / 2) - 1) * 2.5)))
    jj[2] = "{}({})".format(type2[calc2(u_bust + (5 - (u_bust % 5)) / 2) - 1], u_bust + (5 - (u_bust % 5)))
    ii[3] = ((u_bust % 5) / 2) + abs(bust - ((u_bust - (u_bust % 5) / 2) + (calc2(u_bust - ((u_bust % 5)) / 2) * 2.5 + 2.5)))
    jj[3] = "{}({})".format(type2[calc2(u_bust - ((u_bust % 5)) / 2)], u_bust - (u_bust % 5))
    ii[4] = ((u_bust % 5) / 2) + abs(bust - ((u_bust - (u_bust % 5) / 2) + ((calc2(u_bust - ((u_bust % 5)) / 2) + 1) * 2.5 + 2.5)))
    jj[4] = "{}({})".format(type2[calc2(u_bust - ((u_bust % 5)) / 2) + 1], u_bust - (u_bust % 5))
    ii[5] = ((u_bust % 5) / 2) + abs(bust - ((u_bust - (u_bust % 5) / 2) + ((calc2(u_bust - ((u_bust % 5)) / 2) - 1) * 2.5 + 2.5)))
    jj[5] = "{}({})".format(type2[calc2(u_bust - ((u_bust % 5)) / 2) - 1], u_bust - (u_bust % 5))

    for i in range(6):
        for j in range(i, 6):
            if ii[i] > ii[j]:
                ii[i], ii[j] = ii[j], ii[i]
                jj[i], jj[j] = jj[j], jj[i]

    if -13.75 < difference < 31.25:
        buy_cup += "、最もフィットするのは……{}".format(jj[0])

    if -13.75 < difference < 31.25:
        buy_cup2 = "{}, {}, {}, {}, {}".format(jj[0], jj[1], jj[2], jj[3], jj[4])
    else:
        buy_cup2 = ""

    result = {
        "u_bust": u_bust,
        "type": type_[num],
        "advice": advice,
        "buy_cup": buy_cup,
        "buy_cup2": buy_cup2,
        "risou_bust": risou_bust,
        "risou_waist": risou_waist,
        "risou_hip": risou_hip
    }

    return result


def calc2(hikisu):
    if (bust - hikisu) < 3.75:
        return 0
    elif (bust - hikisu) < 6.25:
        return 1
    elif (bust - hikisu) < 8.75:
        return 2
    elif (bust - hikisu) < 11.25:
        return 3
    elif (bust - hikisu) < 13.75:
        return 4
    elif (bust - hikisu) < 16.25:
        return 5
    elif (bust - hikisu) < 18.75:
        return 6
    elif (bust - hikisu) < 21.25:
        return 7
    elif (bust - hikisu) < 23.75:
        return 8
    elif (bust - hikisu) < 26.25:
        return 9
    elif (bust - hikisu) < 28.75:
        return 10
    elif (bust - hikisu) < 31.25:
        return 11
    elif (bust - hikisu) < 33.75:
        return 12
    elif (bust - hikisu) < 36.25:
        return 13
    elif (bust - hikisu) < 38.75:
        return 14
    elif (bust - hikisu) < 41.25:
        return 15
    elif (bust - hikisu) < 43.75:
        return 16
    elif (bust - hikisu) < 46.25:
        return 17
    elif (bust - hikisu) < 48.75:
        return 18
    else:
        return 19

# 使用例
height = 160.0  # 身長(cm)
bust = 85.0     # バスト(cm)
waist = 60.0    # ウエスト(cm)
is_first_option_checked = True  # 第一のオプションがチェックされているか

result = calc_bra_size(height, bust, waist, is_first_option_checked)
pm.mel.eval('print("{}")'.format(result))
