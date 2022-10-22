const int lim = 

bool prime[lim + 10];
vector <int> pNum, pf, times;

void sieve()
{
    mem(prime, true, sizeof(prime));
    prime[0] = prime[1] = false;
    for(int i = 2; (ll)i * i <= lim; i++)
    {
        if(prime[i])
        {
            for(int j = i * i; j <= lim; j += i)
            {
                prime[j] = false;
            }
        }
    }

    for(int i = 2; i <= lim; i++)
    {
        if(prime[i])
            pNum.push_back(i);
    }
}

void fact(ll n)
{
    for(int i = 0; i < pNum.size(); i++)
    {
        ll p = pNum[i];

        if(p * p > n)
            break;
            

        int cnt = 0;
        if(n % p == 0)
        {
            while(n % p == 0)
            {
                n /= p;
                cnt++;
            }
            pf.push_back(p);
            times.push_back(cnt);
        }
    }
    if(n > 1)
    {
        pf.push_back(n);
        times.push_back(1);
    }
}