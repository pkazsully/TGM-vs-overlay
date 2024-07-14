import requests

data = {
    "match":{
        "firstTo":2
    },
    "players":[
        {
            "username":"pkaz",
            "pfp":"https://www.gravatar.com/avatar/94b581a0f4fad5a5d70c5e5e257a84e4?s=250",
            "rank":"A",
            "country":"United States",
            "flag_img":"https://cdn.britannica.com/33/4833-004-828A9A84/Flag-United-States-of-America.jpg",
            "since":"2023-09-24",
            "stats":[
                [0, 0, 0],
                [999, 999, 100],
                [99, 99, 50],
                [0,0,1],
                [0,0,0]
            ],
            "rival":"Hikarus"
        },
        {
            "username":"colour_thief",
            "pfp":"https://www.gravatar.com/avatar/28ae93459bcbfe67df80f3ac082fcac8?s=250",
            "rank":"A",
            "country":"Canada",
            "flag_img":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTyiYirHiGCymBqqOjCzm5A71AuealRFxjiUA&s",
            "since":"2021-01-18",
            "stats":[
                [9999, 9999, 100],
                [999, 999, 100],
                [99, 99, 50],
                [0,0,1],
                [9999,9999,100]
            ],
            "rival":"DeHackEd"
        }
    ]
}

data2={
    "match":{"firstTo":5},
    "players":[
        {
            "username":"d4nin3u","pfp":"https://www.gravatar.com/avatar/f3a4a0005ae05e09a66c77bce56b166c?s=250","rank":"B","country":"United Kingdom","flag_img":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvwtwkduPTWWCLfVE37c1vlKoN7GrpUKukM98EgKNprg&s",
            "since":"2021-01-22","stats":[[0, 0, 0],[999, 999, 100],[99, 99, 50],[0,0,1],[0,0,0]],"rival":"colour_thief"
        },
        {
            "username":"Hikarus","pfp":"https://www.gravatar.com/avatar/8be848ad99bda337ad90dfc3185c5a73?s=250","rank":"A","country":"Argentina","flag_img":"https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Flag_of_Argentina.svg/1200px-Flag_of_Argentina.svg.png",
            "since":"2020-12-19","stats":[[9999, 9999, 100],[999, 999, 100],[99, 99, 50],[0,0,1],[9999,9999,100]],"rival":"idk everyone"
        }
    ]
}

scores = {"p1":"2", "p2":"1"}


while(True):
    temp = input("1 to hide, 2 to show, 3 to update score, 4 to update data, 5 to update data to data2, 6 to clear data: ")
    if temp == "1":
        url = "http://127.0.0.1:5000/hide"
        response = requests.post(url)

        # Check the response from the server
        if response.status_code == 200:
            print("Data sent successfully")
        else:
            print("Error:", response.text) 
    elif temp =="2":
        url = "http://127.0.0.1:5000/show"
        response = requests.post(url)

        # Check the response from the server
        if response.status_code == 200:
            print("Data sent successfully")
        else:
            print("Error:", response.text) 
    elif temp == "3":
        p1 = input("Player 1 Score: ")
        p2 = input("Player 2 Score ")
        url = "http://127.0.0.1:5000/update_scores"
        response = requests.post(url, json={"p1":p1, "p2":p2})

        # Check the response from the server
        if response.status_code == 200:
            print("Data sent successfully")
        else:
            print("Error:", response.text) 
    elif temp == "4":
        url = "http://127.0.0.1:5000/update_data"
        response = requests.post(url, json=data)

        # Check the response from the server
        if response.status_code == 200:
            print("Data sent successfully")
        else:
            print("Error:", response.text) 
        
    elif temp == '5':
        url = "http://127.0.0.1:5000/update_data"
        response = requests.post(url, json=data2)

        # Check the response from the server
        if response.status_code == 200:
            print("Data sent successfully")
        else:
            print("Error:", response.text) 
    elif temp == '6':
        url = "http://127.0.0.1:5000/clear"
        response = requests.post(url)

        # Check the response from the server
        if response.status_code == 200:
            print("Data sent successfully")
        else:
            print("Error:", response.text) 



url = "http://127.0.0.1:5000/update_data"
response = requests.post(url, json=data)

# Check the response from the server
if response.status_code == 200:
    print("Data sent successfully")
else:
    print("Error:", response.text) 

""" url = "http://127.0.0.1:5000/update_scores"
response = requests.post(url, json=scores)

# Check the response from the server
if response.status_code == 200:
    print("Data sent successfully")
else:
    print("Error:", response.text)
 """
