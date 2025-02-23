import random

# ルーレットをマーチンゲール法でシミュレーションし、適切な資金と掛け金のバランスを確認する
def martingale_simulation(initial_balance, initial_bet, num_rounds):
    balance = initial_balance
    bet = initial_bet
    for _ in range(num_rounds):
        if balance < bet:
            print("No money...") # 資金が尽きて掛金がなくなりました
            break
        # 勝率が最も高い（負ける可能性が最も低い）赤か黒のどちらか一方にずっと賭け続けることを想定
        win = random.random() < 18 / 37 # アメリカンルーレットは分母を38に変更
        if win:
            balance += bet
            bet = initial_bet # 買った時は初期の掛け金に戻す
        else:
            balance -= bet
            bet *= 2 # 負けた時は賭け金を倍にする
        print(f"資金: ${balance}, 賭金: ${bet}")

    return balance

# 引数の資金と賭け金とラウンド数を変えてシミュレーションを実行
final_balance = martingale_simulation(initial_balance=300, initial_bet=10, num_rounds=20)
print(f"最終残高: ${final_balance}")