insert into CaptainConsole_users(password,avatar,nickname,email)
values("password1",1,"nickname","nickname@gmail.com");
insert into CaptainConsole_users(password,avatar,nickname,email)
values("password2",2,"nickname1","nickname1@gmail.com");
insert into CaptainConsole_users(password,avatar,nickname,email)
values("password3",3,"nickname2","nickname2@gmail.com");

insert into CaptainConsole_shoppingchart(userID,productIDs)
values (1,1);
insert into CaptainConsole_shoppingchart(userID,productIDs)
values (2,2);
insert into CaptainConsole_shoppingchart(userID,productIDs)
values (3,3);


insert into CaptainConsole_searchhistory(keywordIDs,search,datetime)
values (1,"ps2","2002-05-07T12:28");
insert into CaptainConsole_searchhistory(keywordIDs,search,datetime)
values (2,"ps3","2020-05-07T12:28");
insert into CaptainConsole_searchhistory(keywordIDs,search,datetime)
values (3,"ps4","2020-05-07T12:29");


insert into CaptainConsole_reviews(productID,rating,review)
values(1,5,"Alveg geggjuð vara vá hvað ég ér sáttur/sátt/sætt ahahhahaaha");
insert into CaptainConsole_reviews(productID,rating,review)
values(2,5,"Alveg geggjuð vara vá hvað ég ér sáttur/sátt/sætt ahahhahaaha");
insert into CaptainConsole_reviews(productID,rating,review)
values(3,4,"Alveg geggjuð vara vá hvað ég ér sáttur/sátt/sætt ahahhahaaha");


insert into CaptainConsole_products(name,price,description,manufacturer,photoID)
values("ps2",200,"The PlayStation 2 (PS2) is a dedicated machine – ''games console'' – for playing video games, which connects to your television. The third in Sony''s extremely successful series of game consoles, the PlayStation 2 was released in 2000.",Sony,2);
insert into CaptainConsole_products(name,price,description,manufacturer,photoID)
values("ps3",200,"The PlayStation 3 (PS3) is a dedicated machine – ''games console'' – for playing video games, which connects to your television. The third in Sony''s extremely successful series of game consoles, the PlayStation 3 was released in 2007.",Sony,2);
insert into CaptainConsole_products(name,price,description,manufacturer,photoID)
values("ps4",200,"The PlayStation 4 (PS4) is a dedicated machine – ''games console'' – for playing video games, which connects to your television. The fourth in Sony''s extremely successful series of game consoles, the PlayStation 4 was released in 2013.",Sony,3);


insert into CaptainConsole_orders(shoppingCartID,name,price,amount,additionalInfo,address,zipcode,city,country)
values (1,ps2,200,1,"","smárarimi 1000",112,"Reykjavik","Iceland");
insert into CaptainConsole_orders(shoppingCartID,name,price,amount,additionalInfo,address,zipcode,city,country)
values (2,ps3,200,1,"","smárarimi 13",112,"Reykjavik","Iceland");
insert into CaptainConsole_orders(shoppingCartID,name,price,amount,additionalInfo,address,zipcode,city,country)
values (3,ps4,200,1,"","smárarimi 69",112,"Reykjavik","Iceland");






