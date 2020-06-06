# Splitswise High Level Desgin

### Reqiurements
As described in README.md

### Estimations (Scale)
This app at a time could host 10-100 Million users each user can have around
avg 2 expenses shared with average of 3 users per day
So in a year we can no.of expenses per user can grow to:
2*3*365 =  2190 expenses

This combining with total user base , so there will be total of:
``2190*100*10^6=2.2*10^8`` expenses \
Each expense (at minimum) will hold a float data-> 4 byte, int data -> 4 byte and
string data(avg) -> 6 bytes \
So total memory consumption in a year:  
``
(6+4+4=14)*2.2*10^8 bytes => 2.9GB
``\
Without loss of generality we can safely assume read:write ration of 5:1 \
Read operation -> Getting Balances \
Write operation -> Adding Expense,Add user etc.

## Tradeoffs and Architecture

- We wouldn't want user settle with other user with a wrong balance
- Emphasis would be on consistency rather than availibily
- Given the size of data and available systems are available with 1TB storage
One or two machines should be sufficient, however as expense activity will
increase, this assumption may not hold true
- User are mostly going to be local when adding expenses. In that case it make
sense to do data sharding on basis of user's geolocation. This will improve
read latency 
- While updating the balance sheet, care must taken regarding simultaneous
writes so that it doesn't lead to inconsistency in user balance sheet. One
can use a queue to manage this expense addition and balance sheet updation


