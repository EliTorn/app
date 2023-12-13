import streamlit as st

# יצירת לוח משחק
board = [' '] * 9
current_player = 'X'


def display_board(board):
    for i in range(0, 9, 3):
        st.write(f"{board[i]} | {board[i + 1]} | {board[i + 2]}")
        if i < 6:
            st.write("---------")


def check_winner(board, player):
    # בדיקת שורות ועמודות
    for i in range(3):
        if all([board[i * 3 + j] == player for j in range(3)]) or \
                all([board[i + j * 3] == player for j in range(3)]):
            return True
    # בדיקת אלכסונים
    if all([board[i * 4] == player for i in range(3)]) or \
            all([board[i * 2 + 2] == player for i in range(1, 4)]):
        return True
    return False


# פונקציה לתור השחקן הנוכחי
def switch_player(player):
    return 'O' if player == 'X' else 'X'


# הצגת האפליקציה ב-Streamlit
st.title("משחק איקס עיגול עם שני שחקנים")
key = 0
# לולאת המשחק
while ' ' in board:
    display_board(board)

    # בחירת משתמש
    move = st.number_input(f"בחר מיקום ל-{current_player} (1-9)", 1, 9, step=1, key=f"move-{current_player} {key}")
    key += 1

    # בדיקה שהמקום פנוי
    if board[move - 1] == ' ':
        board[move - 1] = current_player
        if check_winner(board, current_player):
            st.success(f"{current_player} ניצח!")
            break
        current_player = switch_player(current_player)
    else:
        st.warning("המקום תפוס, בחר מקום אחר.")

    # המשחק מסתיים בתיקו אם אין מקומות פנויים נוספים
    if ' ' not in board:
        st.info("המשחק נגמר בתיקו.")
        break

# הצגת הלוח לאחר סיום המשחק
display_board(board)
