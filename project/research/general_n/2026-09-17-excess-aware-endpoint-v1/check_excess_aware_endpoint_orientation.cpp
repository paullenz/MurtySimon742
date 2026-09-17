// Independent arithmetic implementation of the strict excess-aware profile.
#include <bits/stdc++.h>
using namespace std;
struct L{int s,e,C;};
int main(){
 const int a=20,b=23,Q=80;
 vector<int> rho; rho.insert(rho.end(),7,5); rho.insert(rho.end(),8,4); rho.push_back(2); rho.insert(rho.end(),7,1);
 vector<L> lab; lab.push_back({4,0,9}); for(int i=0;i<14;i++)lab.push_back({4,0,8}); for(int i=0;i<5;i++)lab.push_back({4,0,7});
 auto P0=[&](int r){return min(b-1,r+b-a-1);};
 auto A=[&](int r,int p){int z=0; for(auto v:lab) if(v.s<=r && v.e>=max(0,p-r+1)) z=max(z,min(b-1-p,v.C-p)); return max(0,z);};
 long long basic=0, weighted=0;
 for(int r:rho){
   int M=-1; for(auto v:lab)if(v.s<=r)M=max(M,v.C);
   basic+=max(P0(r),M);
   int H=0; for(int p=0;p<=P0(r);p++)H=max(H,2*A(r,p)+3*p); weighted+=H;
 }
 vector<int> dp(Q+1,-1000000); dp[0]=0;
 for(int r:rho){vector<int> nd(Q+1,-1000000); for(int z=0;z<=Q;z++)if(dp[z]>-100000)for(int p=0;p<=P0(r)&&z+p<=Q;p++)nd[z+p]=max(nd[z+p],dp[z]+A(r,p)); dp.swap(nd);}
 cout << basic << ' ' << weighted << ' ' << dp[Q] << '\n';
 return !(basic==160 && weighted==397 && dp[Q]==78);
}
