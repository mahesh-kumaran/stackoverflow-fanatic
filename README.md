
# Claim your Fanatic Badge  ⭐
#### For the love of collecting Stackoverflow Gold Badges ❤️, 

To collect Stackoverflow badges like __fanatic__, A user must log in to the site for 100 consecutive days.  
I was able to cross the halfway mark, I missed it around __62__ days.  
So just came up with a script and hosted it on a VM !!  
Run this script and collect yours too !  

Before running the script , set the following ```env```  values, 

```
export STACKOVERFLOW_EMAIL = <your_email>
export STACKOVERFLOW_PASSWORD = <your_password>
```


To containerize and run any where you like , use the ```Dockerfile```

```
docker build -t stackoverflow_fanatic .
docker run --name=fanatic_container -e PYTHONUNBUFFERED=0 -d stackoverflow_fanatic
```



Bonus: At 30-day mark you get a silver badge: ⚪ __Enthusiast__  