#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
using U=std::uint64_t;
int pc(U x){return __builtin_popcountll(x);}
bool close(const std::vector<U>& a,int x,int y){
    if(x==y || ((a[x]>>y)&1))return true;
    for(int z=0;z<(int)a.size();++z)if(((a[x]>>z)&1)&&((a[z]>>y)&1))return true;
    return false;
}
int main(){
    std::ios::sync_with_stdio(false);std::cin.tie(nullptr);
    std::string type;long long index=0;
    while(std::cin>>type){
        if(type=="G"){
            int n,d,k;std::cin>>n>>d>>k;std::vector<U>a(n);for(auto&x:a)std::cin>>x;
            bool universal=true, common=k>=d && ((a[k]&3)==3), covered=true;int singles=0,edges=0;
            for(int t=0;t<d;t++)for(int s=t+1;s<d;s++)edges+=(a[t]>>s)&1;
            for(int t=0;t<2;t++)for(int s=0;s<d;s++)if(t!=s&&!((a[t]>>s)&1))universal=false;
            for(int x=d;x<n;x++){
                int count=0,last=-1;for(int t=0;t<d;t++)if((a[x]>>t)&1){count++;last=t;}
                if(count==1&&last<2){singles++;if(!((a[k]>>x)&1))covered=false;}
            }
            bool eligible=d>=3&&((a[0]>>1)&1)&&universal&&common&&covered;
            auto b=a;b[0]&=~U(2);b[1]&=~U(1);int lost=0;bool dia=true;
            for(int x=0;x<n;x++)for(int y=x+1;y<n;y++){
                bool before=close(a,x,y);dia&=before;lost+=before&&!close(b,x,y);
            }
            if(eligible&&lost){std::cerr<<"graph counterexample "<<index<<"\n";return 2;}
            std::cout<<index<<" G "<<eligible<<" "<<d*(d-1)/2-edges<<" "<<singles<<" "<<dia<<" "<<lost<<"\n";
        }else if(type=="I"){
            int d,k;std::cin>>d>>k;std::vector<U>q(d),mask(k);std::vector<int>p(d),beta(d),w(k),row(d),marked(d),universal(d);
            for(auto&x:q)std::cin>>x;
            for(auto&x:p)std::cin>>x;
            for(auto&x:beta)std::cin>>x;
            bool valid=d>=3;int L=0,bs=0,m=0,degs=0;
            for(int j=0;j<k;j++){
                std::cin>>mask[j]>>w[j];int count=pc(mask[j]);L+=w[j]-count;
                valid&=count>0&&(w[j]==d||w[j]==d-1)&&count<=w[j];
                for(int t=0;t<d;t++)if((mask[j]>>t)&1){row[t]++;if(count==1)marked[t]=1;}
            }
            int g=0,u=0;for(int t=0;t<d;t++){universal[t]=pc(q[t])==d-1;g+=universal[t];u+=universal[t]&&!marked[t];m+=p[t];bs+=beta[t];degs+=pc(q[t]);valid&=p[t]>=1&&beta[t]>=0;}
            for(int t=0;t<d;t++)valid&=row[t]==1+m-p[t]+beta[t]+d-1-pc(q[t]);
            bool cover=true;for(auto s:mask){int count=0;for(int t=0;t<d;t++)if(universal[t]&&!marked[t]&&((s>>t)&1))count++;if(count>1)cover=false;}
            int mu=d*(d-1)/2-degs/2,D=L+bs+2*mu,bound=2*mu+(d-2)*std::max(0,g-1);bool eligible=valid&&cover,pass=D>=bound;
            if(eligible&&!pass){std::cerr<<"incidence counterexample "<<index<<"\n";return 3;}
            std::cout<<index<<" I "<<eligible<<" "<<g<<" "<<u<<" "<<mu<<" "<<L<<" "<<bs<<" "<<D<<" "<<bound<<" "<<pass<<"\n";
        }else{std::cerr<<"unknown record type\n";return 4;}
        if(!std::cin){std::cerr<<"truncated input\n";return 5;}index++;
    }
    return 0;
}
