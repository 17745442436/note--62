# 简易笔记工具
def add_note(notes, content):
    notes.append(content)
    print("dev分支：笔记添加成功✅")

def show_notes(notes):
    if len(notes) == 0:
        print("暂无笔记")
    else:
        for i, n in enumerate(notes):
            print(f"{i+1}. {n}")

if __name__ == "__main__":
    note_list = []
    add_note(note_list, "这是我的第一条测试笔记")
    show_notes(note_list)
