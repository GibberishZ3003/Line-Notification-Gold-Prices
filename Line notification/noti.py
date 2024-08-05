import requests

def send_line_notify(message):
    url = "https://notify-api.line.me/api/notify"
    token = "YOUR_TOKEN"
    header = {'Content-Type': 'application/x-www-form-urlencoded','Authorization': 'Bearer ' + token}

    response = requests.post(url , headers=header , data=message)
    if response.status_code == 200:
        print("Success")
    else:
        print("Error")

price = 0
while True:
    url = 'https://api.chnwt.dev/thai-gold-api/latest'
    res = requests.get(url)
    data = res.json()

    day = data['response']['date']
    times = data['response']['update_time']

    gold_buy = data['response']['price']['gold']['buy']
    gold_sell = data['response']['price']['gold']['sell']
    goldbar_buy = data['response']['price']['gold_bar']['buy']
    goldbar_sell = data['response']['price']['gold_bar']['sell']

    chg = data['response']['price']['change']['compare_previous']
    chg_y = data['response']['price']['change']['compare_yesterday']
    
    last = gold_buy
    if price != last:
        msg = f" \n"\
        f"-------------------- \n"\
        f"{day} [ {times} ] \n"\
        f"-------------------- \n"\
        f"ทองคำแท่ง : \n"\
        f"รับชื้อ : {goldbar_buy} \n"\
        f"ขายออก : {goldbar_sell} \n"\
        f"-------------------- \n"\
        f"ทองรูปพรรณ : \n"\
        f"รับชื้อ : {gold_buy} \n"\
        f"ขายออก : {gold_sell} \n"\
        f"-------------------- \n"\
        f"ราคาทองเทียบกับ(เมื่อวาน) : {chg_y} \n"\
        f"ราคาทองเทียบกับ(ก่อนหน้า) : {chg} \n"\
        f"--------------------"

        message = {'message': msg}
        send_line_notify(message)
        price = last