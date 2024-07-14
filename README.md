# TGM Tourney Overlay

## What is included

* server.py is the backend for the overlay

* requirements.txt is the dependencies for server.py

* the static and templates directories contain all of the frontend stuff

* sampledata.json is an example data json which I was using for testing

* demo.py is a basic script for testing the api endpoints

## How to use

After installing dependencies with requirements.txt, run server.py. You can check if it is working correctly by opening `http://127.0.0.1:{port}/` (default port is 5000) in a browser if you'd like.

Next in obs, make a browser source with the same url (`http://127.0.0.1:{port}/`). Set the width and height to whatever reasonable 16:9 resolution you want, and leave on the custom css that enables transparency.

Now by making post requests to that url at the different endpoints listed below, you should be able to update the overlay.

## API Endpoints

Here are all the server api endpoints, what they expect, and what they do

### POST /update_data

expects the big json of player data

updates the interface with the data it's given, resets scores, and shows the overlay if it was previously hidden

### POST /update_scores

expects a json of form {"p1": num, "p2": num}

updates the scores as given

### POST /hide

expects nothing (as do the rest)

hides the overlay if it was shown, otherwise does nothing

### POST /show

shows the overlay if it was hidden, otherwise does nothing

### POST /clear

effectively update_data, but with blank player information

### GET /

returns the interface

## Sample JSON

Wait I just realized I was already going to include this in the repo anyway. Whatever. Its here now too. Here is a sample of the aforementioned big json of player data:

```json
{
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
```

The stats table is formatted such that `stats[0]` is A tier, `stats[1]` is B tier and so on, with the exception of `stats[4]` being the other player. Then for the inner arrays, `stats[x][0]` is wins, `stats[x][1]` is losses, and `stats[x][2]` is the percentage

## Other Notes

If you need to change the port that the webserver runs on, it is on line 4 in server.py
