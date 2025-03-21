import streamlit as st

# チャットボットの応答辞書
responses = {
    "調子はどう？": "元気だよ！今日も頑張ってるよ〜 😊",
    "お腹すいた": "私もお腹すいたな〜 🍙 何か食べたいね！",
    "疲れた": "お疲れさま！少し休憩した方がいいかも☕",
    "バイバイ": "また会おうね！良い1日を！👋",
    "おはよう": "おはよう！今日も素敵な1日になりますように✨",
    "暇": "退屈なの？私と話そう！何か面白い話題はある？🎵",
    "眠い": "私も眠くなってきた...（´･ω･`）ｽﾔｧ",
    "天気": "外を見る余裕がないんだ... でも一緒に天気の話はできるよ！☀️"
}

def main():
    st.title("🤖 フレンドリーチャットボット")
    
    # セッション状態の初期化
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # チャット履歴の表示
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # 定型文から選択
    user_input = st.selectbox("話しかけてみよう：", list(responses.keys()))

    # 送信ボタン
    if st.button("送信", key="send") and user_input:
        # ユーザーの入力を表示
        with st.chat_message("user"):
            st.write(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        # ボットの応答を表示
        with st.chat_message("assistant"):
            response = responses[user_input]
            st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

    # リセットボタン
    if st.button("会話をリセット"):
        st.session_state.messages = []
        st.rerun()

if __name__ == "__main__":
    main()