import translate

def trans(action, sentence):
    source = "english"
    target = "chinese"
    if action == 1:
        pass
    elif action == 2:
        source = "chinese"
        target = "english"
    print(translate.trans(source, target, sentence))
    # pass

# def trans_en_to_cn:
#     pass

if __name__ == '__main__':
    action = input("你想使用什么功能？1 英译中； 2 中译英 \n")
    if (action == '1' or action == '2'):
        sentence = input("输入内容： \n")
        trans(int(action), sentence)

    # print("你选择了 " + action)
