import streamlit as st
import random
import styles
import time

st.set_page_config("开箱吧", "🎁")
styles.apply_styles()

# ============================初始化============================#
if "page" not in st.session_state:
    # ------ 箱子掉落物 ------ #
    st.session_state.junk = {
        0: "🔗古董版解压神器", 1: "🧿弹珠", 2: "🧨燃烧了的烟花棒", 3: "🔗古董版解压神器",
        4: "🧨燃烧了的烟花棒", 5: "🧨燃烧了的烟花棒", 6: "🧿弹珠", 7: "🕶电影墨镜",
        8: "⚾废弃的棒球", 9: "🧨燃烧了的烟花棒", 10: "🧨燃烧了的烟花棒", 11: "🔗古董版解压神器",
        12: "🧿弹珠", 13: "🧨燃烧了的烟花棒", 14: "🔗古董版解压神器", 15: "🧨燃烧了的烟花棒",
        16: "🧨燃烧了的烟花棒", 17: "🧿弹珠", 18: "🕶电影墨镜", 19: "⚾废弃的棒球",
        20: "🧨燃烧了的烟花棒", 21: "🕶电影墨镜", 22: "🥼西装", 23: "🧨燃烧了的烟花棒",
        24: "⚾废弃的棒球", 25: "🧿弹珠", 26: "🔗古董版解压神器", 27: "🥼西装",
        28: "🥼西装", 29: "🕶电影墨镜", 30: "🕶电影墨镜",
    }
    st.session_state.junior = {
        0: "🕶电影墨镜", 1: "🥼西装", 2: "🧨燃烧了的烟花棒", 3: "⚾废弃的棒球",
        4: "🧿弹珠", 5: "🔗古董版解压神器", 6: "🥼西装", 7: "🥼西装",
        8: "🧿弹珠", 9: "🕶电影墨镜", 10: "🕶电影墨镜", 11: "🧿弹珠",
        12: "🧨燃烧了的烟花棒", 13: "🔗古董版解压神器", 14: "🧨燃烧了的烟花棒", 15: "🧨燃烧了的烟花棒",
        16: "🧿弹珠", 17: "🕶电影墨镜", 18: "⚾废弃的棒球", 19: "🧨燃烧了的烟花棒",
        20: "🧨燃烧了的烟花棒", 21: "👓科技镜", 22: "🎀全新蝴蝶结", 23: "🧧红包",
        24: "🎟黄金票", 25: "🖼世界名画", 26: "🥽全新VR", 27: "🦺救生服",
        28: "👑镶金的皇冠", 29: "🎫来自外星的'身份证'", 30: "🧧红包",
    }
    st.session_state.medium = {
        0: "👓科技镜", 1: "🎀全新蝴蝶结", 2: "🧧红包", 3: "🎟黄金票",
        4: "🖼世界名画", 5: "🥽全新VR", 6: "🦺救生服", 7: "👑镶金的皇冠",
        8: "🎫来自外星的'身份证'", 9: "🧧红包", 10: "🎞录像带", 11: "🔗古董版解压神器",
        12: "🧿弹珠", 13: "🧨燃烧了的烟花棒", 14: "🔗古董版解压神器", 15: "🧨燃烧了的烟花棒",
        16: "🧨燃烧了的烟花棒", 17: "👓科技镜", 18: "🎀全新蝴蝶结", 19: "🧧红包",
        20: "🎟黄金票", 21: "🖼世界名画", 22: "🥽全新VR", 23: "🎮游戏机",
        24: "🎮游戏机", 25: "🧰古老的工作箱", 26: "🧰古老的工作箱", 27: "🧰古老的工作箱",
        28: "🎟黄金票", 29: "🖼世界名画", 30: "🥽全新VR",
    }
    st.session_state.advanced = {
        0: "🔗古董版解压神器", 1: "🧿弹珠", 2: "🧨燃烧了的烟花棒", 3: "🔗古董版解压神器",
        4: "🧨燃烧了的烟花棒", 5: "🧨燃烧了的烟花棒", 6: "🧿弹珠", 7: "🕶电影墨镜",
        8: "⚾废弃的棒球", 9: "🧨燃烧了的烟花棒", 10: "🎞录像带", 11: "🔗古董版解压神器",
        12: "🧿弹珠", 13: "🧨燃烧了的烟花棒", 14: "🔗古董版解压神器", 15: "🧨燃烧了的烟花棒",
        16: "🧨燃烧了的烟花棒", 17: "👓科技镜", 18: "🎀全新蝴蝶结", 19: "🧧红包",
        20: "🎟黄金票", 21: "👓科技镜", 22: "🎀全新蝴蝶结", 23: "🧧红包",
        24: "🎟黄金票", 25: "🖼世界名画", 26: "🥽全新VR", 27: "🦺救生服",
        28: "👑镶金的皇冠", 29: "🎫来自外星的'身份证'", 30: "🧧红包",
    }
    st.session_state.ultimate = {
        0: "💽李鹏诚的光盘", 1: "✨远古之心", 2: "💎来自北极的钻石", 3: "📜绝密文件",
        4: "📱控制板", 5: "🧭黄金指南针", 6: "💧来自北极的纯净水晶", 7: "💌淡黄的情书",
        8: "🥇马拉松奖牌", 9: "📹李国诚的相机", 10: "🎥李芝雅的播放器", 11: "🔗古董版解压神器",
        12: "🧿弹珠", 13: "🧨燃烧了的烟花棒", 14: "🔗古董版解压神器", 15: "🧨燃烧了的烟花棒",
        16: "🧨燃烧了的烟花棒", 17: "🧿弹珠", 18: "🕶电影墨镜", 19: "⚾废弃的棒球",
        20: "🧨燃烧了的烟花棒", 21: "👓科技镜", 22: "🎀全新蝴蝶结", 23: "🧧红包",
        24: "🎟黄金票", 25: "🖼世界名画", 26: "🥽全新VR", 27: "🦺救生服",
        28: "👑镶金的皇冠", 29: "🎫来自外星的'身份证'", 30: "🧧红包",
    }

    # ------ 玩家信息 ------ #
    st.session_state.EXP = 0
    st.session_state.money = 10000
    st.session_state.my_items = {
        "junk": 0, "junior": 0, "medium": 0, "advanced": 0, "ultimate": 0,
        "exp": 0, "else_items": [], "max": 10000
    }
    st.session_state.page = "start"
    st.session_state.Pulled = ""
    st.session_state.sell = []

    # 银行卡
    st.session_state.card = ["卡一"]
    st.session_state.bank_card = {}

    # ------ 物品价格表 ------ #
    st.session_state.item_prices = {
        "🔗古董版解压神器": 20, "🧿弹珠": 15, "🧨燃烧了的烟花棒": 10,
        "🕶电影墨镜": 50, "⚾废弃的棒球": 30, "🥼西装": 150,
        "👓科技镜": 200, "🎀全新蝴蝶结": 250, "🧧红包": 400,
        "🎟黄金票": 550, "🖼世界名画": 700, "🦺救生服": 900,
        "🎞录像带": 600, "🎮游戏机": 950, "🧰古老的工作箱": 1200, "🥽全新VR": 1500,
        "👑镶金的皇冠": 1000, "🎫来自外星的'身份证'": 1500, "💽李鹏诚的光盘": 58000, "✨远古之心": 3500,
        "💌淡黄的情书": 1800, "🥇马拉松奖牌": 2200, "💎来自北极的钻石": 3000, "📜绝密文件": 3500,
        "💧来自北极的纯净水晶": 4000, "📱控制板": 4500, "🧭黄金指南针": 5000, "📹李国诚的相机": 6500,
        "🎥李芝雅的播放器": 6000,
    }

# ==========================================================#


if st.session_state.my_items["exp"] >= 1000 and "卡二" not in st.session_state.card:
    st.session_state.card.append("卡二")
    st.session_state.my_items["max"] += 10000
if st.session_state.my_items["exp"] >= 2000 and "卡三" not in st.session_state.card:
    st.session_state.card.append("卡三")
    st.session_state.my_items["max"] += 20000
if st.session_state.my_items["exp"] >= 4000 and "卡四" not in st.session_state.card:
    st.session_state.card.append("卡四")
    st.session_state.my_items["max"] += 50000


# ============================ 初始页 ============================#
if st.session_state.page == "start":
    st.markdown(":yellow[开箱模拟器]")
    if st.button("开始", key="blue"):
        st.session_state.page = "game"
        st.rerun()
    if st.button("规则", key="green"):
        st.session_state.page = "Rule"
        st.rerun()

# ============================ 规则 ============================#
elif st.session_state.page == "Rule":
    st.markdown(":blue[只需要记住:买箱子,开箱子就行]")
    if st.button("开始", key="start_btn"):
        st.session_state.page = "game"
        st.rerun()

# ============================ 游戏主页 ============================#
elif st.session_state.page == "game":
    st.markdown("干些什么呢???")

    if st.button("买箱", key="green"):
        st.session_state.page = "buy"
        st.rerun()
    if st.button("开箱", key="green1"):
        st.session_state.page = "Unboxing"
        st.rerun()
    if st.button("银行", key="blue2"):
        st.session_state.page = "Bank"
    if st.button("我的", key="blue"):
        st.session_state.page = "Mine"
        st.rerun()

# ============================ 我的 ============================#
elif st.session_state.page == "Mine":
    junk_count = st.session_state.my_items["junk"]
    junior_count = st.session_state.my_items["junior"]
    medium_count = st.session_state.my_items["medium"]
    advanced_count = st.session_state.my_items["advanced"]
    ultimate_count = st.session_state.my_items["ultimate"]
    money = st.session_state.money

    st.markdown(
        f":green[你有 {junk_count} 个废物箱, {junior_count} 个低级箱, {medium_count} 个中级箱, {advanced_count} 个高级箱, {ultimate_count} 个终极箱。]")
    st.markdown(f":green[你还有 {money} 元]")

    if st.button("收藏馆", key="blue"):
        st.session_state.page = "Collection"
        st.rerun()

    if st.button("退出", key="blue1"):
        st.session_state.page = "game"
        st.rerun()

# ============================ 买箱子 ============================#
elif st.session_state.page == "buy":
    st.markdown(":blue[要哪种]")
    if st.button("退出", key="blue_exit_buy"):
        st.session_state.page = "game"
        st.rerun()

    if st.session_state.money >= 100:
        if st.button("废物箱子 100元", key="green"):
            st.session_state.money -= 100
            st.session_state.my_items["junk"] += 1
            st.rerun()

    if st.session_state.money >= 500:
        if st.button("低级箱子 500元", key="green1"):
            st.session_state.money -= 500
            st.session_state.my_items["junior"] += 1
            st.rerun()

    if st.session_state.money >= 800:
        if st.button("中级箱子 800元", key="green2"):
            st.session_state.money -= 800
            st.session_state.my_items["medium"] += 1
            st.rerun()

    if st.session_state.money >= 1200:
        if st.button("高级箱子 1200元", key="green3"):
            st.session_state.money -= 1200
            st.session_state.my_items["advanced"] += 1
            st.rerun()

    if st.session_state.money >= 2000:
        if st.button("终极箱子 2000元", key="green4"):
            st.session_state.money -= 2000
            st.session_state.my_items["ultimate"] += 1
            st.rerun()

# ============================ 开箱子 ============================#
elif st.session_state.page == "Unboxing":
    st.markdown(":blue[开什么呢???]")
    if st.button("退出", key="purple"):
        st.session_state.page = "game"
        st.rerun()

    if st.session_state.my_items["junk"] > 0:
        if st.button("开废物箱子", key="blue"):
            st.session_state.my_items["junk"] -= 1
            st.session_state.Pulled = st.session_state.junk[random.randint(0, 30)]
            st.session_state.my_items["else_items"].append(st.session_state.Pulled)
            st.session_state.page = "Reward"
            st.session_state.my_items["exp"] += 1
            st.rerun()

    if st.session_state.my_items["junior"] > 0:
        if st.button("开低级箱子", key="blue1"):
            st.session_state.my_items["junior"] -= 1
            st.session_state.Pulled = st.session_state.junior[random.randint(0, 30)]
            st.session_state.my_items["else_items"].append(st.session_state.Pulled)
            st.session_state.page = "Reward"
            st.session_state.my_items["exp"] += 4
            st.rerun()

    if st.session_state.my_items["medium"] > 0:
        if st.button("开中级箱子", key="blue2"):
            st.session_state.my_items["medium"] -= 1
            st.session_state.Pulled = st.session_state.medium[random.randint(0, 30)]
            st.session_state.my_items["else_items"].append(st.session_state.Pulled)
            st.session_state.page = "Reward"
            st.session_state.my_items["exp"] += 5
            st.rerun()

    if st.session_state.my_items["advanced"] > 0:
        if st.button("开高级箱子", key="blue3"):
            st.session_state.my_items["advanced"] -= 1
            st.session_state.Pulled = st.session_state.advanced[random.randint(0, 30)]
            st.session_state.my_items["else_items"].append(st.session_state.Pulled)
            st.session_state.page = "Reward"
            st.session_state.my_items["exp"] += 10
            st.rerun()

    if st.session_state.my_items["ultimate"] > 0:
        if st.button("开终极箱子", key="blue4"):
            st.session_state.my_items["ultimate"] -= 1
            st.session_state.Pulled = st.session_state.ultimate[random.randint(0, 30)]
            st.session_state.my_items["else_items"].append(st.session_state.Pulled)
            st.session_state.page = "Reward"
            st.session_state.my_items["exp"] += 15
            st.rerun()

elif st.session_state.page == "Reward":
    st.markdown(f"开出了 {st.session_state.Pulled}")
    if st.button("继续开箱子", key="green"):
        st.session_state.page = "Unboxing"
        st.rerun()

# ====== 收藏馆 ======#
elif st.session_state.page == "Collection":
    st.markdown("收藏的东西......")
    my_items_list = st.session_state.my_items["else_items"]
    st.markdown(f":orange[{my_items_list}]")
    if st.button("回到游戏", key="blue"):
        st.session_state.page = "game"
        st.rerun()
    if st.button("出售", key="green"):
        st.session_state.page = "Sell"
        st.rerun()

elif st.session_state.page == "Sell":
    st.markdown(":blue[出售什么???]")
    st.session_state.sell = st.multiselect("选择要出售的物品", st.session_state.my_items["else_items"],
                                           key="sell_multiselect")

    if st.button("出售", key="blue"):
        total_price = 0
        for item in st.session_state.sell:
            count = st.session_state.my_items["else_items"].count(item)
            price = st.session_state.item_prices.get(item, 0)
            total_price += price * count
        st.session_state.money += total_price
        st.session_state.my_items["else_items"] = [
            i for i in st.session_state.my_items["else_items"]
            if i not in st.session_state.sell
        ]
        st.success(f"出售成功！赚了 {total_price} 元")
        time.sleep(1)
        st.session_state.page = "game"
        st.rerun()

# ============================ 银行系统 ============================#
elif st.session_state.page == "Bank":
    st.markdown(":blue[银行职员:] :green[你需要什么服务]")
    if st.button("存款", key="green"):
        st.session_state.page = "Deposit"
        st.rerun()
    if st.button("取款", key="green1"):
        st.session_state.page = "Withdraw"
        st.rerun()
    if st.button("退出", key="green2"):
        st.session_state.page = "game"
        st.rerun()

elif st.session_state.page == "Deposit":
    st.markdown(":blue[银行职员:] :green[存多少???]")
    selected_card = st.selectbox("选择哪张卡", options=st.session_state.card, key="select_card_bank")
    deposit_type = st.selectbox(
        "存什么类型",
        options=["活期存款", "定期存款:整存整取", "定期存款:零存整取", "定期存款:存本取息", "定期存款:整存零取"],
        key="select_type_bank"
    )
    deposit_money = st.number_input(
        "金额",
        min_value=1.0,
        max_value=float(max(1, st.session_state.money)),
        step=1.0
    )

    if st.button("确定存款", key="confirm_deposit"):
        if selected_card in st.session_state.bank_card and len(st.session_state.bank_card[selected_card]) > 0:
            st.error("❌ 这张卡里已经有存款了！请先取款，或者换一张卡。")
        else:
            if st.session_state.money >= deposit_money:
                st.session_state.money -= deposit_money
                if deposit_type == "活期存款":
                    rate = 0.005
                else:
                    rate = 0.05

                if selected_card not in st.session_state.bank_card:
                    st.session_state.bank_card[selected_card] = []
                new_record = {
                    "id": int(time.time() * 1000),
                    "类型": deposit_type,
                    "本金": deposit_money,
                    "利率": rate,
                    "存款时间": time.time()
                }
                st.session_state.bank_card[selected_card].append(new_record)

                st.success(f"存款成功！存了 {deposit_money} 元（{deposit_type}）")
                time.sleep(1)
                st.session_state.page = "Bank"
                st.rerun()

    if st.button("退出存款机", key="blue"):
        st.session_state.page = "Bank"

elif st.session_state.page == "Withdraw":
    st.markdown(":blue[银行职员:] :green[你要取钱吗?]")
    if not st.session_state.bank_card:
        st.write("你还没有存款。")
    else:
        for card_name, records in st.session_state.bank_card.items():
            st.write(f"💳 **{card_name}**")
            for record in records:
                time_passed = time.time() - record["存款时间"]
                game_days = time_passed / 60.0
                interest = record["本金"] * record["利率"] * game_days

                # ================= 取款规则处理 =================#
                if record["类型"] == "活期存款":
                    st.info(f"【活期】本金：{record['本金']}元 | 存了 {game_days:.1f} 天 | 利息：{interest:.2f}元")
                    if st.button(f"取走本息 {record['本金'] + interest:.2f}元", key=f"wd_{record['id']}"):
                        st.session_state.money += record["本金"] + interest
                        records.remove(record)
                        st.rerun()
                elif "整存整取" in record["类型"]:
                    if game_days < 10:
                        st.warning(
                            f"【整存整取】未满期！已存 {game_days:.1f} 天，需存满 10 天。提前取只能拿回本金 {record['本金']}元。")
                        if st.button(f"强行取回本金 {record['本金']}元", key=f"wd_{record['id']}"):
                            st.session_state.money += record["本金"]
                            records.remove(record)
                            st.rerun()
                    else:
                        st.success(f"【整存整取】已满期！本金：{record['本金']}元 | 利息：{interest:.2f}元")
                        if st.button(f"取走本息 {record['本金'] + interest:.2f}元", key=f"wd_{record['id']}"):
                            st.session_state.money += record["本金"] + interest
                            records.remove(record)
                            st.rerun()
                elif "存本取息" in record["类型"]:
                    st.info(f"【存本取息】本金锁死：{record['本金']}元 | 累计可领利息：{interest:.2f}元")
                    if st.button(f"领取当前利息 {interest:.2f}元", key=f"wd_{record['id']}"):
                        st.session_state.money += interest
                        record["存款时间"] = time.time()
                        st.rerun()
                elif "零存整取" in record["类型"]:
                    st.info(f"【零存整取】本金：{record['本金']}元 | 存了 {game_days:.1f} 天 | 利息：{interest:.2f}元")
                    if st.button(f"取走本息 {record['本金'] + interest:.2f}元", key=f"wd_{record['id']}"):
                        st.session_state.money += record["本金"] + interest
                        records.remove(record)
                        st.rerun()
                elif "整存零取" in record["类型"]:
                    daily_limit = record["本金"] * 0.1
                    st.info(f"【整存零取】总本金：{record['本金']}元 | 每天限取：{daily_limit:.2f}元")
                    if st.button(f"取出今天份额 {daily_limit:.2f}元", key=f"wd_{record['id']}"):
                        st.session_state.money += daily_limit
                        record["本金"] -= daily_limit
                        if record["本金"] <= 0:
                            records.remove(record)
                        st.rerun()
    st.write("---")
    if st.button("退出银行", key="exit_bank"):
        st.session_state.page = "Bank"
        st.rerun()