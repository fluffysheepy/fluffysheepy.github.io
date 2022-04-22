from datetime import datetime

comment1 = {
    "Text" : "What time are you going?",
    "Name": "Charlie",
    "Username" : "chucky",
    "Picture" : "charlie_profile.png",
    "DateTime" : datetime(2021, 7, 1, 18, 0, 0),
}

comment2 = {
    "Text" : "I'm going to go at 7 tonight!",
    "Name": "Melba",
    "Username" : "melba",
    "Picture" : "melba_profile.png",
    "DateTime" : datetime(2021, 7, 1, 18, 30, 0),
}


comment3 = {
    "Text" : "You bet!  I love naps.",
    "Name": "Melba",
    "Username" : "melba",
    "Picture" : "melba_profile.png",
    "DateTime" : datetime(2021, 6, 29, 9, 30, 0),
}


post1 = {
    "PostId" : 1,
    "Text": "I can't wait to go to the park today",
    "Name": "Melba",
    "Username" : "melba",
    "Likes": ["charlie"],
    "Comments" : [comment1, comment2],
    "DateTime" : datetime(2021, 7, 1, 17, 0, 0),
    "Picture" : "melba_profile.png"
}

post2 = {
    "PostId" : 2,
    "Text": "I could really use a treat right now",
    "Name": "Melba",
    "Username" : "melba",
    "Likes": [],
    "Comments" : [],
    "DateTime" : datetime(2021, 6, 30, 12, 30, 0),
    "Picture" : "melba_profile.png"
}

post3 = {
    "PostId" : 3,
    "Text": "Arent' naps the best?",
    "Name": "Charlie",
    "Username" : "chucky",
    "Likes": ["melba"],
    "Comments" : [comment3],
    "DateTime" : datetime(2021, 6, 29, 9, 0, 0),
    "Picture" : "charlie_profile.png"
}

test_posts = {
    1 : post1,
    2 : post2,
    3 : post3
}

melba_posts = {
    1: post1,
    2 : post2
}

chucky_posts = {
    3: post3
}

melba = {
    "ProfileId" : "melba",
    "About" : "I am Melba! You can add me, but I need to ask Paul's permission first.",
    "Name": "Melba",
    "Username" : "melba",
    "Birthday" : datetime(2018, 6, 29, 9, 0, 0),
    "Picture" : "melba_profile.png",
    "Posts" : melba_posts
}

chucky = {
    "ProfileId" : "chucky",
    "About" : "I am Charlie! Living my best nap life!",
    "Name": "Charlie",
    "Username" : "chucky",
    "Birthday" : datetime(2018, 6, 29, 9, 0, 0),
    "Picture" : "charlie_profile.png",
    "Posts" : chucky_posts

}
profiles = {
    "melba" : melba,
    "chucky" : chucky
}
