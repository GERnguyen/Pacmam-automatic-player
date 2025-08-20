import random

def dating_recommendation(budget, personality, interest, goal, nervous, weather):

    if budget == 1 and weather == 1:
        suggestion = "một buổi picnic ở công viên 🌳"
    elif budget == 2 and interest == 1:
        suggestion = "một buổi xem phim ấm áp 🎬"
    elif budget == 3 and interest == 2:
        suggestion = "một bữa ăn sang trọng ở nhà hàng 🍷"
    elif personality == 3:
        suggestion = "đi dạo ở các nơi chưa từng đến 🗝️"
    elif personality == 4:
        suggestion = "một bữa ăn tối vào lúc hoàng hôn 🌅"
    elif personality == 1 and goal == 2:
        suggestion = "một buổi hẹn hò ở quán cafe nhẹ nhàng ☕"
    elif personality == 2 and goal == 1:
        suggestion = "một buổi hẹn hò ở show diễn nhạc nhỏ 💃"
    elif nervous == 1:
        suggestion = "một buổi hẹn hò ở quán quen của bạn để cảm thấy thoải mái "
    else:
        suggestion = "một buổi đi bộ cùng nhau 🚶‍♂️🚶‍♀️"


    score = random.randint(50, 90)  
    if goal == 2:
        score += 5
    if nervous == 1:
        score -= 5
    if weather == 2:
        score -= 10
    score = max(0, min(100, score))  


    result = f"🔮 Bạn nên có {suggestion}!"
    result += f"\n💘 Tỉ lệ thành công: {score}%"

    return result



print("=== Dating Recommendation Expert System ===")

budget = input("Có bao nhiêu tiền? (1.Ít / 2.Vừa đủ / 3.Nhiều) ").strip()
personality = input("Cô ấy là mẫu người thế nào? (1.Hướng nội / 2.Hướng ngoại / 3.Tò mò / 4.Lãng mạng): ").strip()
interest = input("Sở thích của cô ấy (1.Phim / 2.Đồ ăn / 3.Âm nhạc / 4.Mèo / 5.Sách / 6.Khác): ").strip()
goal = input("Mục tiêu hẹn hò (1.Vui vẻ / 2.Nghiêm túc): ").strip()
nervous = input("Bạn có lo lắng không? (1.Có / 2.Không hề): ").strip()
weather = input("Thời tiết hôm nay (1.Đẹp / 2.Mưa / 3.Lạnh): ").strip()

print("\n" + dating_recommendation(budget, personality, interest, goal, nervous, weather))
