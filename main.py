import os,json,urllib.request as u
S="OOOOTYY;TJEOOOOcTTYhYYcm~~~~OOOO!'11';OT1TY^1O^c1T^c1OY^';OO!'11;EEEETOOEYYYEOYYETTYEOTYEOOO;EEEOOOTJOOOJOOOJOOOJOOOJOOOTYYYOOOO;EEJEOTOETTTOOTTJOTTEOTTEOOO;EEJcmYOccOOE;;;;11'1''!1''!1''!1''!"
M=dict(zip('PNBRQK.',[100,320,330,500,900,0,0]))
N=(-21,-19,-12,-8,8,12,19,21)
G=(-11,-10,-9,-1,1,9,10,11)
V={p:[M[p]+ord(S[o+(9-i//10)*4+min(i%10-1,8-i%10)])-79 if 20<i<99 else 0 for i in range(120)] for p,o in zip('PNBRQK',range(0,192,32))}
Z={95:12,98:14,91:13,25:3,28:11,21:7}
TT={};H={};ND=0;BD=6e4;MA=1e5
X=Exception
def att(b,s,w):
 u='PNBRQK'if w else'pnbrqk';d=1 if w else-1
 for x in N:
  if b[s+x]==u[1]:return 1
 for x in G:
  if b[s+x]==u[5] or b[s+x]==u[0] and x*d in (9,11):return 1
  j=s+x
  while b[j]=='.':j+=x
  if b[j] in u[3-(abs(x) in(9,11))]+u[4]:return 1
 return 0
def gen(b,c,e,w):
 d=-10 if w else 10;my='PNBRQK'if w else'pnbrqk';fo=my.swapcase()
 for i,p in enumerate(b):
  if p in my:
   u=p.upper()
   if u=='P':
    for x in (d,d-1,d+1):
     j=i+x;q=b[j]
     if (x==d and q=='.') or (x!=d and (q in fo or j==e)):
      if j//10 in (2,9):
       for r in 'QRBN':yield i,j,r
      else:
       yield i,j,''
       if x==d and i//10 in (8,3) and b[i+2*d]=='.':yield i,i+2*d,''
   elif u in'NK':
    for x in N if u=='N' else G:
     j=i+x;q=b[j]
     if q=='.' or q in fo:yield i,j,''
   else:
    for x in G if u=='Q' else (-11,-9,9,11) if u=='B' else (-10,-1,1,10):
     j=i+x
     while b[j]=='.' or b[j] in fo:
      yield i,j,''
      if b[j] in fo:break
      j+=x
 if c:
  k,a,y=(95,1,2)if w else(25,4,8)
  if not att(b,k,not w):
   if c&a and b[k+1:k+3]=='..' and not att(b,k+1,not w) and not att(b,k+2,not w):yield k,k+2,''
   if c&y and b[k-3:k]=='...' and not att(b,k-1,not w) and not att(b,k-2,not w):yield k,k-2,''
def do(b,m,c,e):
 i,j,q=m;p=b[i];l=list(b);l[i]='.';U=p.upper()
 if U=='P' and j==e:l[i-i%10+j%10]='.'
 if U=='K' and abs(j-i)==2:l[j+1 if j>i else j-2]='.';l[j-1 if j>i else j+1]='R' if p=='K' else 'r'
 l[j]=(q.lower()if p=='p' else q)or p
 return ''.join(l),c&Z.get(i,15)&Z.get(j,15),(i+j)//2 if U=='P' and abs(i-j)==20 else -1
def ok(b,c,e,m,w):
 b2,_,_=do(b,m,c,e)
 return not att(b2,b2.index('Kk'[not w]),not w)
def sr(b,c,e,w,d,a,be,pl):
 global ND
 ND+=1
 if ND>BD:raise X
 ck=att(b,b.index('Kk'[not w]),not w)
 k=(b,c,e,w);t=TT.get(k)if d>0 else 0
 if t and t[0]>=d:return t[1]
 tm=t and t[2]
 if d<=0 and not ck:
  ev=sum(V[p][i] if p.isupper() else -V[p.upper()][119-i] for i,p in enumerate(b) if p.isalpha())
  if not w:ev=-ev
  if ev>=be:return be
  if ev>a:a=ev
  ms=[m for m in gen(b,c,e,w) if (b[m[1]]!='.' or m[1]==e or m[2]) and ok(b,c,e,m,w) and (m[1]==e or m[2] or ev+M[b[m[1]].upper()]+200>=a)]
 else:
  ms=[m for m in gen(b,c,e,w) if ok(b,c,e,m,w)]
  if not ms:return -MA+pl if ck else 0
  a0=a;bm=ms[0]
 ms.sort(key=lambda m:-1e9 if m==tm else -1e6-10*M[b[m[1]].upper()] if b[m[1]]!='.' or m[1]==e else -H.get(m,0))
 for n,m in enumerate(ms):
  b2,c2,e2=do(b,m,c,e)
  s=-sr(b2,c2,e2,not w,d-1,-a-1 if d>0 and n else -be,-a,pl+1)
  if d>0 and n and s>a:s=-sr(b2,c2,e2,not w,d-1,-be,-a,pl+1)
  if s>a:a=s;bm=m
  if a>=be:H[m]=H.get(m,0)+d*d;break
 if d>0 and abs(a)<9e4:TT[k]=(d if a0<a<be else -d,a,bm)
 return a
def pf(f):
 p=f.split()
 b=' '*20+''.join(' '+''.join(c if c>'9' else '.'*int(c) for c in r)+' ' for r in p[0].split('/'))+' '*20
 c=sum(1<<'KQkq'.index(x) for x in p[2] if x!='-')
 e=-1 if p[3]=='-'else(10-int(p[3][1]))*10+ord(p[3][0])-96
 return b,c,e,p[1]=='w'
U=os.getenv('MAKEFUN_ENV_URL')
def post(p,o):
 for _ in'12':
  try:return json.load(u.urlopen(U+p,json.dumps(o).encode(),timeout=4))
  except:pass
 raise X
f=lambda x:chr(96+x%10)+str(10-x//10)
while 1:
 g=post('/game',{})
 if g['status']=='done':break
 b,c,e,w=pf(g['fen'])
 lg=[m for m in gen(b,c,e,w) if ok(b,c,e,m,w)]
 ND=0;bm=lg[0];d=1
 while d<64:
  try:
   a=-MA
   for m in lg:
    b2,c2,e2=do(b,m,c,e)
    s=-sr(b2,c2,e2,not w,d-1,-MA,-a,1)
    if s>a:a=s;bm=m
   lg.sort(key=lambda m:m!=bm)
   d+=1
  except X:break
 mv=f(bm[0])+f(bm[1])+bm[2].lower()
 post('/move',{'game':g['game'],'move':mv})
