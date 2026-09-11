// Independent exhaustive corroboration of the written clipping arguments.
// It is NOT a premise of the hand proofs. Integer arithmetic only.
#include <array>
#include <algorithm>
#include <fstream>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <vector>
using Hist=std::array<int,13>;
constexpr int BAD=-1000000;
int thresholds[13][157][2]; // bounded b=16 / unbounded first admissible z

int value(const Hist &c,int upper) {
  int total=0,w=0,penalty=0;
  for(int h=0;h<=12;h++) total+=h*c[h];
  for(int h=12;h>=2;h--) {
    w+=h*c[h];
    int z=thresholds[h][w][upper];
    if(z<0) return BAD;
    penalty+=z;
  }
  return total-penalty;
}
Hist clip(Hist c,int cap) {
  for(int h=cap+1;h<=12;h++){c[cap]+=c[h];c[h]=0;}
  return c;
}
std::vector<int> expand(const Hist &c) {
  std::vector<int> s;
  for(int h=0;h<=12;h++) for(int k=0;k<c[h];k++) s.push_back(h);
  return s;
}
struct Run {
  int a,maxentry,maximum=BAD,maxwithsix=BAD;
  long long total=0,inadmissible=0,clipping_checks=0,exceptional_fives=0;
  std::array<long long,4> clips{};
  std::vector<std::vector<int>> high;
  std::vector<int> scores;
  Run(int aa):a(aa),maxentry(aa-1){}
  void leaf(const Hist &c) {
    total++;
    int upper=a==13?0:1;
    int q=value(c,upper);
    if(q==BAD) inadmissible++;
    maximum=std::max(maximum,q);
    int mx=12;while(mx>0&&!c[mx])mx--;
    if(mx>=6)maxwithsix=std::max(maxwithsix,q);
    if(q>=18){high.push_back(expand(c));scores.push_back(q);}
    if(a==13){
      Hist current=c;int before=q;
      for(int cap: {7,6,5,4}){
        Hist after=clip(current,cap);int next=value(after,0);
        if(next<before)throw std::runtime_error("N30 clipping counterexample");
        clips[7-cap]++;clipping_checks++;current=after;before=next;
      }
    } else {
      // Twelve-label proof: clip high tails, then 6->5; (5^12) is
      // discharged directly instead of claiming a monotone 5->4 step.
      Hist c6=clip(c,6),c5=clip(c6,5),c4=clip(c5,4),c3=clip(c4,3);
      if(value(c6,1)<q||value(c5,1)<value(c6,1))throw std::runtime_error("Twelve-label high clipping failure");
      clipping_checks+=2;
      if(c5[5]==12){if(value(c5,1)!=16)throw std::runtime_error("Exceptional fives");exceptional_fives++;}
      else {
        if(value(c4,1)<value(c5,1)||value(c3,1)<value(c4,1))throw std::runtime_error("Twelve-label lower clipping failure");
        clipping_checks+=2;
      }
      if(q>18)throw std::runtime_error("Twelve-label tail bound failed");
    }
  }
  void visit(Hist &c,int level,int remaining){
    if(level==maxentry){c[level]=remaining;leaf(c);c[level]=0;return;}
    for(int k=0;k<=remaining;k++){c[level]=k;visit(c,level+1,remaining-k);}c[level]=0;
  }
  void write(std::ostream &o){
    o<<"{\"a\":"<<a<<",\"profiles_tested\":"<<total
     <<",\"threshold_inadmissible\":"<<inadmissible<<",\"maximum_Q\":"<<maximum
     <<",\"maximum_Q_with_demand_at_least_6\":"<<maxwithsix
     <<",\"clipping_comparisons\":"<<clipping_checks
     <<",\"clipping_counterexamples\":0,\"exceptional_fives_images\":"<<exceptional_fives
     <<",\"high_profiles\":[";
    std::vector<size_t> order(high.size());for(size_t i=0;i<order.size();i++)order[i]=i;
    std::sort(order.begin(),order.end(),[&](size_t i,size_t j){return high[i]<high[j];});
    bool first=true;for(size_t i:order){if(!first)o<<",";first=false;o<<"{\"s\":[";
      for(size_t j=0;j<high[i].size();j++){if(j)o<<",";o<<high[i][j];}o<<"],\"Q\":"<<scores[i]<<"}";}
    o<<"]}";
  }
};
int main(int argc,char **argv){
  if(argc!=2){std::cerr<<"usage: profile_regression OUTPUT.json\n";return 2;}
  for(int h=2;h<=12;h++)for(int w=0;w<=156;w++){
    int z=0;if(w){z=h;while(2*w>z*(z-1)+h*(h+1))z++;}
    thresholds[h][w][0]=z>16?-1:z;thresholds[h][w][1]=z;
  }
  Run r13(13),r12(12);Hist c{};r13.visit(c,0,13);r12.visit(c,0,12);
  if(r13.total!=5200300||r13.maximum!=21||r13.high.size()!=100||r12.total!=1352078||r12.maximum!=18)return 1;
  std::ofstream out(argv[1]);if(!out)return 2;
  out<<"{\"status\":\"PASS\",\"role\":\"Independent exhaustive corroboration; not a proof premise\",\"runs\":[";
  r13.write(out);out<<",";r12.write(out);out<<"]}\n";
  std::cout<<"PASS: 5200300 thirteen-label profiles and 1352078 twelve-label profiles; no clipping counterexamples\n";
}
